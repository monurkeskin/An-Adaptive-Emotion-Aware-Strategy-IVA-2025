# Reproducibility

This companion distinguishes **running software**, **recomputing a specified result**
and **replicating a human finding**. The associated paper is [An Adaptive Emotion-Aware Strategy for Human-Agent Negotiation: Insights from Real-World Human-Robot Experiments](https://doi.org/10.1145/3717511.3747087).

## Available targets

| Manifest under `reproduction/` | Evidence |
| --- | --- |
| `method.json` | Recompute and check against independent references |
| `profile-1.json` | Recompute and check against independent references |
| `profile-2.json` | Recompute and check against independent references |
| `paired-example.json` | Recompute and check against independent references |
| `published-results.json` | Unavailable original inputs; no numbers fabricated |

```bash
python verify.py --output verification-output
```

This validates engine identity, then runs every listed recipe. Each writes
`report.json`, `index.html` and `ro-crate-metadata.json`. Available computations also
produce `results.csv`, `table.tex` and applicable SVG/PDF figures. `verification.json`
records the status of each target and total elapsed time. It succeeds only when
available recipes match and the original-data target explicitly reports unavailable.

To inspect the original-result gap directly:

```bash
negotiator reproduce reproduction/published-results.json --output original-result-status
```

This command intentionally exits **3** while inputs are unavailable. Exit **0**
means the configured computation completed (inspect `status` for verified versus
unchecked); **2** is a reference mismatch and **1** an invalid input/configuration.
No expected paper number is passed to the calculation. Expected values are used
only after recomputation, with explicit absolute/relative tolerance.

## Data and environment identity

`requirements.txt` pins the framework Git revision and `constraints.txt` its resolved
runtime dependencies. Manifests identify input SHA-256 and engine version; runtime
receipts also record Python, platform, actual dependencies and package content hash.
The exact original experiment environment is not claimed to be recovered.

All shipped paired observations are visibly synthetic. Original participant data,
video/audio, affect weights and licensed robot resources are absent. Source inputs
must reside inside the recipe directory, have a matching SHA-256 and be permitted
for the intended use. Missing inputs yield null results with reasons. Existing
outputs are never overwritten.

## Analysis unit and historical interpretation

Five-minute Hybrid practice, two counterbalanced ten-minute main sessions, ten-minute break and post-session nine-point questionnaires; fruit score tables follow session position.

The paired example uses one record per participant/condition and keeps study, cohort
and domain separate. It excludes whole pairs for missing conditions, missing utility
or a prespecified round rule. It never counts offers as independent people. A round
count must be converted from the historical protocol explicitly; one offer is not
assumed to be a complete exchange. The example's bootstrap resamples participants
with seed 42. Its intervals are a maintained analysis demonstration, not a recovered
paper p-value or a substitute for a prespecified historical analysis.

Read [analysis](docs/analysis.md) before replacing synthetic inputs. The original
result target remains unavailable until the appropriate original analysis recipe,
permitted records and inclusion ledger are supplied together.
