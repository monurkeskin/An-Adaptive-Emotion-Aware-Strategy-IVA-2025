# Contribute a reproducible change

The engine is a dependency; this repository contains this paper's scientific
choices and independent tests. Do not copy a new engine into the companion.

| Responsibility | Location |
| --- | --- |
| Published profile/protocol | `configs/`, `protocol-schedule.json` |
| Equation/algorithm-to-code traceability | `paper-map.json`, `METHOD.md` |
| Inputs, analysis recipe and comparisons | `reproduction/` |
| Independent profile/protocol/result assertions | `tests/` |
| Preferred paper and software citation | `citation-metadata.json` → generated citation files |

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python run.py --output development-example
python verify.py --output development-verification
```

Start a bug fix with a failing test tied to a specific paper requirement. For a
profile discrepancy, transcribe expected points from the paper independently, then
enumerate the small outcome space and compare both actors. Change only the profile
conversion, rerun affected tests, and record whether past numeric results change.
For a protocol issue, assert practice/main order, timed breaks, survey phase and
isolation between sessions before altering the configuration.

To try a new study, copy the configuration to a new file, select `custom-study`,
and remove the published-protocol identity. Record your own methods and assets;
a different configuration is not automatically a reproduction of this paper.
For a shared engine bug, submit the minimal failing fixture upstream and then
update the exact engine pin here after its tests pass.

The engine exposes `Agent.decide(Observation) -> Decision` and
`negotiator.testing.assert_agent_contract(factory, own_preference)`. A factory takes
`(own_preference, seed)`; contract tests check legal actions, deterministic retries,
local RNG and deadlines. Device adapters use a separate process protocol, keeping
older SDK requirements away from the core Python environment.

Update METHOD, the paper-map row and the reproduction target with every scientifically
meaningful change. Preserve source notices and data licenses. Report examples using
synthetic records, not participant identities or recordings.
