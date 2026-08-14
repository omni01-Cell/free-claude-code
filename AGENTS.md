---
trigger: always_on
---

# Git-Context-Controller (GCC) Protocol

This protocol governs context persistence, architecture tracking, and session handoff mechanics. It must be strictly executed by the AI agent at specific session milestones.

<file_matrix>
<file path=".GCC/main.md" lifecycle="persistent">
<scope>
Acts as the global project registry. Contains high-level milestones, objective, chronological decision log, and an active index of valid plans.
</scope>
</file>
<file path=".GCC/branches/plan_[name].md" lifecycle="transient">
<scope>
Step-by-step tactical implementation plan for complex, multi-session epics only.
</scope>
</file>
<file path=".GCC/resume.md" lifecycle="dynamic">
<scope>
Factual technical changelog and precise transition state. Overwritten at the absolute end of every session to ensure seamless state-recovery in fresh chat environments.
</scope>
</file>
<file path=".GCC/branches/test.md" lifecycle="persistent">
<scope>
Persistent test execution log, tracking completed tests, results, bugs found, and fixes applied.
</scope>
</file>
<file path=".GCC/branches/test_afaire.md" lifecycle="persistent">
<scope>
Test backlog tracking all pending scenarios and test suites to be executed.
</scope>
</file>
</file_matrix>

<event_driven_protocols>

<protocol id="A" name="session_bootstrap">
<trigger>Agent receives the first message from the user in a new chat/session.</trigger>
<step id="1">
<action>TOOL INVOCATION: Read `.GCC/main.md` to load the project's macro state and retrieve active plans.</action>
</step>
<step id="2">
<action>TOOL INVOCATION: Read `.GCC/resume.md` (if it exists) to retrieve the precise technical transition state and immediate next-action directives.</action>
</step>
<step id="3" phase="context_alignment">
<instruction>
Complete the context restoration (Step 1 and Step 2) prior to making any code or file modifications outside of the `.GCC/` directory. This ensures full alignment with the codebase state before taking action.
</instruction>
</step>
<step id="4">
<action>State the current technical objective loaded from `resume.md` using factual, concise French to align with the user.</action>
</step>
</protocol>

<protocol id="B" name="task_planning_and_execution">
<trigger>A complex, multi-session, or multi-file architectural change is initiated.</trigger>
<planning_threshold>
<instruction>
Reserve plan creation (`.GCC/branches/plan_[task_name].md`) for structural refactorings, package migrations, or multi-module tasks. For simple, single-file edits or quick bug fixes (< 10 minutes), proceed directly with implementation without generating a plan file.
</instruction>
</planning_threshold>
<step id="1">
<action>TOOL INVOCATION: Create the plan file `.GCC/branches/plan_[task_name].md` using the precise template below.</action>
</step>
<step id="2">
<action>TOOL INVOCATION: Update `.GCC/main.md` under `## 🌿 Active Branches / Plans` with the plan's exact file link and scope.</action>
</step>
<step id="3" execution="sequential_verification">
<instruction>
Execute the plan sequentially, step by step:
1. Modify the targeted code for the active step.
2. Run validation tools (tests, compilers, linters).
3. Paste the raw, unaltered terminal outputs into the plan file as proof of verification before modifying adjacent files or proceeding to the next step.
</instruction>
</step>
<step id="4" name="proactive_risk_management">
<instruction>
When documenting risks under "Mitigations & Edge Cases" in a plan file, proactively summarize the identified risk and proposed mitigation directly to the user in the chat. Do not wait for the user to read `.GCC/` files. Explicitly inform the user whether you are applying the mitigation autonomously or if their input/verification is required before proceeding.
</instruction>
</step>
</protocol>

<protocol id="C" name="decision_logging">
<trigger>Any package dependency change, design pattern choice, database schema modification, or structural API boundary pivot.</trigger>
<step id="1">
<action>
TOOL INVOCATION: Immediately append the technical choice, discarded alternative options, and concrete technical reasoning inside `.GCC/main.md` under `## 🧠 Decisions Made` at the moment the decision is established.
</action>
</step>
</protocol>

