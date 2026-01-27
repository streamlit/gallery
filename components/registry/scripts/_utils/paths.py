from __future__ import annotations

from pathlib import Path


def source_components_dir(repo_root: Path) -> Path:
    """Return the directory containing source-of-truth component submissions."""
    return repo_root / "components" / "registry" / "components"
