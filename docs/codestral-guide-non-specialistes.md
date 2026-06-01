# Guide Codestral pour non-spécialistes

Ce guide explique, pas à pas, comment installer Free Claude Code et le configurer avec le provider **Codestral**. L’objectif est de pouvoir utiliser Claude Code avec le modèle `codestral/codestral-latest`, sans modifier de fichiers à la main.

## À quoi sert Free Claude Code ?

Free Claude Code est un petit serveur local. Il reçoit les requêtes de Claude Code, puis les envoie au provider de modèle que vous choisissez. Ici, le provider choisi est **Codestral**, via l’adresse `https://codestral.mistral.ai/v1`.

En pratique, vous lancerez deux choses :

1. `fcc-server` : le serveur local Free Claude Code.
2. `fcc-claude` : le lanceur Claude Code déjà configuré pour parler à ce serveur local.

## Ce qu’il vous faut avant de commencer

- Un ordinateur macOS, Linux, ou Windows.
- Une connexion Internet.
- Une clé API Codestral, à copier dans `CODESTRAL_API_KEY`.
- Un terminal : Terminal sur macOS/Linux, PowerShell sur Windows.

Vous n’avez pas besoin de connaître Python, FastAPI, Anthropic, ou OpenAI pour suivre ce guide.

## Étape 1 — Installer Free Claude Code

### macOS ou Linux

Ouvrez un terminal, copiez-collez cette commande, puis appuyez sur Entrée :

```bash
curl -fsSL "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.sh?raw=1" | sh
```

### Windows PowerShell

Ouvrez PowerShell, copiez-collez cette commande, puis appuyez sur Entrée :

```powershell
irm "https://github.com/Alishahryar1/free-claude-code/blob/main/scripts/install.ps1?raw=1" | iex
```

L’installateur prépare les commandes `fcc-server` et `fcc-claude`. Si Claude Code n’est pas encore installé, l’installateur vous indique aussi quoi faire.

## Étape 2 — Démarrer le serveur local

Dans votre terminal, lancez :

```bash
fcc-server
```

Gardez cette fenêtre ouverte. Elle héberge le proxy local.

Après le démarrage, cherchez une ligne qui ressemble à ceci :

```text
Admin UI: http://127.0.0.1:8082/admin
```

Ouvrez cette adresse dans votre navigateur. Si votre installation utilise un autre port que `8082`, utilisez l’adresse affichée dans votre terminal.

## Étape 3 — Configurer Codestral dans l’Admin UI

Dans l’Admin UI :

1. Ouvrez l’onglet **Providers** si vous n’y êtes pas déjà.
2. Trouvez le champ **Codestral API Key** ou `CODESTRAL_API_KEY`.
3. Collez votre clé API Codestral.
4. Ouvrez l’onglet **Model Config**.
5. Dans le champ `MODEL`, mettez :

```text
codestral/codestral-latest
```

6. Cliquez sur **Validate**.
7. Si la validation ne signale pas d’erreur, cliquez sur **Apply**.

Le préfixe important est `codestral/`. Il indique à Free Claude Code d’utiliser le provider Codestral. L’ancien préfixe `mistral_codestral/` reste accepté pour les anciennes configurations, mais utilisez `codestral/` pour une nouvelle installation.

## Étape 4 — Lancer Claude Code

Ouvrez un deuxième terminal, puis lancez :

```bash
fcc-claude
```

Utilisez Claude Code normalement. Le lanceur `fcc-claude` configure automatiquement Claude Code pour utiliser le proxy local déjà démarré avec `fcc-server`.

## Étape 5 — Vérifier que tout fonctionne

Dans Claude Code, envoyez une demande très simple, par exemple :

```text
Réponds uniquement: OK
```

Si Claude Code répond, l’installation fonctionne.

Vous pouvez aussi retourner dans l’Admin UI et vérifier que :

- `CODESTRAL_API_KEY` est renseigné.
- `MODEL` vaut `codestral/codestral-latest`.
- La validation ne signale pas de clé manquante.

## Erreurs fréquentes et solutions simples

### `CODESTRAL_API_KEY is not set`

Votre clé Codestral n’a pas été enregistrée.

Solution : retournez dans l’Admin UI, collez la clé dans `CODESTRAL_API_KEY`, puis cliquez sur **Validate** et **Apply**.

### Claude Code ne répond pas

Vérifiez que `fcc-server` tourne encore dans le premier terminal. Si vous avez fermé ce terminal, relancez :

```bash
fcc-server
```

Puis relancez Claude Code dans un autre terminal :

```bash
fcc-claude
```

### Mauvais modèle ou mauvais provider

Vérifiez que `MODEL` commence bien par :

```text
codestral/
```

Pour Codestral, un exemple sûr est :

```text
codestral/codestral-latest
```

### L’Admin UI ne s’ouvre pas

Vérifiez l’adresse exacte affichée par `fcc-server`. Par défaut, elle ressemble à :

```text
http://127.0.0.1:8082/admin
```

Si le terminal affiche un autre port, remplacez `8082` par ce port.

## Configuration avancée facultative

Vous pouvez garder `MODEL` sur Codestral et utiliser d’autres providers seulement pour certains niveaux Claude :

- `MODEL_OPUS`
- `MODEL_SONNET`
- `MODEL_HAIKU`

Pour une première installation, laissez ces champs vides. Ils hériteront de `MODEL`, donc de Codestral.

## Résumé rapide

1. Installer Free Claude Code.
2. Lancer `fcc-server`.
3. Ouvrir `http://127.0.0.1:8082/admin`.
4. Mettre votre clé dans `CODESTRAL_API_KEY`.
5. Mettre `MODEL` à `codestral/codestral-latest`.
6. Cliquer **Validate**, puis **Apply**.
7. Lancer `fcc-claude` dans un deuxième terminal.
