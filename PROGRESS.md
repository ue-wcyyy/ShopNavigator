# Progress log

Dated, append-only record of what the team actually did. Updated **at least weekly** and never
rewritten into a final-week summary. Newest entry on top.

Every entry records: what was completed · who contributed · experiments and results · design
changes · obstacles · fixes · links to commits / issues / PRs.

## Log

### 2026-11-22 — Week 1: repository skeleton

- **Done:** created the repository skeleton (docs, `src/shopnavigator/` packages, `data/`,
  `evaluation/`, `tests/`, CI workflow, issue/PR templates); started the proposal outline and the
  five user journeys.
- **Contributors:** TODO (member A / B / C — split below once roles are agreed)
- **Experiments / results:** none yet.
- **Design changes:** none yet.
- **Obstacles:** WebShop upstream setup (older Python/Java, downloaded indexes) — decision pending
  between the 1,000-product small mode and a recreated tiny local store.
- **Fixes:** n/a.
- **Links:** TODO — first commit / issue numbers.
- **Next:** agree stack and roles → fill `docs/proposal.md` → commit the proposal before any code.

## Entry template

```markdown
### YYYY-MM-DD — Week N: <short title>

- **Done:**
- **Contributors:**
- **Experiments / results:** (numbers, not adjectives)
- **Design changes:**
- **Obstacles:**
- **Fixes:**
- **Links:** commit / issue / PR
- **Next:**
```

## Milestone checkpoints

| Milestone | Planned week | Evidence required |
| --- | --- | --- |
| `v0.1` feasibility + baseline | TODO | pilot notes, baseline numbers, reproducible run |
| `v0.2` integrated end-to-end workflow | TODO | working UI demo, integration test |
| `v1.0` tested product + final evidence | TODO | 40-task results, 15 hard cases, 5 journeys, usability review |
