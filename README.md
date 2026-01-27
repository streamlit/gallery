# gallery

Scripts-first repo with:

- `pre-commit` for consistent checks on commit
- Ruff for Python linting/formatting
- Prettier for JSON formatting

## Setup (local)

Create a virtualenv and install dev tools:

```bash
uv venv
source .venv/bin/activate
uv sync --dev
```

Install git hooks:

```bash
pre-commit install
```

Run all hooks:

```bash
pre-commit run --all-files
```

Note: `pre-commit` will also set up an isolated Node environment to run Prettier.
