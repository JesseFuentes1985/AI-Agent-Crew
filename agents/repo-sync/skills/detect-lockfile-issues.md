# detect-lockfile-issues

Check whether repository contains a supported lockfile (`package-lock.json`, `npm-shrinkwrap.json`, or `yarn.lock`). If missing and the repo uses npm, generate `package-lock.json` locally and prepare a minimal commit or PR with changes. Steps:

1. Inspect repository root for supported lockfiles.
2. If using `package.json` and no lockfile present, run `npm install` to generate `package-lock.json`.
3. Verify `npm run build` succeeds.
4. If build succeeds, prepare a branch `fix/lockfile-<date>` with the new lockfile and open a PR with an explanation.

Constraints:
- Do not push directly to `main` without approval.
- Use smallest possible change set.
