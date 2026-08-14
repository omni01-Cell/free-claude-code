# Current Project Context

## 🏆 Major Milestones (Archived Epics)
- 2026-08-14: **Version 4.28.0 Release sur `main`** :
  1. Isolation stricte et dédiée du stockage d'authentification des providers sous `~/.fcc/auth/{provider}/` :
     - Google Antigravity : `~/.fcc/auth/antigravity/oauth.json`, `oauth.lock` et `google_accounts.json`
     - OpenAI / Codex : `~/.fcc/auth/openai/oauth.json` et `oauth.lock`
  2. Découplage total avec l'hôte : la déconnexion et la gestion de session dans FCC ne touchent plus les sessions de l'hôte (`~/.gemini/`, etc.).
  3. Découverte directe des modèles Google Antigravity via l'endpoint officiel `POST /v1internal:fetchAvailableModels` (support complet de Gemini 3.7 Flash).
  4. Renommage officiel du fournisseur en **Google Antigravity** dans le catalogue (`display_name = "Google Antigravity"`).
  5. Résolution de l'affichage de l'identité de compte dans l'interface d'administration.
  6. Empreinte HTTP mise à jour vers CLI v1.1.13.
  7. Synchronisation dynamique du catalogue complet de modèles de Free Claude Code (`/v1/models`) dans la configuration `~/.qwen/settings.json` lors du lancement de `fcc-qwen`.
  8. Validation intégrale de la suite CI (**2993 tests passés**, 59 skipped, 0 erreurs Ruff / Ty).
- 2026-08-12: **Version 4.24.0 Release sur `main`** : Intégration complète des adaptateurs universels `openai_compatible` et `anthropic_compatible`, extension à 7 providers personnalisés et 5 providers amont réconciliés.
- 2026-08-12: Réconciliation et fusion des 5 commits amont sur la branche `upstream-sync` et `main`.

## 🎯 Objective
Maintenir le serveur proxy local free-claude-code à un niveau de qualité zéro-défaut pour Claude Code CLI, Codex, Pi et Qwen Code, assurer la compatibilité multi-provider et la conformité stricte aux garde-fous CI `./scripts/ci.sh`.

## 🧠 Decisions Made
- 2026-08-14: **Isolation du Stockage d'Authentification par Provider** : Architecture sous `~/.fcc/auth/<provider>/oauth.json` résolue par `paths.py` (`antigravity_auth_path`, `openai_auth_path`), éliminant tout risque de conflit, de bascule de compte involontaire ou de modification destructrice sur les fichiers hôtes (`~/.gemini/`, `~/.codex/`).
- 2026-08-14: **Découverte Directe de Modèles `fetchAvailableModels`** : Remplacement des endpoints de quota obsolètes (`retrieveUserQuota`) par l'endpoint officiel `/v1internal:fetchAvailableModels` qui expose le catalogue dynamique complet des modèles Gemini (y compris Gemini 3.7 Flash).
- 2026-08-14: **Identification Multi-Provider dans l'Admin UI** : Découplage de `connectedAccountMeta` et des boîtes de dialogue de déconnexion pour utiliser dynamiquement `display_name` et `status.email` spécifique à chaque provider au lieu d'une valeur de repli OpenAI hardcodée.
- 2026-08-14: **Catalogue Qwen Code sous Protocole Anthropic** : Synchronisation non destructive du catalogue complet `/v1/models` dans `~/.qwen/settings.json` sous `modelProviders.anthropic`.
- 2026-08-14: **Factorisation HTTP Launcher** : Centralisation de `fetch_proxy_models_response` dans `src/free_claude_code/cli/launchers/common.py`.

## 🌿 Active Branches / Plans
- `plan_isolated_auth_paths` : Isolation complète des fichiers d'authentification et de comptes (Google Antigravity et Codex/OpenAI) sous `~/.fcc/auth/{provider}/` ([`.GCC/branches/plan_isolated_auth_paths.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_isolated_auth_paths.md)).
- `plan_gemini_37_direct_api_discovery` : Découverte directe des modèles Google Antigravity (Gemini 3.7 Flash, etc.) via l'endpoint `/v1internal:fetchAvailableModels` ([`.GCC/branches/plan_gemini_37_direct_api_discovery.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_gemini_37_direct_api_discovery.md)).
- `plan_antigravity_fingerprint_and_qwen_models` : Mise à jour de l'empreinte Antigravity CLI vers v1.1.13, renommage Google Antigravity, extraction email et synchronisation dynamique du catalogue complet de modèles pour `fcc-qwen` ([`.GCC/branches/plan_antigravity_fingerprint_and_qwen_models.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_antigravity_fingerprint_and_qwen_models.md)).

## 📈 Current Status
- ✅ Done: Version 4.28.0 implémentée, isolée et validée (2993 tests passés, 0 warnings/erreurs).
- 🔄 In progress: Aucun (tâche terminée avec succès).
- ⏳ Pending: Nouveaux retours ou tâches utilisateur.

## 👉 Next Session Direction
Le proxy et l'ensemble des 4 lanceurs CLI (`fcc-claude`, `fcc-codex`, `fcc-pi`, `fcc-qwen`) sont pleinement synchronisés et validés sur la version 4.28.0 avec l'authentification isolée.
