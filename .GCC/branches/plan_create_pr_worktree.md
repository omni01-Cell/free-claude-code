# Execution Plan: Create PR Worktree and Prepare Upstream Submission Branch

## 📋 Target Invariant & Pre-requisites
- **Target Invariant**: A dedicated git worktree `/home/omni/free-claude-code-pr` on branch `pr/upstream-submission` is created. The install scripts (`scripts/install.sh`, `scripts/install.ps1`) and their tests are configured for upstream (`Alishahryar1/free-claude-code`). All features (Google Antigravity CLI, Connected Account, Codex Desktop launcher `fcc-codex-desktop`, stateful tool streaming deduplication) are present, intact, and 100% CI green.
- **Pre-requisites**: `main` branch is at `v4.23.0`, clean working tree.

## 🛠️ Step-by-Step Sequence

### Step 1: Create git worktree `/home/omni/free-claude-code-pr` on branch `pr/upstream-submission`
- [x] **Action**: `git worktree add -b pr/upstream-submission /home/omni/free-claude-code-pr main`
- [x] **Verify**: `git worktree list`
- **Verification Proof**:
```text
/home/omni/free-claude-code     c1478a9 [main]
/home/omni/free-claude-code-pr  c1478a9 [pr/upstream-submission]
```

### Step 2: Configure install scripts and installer tests for upstream in the worktree
- [x] **Action**: In `/home/omni/free-claude-code-pr`, update `scripts/install.sh`, `scripts/install.ps1`, and `tests/scripts/test_installers.py` to target `Alishahryar1/free-claude-code`.
- [x] **Verify**: `git diff scripts/ tests/scripts/`
- **Verification Proof**:
```text
[pr/upstream-submission 3eee4fb] feat(installers): target Alishahryar1 upstream repo archive URLs
 3 files changed, 7 insertions(+), 7 deletions(-)
```

### Step 3: Run full CI test suite in the worktree
- [x] **Action**: Run `./scripts/ci.sh` inside `/home/omni/free-claude-code-pr`.
- [x] **Verify**: 100% pass across all 5 check jobs (suppression grep, ruff-format, ruff-check, ty, pytest).
- **Verification Proof**:
```text
==> Ban suppressions and legacy annotations
==> ruff format: 546 files left unchanged
==> ruff check --fix: All checks passed!
==> ty check: All checks passed!
==> pytest: 2968 passed, 69 skipped in 117.90s (0:01:57)
All selected CI checks passed.
```

### Step 4: Commit changes and push `pr/upstream-submission` to `origin`
- [x] **Action**: Commit changes on `pr/upstream-submission` and push to `origin/pr/upstream-submission`.
- [x] **Verify**: `git push origin pr/upstream-submission` output and PR URL generation.
- **Verification Proof**:
```text
To https://github.com/omni01-Cell/free-claude-code.git
 * [new branch]      pr/upstream-submission -> pr/upstream-submission
```

## ⚠️ Mitigations & Edge Cases
- **Risk**: Environment/venv isolation in new worktree.
- **Mitigation**: `uv` automatically uses shared package cache and venv in worktree.
