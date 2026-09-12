# Analyze this paper's session records

The analysis unit is the **participant**. Five-minute Hybrid practice, two counterbalanced ten-minute main sessions, ten-minute break and post-session nine-point questionnaires; fruit score tables follow session position.

## Available example

```bash
negotiator reproduce reproduction/paired-example.json --output paired-output
```

The three synthetic participant pairs have differences 0.4, 0.1 and -0.2; their
mean is 0.1. This number is a hand-checkable fixture, not a result from the paper.
`paired-output/results.csv` contains computed group summaries and interval bounds;
`table.tex` formats those same values and `paired-contrasts.svg`/`.pdf` plots them.
Rounding is applied only when formatting the table. Full precision remains in JSON/CSV.

## Input dictionary

| Field | Meaning |
| --- | --- |
| `study_id`, `participant_id`, `session_id` | Stable identities; participants are paired within one study |
| `condition`, `cohort`, `domain` | Experimental condition and distinct design groups |
| `rounds` | Nonnegative integer using a documented original-protocol definition |
| `utility` | Selected normalized outcome measure in [0,1], or null when missing |
| `practice` | Excluded from main-condition inference |

Choose explicitly whether the intended outcome is raw agreement utility or the
game payoff. Failure/no agreement and missing/incomplete measurement are different
states. Never turn missing data into zero. The example rejects duplicated session
or participant-condition identities; it excludes the complete pair when either
required member is missing or fails the declared round criterion.

Cohorts and domains remain separate unless a protocol justifies a named domain
mapping. Inspect counts and exclusion reasons before any inference. Do not select a
significance test by searching for a favorable result. The paper's original decisions
and records are required to claim exact recomputation of its tables or figures.
The modern percentile bootstrap in the example is a separate declared analysis.
