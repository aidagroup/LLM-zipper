"""Command-line entry point: ``llm-zipper``."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from llm_zipper import __version__

ROADMAP = (
    "KV-cache compression across layers, heads and context lengths",
    "Theory of LLM tensorizability",
    "Efficient fine-tuning",
    "RAG compression with tensors",
    "Tensorization of RL agents",
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="llm-zipper",
        description="Know before you compress: cheaper, faster, energy-efficient LLMs.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)

    print(f"LLM-zipper {__version__} (pre-alpha)\n")
    print("Planned modules:")
    for item in ROADMAP:
        print(f"  - {item}")
    print("\nFollow progress: https://github.com/aidagroup/LLM-zipper")
    return 0
