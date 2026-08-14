"""Build and synchronize Qwen Code model catalogs from FCC `/v1/models` route."""

import json
import uuid
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


def build_qwen_model_catalog(
    models_response: Mapping[str, Any],
    *,
    proxy_root_url: str,
) -> list[dict[str, Any]]:
    """Convert FCC `/v1/models` data into a list of Qwen Anthropic ModelConfigs."""

    data = models_response.get("data")
    if not isinstance(data, list):
        return []

    models: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for item in data:
        if not isinstance(item, Mapping):
            continue
        model_id = item.get("id")
        if not isinstance(model_id, str) or not model_id.strip():
            continue
        model_id = model_id.strip()
        if model_id in seen_ids:
            continue
        seen_ids.add(model_id)

        display_name = item.get("display_name")
        if not isinstance(display_name, str) or not display_name.strip():
            display_name = model_id

        models.append(
            {
                "id": model_id,
                "name": display_name.strip(),
                "baseUrl": proxy_root_url.rstrip("/"),
                "envKey": "ANTHROPIC_API_KEY",
                "description": "Free Claude Code provider model",
            }
        )

    return models


def sync_qwen_settings(
    settings_path: Path,
    models: Sequence[Mapping[str, Any]],
    *,
    default_model: str | None = None,
) -> bool:
    """Safely sync FCC models into Qwen settings.json preserving user config."""

    existing_config: dict[str, Any] = {}
    try:
        content = settings_path.read_text(encoding="utf-8")
        loaded = json.loads(content)
        if isinstance(loaded, dict):
            existing_config = loaded
    except FileNotFoundError, json.JSONDecodeError, OSError:
        existing_config = {}

    model_providers = existing_config.setdefault("modelProviders", {})
    if not isinstance(model_providers, dict):
        model_providers = {}
        existing_config["modelProviders"] = model_providers

    model_providers["anthropic"] = list(models)

    security = existing_config.setdefault("security", {})
    if isinstance(security, dict):
        auth = security.setdefault("auth", {})
        if isinstance(auth, dict):
            auth["selectedType"] = "anthropic"

    model_section = existing_config.setdefault("model", {})
    if isinstance(model_section, dict):
        if default_model and default_model.strip():
            model_section["name"] = default_model.strip()
        elif "name" not in model_section and models:
            first_model = models[0].get("id")
            if isinstance(first_model, str) and first_model:
                model_section["name"] = first_model

    new_bytes = (
        json.dumps(existing_config, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    try:
        if settings_path.read_bytes() == new_bytes:
            return False
    except FileNotFoundError:
        pass

    settings_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = settings_path.with_name(f".{settings_path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temp_path.write_bytes(new_bytes)
        temp_path.replace(settings_path)
    finally:
        temp_path.unlink(missing_ok=True)
    return True
