from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        # Use 2-space indentation for human-friendly diffs in GitHub PRs.
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def dump_json_atomic(path: Path, obj: Any) -> None:
    """Write JSON to `path` atomically (best-effort).

    Writes to a temp file in the same directory and then replaces `path`, which
    avoids leaving partially-written files on failure.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f"{path.name}.tmp.{os.getpid()}")
    try:
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)
            f.write("\n")
        tmp.replace(path)
    finally:
        # If replace failed, try to clean up the temp file.
        try:
            if tmp.exists():
                tmp.unlink()
        except Exception:
            pass