<protocol id="D" name="session_teardown_and_handoff">
<trigger>The user signals the end of the session, or the agent approaches context/token capacity limits.</trigger>
<step id="1">
<action>TOOL INVOCATION: Run the project's compilation and static validation tools to verify codebase integrity.</action>
</step>
<step id="2">
<action>TOOL INVOCATION: Update `.GCC/main.md` status, archiving completed milestones and updating active targets.</action>
</step>
<step id="3" verification="user_confirmation">
<instruction>
Maintain plan files in an active state until all related tasks and bugs are verified and logged in `.GCC/branches/test.md`, and the user provides explicit written confirmation in the chat to delete or archive the plan.
</instruction>
</step>
<step id="4" quality="technical_precision">
<action>
TOOL INVOCATION: Overwrite `.GCC/resume.md` with ultra-precise transition details.
</action>
<instruction>
Write technically descriptive entries that explicitly detail specific file paths, function signatures, modified line numbers, exact terminal commands, and raw error logs to ensure seamless handoff recovery.
</instruction>
</step>
</protocol>

<protocol id="E" name="test_session_sync">
<trigger>Completion of any automated or manual test run.</trigger>
<step id="1">
<action>TOOL INVOCATION: Move completed test scenarios from `.GCC/branches/test_afaire.md` to `.GCC/branches/test.md` with explicit results.</action>
</step>
<step id="2">
<action>TOOL INVOCATION: Append newly discovered bugs, regressions, or integration blocks to `.GCC/branches/test.md` immediately upon discovery.</action>
</step>
</protocol>

</event_driven_protocols>

<strict_markdown_templates>

### 3.1. `.GCC/main.md` Template

```markdown
# Current Project Context

## 🏆 Major Milestones (Archived Epics)

- [YYYY-MM-DD] Name of completed milestone/epic

## 🎯 Objective

[High-level description of what the project is solving or building]

## 🧠 Decisions Made

- [YYYY-MM-DD] [Technical choice name]
- **Context**: [Why the decision was necessary]
- **Discarded Options**: [Option A, Option B with brief technical rejection reasons]
- **Rationale**: [Concrete architectural justification for the selected path]

## 🌿 Active Branches / Plans

- `[branch-or-task-name]` : [Factual description of the task being solved and link to the plan file]

## 📈 Current Status

- ✅ Done: [List of high-level completed features]
- 🔄 In progress: [High-level epic currently being built]
- ⏳ Pending: [Remaining roadmap items]

## 👉 Next Session Direction

[Single sentence summarizing where the project points next]
```

### 3.2. `.GCC/branches/plan_[name].md` Template

````markdown
# Execution Plan: [Task Name]

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: [State the state/rule that must remain true during and after this task]
- **Pre-requisites**: [Required packages, configurations, or pre-existing code structures]

## 🛠️ Step-by-Step Sequence

### Step 1: [Short Action Description]

- [ ] **Action**: [Exact file path to edit or command to run]
- [ ] **Verify**: [Validation command, e.g., `npm test`, `tsc --noEmit`]
- **Verification Proof**:

```text
[Paste terminal/compiler validation output here]
```
````

### Step 2: [Short Action Description]

- [ ] **Action**: [Exact file path to edit or command to run]
- [ ] **Verify**: [Validation command]
- **Verification Proof**:

```text
[Paste validation output here]
```

## ⚠️ Mitigations & Edge Cases

- **Risk**: [Identify potential risk, e.g., API rate-limits, dependency clash]
- **Mitigation**: [Describe fallback behavior]

````

### 3.3. `.GCC/resume.md` Template

