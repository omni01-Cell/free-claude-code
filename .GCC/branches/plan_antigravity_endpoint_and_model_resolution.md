# Execution Plan: Antigravity Endpoint and Model Resolution

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: `AntigravityProvider` route les requêtes vers l'endpoint actif `https://daily-cloudcode-pa.googleapis.com` avec failover, supporte la récupération de session depuis le Keyring système et résout les alias de modèles Claude / Gemini sans lever d'erreur `RESOURCE_EXHAUSTED` ni `MODEL_CAPACITY_EXHAUSTED`.
- **Pre-requisites**: Jeton OAuth valide dans `~/.fcc/auth/antigravity/oauth.json` ou dans le Keyring système.

## 🛠️ Step-by-Step Sequence

### Step 1: Mettre à jour les URLs de base et le support Keyring dans `auth.py`

- [x] **Action**: Modifier [`src/free_claude_code/providers/antigravity/auth.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/auth.py) pour définir `ANTIGRAVITY_DEFAULT_BASE_URL = "https://daily-cloudcode-pa.googleapis.com"`, ajouter le support de lecture du Secret Service (`gemini:antigravity`) et la synchronisation automatique.
- [x] **Verify**: `uv run pytest tests/providers/test_antigravity_auth.py -v`
- **Verification Proof**:

```text
============================= 23 passed in 15.20s ==============================
```

### Step 2: Intégrer l'aliasing des modèles et le failover d'endpoint dans `client.py`

- [x] **Action**: Modifier [`src/free_claude_code/providers/antigravity/client.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/client.py) pour mapper les alias de modèles (`claude-3-7-sonnet` -> `claude-sonnet-4-6`, `gemini-2.5-pro` -> `gemini-3.6-flash-high`, etc.) et gérer le failover d'endpoint.
- [x] **Verify**: `uv run pytest tests/providers/test_antigravity_client.py -v`
- **Verification Proof**:

```text
============================= 44 passed in 22.41s ==============================
```

### Step 3: Validation complète de la suite CI et test fonctionnel en direct

- [x] **Action**: Exécuter `uv run ty check` et un script de streaming en direct pour Gemini et Claude.
- [x] **Verify**: Streaming en direct `stream_response` 200 OK + `ty check`
- **Verification Proof**:

```text
All checks passed!
=== Testing AntigravityProvider with claude-3-7-sonnet (mapped to claude-sonnet-4-6) ===
event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": " Claude Parfait"}}
```

## ⚠️ Mitigations & Edge Cases

- **Risk**: Indisponibilité temporaire de `daily-cloudcode-pa.googleapis.com`.
- **Mitigation**: Failover transparent vers `cloudcode-pa.googleapis.com` en cas d'erreur réseau 5xx ou 404.
