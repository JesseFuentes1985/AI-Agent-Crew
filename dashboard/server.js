const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3131;
const DATA_FILE = path.join(__dirname, '..', 'agent-tasks.json');
const BUDGET_FILE = path.join(__dirname, 'budget.json');
const WORKSPACE_ROOT = path.join(__dirname, '..', '..');

app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// ── Helpers ──────────────────────────────────────────────

function readData() {
  const data = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  // Migrate: ensure every task has a status field
  let changed = false;
  Object.values(data.agents).forEach(agent => {
    agent.tasks.forEach(task => {
      if (!task.status) {
        task.status = task.done ? 'done' : 'queue';
        changed = true;
      }
    });
  });
  if (changed) fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
  return data;
}

function writeData(data) {
  data.lastUpdated = new Date().toISOString().split('T')[0];
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

function getWorkspacePath(agentId) {
  return agentId === 'orbit'
    ? path.join(__dirname, '..')
    : path.join(WORKSPACE_ROOT, `workspace-${agentId}`);
}

function syncTasksToMarkdown(agentId, agent) {
  const wsPath = getWorkspacePath(agentId);
  if (!fs.existsSync(wsPath)) return;
  const tasksPath = path.join(wsPath, 'TASKS.md');

  const queue    = agent.tasks.filter(t => t.status === 'queue');
  const progress = agent.tasks.filter(t => t.status === 'progress');
  const done     = agent.tasks.filter(t => t.status === 'done');

  const lines = [
    `# Task Board — ${agent.name}`,
    ``,
    `> Synced from Mission Control | ${new Date().toISOString()}`,
    ``,
    `## Skills`,
    ``,
    (agent.skills || []).map(s => `- ${s}`).join('\n') || '_None listed_',
    ``,
    `---`,
    ``,
    `## 🔄 In Progress (${progress.length})`,
    ``,
    progress.length ? progress.map(t => `- [ ] ${t.text}`).join('\n') : '_Nothing in progress_',
    ``,
    `## 📋 In Queue (${queue.length})`,
    ``,
    queue.length ? queue.map(t => `- [ ] ${t.text}`).join('\n') : '_Queue is empty_',
    ``,
    `## ✅ Done (${done.length})`,
    ``,
    done.length ? done.map(t => `- [x] ${t.text}`).join('\n') : '_Nothing completed yet_',
    ``
  ];
  fs.writeFileSync(tasksPath, lines.join('\n'));
}

function syncNotesToMarkdown(agentId, agent) {
  const wsPath = getWorkspacePath(agentId);
  if (!fs.existsSync(wsPath)) return;
  const notesPath = path.join(wsPath, 'NOTES.md');
  const notes = agent.notes || [];

  if (notes.length === 0) {
    fs.writeFileSync(notesPath, `# Notes — ${agent.name}\n\n_No notes yet._\n`);
    return;
  }
  const lines = [
    `# Notes — ${agent.name}`,
    ``,
    `> Synced from Mission Control | ${new Date().toISOString()}`,
    ``
  ];
  notes.forEach(n => {
    const d = new Date(n.createdAt);
    lines.push(`## ${d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })} ${d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}`);
    lines.push(``, n.text, ``, `---`, ``);
  });
  fs.writeFileSync(notesPath, lines.join('\n'));
}

function readBudget() {
  if (!fs.existsSync(BUDGET_FILE)) return { balance: null, lastUpdated: null };
  return JSON.parse(fs.readFileSync(BUDGET_FILE, 'utf8'));
}

// ── Routes ────────────────────────────────────────────────

// Tasks
app.get('/api/tasks', (req, res) => res.json(readData()));

app.post('/api/tasks/:agentId', (req, res) => {
  const { agentId } = req.params;
  const { text } = req.body;
  if (!text?.trim()) return res.status(400).json({ error: 'Task text required' });
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  const task = { id: `${agentId}-${Date.now()}`, text: text.trim(), done: false, status: 'queue' };
  agent.tasks.push(task);
  writeData(data);
  syncTasksToMarkdown(agentId, agent);
  res.json(task);
});

// PATCH: update status and/or text
app.patch('/api/tasks/:agentId/:taskId', (req, res) => {
  const { agentId, taskId } = req.params;
  const { status, text } = req.body || {};
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  const task = agent.tasks.find(t => t.id === taskId);
  if (!task) return res.status(404).json({ error: 'Task not found' });

  if (status !== undefined) {
    task.status = status;
    task.done = status === 'done';
  } else if (text === undefined) {
    // Legacy toggle
    task.done = !task.done;
    task.status = task.done ? 'done' : 'queue';
  }
  if (text !== undefined) task.text = text.trim();

  writeData(data);
  syncTasksToMarkdown(agentId, agent);
  res.json(task);
});

app.delete('/api/tasks/:agentId/:taskId', (req, res) => {
  const { agentId, taskId } = req.params;
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  agent.tasks = agent.tasks.filter(t => t.id !== taskId);
  writeData(data);
  syncTasksToMarkdown(agentId, agent);
  res.json({ success: true });
});

// Skills
app.patch('/api/skills/:agentId', (req, res) => {
  const { agentId } = req.params;
  const { skills } = req.body;
  if (!Array.isArray(skills)) return res.status(400).json({ error: 'skills must be array' });
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  agent.skills = skills.map(s => s.trim()).filter(Boolean);
  writeData(data);
  syncTasksToMarkdown(agentId, agent);
  res.json(agent.skills);
});

// Notes
app.get('/api/notes/:agentId', (req, res) => {
  const data = readData();
  const agent = data.agents[req.params.agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  res.json(agent.notes || []);
});

app.post('/api/notes/:agentId', (req, res) => {
  const { agentId } = req.params;
  const { text } = req.body;
  if (!text?.trim()) return res.status(400).json({ error: 'Note text required' });
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  if (!agent.notes) agent.notes = [];
  const note = { id: `note-${Date.now()}`, text: text.trim(), createdAt: new Date().toISOString() };
  agent.notes.unshift(note);
  writeData(data);
  syncNotesToMarkdown(agentId, agent);
  res.json(note);
});

app.delete('/api/notes/:agentId/:noteId', (req, res) => {
  const { agentId, noteId } = req.params;
  const data = readData();
  const agent = data.agents[agentId];
  if (!agent) return res.status(404).json({ error: 'Agent not found' });
  agent.notes = (agent.notes || []).filter(n => n.id !== noteId);
  writeData(data);
  syncNotesToMarkdown(agentId, agent);
  res.json({ success: true });
});

// Budget
app.get('/api/budget', (req, res) => res.json(readBudget()));

app.post('/api/budget', (req, res) => {
  const { balance } = req.body;
  if (isNaN(parseFloat(balance))) return res.status(400).json({ error: 'Invalid balance' });
  const data = { balance: parseFloat(parseFloat(balance).toFixed(2)), lastUpdated: new Date().toISOString() };
  fs.writeFileSync(BUDGET_FILE, JSON.stringify(data, null, 2));
  res.json(data);
});

app.listen(PORT, () => console.log(`🛸 Dashboard running at http://localhost:${PORT}`));
