# Method and evidence

Associated paper: [An Adaptive Emotion-Aware Strategy for Human-Agent Negotiation: Insights from Real-World Human-Robot Experiments](https://doi.org/10.1145/3717511.3747087).

## Scientific contract

Mean categorical affect in the response interval, opponent awareness, fixed move centroids, current-decision adaptation and comparison with the estimated Nash-product offer.

Five-minute Hybrid practice, two counterbalanced ten-minute main sessions, ten-minute break and post-session nine-point questionnaires; fruit score tables follow session position.

The machine-readable [paper map](paper-map.json) links selected manuscript labels,
source hashes and locations to implementation, independent tests, configurations
and result targets. Only the selected active LaTeX entry was used. Manuscript
working files, inactive drafts and reviewer correspondence are not redistributed.


## Algorithm and source differences

The maintained 2.0 engine follows `alg-solver` by applying adaptation before the
current offer and comparing that offer with a bid maximizing estimated utility
product. `tbl-sensitivity`'s Silent direction now decreases the response multiplier.
Awareness uses the unclipped category-response ratio; the undefined zero-denominator
case is explicitly 0. Affect is averaged over the interval from the agent's offer
presentation attempt (or commit if no attempt exists) to the human reply. Ignored
Fear/Disgust mass is not redistributed. No frame in the interval means missing affect.

The paper does not numerically identify every implementation choice. Configurations
expose `adaptation_min_human_offers=9`, `concession_step=.2`, `silent_multiplier=.5`
and `selfish_multiplier=1.5`; the class-change trigger and historical lag are also
recorded in diagnostics. These are **maintained choices**, not recovered experiment
parameters. The linked public source's valence/arousal variation is a different
method interpretation. The published categorical equation is the selected scope.

## Utility, targets and game scores

A bid always states the human share. Agent utility uses the complementary allocation.
Utility is computed at full precision; rendering multiplies by 100 for display.
A target score is distinct from a reservation constraint. In the fruit papers,
a human agreement below 40 points is permitted but earns zero game points;
raw utility and game payoff remain separate logged fields. The Jennifer papers'
30-point goal is not silently turned into a prohibition on lower agreements.
The short Solver and Appearance examples do not claim those fruit reward rules.

## Remaining evidence gaps

- Historical numeric adaptation threshold, step sizes, zero-denominator and class-change conventions.
- Original practice profiles, questionnaires, camera model and frame timestamps.
- Permitted human outcomes, original model-comparison inputs and centroid-training records.

Unknown inputs are not filled with simulated participants or invented historical
constants. The existing templates are inspectable, but their published-protocol
preflight prevents starting before required evidence is supplied and reviewed.
A custom study has its own declared configuration and cannot inherit a reproduction
claim merely by using the same strategy name.

## Relationship to the research series

Extends Solver concepts and reuses fruit profiles; maintained categorical implementation differs from the separately linked valence/arousal source variant.

The common engine owns utility, lifecycle, logs, GUI, shared methods and device
contracts. This repository owns paper-specific profiles, protocol choices, analysis
rules, reproduction targets and tests. [framework.json](framework.json) pins the
engine; [NOTICE](NOTICE) preserves original source attribution.
