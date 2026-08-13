# Current Project Context

## 🏆 Major Milestones (Archived Epics)
- 2026-08-12: **Version 4.24.0 Release sur `main`** : Intégration complète des adaptateurs universels `openai_compatible` et `anthropic_compatible`, extension à 7 providers personnalisés (Google Antigravity CLI, Connected Account, AgentRouter, CommandCode, TokenRouter, Alibaba, OpenAI/Anthropic Compatible) et 5 providers amont réconciliés (Together AI, QwenCloud, xAI Grok, Novita AI, NaraRoute). Correctif de sécurité P1 du serveur OAuth callback (validation de token `state`). Lanceur `fcc-codex-desktop` et suite de documentation modulaire Diátaxis (`docs/documentations/`). Validation CI à 100% (**2969 tests passés**).
- 2026-08-12: Réconciliation et fusion des 5 commits amont (Together AI, QwenCloud, xAI Grok, Novita AI, NaraRoute) sur la branche `upstream-sync` et `main`. Bump version `v4.23.0`, `uv.lock` ré-généré et validation 100% CI (2968 tests passés avec `./scripts/ci.sh`).
- 2026-08-12: Correction des URL d'archives d'installation dans [`scripts/install.sh`](file:///home/omni/free-claude-code/scripts/install.sh) et [`scripts/install.ps1`](file:///home/omni/free-claude-code/scripts/install.ps1) pointant directement sur le fork `omni01-Cell/free-claude-code`.
- 2026-08-12: Intégration de Google Antigravity CLI en tant que Connected Account dans l'Admin UI (`v4.20.0`).
- 2026-08-12: Lanceur hybride Codex Desktop / ChatGPT GUI (`fcc-codex-desktop`) v4.19.3.

## 🎯 Objective
Maintenir le serveur proxy local free-claude-code à un niveau de qualité zéro-défaut pour Claude Code CLI et Codex, assurer la compatibilité multi-provider et la conformité stricte aux garde-fous CI `./scripts/ci.sh`.

## 🧠 Decisions Made
- 2026-08-12: **Adaptateurs de Compatibilité Universels** : Implémentation des providers `openai_compatible` et `anthropic_compatible` permettant de connecter dynamiquement n'importe quelle API ou proxy conforme sans ajouter de code d'adaptation dédié.
- 2026-08-12: **Sécurité OAuth PKCE** : Injection et vérification d'un token `state` crypto-sécurisé (`secrets.token_urlsafe(32)`) lors du callback OAuth local pour bloquer toute attaque d'injection/Login CSRF (faille P1 résolue).
- 2026-08-12: **Stratégie PRs Atomiques pour l'avenir** : Soumettre des Pull Requests amont ultra-ciblées (1 seule fonctionnalité par PR) pour faciliter la revue par l'auteur amont.

## 🌿 Active Branches / Plans
- `main` : Branche principale à jour (`v4.24.0`), 100% qualifiée avec 2969 tests passés et poussée sur `origin/main`.

## 📈 Current Status
- ✅ Done: Toutes les fonctionnalités, correctifs de sécurité, documentations et tests CI intégrés sur `main`. Branche temporaire PR nettoyée.
- 🔄 In progress: Fin de session enregistrée.

## 👉 Next Session Direction
Pour les prochaines contributions amont (`Alishahryar1`), préparer des PRs atomiques et très ciblées (ex: 1 PR dédiée uniquement à un provider ou un correctif).
