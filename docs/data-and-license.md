# Dataset, environment and licence review

Required by the proposal checklist: dataset access, licence review and what we do *not* commit.

## Upstream

| Item | Value |
| --- | --- |
| Dataset / environment | WebShop |
| Source | <https://github.com/princeton-nlp/WebShop> |
| Task type | Simulated e-commerce product search with a navigable storefront |
| Scale | Full setup is heavy; the brief points to the 1,000-product small mode or a faithful tiny local store |
| Licence | **TODO — verify the upstream repository licence and record it here verbatim** |
| Access | Public GitHub repository; no application form |
| Redistribution | **TODO — decide what derived artifacts may live in this repo** |

## Known setup friction

The original environment targets older Python and Java and downloads product indexes. Before the
project is approved we must check that the environment runs. Options, in order of preference:

1. Upstream **small mode (1,000 products)** if it installs within a time-boxed pilot.
2. **Recreated tiny local store** (e.g. 100–300 products) with the same action semantics and
   observation format, if upstream setup is too brittle.
3. Fixed **snapshot** of catalog + tasks with recorded seeds, so every result is reproducible.

Whichever option is chosen: document the exact commands, versions and seeds in `README.md` and log
the decision in `PROGRESS.md`.

## Repository data policy

| Path | Committed? | Contents |
| --- | --- | --- |
| `data/raw/` | No (`.gitkeep` only) | Downloaded upstream files |
| `data/processed/` | No | Cleaned catalog, task inputs, seeds |
| `data/tasks/` | No (small, hand-written samples may be added later with review) | Task definitions |
| `evaluation/tasks/` | No | Held-out evaluation tasks |
| `evaluation/results/` | No | Raw run outputs and metrics |
| `.env` | No — git-ignored | Local API keys |
| `.env.example` | Yes | Empty template |

**Never commit:** API keys or tokens, `.env`, private or personal data, restricted dataset copies,
scraped pages from real retailers, or held-out answers that would leak into prompts.

## Leakage controls

- Test tasks are held out from prompt templates and from the agent's available context.
- Product labels/answers are not exposed to the planner — only the observable page state.
- Prompt templates and any few-shot examples are reviewed for accidental test data before release.
