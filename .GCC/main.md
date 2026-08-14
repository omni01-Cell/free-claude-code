# Current Project Context

## 🏆 Major Milestones (Archived Epics)
- 2026-08-14: **Version 4.26.0 Release sur `main`** :
  1. Découverte directe des modèles Google Antigravity via l'endpoint officiel `POST /v1internal:fetchAvailableModels` : découverte dynamique et support complet de **Gemini 3.7 Flash** (`gemini-3.7-flash-high`, `gemini-3.7-flash-medium`, `gemini-3.7-flash-low`, `gemini-3.7-flash`, `gemini-3.7-flash-tiered`) et extraction des groupes de tri (`agentModelSorts`) et tiers.
  2. Renommage officiel du fournisseur en **Google Antigravity** dans le catalogue (`display_name = "Google Antigravity"`).
  3. Résolution de l'affichage de l'identité de compte dans l'interface d'administration : extraction robuste de l'email depuis `id_token`, les métadonnées de token et `google_accounts.json`, avec fallback adapté au fournisseur au lieu du texte hardcodé "ChatGPT subscription connected".
  4. Mise à jour de l'empreinte HTTP du provider Antigravity vers CLI v1.1.13 (`ANTIGRAVITY_USER_AGENT = "AntigravityCLI/1.1.13"` et `ANTIGRAVITY_GOOG_API_CLIENT = "gl-go/1.22.0 gd/1.1.13"`).
  5. Synchronisation automatique et dynamique du catalogue complet de modèles de Free Claude Code (`/v1/models`) dans la configuration `~/.qwen/settings.json` sous `modelProviders.anthropic` lors du lancement de `fcc-qwen`, rendant tous les modèles sélectionnables dans l'invite interactive `/model`.
  6. Validation intégrale de la suite CI (**2991 tests passés**, 59 skipped, 0 erreurs Ruff / Ty).
- 2026-08-12: **Version 4.24.0 Release sur `main`** : Intégration complète des adaptateurs universels `openai_compatible` et `anthropic_compatible`, extension à 7 providers personnalisés (Google Antigravity, Connected Account, AgentRouter, CommandCode, TokenRouter, Alibaba, OpenAI/Anthropic Compatible) et 5 providers amont réconciliés (Together AI, QwenCloud, xAI Grok, Novita AI, NaraRoute). Correctif de sécurité P1 du serveur OAuth callback (validation de token `state`). Lanceur `fcc-codex-desktop` et suite de documentation modulaire Diátaxis (`docs/documentations/`). Validation CI à 100% (**2969 tests passés**).
- 2026-08-12: Réconciliation et fusion des 5 commits amont (Together AI, QwenCloud, xAI Grok, Novita AI, NaraRoute) sur la branche `upstream-sync` et `main`. Bump version `v4.23.0`, `uv.lock` ré-généré et validation 100% CI (2968 tests passés avec `./scripts/ci.sh`).

## 🎯 Objective
Maintenir le serveur proxy local free-claude-code à un niveau de qualité zéro-défaut pour Claude Code CLI, Codex, Pi et Qwen Code, assurer la compatibilité multi-provider et la conformité stricte aux garde-fous CI `./scripts/ci.sh`.

## 🧠 Decisions Made
- 2026-08-14: **Découverte Directe de Modèles `fetchAvailableModels`** : Remplacement des endpoints de quota obsolètes (`retrieveUserQuota`) par l'endpoint officiel `/v1internal:fetchAvailableModels` qui expose le catalogue dynamique complet des modèles Gemini (y compris Gemini 3.7 Flash) avec leurs métadonnées de réflexion et quotas.
- 2026-08-14: **Identification Multi-Provider dans l'Admin UI** : Découplage de `connectedAccountMeta` et des boîtes de dialogue de déconnexion pour utiliser dynamiquement `display_name` et `status.email` spécifique à chaque provider au lieu d'une valeur de repli OpenAI hardcodée.
- 2026-08-14: **Catalogue Qwen Code sous Protocole Anthropic** : Synchronisation non destructive du catalogue complet `/v1/models` dans `~/.qwen/settings.json` sous `modelProviders.anthropic` (pointant vers `${ANTHROPIC_BASE_URL}/v1/messages`), permettant l'utilisation native du sélecteur interactif `/model` de Qwen Code avec la chaîne de streaming et d'outils de FCC.
- 2026-08-14: **Factorisation HTTP Launcher** : Centralisation de `fetch_proxy_models_response` dans `src/free_claude_code/cli/launchers/common.py` pour un usage partagé et DRY entre `codex.py` et `qwen.py`.
- 2026-08-12: **Adaptateurs de Compatibilité Universels** : Implémentation des providers `openai_compatible` et `anthropic_compatible` permettant de connecter dynamiquement n'importe quelle API ou proxy conforme sans ajouter de code d'adaptation dédié.
- 2026-08-12: **Sécurité OAuth PKCE** : Injection et vérification d'un token `state` crypto-sécurisé (`secrets.token_urlsafe(32)`) lors du callback OAuth local pour bloquer toute attaque d'injection/Login CSRF (faille P1 résolue).

## 🌿 Active Branches / Plans
- `plan_gemini_37_direct_api_discovery` : Découverte directe des modèles Google Antigravity (Gemini 3.7 Flash, etc.) via l'endpoint `/v1internal:fetchAvailableModels` ([`.GCC/branches/plan_gemini_37_direct_api_discovery.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_gemini_37_direct_api_discovery.md)).
- `plan_antigravity_fingerprint_and_qwen_models` : Mise à jour de l'empreinte Antigravity CLI vers v1.1.13, renommage Google Antigravity, extraction email et synchronisation dynamique du catalogue complet de modèles pour `fcc-qwen` ([`.GCC/branches/plan_antigravity_fingerprint_and_qwen_models.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_antigravity_fingerprint_and_qwen_models.md)).

## 📈 Current Status
- ✅ Done: Version 4.26.0 enrichie avec Gemini 3.7 Flash et validée (2991 tests passés, 0 warnings/erreurs).
- 🔄 In progress: Aucun (tâche terminée avec succès).
- ⏳ Pending: Nouveaux retours ou tâches utilisateur.

## 👉 Next Session Direction
Le proxy et l'ensemble des 4 lanceurs CLI (`fcc-claude`, `fcc-codex`, `fcc-pi`, `fcc-qwen`) sont pleinement synchronisés et validés sur la version 4.26.0 avec le support complet de Gemini 3.7 Flash.
