# Execution Plan: Strict FCC Auth Isolation for Antigravity

## 📋 Target Invariant & Pre-requisites

- **Target Invariant**: FCC lit et écrit exclusivement ses jetons dans `~/.fcc/auth/antigravity/oauth.json` (et `ANTIGRAVITY_TOKEN_FILE` / `ANTIGRAVITY_ACCESS_TOKEN` si définis dans l'environnement), sans aucun fallback ni bootstrap automatique depuis le trousseau système (Secret Service / Keyring) ou les dossiers hôtes (`~/.gemini/`).
- **Pre-requisites**: Jeton configuré dans `~/.fcc/auth/antigravity/oauth.json`.

## 🛠️ Step-by-Step Sequence

### Step 1: Nettoyage et verrouillage de `auth.py`

- [x] **Action**: Modifier [`src/free_claude_code/providers/antigravity/auth.py`](file:///home/omni/free-claude-code/src/free_claude_code/providers/antigravity/auth.py) pour restreindre strictement la découverte de jetons à `~/.fcc/auth/antigravity/oauth.json`.
- [x] **Verify**: `uv run pytest tests/providers/test_antigravity_auth.py -v`
- **Verification Proof**:

```text
============================== 23 passed in 10.45s ==============================
```

### Step 2: Mise à jour des tests unitaires

- [x] **Action**: Adapter [`tests/providers/test_antigravity_auth.py`](file:///home/omni/free-claude-code/tests/providers/test_antigravity_auth.py) pour valider l'absence de lecture des sources hôtes.
- [x] **Verify**: `uv run pytest tests/providers/test_antigravity_auth.py tests/providers/test_antigravity_client.py -v`
- **Verification Proof**:

```text
============================== 45 passed in 7.07s ==============================
```

### Step 3: Contrôle qualité statique et validation en direct

- [x] **Action**: Exécuter `uv run ty check`, `uv run ruff check` et un test de streaming en direct.
- [x] **Verify**: `uv run ty check && uv run ruff check`
- **Verification Proof**:

```text
All checks passed!
All checks passed!
```

## ⚠️ Mitigations & Edge Cases

- **Risk**: Un utilisateur avec un dossier `~/.fcc/` vide tente de lancer FCC sans s'authentifier.
- **Mitigation**: `AuthenticationError` explicite indiquant d'ouvrir `fcc-server` ou de se connecter dans `~/.fcc/`.
