#!/usr/bin/env python3
"""
Professional Python template (CLI app)

Features:
- Type hints + dataclasses
- Structured logging
- Centralized config
- Clean error handling
- Test-friendly architecture

Usage:
  python app.py --name "World" --repeat 2
"""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from typing import Sequence


# -----------------------------
# Configuration
# -----------------------------
@dataclass(frozen=True)
class AppConfig:
    name: str
    repeat: int
    log_level: str = "INFO"


# -----------------------------
# Logging
# -----------------------------
def setup_logging(level: str) -> None:
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level!r}")

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


# -----------------------------
# Business logic (replace this)
# -----------------------------
class GreeterService:
    def __init__(self) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)

    def greet(self, name: str, repeat: int) -> list[str]:
        if repeat < 1:
            raise ValueError("repeat must be >= 1")

        self._logger.debug("Creating greeting messages: name=%s repeat=%s", name, repeat)
        return [f"Hello, {name}!" for _ in range(repeat)]


# -----------------------------
# CLI / Parsing
# -----------------------------
def parse_args(argv: Sequence[str]) -> AppConfig:
    parser = argparse.ArgumentParser(description="Professional Python CLI template")
    parser.add_argument("--name", required=True, help="Name to greet")
    parser.add_argument("--repeat", type=int, default=1, help="Number of greetings (>= 1)")
    parser.add_argument("--log-level", default="INFO", help="DEBUG, INFO, WARNING, ERROR")

    args = parser.parse_args(argv)

    return AppConfig(
        name=args.name,
        repeat=args.repeat,
        log_level=args.log_level,
    )


# -----------------------------
# App Orchestration
# -----------------------------
def run_app(cfg: AppConfig) -> int:
    logger = logging.getLogger("app")
    logger.info("Starting app")

    service = GreeterService()
    messages = service.greet(cfg.name, cfg.repeat)

    for msg in messages:
        print(msg)

    logger.info("Done")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    try:
        cfg = parse_args(argv)
        setup_logging(cfg.log_level)
        return run_app(cfg)
    except KeyboardInterrupt:
        # Conventional exit code for SIGINT
        return 130
    except Exception as exc:
        logging.getLogger("app").exception("Fatal error: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
