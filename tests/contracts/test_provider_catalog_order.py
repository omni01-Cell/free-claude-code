"""Freeze ``PROVIDER_CATALOG`` insertion order used as canonical provider ranking."""

from __future__ import annotations

from config.provider_catalog import PROVIDER_CATALOG, SUPPORTED_PROVIDER_IDS

_EXPECTED_PROVIDER_ORDER: tuple[str, ...] = (
    "nvidia_nim",
    "open_router",
    "gemini",
    "deepseek",
    "mistral",
    "codestral",
    "mistral_codestral",
    "opencode",
    "opencode_go",
    "wafer",
    "kimi",
    "cerebras",
    "groq",
    "fireworks",
    "zai",
    "lmstudio",
    "llamacpp",
    "ollama",
)


def test_provider_catalog_key_order_matches_canonical_plan() -> None:
    """NIM first; DeepSeek fourth; Wafer tenth / Kimi eleventh (see contributor plan)."""

    assert tuple(PROVIDER_CATALOG.keys()) == _EXPECTED_PROVIDER_ORDER
    assert SUPPORTED_PROVIDER_IDS == _EXPECTED_PROVIDER_ORDER
