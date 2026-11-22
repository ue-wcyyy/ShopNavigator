# ShopNavigator

**Web Shopping Agent in a Simulated Store** — DSC 120C final project, Topic 5.

An autonomous shopping agent navigates a *simulated* storefront to satisfy a detailed
natural-language instruction (budget, mandatory product properties, soft preferences), and shows the
evidence behind every decision. The agent must plan from what it actually observes — the pages it
opens and the options it selects — instead of recommending a product from model memory. No real
purchases, no payment data, no commercial accounts.

> **Status:** repository skeleton (`v0.0`), created at project start per course rules.
> Weekly log: [PROGRESS.md](PROGRESS.md) · Prioritised tasks: [BACKLOG.md](BACKLOG.md) ·
> Releases: [CHANGELOG.md](CHANGELOG.md).

## Problem

A shopper asks for something like *"a 15-inch laptop under $900, at least 16 GB RAM, silver, no
gaming branding"*. A plausible-sounding recommendation is not enough: the agent has to search the
simulated catalog, open product pages, check attributes, prices and option combinations, and either
justify a selection from observed evidence or stop and explain which constraint cannot be met.
Free-form LLM text is never treated as proof of task success — the simulator state is.

## Intended users

| User | Need |
| --- | --- |
| Shopper (primary) | Describe a goal once, get a defensible shortlist, review before any final action |
| Product reviewer / teaching staff | Inspect a saved run: every step, tool call, cost and final constraint check |
| (TODO) | Confirm personas and journeys in [docs/user-journeys.md](docs/user-journeys.md) |

## Milestones

| Tag | Scope | Status |
| --- | --- | --- |
| `v0.1` | Simulator feasibility pilot (tiny local store, reproducible tasks) + reactive baseline | planned |
| `v0.2` | Closed-loop constraint-aware navigation agent + integrated UI (goal → comparison → cart review) | planned |
| `v1.0` | 40-task evaluation, 15 hard cases, 5 end-to-end journeys, usability review, final report | planned |

## Repository map

| Path | Purpose |
| --- | --- |
| `app.py` | UI entry point (`streamlit run app.py`) |
| `src/shopnavigator/simulator/` | Catalog, store state, action space — the only environment the agent may act on |
| `src/shopnavigator/constraints/` | Natural-language goal → structured constraint checklist, product checks |
| `src/shopnavigator/agent/` | Planner, policy (reactive vs constraint-aware), tool/action layer |
| `src/shopnavigator/ui/` | Screens: goal entry, checklist, agent status, comparison, cart review, run replay |
| `src/shopnavigator/evaluation/` | Metrics and batch evaluation runner |
| `src/shopnavigator/tracing.py` | Structured run traces (steps, actions, costs, failures) |
| `configs/` | Committed, secret-free configuration |
| `data/` | `raw/` → `processed/` → `tasks/` (contents not committed) |
| `evaluation/` | Task set and result artifacts (results not committed) |
| `docs/` | Proposal, architecture, journeys, evaluation plan, cost budget, limitations, roadmap |
| `tests/` | Unit and integration tests |
| `scripts/` | Data preparation and demo CLI |
| `.github/` | CI workflow, issue/PR templates |

## Quick start (target — commands become live in `v0.1`)

```bash
git clone <repo-url>
cd ShopNavigator
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env          # add your own API key; .env is git-ignored
pytest -q
streamlit run app.py
```

Runtime dependencies (UI framework, LLM client) are deliberately not pinned yet — see the `TODO` in
`pyproject.toml` and the open questions in [docs/architecture.md](docs/architecture.md). Until they
are added, the last two commands are targets rather than working commands.

## Team

| Member | Role | Owns |
| --- | --- | --- |
| Weican Ye | Team leader | TODO |
| Mohammed Parvez | TODO | TODO |
| Akash Reddy | TODO | TODO |

All three members must be able to explain the whole system (see
[docs/team-and-roles.md](docs/team-and-roles.md)).

## Documentation

- [docs/proposal.md](docs/proposal.md) — the required first commit
- [docs/architecture.md](docs/architecture.md) — components and data flow
- [docs/evaluation-plan.md](docs/evaluation-plan.md) — baselines, metrics, test sets
- [docs/user-journeys.md](docs/user-journeys.md) — five end-to-end journeys
- [docs/data-and-license.md](docs/data-and-license.md) — dataset access and licence review
- [docs/api-cost-budget.md](docs/api-cost-budget.md) — cost assumptions and hard caps
- [docs/limitations.md](docs/limitations.md) · [docs/roadmap.md](docs/roadmap.md)

## Data and secrets

Upstream dataset: [WebShop](https://github.com/princeton-nlp/WebShop) — the original setup targets
older Python/Java and downloads indexes, so the plan is the 1,000-product small mode or a faithfully
recreated tiny local store. **Never commit** API keys, `.env` files, private data or restricted
dataset copies; see [docs/data-and-license.md](docs/data-and-license.md) and `.gitignore`.
