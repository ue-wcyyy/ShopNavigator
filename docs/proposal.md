# Project proposal — ShopNavigator

> Status: **draft outline**. Must be completed and committed as the *first* meaningful commit
> (`docs/proposal.md`), before implementation work starts.
>
> One-line pitch: an autonomous agent shops a simulated storefront to satisfy a detailed
> instruction, and proves every step from what it actually observed.

## 1. Problem statement

Shoppers rarely have a single crisp query; they have a bundle of constraints — a budget, mandatory
properties ("16 GB RAM", "15-inch"), soft preferences ("silver", "quiet") — spread across a catalog
where availability, prices and option combinations change from page to page. Current LLM shopping
assistants answer fluently from parametric memory and cannot show whether a recommended product
actually satisfies the constraints or even exists in the catalog.

This project builds an agent that treats the store as the source of truth. It must search, open
product pages, compare candidates, select options, and either justify a finalist from observed page
content or stop and explain which constraint is unreachable. Task success is measured in simulator
state, never in the fluency of the explanation.

**Research question:** how much does constraint-aware, observation-grounded navigation improve
task success and rule compliance over a reactive "search once, recommend" baseline, and at what
cost in steps, runtime and API spend?

## 2. Intended users

| User | Context | Primary need | Success looks like |
| --- | --- | --- | --- |
| Shopper (primary) | Non-expert, has a goal but not a product name | A shortlist they can trust, with reasons | Understands *why* each item was chosen/rejected; can correct the checklist |
| Reviewer (grader/teammate) | Audits quality after the fact | Replayable evidence: steps, actions, costs, final check | Can reproduce a run and see exactly where it failed |
| (TODO) | | | |

TODO: two or three short personas with a concrete example instruction each.

## 3. Scope

**In scope:** simulated storefront only; text/browser-style navigation actions; budget and attribute
constraints; comparison and explanation; simulated cart with explicit user review; saved/replayed
runs; batch evaluation.

**Out of scope:** real purchasing, payment data, real retailer scraping, accounts or credentials,
price prediction, investment-style recommendations, GPU training.

## 4. Functional requirements

Derived from the Topic 5 brief; refine and keep the IDs stable so tests and backlog items can cite
them.

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| FR-1 | Parse a natural-language shopping goal into constraints and preferences | Checklist shown to the user before navigation starts |
| FR-2 | Search the simulated catalog and open product detail pages | Observations returned per action; no page content invented |
| FR-3 | Compare attributes, prices and option combinations | Comparison panel with per-constraint pass/fail |
| FR-4 | Choose actions and record every decision | Trace with action, observation digest, rationale, cost |
| FR-5 | Maintain a simulated cart and validate the final product | Final validation before any confirmation step |
| FR-6 | Explain unmet constraints and stop when no valid option exists | Infeasible task ends with a specific blocking constraint |
| FR-7 | Deliver an integrated, usable application (not a notebook or one API call) | Goal entry, status, comparison, cart review, retained state |
| FR-8 | Closed-loop navigation verified against actual simulator observations | Each state transition checked; invalid actions logged |
| FR-9 | Structured, user-visible constraint checklist (budget, hard, soft) | User can edit and re-run |
| FR-10 | Selection/rejection explanations grounded in observed page data | Every claim links to an observation |
| FR-11 | Handle unavailable products, odd option combinations, inconsistent descriptions, navigation errors | Bounded replanning; no infinite loops |
| FR-12 | Save, replay and compare complete shopping runs | Tool calls, costs, invalid actions, final satisfaction |
| FR-13 | Input validation and recoverable failures | Bad goal/empty catalog/expired session handled without a crash |
| FR-14 | (TODO) Add anything the team extends beyond the brief | |

