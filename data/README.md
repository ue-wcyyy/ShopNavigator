# Data directory

Nothing here is committed except the `.gitkeep` placeholders — datasets and derived copies stay
local (see [../docs/data-and-license.md](../docs/data-and-license.md)).

| Folder | Contents | Produced by |
| --- | --- | --- |
| `raw/` | Untouched downloads (WebShop catalog/index files) | `scripts/prepare_data.py` |
| `processed/` | Cleaned catalog, product records, option tables | `scripts/prepare_data.py` |
| `tasks/` | Task definitions with seeds, constraints and expected outcomes | team, or generated |

## Conventions (TODO: confirm during the `v0.1` pilot)

- `processed/catalog.json` — list of products: id, title, price, attributes, options.
- `tasks/tasks.json` — list of tasks: id, goal text, hard constraints, budget, seed, expected outcome.
- Every file that drives a result must be reproducible from a documented command plus a seed.
- Never edit `raw/` by hand; fix the preparation script instead.
