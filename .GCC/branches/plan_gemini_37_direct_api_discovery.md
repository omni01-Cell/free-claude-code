# Execution Plan: Direct Google Antigravity Model Fetch via `fetchAvailableModels`

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: `AntigravityProvider.list_model_ids()` interroge directement l'endpoint officiel `POST /v1internal:fetchAvailableModels` pour obtenir l'ensemble des modèles supportés et leurs déclinaisons en temps réel sans dépendre des quotas obsolètes de `retrieveUserQuota`.
- **Pre-requisites**: Authentification OAuth Google Antigravity valide ou jeton de test.

## 🛠️ Step-by-Step Sequence

### Step 1: Implémentation du fetch direct `fetchAvailableModels` dans `client.py`

- [ ] **Action**: Modifier [`src/free_claude_code/providers/antigravity/client.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/client.py) pour appeler `POST /v1internal:fetchAvailableModels`, parser les clés `models`, `agentModelSorts`, `tieredModelIds`, et inclure le mapping de toutes les variantes 3.7.
- [ ] **Verify**: `uv run python -c "..."`

### Step 2: Mise à jour et validation des tests unitaires

- [ ] **Action**: Adapter et étendre [`tests/providers/test_antigravity.py`](file:///home/omni/free-claude-code/tests/providers/test_antigravity.py).
- [ ] **Verify**: `uv run pytest tests/providers/test_antigravity.py -v`

### Step 3: Validation complète CI

- [ ] **Action**: Exécuter `./scripts/ci.sh`.
- [ ] **Verify**: `./scripts/ci.sh` (0 erreurs Ruff, 0 erreurs Ty, 100% tests passés).

## ⚠️ Mitigations & Edge Cases

- **Risk**: Si Google Cloud Code PA renvoie un code d'erreur HTTP transitoire sur `fetchAvailableModels`.
- **Mitigation**: Fallback gracieux sur les modèles par défaut connus et le CLI local `agy`.
