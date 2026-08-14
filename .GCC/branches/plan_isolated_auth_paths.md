# Execution Plan: Provider Authentication Isolation under `~/.fcc/auth/{provider}/oauth.json`

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: Free Claude Code stocke et gère l'ensemble de ses fichiers d'authentification et de comptes de manière isolée sous `~/.fcc/auth/antigravity/oauth.json`, `~/.fcc/auth/antigravity/google_accounts.json` et `~/.fcc/auth/openai/oauth.json` (résolus via [`paths.py`](file:///home/omni/free-claude-code/src/free_claude_code/config/paths.py)), sans modifier ni interférer avec la configuration de l'hôte (`~/.gemini/`, etc.).
- **Pre-requisites**: Module [`paths.py`](file:///home/omni/free-claude-code/src/free_claude_code/config/paths.py) configuré pour exposer les fonctions de chemins canoniques par fournisseur.

## 🛠️ Step-by-Step Sequence

### Step 1: Définition des chemins d'authentification dans `paths.py`

- [ ] **Action**: Modifier [`src/free_claude_code/config/paths.py`](file:///home/omni/free-claude-code/src/free_claude_code/config/paths.py) pour exposer `auth_dir_path()`, `antigravity_auth_dir_path()`, `antigravity_auth_path()`, `antigravity_auth_lock_path()`, `antigravity_accounts_path()`, `openai_auth_dir_path()`, `openai_auth_path()`, `openai_auth_lock_path()`.
- [ ] **Verify**: `uv run python -c "from free_claude_code.config.paths import antigravity_auth_path, openai_auth_path; print(antigravity_auth_path(), openai_auth_path())"`

### Step 2: Isolation de l'authentification Google Antigravity & OpenAI Codex

- [ ] **Action**: Adapter [`src/free_claude_code/providers/antigravity/auth.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/auth.py), [`scripts/antigravity_login.py`](file:///home/omni/free-claude-code/scripts/antigravity_login.py) et [`src/free_claude_code/providers/openai_codex/auth.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/openai_codex/auth.py).
- [ ] **Verify**: `uv run pytest tests/providers/test_antigravity_auth.py tests/providers/test_openai_codex_auth.py`

### Step 3: Alignement de l'Admin UI et statut

- [ ] **Action**: Modifier [`src/free_claude_code/config/admin/status.py`](file:///home/omni/free-claude-code/src/free_claude_code/config/admin/status.py) pour utiliser `antigravity_auth_path()`.
- [ ] **Verify**: `uv run pytest tests/api/test_admin.py`

### Step 4: Validation complète CI

- [ ] **Action**: Exécuter `./scripts/ci.sh`.
- [ ] **Verify**: `./scripts/ci.sh` (0 erreurs Ruff, 0 erreurs Ty, 100% tests passés).

## ⚠️ Mitigations & Edge Cases

- **Risk**: Première exécution sans token dans `~/.fcc/auth/`.
- **Mitigation**: Amorçage automatique (bootstrap/copy initial) des credentials existants de l'hôte vers `~/.fcc/auth/<provider>/` lors de la toute première découverte, garantissant une continuité transparente pour l'utilisateur.
