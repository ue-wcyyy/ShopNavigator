# Known limitations

Living document — updated as evidence arrives. The final version must accompany the `v1.0` results.

## Current (skeleton stage)

- No implementation yet: the repository contains the structure, plans and placeholder modules.
- No measured results; every number in the docs is a target, not a finding.
- Dataset mode undecided (upstream small mode vs a recreated tiny local store).

## Expected limitations to verify

| Area | Limitation | How we will check |
| --- | --- | --- |
| Environment fidelity | A recreated tiny store may be easier than the real WebShop environment | Compare task difficulty and success rates; document the delta |
| Catalog scale | 100–1,000 products is far smaller than a real store | Report success per constraint complexity, not just an average |
| Language | Goals in one language only (TODO: which) | State the supported input language explicitly |
| Reasoning | The planner may still rely on priors when pages are sparse | Check every claim against a logged observation |
| Cost | LLM calls per step make long runs expensive | Report cost per successful task |
| Evaluation size | 40 tasks gives coarse confidence intervals | Report per-category counts and failure examples |
| Usability | ≥3 participants is a small sample | Present it as a defect-finding exercise, not a benchmark |

## Out of scope

Real purchases, payment data, live retailer scraping, price forecasting, investment advice.
