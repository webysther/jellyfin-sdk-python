# Copilot instructions for jellyfin-sdk-python

## Big picture
- This SDK is a thin, high-level wrapper over OpenAPI-generated bindings.
  - High-level API lives in `src/jellyfin/` (e.g., `api.py`, `items.py`, `users.py`).
  - Generated bindings live under `src/jellyfin/generated/api_10_10` and `api_10_11` (from `specs/openapi_*.json`).
  - Legacy compatibility lives in `src/jellyfin/legacy/` and is enabled by the optional `legacy` extra.
- The public entrypoint is `jellyfin.api(...)` (see `src/jellyfin/api.py`), which wires `ApiClient`, config, auth headers, and the versioned module proxy.

## Key conventions & patterns
- Version selection is explicit: `Api(..., version=Version.V10_10)` or string values like `'10.11'` (see `src/jellyfin/api.py`).
- High-level APIs are lazy and chainable:
  - `ItemSearch` uses builder-style filters with `.add(...)`, attribute setters, `.recursive()`, `.paginate()`, and `.all` (see `src/jellyfin/items.py`).
  - Collections are iterable wrappers with pagination handled by `Collection` in `src/jellyfin/base.py`.
- User context is required for user-scoped endpoints; `Users.of(...)` sets context and `Users.views` will raise if not set (see `src/jellyfin/users.py`).
- Debugging: setting `api.debug = True` enables curl-style request logging in the generated client (documented in `README.md`).
- `Api.register_client(...)` expands auth headers with client/device metadata (see `src/jellyfin/api.py`).

## Critical workflows
- Regenerate bindings from OpenAPI specs:
  - `build.sh <version>` (e.g., `10_10` or `10_11`) uses `openapi-generator-cli` with templates in `templates/python/` and outputs to `src/`.
- Package metadata and dependencies are in `pyproject.toml` (Python >=3.10, Pydantic v2, httpx/aiohttp, etc.).

## Integration points
- OpenAPI specs: `specs/openapi_10_10.json` and `specs/openapi_10_11.json`.
- Docs site is built from generated content in a separate repo `jellyfin-sdk-python.github.io/` (see workspace). Reference API docs under `docs/api_10_10/` and `docs/api_10_11/`.

## When editing
- Prefer updating high-level wrappers in `src/jellyfin/` rather than generated code; generated bindings should be updated via `build.sh`.
- Keep method-chaining and lazy instantiation patterns consistent with `Items`, `Users`, and `Api` classes.
