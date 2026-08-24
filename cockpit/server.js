#!/usr/bin/env node
/**
 * 🛸 CREW COCKPIT — fresh, zero-dependency control surface
 * Live agent status + growth insights + per-agent voices.
 * Pure Node stdlib (http/fs/child_process). No npm install needed.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFile, spawn } = require('child_process');

const PORT = 4000;
const ROOT = __dirname;                                   // .../workspace-main/cockpit
const WS_MAIN = path.join(ROOT, '..');                    // .../workspace-main
const OPENCLAW_HOME = path.join(WS_MAIN, '..');           // .../.openclaw
const TASKS_FILE = path.join(WS_MAIN, 'agent-tasks.json');
const BUDGET_FILE = path.join(WS_MAIN, 'dashboard', 'budget.json');

// ── Static roster (identity + persona voice) ────────────────────────
// Voices use macOS `say -v`. Each agent gets a distinct, on-character voice.
const ROSTER = {
  orbit:        { name: 'Orbit',        emoji: '🛸', title: 'Core Architect · Command',   color: '#00d4ff', voice: 'Samantha',             rate: 175 },
  rick:         { name: 'Rick',         emoji: '🔬', title: 'DevOps & SysAdmin',          color: '#00b894', voice: 'Fred',                 rate: 180 },
  baymax:       { name: 'Baymax',       emoji: '🤖', title: 'Health Guardian',            color: '#ff6b6b', voice: 'Reed (English (US))',  rate: 165 },
  beast:        { name: 'Beast',        emoji: '📚', title: 'Learning & Knowledge',       color: '#4ecdc4', voice: 'Daniel',               rate: 175 },
  greenlantern: { name: 'Green Lantern',emoji: '🟢', title: 'Creativity & Worldbuilding', color: '#2ed573', voice: 'Rocko (English (US))', rate: 185 },
  quigon:       { name: 'Qui-Gon',      emoji: '🧘', title: 'Wellness & Mindfulness',     color: '#a29bfe', voice: 'Rishi',                rate: 165 },
  thanos:       { name: 'Thanos',       emoji: '👊', title: 'Productivity & Focus',       color: '#fd79a8', voice: 'Ralph',                rate: 170 },
  tonystark:    { name: 'Tony Stark',   emoji: '💰', title: 'Entrepreneur & Strategy',    color: '#fdcb6e', voice: 'Eddy (English (US))',  rate: 185 },
};
const ORDER = ['orbit','rick','baymax','beast','greenlantern','quigon','thanos','tonystark'];

// ── Helpers ─────────────────────────────────────────────────────────
function readJSON(file, fallback) {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch { return fallback; }
}

function dirBytes(dir, exts) {
  let total = 0;
  let walk;
  walk = (d) => {
    let entries;
    try { entries = fs.readdirSync(d, { withFileTypes: true }); } catch { return; }
    for (const e of entries) {
      if (e.name.startsWith('.') || e.name === 'node_modules') continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p);
      else if (!exts || exts.some(x => e.name.endsWith(x))) {
        try { total += fs.statSync(p).size; } catch {}
      }
    }
  };
  walk(dir);
  return total;
}

// Orbit's internal agent id is "main", not "orbit".
function realAgentId(id) { return id === 'orbit' ? 'main' : id; }

function agentSessions(agentId) {
  // Read the agent's own session store directly (fast, no spawn).
  const store = path.join(OPENCLAW_HOME, 'agents', realAgentId(agentId), 'sessions', 'sessions.json');
  const data = readJSON(store, null);
  if (!data) return { count: 0, lastActive: null };
  // store shapes seen in the wild:
  //   array of sessions  |  { sessions: {...} }  |  { "agent:x:y": {updatedAt}, ... }
  let sessions = [];
  if (Array.isArray(data)) sessions = data;
  else if (data.sessions && typeof data.sessions === 'object')
    sessions = Array.isArray(data.sessions) ? data.sessions : Object.values(data.sessions);
  else {
    // Top-level map of sessionKey -> session object (e.g. "agent:main:main").
    sessions = Object.values(data).filter(v => v && typeof v === 'object' && (v.updatedAt || v.lastInteractionAt || v.sessionId));
  }
  let last = null;
  for (const s of sessions) {
    const t = s.updatedAt || s.lastInteractionAt || s.updated_at || s.ts || null;
    if (t && (!last || t > last)) last = t;
  }
  return { count: sessions.length, lastActive: last };
}

function fmtAge(ms) {
  if (ms == null) return 'never';
  const s = Math.floor(ms / 1000);
  if (s < 60) return `${s}s ago`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m}m ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h}h ago`;
  const d = Math.floor(h / 24);
  return `${d}d ago`;
}

function modelInfo(model) {
  if (!model) return { label: '—', tier: 'unknown', paid: false };
  if (model.startsWith('ollama/')) return { label: model.replace('ollama/', ''), tier: 'local', paid: false };
  if (model.startsWith('anthropic/')) return { label: model.replace('anthropic/', ''), tier: 'cloud', paid: true };
  return { label: model, tier: 'cloud', paid: true };
}

// Pull per-agent model from `openclaw agents list` (cached).
let agentsListCache = { ts: 0, map: {} };
function getAgentsList() {
  return new Promise((resolve) => {
    if (Date.now() - agentsListCache.ts < 30000) return resolve(agentsListCache.map);
    execFile('openclaw', ['agents', 'list'], { timeout: 8000 }, (err, stdout) => {
      const map = {};
      if (!err && stdout) {
        // Parse blocks: "- id (..) (Name)\n ... Model: x/y"
        const lines = stdout.split('\n');
        let cur = null;
        for (const line of lines) {
          const m = line.match(/^-\s+(\w+)\b/);
          if (m) { cur = m[1]; map[cur] = {}; }
          else if (cur) {
            const mm = line.match(/Model:\s*(\S+)/);
            if (mm) map[cur].model = mm[1];
          }
        }
      }
      agentsListCache = { ts: Date.now(), map };
      resolve(map);
    });
  });
}

// ── Build the live crew snapshot ────────────────────────────────────
async function buildCrew() {
  const tasksData = readJSON(TASKS_FILE, { agents: {} });
  const budget = readJSON(BUDGET_FILE, { balance: null });
  const models = await getAgentsList();
  const now = Date.now();

  const agents = ORDER.map(id => {
    const r = ROSTER[id];
    const tdata = tasksData.agents[id] || {};
    const tasks = tdata.tasks || [];
    const queue = tasks.filter(t => (t.status || (t.done ? 'done' : 'queue')) === 'queue').length;
    const progress = tasks.filter(t => t.status === 'progress').length;
    const done = tasks.filter(t => t.done || t.status === 'done').length;
    const skills = (tdata.skills || []).length;

    const sess = agentSessions(id);
    const lastActiveMs = sess.lastActive ? (now - sess.lastActive) : null;
    const online = lastActiveMs != null && lastActiveMs < 15 * 60 * 1000;

    const wsDir = path.join(OPENCLAW_HOME, `workspace-${id}`);
    const memBytes = dirBytes(wsDir, ['.md']);

    const mi = modelInfo(models[realAgentId(id)]?.model);

    return {
      id, name: r.name, emoji: r.emoji, title: r.title, color: r.color, voice: r.voice,
      model: mi.label, tier: mi.tier, paid: mi.paid,
      online, lastActive: fmtAge(lastActiveMs), lastActiveMs,
      sessions: sess.count,
      tasks: { queue, progress, done, total: tasks.length },
      skills, memBytes,
    };
  });

  return { agents, budget, insights: buildInsights(agents), ts: now };
}

// ── Growth insights: rule-based nudges to GROW each agent ───────────
function buildInsights(agents) {
  const out = [];
  for (const a of agents) {
    if (a.sessions === 0) {
      out.push({ id: a.id, kind: 'activate', icon: '🌱', sev: 'high',
        text: `${a.name} has never run — activate it with a first task to bring it online.` });
    } else if (a.lastActiveMs != null && a.lastActiveMs > 7 * 86400000) {
      out.push({ id: a.id, kind: 'idle', icon: '💤', sev: 'med',
        text: `${a.name} has been idle ${fmtAge(a.lastActiveMs)} — give it work to keep momentum.` });
    }
    if (a.memBytes < 300) {
      out.push({ id: a.id, kind: 'memory', icon: '🧠', sev: 'med',
        text: `${a.name} has almost no memory — onboard it with context so it gets smarter.` });
    }
    if (a.tasks.queue > 0 && a.tasks.progress === 0) {
      out.push({ id: a.id, kind: 'backlog', icon: '📋', sev: 'low',
        text: `${a.name} has ${a.tasks.queue} queued task${a.tasks.queue>1?'s':''} but nothing in progress.` });
    }
    if (a.skills === 0) {
      out.push({ id: a.id, kind: 'skills', icon: '🧩', sev: 'low',
        text: `${a.name} has no skills defined — add some to sharpen its focus.` });
    }
    if (a.tasks.total > 0 && a.tasks.done === a.tasks.total) {
      out.push({ id: a.id, kind: 'cleared', icon: '🚀', sev: 'low',
        text: `${a.name} cleared every task — give it a harder goal.` });
    }
  }
  const rank = { high: 0, med: 1, low: 2 };
  out.sort((x, y) => rank[x.sev] - rank[y.sev]);
  return out;
}

// ── Voice: speak text in an agent's voice via macOS `say` ───────────
function speak(voice, rate, text, res) {
  const clean = String(text || '').slice(0, 600);
  if (!clean.trim()) { res.writeHead(400).end('{"error":"empty"}'); return; }
  const args = [];
  if (voice) args.push('-v', voice);
  if (rate) args.push('-r', String(rate));
  args.push(clean);
  const p = spawn('say', args);
  p.on('error', () => { try { res.writeHead(500).end('{"error":"say failed"}'); } catch {} });
  p.on('close', () => { try { res.writeHead(200, {'Content-Type':'application/json'}).end('{"ok":true}'); } catch {} });
}

// ── HTTP ────────────────────────────────────────────────────────────
const MIME = { '.html':'text/html', '.css':'text/css', '.js':'text/javascript',
  '.json':'application/json', '.jpg':'image/jpeg', '.png':'image/png', '.gif':'image/gif', '.svg':'image/svg+xml' };

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const p = url.pathname;
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.writeHead(204).end();

  try {
    if (p === '/api/crew') {
      const data = await buildCrew();
      res.writeHead(200, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify(data));
    }
    if (p === '/api/say' && req.method === 'POST') {
      let body = '';
      req.on('data', c => body += c);
      req.on('end', () => {
        const { agentId, text } = readJSONStr(body);
        const r = ROSTER[agentId] || {};
        return speak(r.voice, r.rate, text, res);
      });
      return;
    }
    // Static files
    let file = p === '/' ? '/index.html' : decodeURIComponent(p);
    const full = path.join(ROOT, file);
    if (!full.startsWith(ROOT)) return res.writeHead(403).end('forbidden');
    if (fs.existsSync(full) && fs.statSync(full).isFile()) {
      res.writeHead(200, { 'Content-Type': MIME[path.extname(full)] || 'application/octet-stream' });
      return fs.createReadStream(full).pipe(res);
    }
    res.writeHead(404).end('not found');
  } catch (e) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: String(e && e.message || e) }));
  }
});

function readJSONStr(s) { try { return JSON.parse(s); } catch { return {}; } }

server.listen(PORT, () => console.log(`🛸 Crew Cockpit live → http://localhost:${PORT}`));
