### Repository snapshot

- This repository currently contains a single Python file at the workspace root: `firs`.
- There is no test harness, dependency manifest, or packaging. Use minimal, non-invasive changes.

### What an AI coding agent should know (big picture)

- Project shape: single-file, small script (Python). There are no services, frameworks, or CI configs to integrate with.
- Primary intent: simple script; changes should be minimal and explicitly explained to the maintainer.

### Immediate developer workflows (how to run & check changes)

- Run the script (macOS / zsh):

  python3 firs

- Quick syntax check (preferred before committing):

  python3 -m py_compile firs

- If you add dependencies, provide a `requirements.txt` and update these instructions.

### Project-specific conventions and examples

- Filename conventions: files are at repo root (no src/). Keep changes small and local.
- Example issue discovered in this repo: `firs` currently contains an invalid print statement. A correct Python 3 replacement is:

  print("me plus you =", total)

- Prefer explicit, minimal edits with an explanation in the commit message and PR body describing why the change is needed.

### What to change and how (concrete guidance for the agent)

- Fix bugs conservatively. For a small file like `firs` prefer a single commit that:
  - fixes syntax/runtime errors
  - adds a one-line docstring or comment if helpful
  - optionally adds a minimal `README.md` or `requirements.txt` if you introduce dependencies

- Write tests only if the change grows beyond a trivial fix. If you add tests, use pytest and include a `pyproject.toml` or `requirements.txt` documenting the test runner.

### Commit, branch and PR guidance

- Branch name: `fix/<short-desc>` or `feat/<short-desc>` (e.g., `fix/print-syntax`)
- Commit message: start with a short imperative summary and one-line body (e.g., `Fix print syntax in firs`)
- PR description: explain the problem, the change, and how to run a quick verification (commands above).

### Integration and external dependencies

- There are currently no external services or third-party integrations in this repo. Avoid introducing infrastructure changes without explicit approval.

### When to ask for clarification

- If a change requires adding tests, a dependency, or restructuring (creating src/, adding packaging), ask the maintainer first.

---

If anything in this guidance is unclear or you want the instructions to be more prescriptive (for example, a strict PR template or test harness), tell me what to add and I will update this file.