```markdown
# Session Handoff

## 🎯 Functional Outcome & Task Reality
- **Requested Task**: [Brief description of what was asked]
- **Functional Status**: [SUCCESS | PARTIAL | FAILED]
- **Behavioral Proof**: [Factual output of runtime test, execution result, or physical check proving whether the feature actually WORKS, independent of compilation]

## ⚡ Technical Diffs / Atomic Modifications
- **File**: `[path/to/modified_file_1.ext]`
- **Scope**: [Added/Modified functions or components]
- **Exact Technical Change**: [Factual description of the changes]

## 🛠️ Static Codebase Health
- **Verification Command Run**: `[e.g., npm run build && tsc --noEmit]`
- **Linter/Compiler Status**: [Paste clean terminal output showing 0 errors, 0 warnings]

## 🚧 Unfinished Work & Technical Failures
- **Blocker / Failure Explanation**: [If Functional Status is PARTIAL or FAILED, explain explicitly WHY it failed, raw error logs, and why static compilation was not enough]

## 👉 Handover Directives for the Next Agent
1. **Target File**: `[Specify exact file path to open first]`
2. **Immediate Action**: `[Specify exact next action or fix to apply]`
3. **Verification Command**: `[Command to run]`

````

---

</strict_markdown_templates>



# AGENTIC DIRECTIVE

> Keep AGENTS.md and CLAUDE.md identical.

## CODING ENVIRONMENT

- Install astral uv using "curl -LsSf https://astral.sh/uv/install.sh | sh" if not already installed and if already installed then update it to the latest version
- Install Python 3.14.0 stable using `uv python install 3.14.0` if not already installed (requires uv >=0.9; see `[tool.uv] required-version` in `pyproject.toml`)
- Always use `uv run` to run files instead of the global `python` command.
- Current uv ruff formatter is set to py314 which has supports multiple exception types without paranthesis (except TypeError, ValueError:)
- Read `.env.example` for environment variables.
- All CI checks must pass; failing checks block merge.
- Add tests for new changes (including edge cases).
- Before pushing, prefer `./scripts/ci.sh` (macOS/Linux) or `.\scripts\ci.ps1` (Windows) to run the local CI sequence; requires `uv` on PATH. The local scripts run Ruff in repair mode (`ruff format`, then `ruff check --fix`) before type checking and tests.
- Use `--only` / `--skip` (PowerShell: `-Only` / `-Skip`) to run a subset when iterating; use `--dry-run` to print commands without running them.
- GitHub CI remains check-only for Ruff (`ruff format --check`, `ruff check`) so branch protection verifies committed code.
- Fall back to individual repair commands when debugging local failures: `uv run ruff format`, `uv run ruff check --fix`, `uv run ty check`, `uv run pytest -v --tb=short`. Use GitHub-style checks only when verifying enforcement locally: `uv run ruff format --check`, `uv run ruff check`.
- Do not add `# type: ignore` or `# ty: ignore`; fix the underlying type issue.
- Do not add `from __future__ import annotations`; Python 3.14 native lazy annotations are the project standard.
- All 5 check IDs are represented in `scripts/ci.sh` / `scripts/ci.ps1` and enforced by `tests.yml` before each merge (parallel jobs: suppression grep, ruff-format, ruff-check, ty, pytest).
- GitHub CI runs only for pull requests targeting `main`. Strict required checks keep each PR current with `main`, so the tested PR tree is the tree squash-merged without a duplicate post-merge run.
- Repository protection should use rulesets: a non-bypassable main integrity ruleset requires pull requests and strict required checks, keeps branches current, and blocks direct/force pushes to `main`; a separate review ruleset may allow `Alishahryar1`/admins to bypass review only.
- Required status checks: set **required status checks** to **all** of those statuses (e.g. **Ban suppressions and legacy annotations**, **ruff-format**, **ruff-check**, **ty**, **pytest**—use the exact labels GitHub shows, which may be prefixed with **CI /**). Remove **ci** from required checks if it was previously added for the old gate job.

## IDENTITY & CONTEXT

- You are an expert Software Architect and Systems Engineer.
- Goal: Zero-defect, root-cause-oriented engineering for bugs; test-driven engineering for new features. Think carefully; no need to rush.
- Code: Write the simplest code possible. Keep the codebase minimal and modular.

## ARCHITECTURE PRINCIPLES

- **Shared utilities**: Put shared Anthropic protocol logic in neutral `src/free_claude_code/core/anthropic/` modules. Do not have one provider import from another provider's utils.
- **Failure ownership**: Keep canonical failure semantics and redaction SDK-free in `core/`; providers alone classify SDK/HTTP failures and own retries; protocol/API adapters alone choose wire error types and commit-boundary serialization.
- **DRY**: Extract shared base classes to eliminate duplication. Prefer composition over copy-paste.
- **Encapsulation**: Use accessor methods for internal state (e.g. `set_current_task()`), not direct `_attribute` assignment from outside.
- **Provider-specific config**: Keep provider-specific fields (e.g. `nim_settings`) in provider constructors, not in the base `ProviderConfig`.
- **Model-independent reasoning**: Resolve client reasoning intent once at the application boundary; provider adapters translate documented provider capabilities. Never branch on upstream model names or versions to choose reasoning behavior.
- **Dead code**: Remove unused code, legacy systems, and hardcoded values. Use settings/config instead of literals (e.g. `settings.provider_type` not `"nvidia_nim"`).
- **Performance**: Use list accumulation for strings (not `+=` in loops), cache env vars at init, prefer iterative over recursive when stack depth matters.
- **Platform-agnostic naming**: Use generic names (e.g. `PLATFORM_EDIT`) not platform-specific ones (e.g. `TELEGRAM_EDIT`) in shared code.
- **No type ignores**: Do not add `# type: ignore` or `# ty: ignore`. Fix the underlying type issue.
- **Python 3.14 annotations**: Do not use `from __future__ import annotations`; rely on native lazy annotations and fix circular import boundaries instead of hiding them with annotation stringization.
- **Imports**: Prefer top-level imports. Avoid `TYPE_CHECKING` and local imports for first-party or required dependencies; if a top-level import creates a cycle, move shared types/protocols to a neutral owner.
- **Complete migrations**: When moving modules, update imports to the new owner and remove old compatibility shims in the same change unless preserving a published interface is explicitly required.
- **Maximum Test Coverage**: There should be maximum test coverage for everything, preferably live smoke test coverage to catch bugs early

## COGNITIVE WORKFLOW

1. **ANALYZE**: Read relevant files. Do not guess.
2. **PLAN**: Map out the logic. Identify root cause or required changes. Order changes by dependency.
3. **EXECUTE**: Fix the cause, not the symptom. Execute incrementally with clear commits.
4. **VERIFY**: Run `./scripts/ci.sh` or `.\scripts\ci.ps1`, plus relevant smoke tests when needed. Confirm the fix via logs or output.
5. **SPECIFICITY**: Do exactly as much as asked; nothing more, nothing less.
6. **PROPAGATION**: Changes impact multiple files; propagate updates correctly.
7. **VERSION**: If the commit touches production files on `main`, bump semver in the same commit (see [Versioning](#versioning-main)).

## VERSIONING (MAIN)

Every commit on `main` that changes a **production file** must include a semver bump in **`pyproject.toml`** in the **same commit**. Do not merge or push prod changes without updating the version.

### Production files

These paths count as production (runtime, packaging, or install surface):

- `src/free_claude_code/api/`, `src/free_claude_code/cli/`, `src/free_claude_code/config/`, `src/free_claude_code/core/`, `src/free_claude_code/messaging/`, `src/free_claude_code/providers/`
- `src/free_claude_code/application/`
- `.env.example`
- `pyproject.toml` (dependencies, scripts, packaging)
- `scripts/install.sh`, `scripts/install.ps1`, `scripts/uninstall.sh`, `scripts/uninstall.ps1`, `scripts/ci.sh`, `scripts/ci.ps1`

These do **not** require a version bump on their own:

- `tests/`, `smoke/`
- Docs and assets: `README.md`, `assets/`, `AGENTS.md`, `CLAUDE.md`
- CI and repo config: `.github/`, `.gitignore`

If a single commit mixes production and non-production edits, still bump the version.

### Semver rules

Use `[project].version` as `MAJOR.MINOR.PATCH`:

- **PATCH** (`x.y.Z+1`): bug fixes, refactors with no user-visible behavior change, dependency updates, packaging/install fixes.
- **MINOR** (`x.Y+1.0`): backward-compatible features—new providers, admin fields, CLI commands, config options, or behavior additions.
- **MAJOR** (`X+1.0.0`): breaking changes—removed or renamed env vars, incompatible API/CLI/default changes, or migrations users must act on.

When unsure between PATCH and MINOR, prefer PATCH for fixes and MINOR for new capability.

### Required steps

1. Classify the change and choose the bump level.
2. Update `version` in `pyproject.toml`.
3. Run `uv lock` so `uv.lock` reflects the new package version.
4. Include the version and lockfile updates in the same commit as the production change.

Example commit on `main` after a packaging fix: bump `1.2.38` → `1.2.39`, run `uv lock`, commit together with the fix.

## SUMMARY STANDARDS

- Summaries must be technical and granular.
- Include: [Files Changed], [Logic Altered], [Verification Method], [Residual Risks] (if no residual risks then say none).

## TOOLS

- Prefer built-in tools (grep, read_file, etc.) over manual workflows. Check tool availability before use.
