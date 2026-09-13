# Installation and compatibility

Use Python 3.11 or 3.12 and Git. `requirements.txt` pins engine 2.1.0 by exact commit;
`constraints.txt` freezes its resolved runtime dependencies. Keep this environment
separate from older robot SDK environments. A source clone plus its installed
requirements runs independently; no other checkout needs to be adjacent.

| Execution | Requirement | Validation scope |
| --- | --- | --- |
| Synthetic method/session example | Core Python environment | Automated tests and clean-install receipt |
| Local browser participant/conductor | Modern browser; GUI bundled with engine | Browser integration tests |
| NAO/Pepper legacy bridge | NAOqi 2.5 family, separate Python 2.7 runtime and matching SDK/firmware | Process contract tested; real hardware still requires lab validation |
| QT legacy bridge | Supported ROS/rosbridge interface and isolated compatible client | Process contract tested; local services and robot version must be checked |
| Recorded historical avatar/gesture corpus | Original licensed assets and matching presentation mapping | Not bundled or empirically validated |

The browser avatar is an illustrative interface. It is not a validated replacement
for a paper's embodiment condition. A newer robot or avatar must pass the engine's
capability/version/failure contracts and a separate recorded hardware test.
See the engine's [device guide](https://github.com/monurkeskin/NEGOTIATOR-IJCAI-2024/blob/v2.1.0/docs/devices.md)
for exact bridge configuration and the supported legacy namespace.

If installation reports `git` missing, install Git before retrying. If an output
directory already exists, choose a new name; do not delete evidence just to rerun.
If a protocol shows missing requirements, read METHOD and supply validated inputs
for your declared scope. A synthetic run cannot clear a historical evidence gap.
