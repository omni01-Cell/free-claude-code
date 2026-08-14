# Execution Plan: Antigravity Fingerprint Update v1.1.13 & Qwen Model Catalog Sync

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: Préservation stricte de la conformité CI (0 erreurs de typage, 0 avertissements linter, 100% tests réussis), intégrité des fichiers utilisateurs `settings.json`, et cohérence de l'empreinte HTTP Antigravity.
- **Pre-requisites**: `uv` et Python 3.14 installés, suite de tests fonctionnelle.

## 🛠️ Step-by-Step Sequence

### Step 1: Mise à jour de l'empreinte Antigravity v1.1.13

- [x] **Action**: Modifier [`src/free_claude_code/providers/antigravity/auth.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/auth.py), [`src/free_claude_code/providers/antigravity/client.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/client.py), [`scripts/antigravity_login.py`](file:///home/omni/free-claude-code/scripts/antigravity_login.py) et la documentation [`docs/documentations/providers/antigravity-explanation.md`](file:///home/omni/free-claude-code/docs/documentations/providers/antigravity-explanation.md).
- [x] **Verify**: `uv run pytest tests/providers/test_antigravity_auth.py tests/providers/test_antigravity_client.py`
- **Verification Proof**:

```text
============================== 35 passed in 2.65s ==============================
```

### Step 2: Création de `qwen_model_catalog.py` et mise à jour de `paths.py`

- [x] **Action**: Ajouter `qwen_dir_path` et `qwen_settings_path` dans [`src/free_claude_code/config/paths.py`](file:///home/omni/free-claude-code/src/free_claude_code/config/paths.py), et implémenter [`src/free_claude_code/cli/launchers/qwen_model_catalog.py`](file:///home/omni/free-claude-code/src/free_claude_code/cli/launchers/qwen_model_catalog.py).
- [x] **Verify**: `uv run ty check`
- **Verification Proof**:

```text
All checks passed!
```

### Step 3: Intégration du catalogue complet dans `fcc-qwen` (`qwen.py`)

- [x] **Action**: Modifier [`src/free_claude_code/cli/launchers/qwen.py`](file:///home/omni/free-claude-code/src/free_claude_code/cli/launchers/qwen.py) pour charger `/v1/models` et synchroniser `settings.json` au lancement.
- [x] **Verify**: `uv run pytest tests/cli/test_entrypoints.py`
- **Verification Proof**:

```text
============================== 52 passed in 8.60s ==============================
```

### Step 4: Tests unitaires, packaging (`v4.26.0`), documentation et validation CI

- [x] **Action**: Mettre à jour [`pyproject.toml`](file:///home/omni/free-claude-code/pyproject.toml), exécuter `uv lock`, ajouter les tests dans [`tests/cli/test_entrypoints.py`](file:///home/omni/free-claude-code/tests/cli/test_entrypoints.py) et valider `./scripts/ci.sh`.
- [x] **Verify**: `./scripts/ci.sh`
- **Verification Proof**:

```text
==> Ban suppressions and legacy annotations: CLEAN (0 found)
==> ruff format: 547 files already formatted
==> ruff check: All checks passed!
==> ty check: All checks passed!
==> pytest: 2988 passed, 59 skipped in 81.36s
```

## ⚠️ Mitigations & Edge Cases

- **Risk**: Écrasement accidentel des préférences personnalisées de l'utilisateur dans `~/.qwen/settings.json`.
- **Mitigation**: `sync_qwen_settings` effectue un chargement non destructif en préservant toutes les clés non liées aux modèles (`ui`, `tools`, `mcp`, etc.) et écrit de façon atomique avec un fichier temporaire unique.
