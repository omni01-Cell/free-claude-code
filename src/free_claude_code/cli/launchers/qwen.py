"""Installed `fcc-qwen` launcher."""

import os
import sys
from collections.abc import Mapping, Sequence

from free_claude_code.cli.local_http import with_local_proxy_bypass
from free_claude_code.cli.proxy_auth import proxy_auth_token
from free_claude_code.config.server_urls import local_proxy_root_url
from free_claude_code.config.settings import get_settings

from .common import preflight_proxy, resolve_client_binary, run_client_process

_DISPLAY_NAME = "Qwen Code"
_DEFAULT_BINARY = "qwen"
_INSTALL_HINT = "Install Qwen Code with: npm install -g @qwen-code/qwen-code@latest"
_STRIPPED_QWEN_ENV_KEYS = frozenset(
    {
        "OPENAI_API_BASE",
        "OPENAI_ORG_ID",
        "OPENAI_ORGANIZATION",
    }
)


def launch(argv: Sequence[str] | None = None) -> None:
    """Launch Qwen Code with Free Claude Code proxy configuration."""

    args = list(sys.argv[1:] if argv is None else argv)
    settings = get_settings()
    proxy_root_url = local_proxy_root_url(settings)
    if error := preflight_proxy(proxy_root_url):
        print(
            f"Free Claude Code proxy is not reachable at {proxy_root_url}: {error}",
            file=sys.stderr,
        )
        print("Start it in another terminal with: fcc-server", file=sys.stderr)
        raise SystemExit(1)

    binary_name = qwen_binary_name()
    binary_path = resolve_client_binary(
        binary_name=binary_name,
        display_name=_DISPLAY_NAME,
        install_hint=_INSTALL_HINT,
    )
    run_client_process(
        command=build_qwen_launcher_command(
            binary_path=binary_path,
            argv=args,
        ),
        env=build_qwen_launcher_env(
            proxy_root_url=proxy_root_url,
            auth_token=settings.anthropic_auth_token,
            model=getattr(settings, "model", None),
            base_env=os.environ,
        ),
        binary_name=binary_name,
        display_name=_DISPLAY_NAME,
        install_hint=_INSTALL_HINT,
    )


def qwen_binary_name() -> str:
    """Return the Qwen Code binary name."""

    return _DEFAULT_BINARY


def build_qwen_launcher_command(
    *,
    binary_path: str,
    argv: Sequence[str],
) -> list[str]:
    """Return a Qwen Code command without altering user arguments."""

    return [binary_path, *argv]


def build_qwen_launcher_env(
    *,
    proxy_root_url: str,
    auth_token: str,
    model: str | None = None,
    base_env: Mapping[str, str],
) -> dict[str, str]:
    """Return an environment targeting the FCC OpenAI-compatible endpoint."""

    env = with_local_proxy_bypass(
        {
            key: value
            for key, value in base_env.items()
            if key not in _STRIPPED_QWEN_ENV_KEYS
        },
        proxy_root_url=proxy_root_url,
    )
    env["OPENAI_BASE_URL"] = _ensure_v1_url(proxy_root_url)
    env["OPENAI_API_KEY"] = proxy_auth_token(auth_token)
    if model and model.strip():
        env["OPENAI_MODEL"] = model.strip()
    return env


def _ensure_v1_url(url: str) -> str:
    stripped = url.rstrip("/")
    return stripped if stripped.endswith("/v1") else f"{stripped}/v1"
