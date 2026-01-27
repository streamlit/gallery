from __future__ import annotations

import os
from collections.abc import Iterable

DEFAULT_GITHUB_TOKEN_ENVS: tuple[str, ...] = ("GH_TOKEN", "GH_API_TOKEN", "GITHUB_TOKEN")


def get_github_token(
    *, preferred_env: str = "GH_TOKEN", extra_envs: Iterable[str] = ()
) -> str | None:
    """Return the first non-empty GitHub token found in the environment.

    Resolution order:
    - preferred_env (if provided)
    - extra_envs (in order)
    - DEFAULT_GITHUB_TOKEN_ENVS (in order)
    """

    candidates: list[str] = []
    if preferred_env and preferred_env.strip():
        candidates.append(preferred_env.strip())
    for k in extra_envs:
        if isinstance(k, str) and k.strip():
            candidates.append(k.strip())
    for k in DEFAULT_GITHUB_TOKEN_ENVS:
        if k not in candidates:
            candidates.append(k)

    for k in candidates:
        v = os.environ.get(k)
        if isinstance(v, str):
            v = v.strip()
            if v:
                return v
    return None


def has_github_token(*, preferred_env: str = "GH_TOKEN", extra_envs: Iterable[str] = ()) -> bool:
    return get_github_token(preferred_env=preferred_env, extra_envs=extra_envs) is not None
