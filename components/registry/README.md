# Component Registry

This repo includes a **community-maintained component registry** of Streamlit components under [`components/registry/components/`](components/). Each file is a small JSON document describing a single component found on the internet.

If you maintain a Streamlit Component, we’d love for you to add it here via a pull request!

## Quick submit (GitHub web editor)

1. **Fork** this repository.
2. In your fork, open [`components/registry/components/`](components/) and click **Add file → Create new file**.
3. Name your file: `components/registry/components/<slug>.json`
   - Use a short, URL-safe slug like `streamlit-my-component.json` (lowercase + hyphens is best).
4. Copy/paste the **Starter template** below, fill in your values.
5. Commit to a new branch in your fork.
6. Open a **Pull Request** back to this repo.

When you open the PR, CI will automatically validate your JSON.

## What happens next?

Once your PR is merged, your component will appear in the gallery after the next weekly refresh (runs early Monday UTC / Sunday evening PT). Metrics like GitHub stars and PyPI downloads are updated automatically.

## Starter template (minimal valid)

> Tip: If you’re editing in VS Code / GitHub’s web editor, you should get live validation + autocomplete from the schema once `.vscode/settings.json` is present in the repo.

```json
{
  "schemaVersion": 1,
  "title": "My Component",
  "author": {
    "github": "your-github-username",
    "displayName": "Your Name (optional)"
  },
  "links": {
    "github": "https://github.com/OWNER/REPO",
    "pypi": null,
    "demo": null,
    "docs": null
  },
  "media": {
    "image": null
  },
  "install": {
    "pip": "pip install your-package-name"
  },
  "governance": {
    "enabled": true,
    "notes": null
  },
  "categories": ["Widgets"]
}
```

## Requirements (what CI checks)

CI runs [`components/registry/scripts/validate.py`](scripts/validate.py) on every PR that touches `components/registry/components/**`.

### Schema requirements

Your JSON must conform to [`components/registry/schemas/component.schema.json`](schemas/component.schema.json). Key points:

- **`schemaVersion`**: must be `1`.
- **`title`**: 1–80 characters.
- **`author.github`**: GitHub username _without_ `@`.
- **`links.github`**: must be a repo URL like `https://github.com/<owner>/<repo>` (no extra path segments).
- **`links.pypi`**: PyPI project name (not a URL), or `null`.
- **`links.docs`**: optional URL to your component’s documentation, or `null`.
- **No extra keys**: the schema uses `additionalProperties: false`, so don’t add custom fields.

### Policy checks beyond schema (common CI failures)

The validator enforces a few “lint” rules to keep the registry stable:

- **Unique repo**: `links.github` must be unique across all submissions. If the same repo was already submitted, CI will fail.
- **HTTPS only**: all URLs must be `https://` and must not use `javascript:`, `data:`, or `file:` schemes.
- **Stable images** (`media.image`): must be a stable `https://` URL.
  - Signed/expiring URLs (S3/GCS/CloudFront-style query params like `X-Amz-Signature`, `Expires`, etc.) are rejected.
  - Proxy hosts like `camo.githubusercontent.com` are rejected.
- **File size**: each `components/registry/components/*.json` must be ≤ 50 KB.

## Categories

Pick **at least one** category (you can pick multiple). Allowed values are:

- `LLMs`
- `Widgets`
- `Charts`
- `Authentication`
- `Connections`
- `Images & video`
- `Audio`
- `Text`
- `Maps`
- `Dataframes`
- `Graphs`
- `Molecules & genes`
- `Code editors`
- `Page navigation`
- `Developer tools`
- `Integrations`

## Self-check your submission (optional, but recommended)

### Option A: No local setup

Open a **draft PR** and let CI validate it automatically.

### Option B: Run the validator locally

From the repo root:

```bash
uv sync
uv run python components/registry/scripts/validate.py
```

If it prints `OK: all validated files passed.`, your submission is valid.

## What not to edit

- Don’t edit `components/registry/compiled/components.json` directly — it’s a generated artifact.
