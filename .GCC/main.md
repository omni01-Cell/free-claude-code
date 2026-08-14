# Current Project Context

## 🏆 Major Milestones (Archived Epics)
- 2026-08-14: **Version 4.28.4 Release sur `main`** :
  1. **Vérité Stricte des Modèles (Zéro Modèle en Dur / Zéro Alias Synthétique)** : Suppression définitive de tout dictionnaire d'alias (`ANTIGRAVITY_MODEL_ALIASES`) et de toute boucle d'injection synthétique. Le catalogue `/v1/models` et les requêtes reflètent exclusivement les modèles réels exposés par l'infrastructure Google en amont (`fetchAvailableModels`).
  2. **Isolation Stricte à 100% dans `~/.fcc/`** : Suppression complète du bootstrap ou fallback automatique depuis le Keyring système ou les dossiers hôtes (`~/.gemini/`). FCC opère exclusivement avec `~/.fcc/auth/antigravity/oauth.json`.
  3. **Résolution Backend Antigravity (`daily-cloudcode-pa.googleapis.com`)** : Élimination définitive de l'erreur `RESOURCE_EXHAUSTED` (faux 429) grâce au ciblage de l'endpoint actif avec failover réseau.
  4. **Validation Qualité CI** : 45 tests unitaires passés sur 45, typage `ty check` et `ruff check` passés à 100%.
- 2026-08-14: **Version 4.28.1 Release sur `main`** :
  1. Tolérance des outils serveur listés non forcés pour compatibilité universelle des providers OpenAI-compatibles et Claude Code CLI.
  2. Isolation modulaire des dossiers d'authentification par provider sous `~/.fcc/auth/{provider}/`.
  3. Découverte dynamique de modèles via `POST /v1internal:fetchAvailableModels`.
  4. Empreinte Antigravity CLI v1.1.13 et synchronisation dynamique `fcc-qwen`.
- 2026-08-12: **Version 4.24.0 Release sur `main`** : Intégration complète des adaptateurs universels `openai_compatible` et `anthropic_compatible`.

## 🎯 Objective
Maintenir le serveur proxy local free-claude-code à un niveau de qualité zéro-défaut pour Claude Code CLI, Codex, Pi et Qwen Code, assurer la compatibilité multi-provider et la conformité stricte aux garde-fous CI `./scripts/ci.sh`.

## 🧠 Decisions & Core Invariants (Règles Fondamentales)
- 2026-08-14: **RÈGLE INVARIANTE - VÉRITÉ API STRICTE ET INTERDICTION DES MODÈLES EN DUR** :
  - **Directive Utilisateur Absolue** : Ne JAMAIS coder en dur des listes de modèles, ne JAMAIS créer d'alias synthétiques qui modifient ou masquent ce que renvoie réellement l'API en amont.
  - **Rationale** : Modifier ou feindre les modèles retournés par une API est contraire à l'intégrité du proxy. Free Claude Code doit toujours exposer et utiliser fidèlement et exclusivement la réalité des modèles renvoyés par les providers.
- 2026-08-14: **RÈGLE INVARIANTE - ISOLATION STRICTE DES COMPTES DANS `~/.fcc/`** :
  - **Directive Utilisateur Absolue** : FCC ne doit JAMAIS lire, synchroniser silencieusement ou dépendre des comptes ou trousseaux de la machine hôte (`~/.gemini/`, Keyring/Secret Service).
  - **Rationale** : Étanchéité absolue entre la machine et l'environnement FCC. Si le jeton dans `~/.fcc/auth/<provider>/oauth.json` est absent, une erreur explicite `AuthenticationError` doit être levée pour inviter à se connecter via FCC.
- 2026-08-14: **Routage Backend Antigravity `daily-cloudcode-pa.googleapis.com`** :
  - **Context** : L'endpoint legacy `cloudcode-pa.googleapis.com` renvoie de faux codes 429 RESOURCE_EXHAUSTED sur les comptes Pro/Free.
  - **Rationale** : Routage par défaut sur `daily-cloudcode-pa.googleapis.com` avec failover transparent en cas d'erreur réseau.
- 2026-08-14: **Tolérance des Outils Serveur Listés Non Forcés** : Modification de `unsupported_server_tool_error` pour n'interdire que les outils serveur explicitement forcés par `tool_choice` lorsque `ENABLE_WEB_SERVER_TOOLS=false`.
- 2026-08-14: **Catalogue Qwen Code sous Protocole Anthropic** : Synchronisation non destructive du catalogue complet `/v1/models` dans `~/.qwen/settings.json` sous `modelProviders.anthropic`.

## 🌿 Active Branches / Plans
- `plan_strict_fcc_auth_isolation` : Isolation stricte à 100% de l'authentification Google Antigravity dans `~/.fcc/auth/antigravity/` sans lecture des sources hôtes ([`.GCC/branches/plan_strict_fcc_auth_isolation.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_strict_fcc_auth_isolation.md)).
- `plan_antigravity_endpoint_and_model_resolution` : Résolution de l'erreur `RESOURCE_EXHAUSTED` du provider Google Antigravity via l'endpoint actif `daily-cloudcode-pa.googleapis.com` ([`.GCC/branches/plan_antigravity_endpoint_and_model_resolution.md`](file:///home/omni/free-claude-code/.GCC/branches/plan_antigravity_endpoint_and_model_resolution.md)).

## 📈 Current Status
- ✅ Done: Version 4.28.4 déployée sur `main`, règles de vérité API et d'isolation stricte gravées dans l'architecture et vérifiées par les tests.
- 🔄 In progress: Aucun.
- ⏳ Pending: Nouveaux retours ou tâches utilisateur.

## 👉 Next Session Direction
Le proxy Free Claude Code opère en conformité intégrale avec les règles d'isolation stricte et de vérité des modèles de l'API sur la version 4.28.4.
