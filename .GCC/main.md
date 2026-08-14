# Current Project Context

## 🏆 Major Milestones (Archived Epics)
- 2026-08-14: **Version 4.28.1 Release sur `main`** :
  1. Correction du rejet des outils serveur Anthropic listés (`web_search` / `web_fetch`) : les requêtes contenant des outils serveur simplement listés (non forcés par `tool_choice`) ne sont plus rejetées avec une erreur `InvalidRequestError`, permettant l'utilisation transparente de modèles OpenAI-compatibles (NVIDIA NIM, DeepSeek, Groq, Qwen, etc.) avec `fcc-qwen` et Claude Code.
  2. Isolation stricte et dédiée du stockage d'authentification des providers sous `~/.fcc/auth/{provider}/` :
     - Google Antigravity : `~/.fcc/auth/antigravity/oauth.json`, `oauth.lock` et `google_accounts.json`
     - OpenAI / Codex : `~/.fcc/auth/openai/oauth.json` et `oauth.lock`
  3. Découplage total avec l'hôte : la déconnexion et la gestion de session dans FCC ne touchent plus les sessions de l'hôte (`~/.gemini/`, etc.).
  4. Découverte directe des modèles Google Antigravity via l'endpoint officiel `POST /v1internal:fetchAvailableModels` (support complet de Gemini 3.7 Flash).
  5. Renommage officiel du fournisseur en **Google Antigravity** dans le catalogue (`display_name = "Google Antigravity"`).
  6. Résolution de l'affichage de l'identité de compte dans l'interface d'administration.
  7. Empreinte HTTP mise à jour vers CLI v1.1.13.
  8. Synchronisation dynamique du catalogue complet de modèles de Free Claude Code (`/v1/models`) dans la configuration `~/.qwen/settings.json` lors du lancement de `fcc-qwen`.
  9. Validation intégrale de la suite CI (**3036 tests passés**, 59 skipped, 0 erreurs Ruff / Ty).
- 2026-08-12: **Version 4.24.0 Release sur `main`** : Intégration complète des adaptateurs universels `openai_compatible` et `anthropic_compatible`, extension à 7 providers personnalisés et 5 providers amont réconciliés.
- 2026-08-12: Réconciliation et fusion des 5 commits amont sur la branche `upstream-sync` et `main`.

## 🎯 Objective
Maintenir le serveur proxy local free-claude-code à un niveau de qualité zéro-défaut pour Claude Code CLI, Codex, Pi et Qwen Code, assurer la compatibilité multi-provider et la conformité stricte aux garde-fous CI `./scripts/ci.sh`.

## 🧠 Decisions Made
- 2026-08-14: **Tolérance des Outils Serveur Listés Non Forcés** : Modification de `unsupported_server_tool_error` pour n'interdire que les outils serveur explicitement *forcés* par `tool_choice` lorsque `ENABLE_WEB_SERVER_TOOLS=false`, tout en laissant passer les outils simplement déclarés dans la liste de capacités du client vers tous les providers.
- 2026-08-14: **Isolation du Stockage d'Authentification par Provider** : Architecture sous `~/.fcc/auth/<provider>/oauth.json` résolue par `paths.py` (`antigravity_auth_path`, `openai_auth_path`), éliminant tout risque de conflit, de bascule de compte involontaire ou de modification destructrice sur les fichiers hôtes (`~/.gemini/`, `~/.codex/`).
- 2026-08-14: **Découverte Directe de Modèles `fetchAvailableModels`** : Remplacement des endpoints de quota obsolètes (`retrieveUserQuota`) par l'endpoint officiel `/v1internal:fetchAvailableModels` qui expose le catalogue dynamique complet des modèles Gemini (y compris Gemini 3.7 Flash).
- 2026-08-14: **Identification Multi-Provider dans l'Admin UI** : Découplage de `connectedAccountMeta` et des boîtes de dialogue de déconnexion pour utiliser dynamiquement `display_name` et `status.email` spécifique à chaque provider.
- 2026-08-14: **Catalogue Qwen Code sous Protocole Anthropic** : Synchronisation non destructive du catalogue complet `/v1/models` dans `~/.qwen/settings.json` sous `modelProviders.anthropic`.
- 2026-08-14: **Suppression des Alias Synthétiques et Vérité API Stricte** : Suppression définitive de toute table de mapping en dur (`ANTIGRAVITY_MODEL_ALIASES`) et de toute injection de modèles synthétiques. Le provider Antigravity expose et accepte exclusivement les modèles découverts et supportés en direct par l'API Google en amont (`fetchAvailableModels`).

## 🌿 Active Branches / Plans
- `plan_strict_fcc_auth_isolation` : Isolation stricte à 100% de l'authentification Google Antigravity dans `~/.fcc/auth/antigravity/` sans lecture des sources hôtes ([`.GCC/branches/plan_strict_fcc_auth_isolation.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_strict_fcc_auth_isolation.md)).
- `plan_antigravity_endpoint_and_model_resolution` : Résolution de l'erreur `RESOURCE_EXHAUSTED` du provider Google Antigravity via l'endpoint actif `daily-cloudcode-pa.googleapis.com` ([`.GCC/branches/plan_antigravity_endpoint_and_model_resolution.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_antigravity_endpoint_and_model_resolution.md)).
- `plan_isolated_auth_paths` : Isolation complète des fichiers d'authentification et de comptes sous `~/.fcc/auth/{provider}/` ([`.GCC/branches/plan_isolated_auth_paths.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_isolated_auth_paths.md)).

## 📈 Current Status
- ✅ Done: Version 4.28.4 implémentée, vérité stricte des modèles sans aucun mapping ou injection en dur, 45 tests unitaires passés.
- 🔄 In progress: Aucun (tâche terminée avec succès).
- ⏳ Pending: Nouveaux retours ou tâches utilisateur.

## 👉 Next Session Direction
Le catalogue des modèles Antigravity reflète à 100% les modèles réels de l'API Google sur la version 4.28.4.
