import os
from collections.abc import Mapping
from pathlib import Path

FCC_CONFIG_DIRNAME = ".fcc"
FCC_ENV_FILENAME = ".env"
LEGACY_REPO_DIRNAME = "free-claude-code"
LEGACY_XDG_CONFIG_DIRNAME = ".config"
MESSAGING_STATE_DIRNAME = "agent_workspace"
FCC_LOGS_DIRNAME = "logs"
SERVER_LOG_FILENAME = "server.log"
CODEX_MODEL_CATALOG_FILENAME = "codex-model-catalog.json"
AUTH_DIRNAME = "auth"
OPENAI_AUTH_FILENAME = "openai.json"
OPENAI_AUTH_LOCK_FILENAME = "openai.lock"
QWEN_DIRNAME = ".qwen"
QWEN_SETTINGS_FILENAME = "settings.json"


def config_dir_path() -> Path:
    """Return the default user config directory."""

    return Path.home() / FCC_CONFIG_DIRNAME


def managed_env_path() -> Path:
    """Return the default user-managed env file path."""

    return config_dir_path() / FCC_ENV_FILENAME


def legacy_env_paths() -> tuple[Path, ...]:
    """Return legacy user env paths that can be migrated to ~/.fcc/.env."""

    home = Path.home()
    return (
        home / LEGACY_REPO_DIRNAME / FCC_ENV_FILENAME,
        home / LEGACY_XDG_CONFIG_DIRNAME / LEGACY_REPO_DIRNAME / FCC_ENV_FILENAME,
    )


def messaging_state_dir_path() -> Path:
    """Return the managed messaging state directory."""

    return config_dir_path() / MESSAGING_STATE_DIRNAME


def server_log_path() -> Path:
    """Return the canonical server log path."""

    return config_dir_path() / FCC_LOGS_DIRNAME / SERVER_LOG_FILENAME


def codex_model_catalog_path() -> Path:
    """Return the generated Codex model catalog path."""

    return config_dir_path() / CODEX_MODEL_CATALOG_FILENAME


def openai_auth_path() -> Path:
    """Return FCC's private ChatGPT credential file path."""

    return config_dir_path() / AUTH_DIRNAME / OPENAI_AUTH_FILENAME


def openai_auth_lock_path() -> Path:
    """Return the cross-process lock path for ChatGPT credentials."""

    return config_dir_path() / AUTH_DIRNAME / OPENAI_AUTH_LOCK_FILENAME


def qwen_dir_path(env: Mapping[str, str] | None = None) -> Path:
    """Return the global Qwen configuration directory path."""

    current_env = os.environ if env is None else env
    if qwen_home := current_env.get("QWEN_HOME"):
        path = Path(qwen_home).expanduser()
        return path if path.is_absolute() else (Path.cwd() / path).resolve()
    return Path.home() / QWEN_DIRNAME


def qwen_settings_path(env: Mapping[str, str] | None = None) -> Path:
    """Return the user-level Qwen settings.json path."""

    return qwen_dir_path(env) / QWEN_SETTINGS_FILENAME