## 5. Non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR-1 | No live purchasing, payment, or commercial account data — simulator only |
| NFR-2 | Hard caps on navigation steps, wall-clock time and API spend, enforced in code |
| NFR-3 | Reproducible catalog/task snapshots with recorded seeds |
| NFR-4 | Navigation whitelist: only permitted actions may be issued; everything else is rejected and logged |
| NFR-5 | Success is defined by simulator state, never by textual recommendation |
| NFR-6 | No hidden product-label leakage into prompts; no test-task answers in the repo |
| NFR-7 | Reproducible local startup, sample config without secrets, automated core-component tests |
| NFR-8 | Documented API-cost and compute budget; CPU-only is acceptable |
| NFR-9 | (TODO) Accessibility, latency or other team-added qualities |

## 6. Dataset and licence review

- Upstream: **WebShop** — <https://github.com/princeton-nlp/WebShop>.
- Known friction: the original setup targets older Python and Java and downloads product indexes.
- Planned approach: the **1,000-product small mode**, or a faithfully recreated **tiny local store**
  if the upstream environment cannot be reproduced quickly (decision + evidence go in `PROGRESS.md`).
- Licence: TODO — record the upstream licence, what we redistribute (catalog subsets? derived task
  files?) and what stays local. Details in [data-and-license.md](data-and-license.md).
- Never commit: restricted dataset copies, scraped pages, API keys, `.env`.

## 7. Architecture

See [architecture.md](architecture.md) for the diagram and data flow. Layers: simulator (state +
actions) → constraint model → agent (planner, policy, tools) → UI → trace/evaluation.

## 8. Baseline

TODO: define the baseline precisely, e.g. a **reactive agent** that issues one search, opens the top
result and recommends it without checking all constraints. Report success, constraint violations,
unnecessary page actions and cost on the same task set as the improved pipeline.

## 9. Evaluation plan

Summary — full detail in [evaluation-plan.md](evaluation-plan.md):

- ≥40 simulated shopping tasks with varied hard constraints and budgets.
- Reactive vs constraint-aware agent on success, rule violations, unnecessary page actions, cost.
- ≥15 difficult cases: unavailable products, misleading descriptions, changing options.
- Five end-to-end journeys including a failure/recovery case, tested after integration.
- One meaningful baseline plus a genuinely improved pipeline on held-out cases.
- Small usability review with ≥3 people outside the team.

## 10. Milestones

| Tag | Milestone | Content | Target |
| --- | --- | --- | --- |
| `v0.1` | Feasibility and baseline | Environment pilot, tiny catalog, task seeds, reactive baseline numbers | TODO |
| `v0.2` | Integrated end-to-end workflow | Constraint-aware agent + UI + trace/replay | TODO |
| `v1.0` | Tested product and final evidence | 40-task eval, 15 hard cases, 5 journeys, usability review, report | TODO |

Suggested sequence from the brief: WebShop environment pilot → search and navigation agent →
constraint and success tests.

## 11. Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| WebShop upstream environment fails to install | Medium | High | Time-boxed pilot; fall back to a recreated tiny local store with the same action semantics |
| Agent loops or burns budget on navigation | High | Medium | Hard step/time/USD caps, loop detection, bounded replan attempts |
| Success measured from LLM text instead of state | Medium | High | Final validation reads simulator state only; text claims are not evidence |
| Test-set leakage into prompts | Medium | High | Held-out tasks, no labels in prompts, audit of prompt templates |
| Evaluation set too small to compare baselines | Medium | Medium | Fix the 40-task set early; report per-category numbers, not one average |
| Team member unavailable near presentations | Medium | High | Shared ownership, weekly commits, documented setup so anyone can run it |
| (TODO) | | | |

## 12. Team responsibilities

| Member | Primary ownership | Secondary | Deliverables |
| --- | --- | --- | --- |
| TODO (A) | | | |
| TODO (B) | | | |
| TODO (C) | | | |

Work packages to distribute: simulator/catalog, constraint model, agent planner/policy, UI,
tracing/replay, evaluation harness, report and demo. All three members must be able to explain the
full system during the final presentation.
