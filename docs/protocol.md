# Configure and conduct this protocol

Five-minute Hybrid practice, two counterbalanced ten-minute main sessions, ten-minute break and post-session nine-point questionnaires; fruit score tables follow session position.

## First inspection

Run `negotiator gui`, open **New study**, import `configs/protocol-solver-first.json`, and inspect
Study, Preferences, Sessions and Review. The conductor sees protocol readiness;
the participant sees only their own preferences, offers, timer and current phase.
Use pseudonymous participant IDs. The application serves the two views locally,
including separate monitors; it is not a remote Internet study service.

| Position | Condition | Role | Deadline | Following break |
| --- | --- | --- | --- | --- |
| 1 | Practice (synthetic three-issue task) | practice | 300 s | 0 s |
| 2 | Solver | main | 600 s | 600 s |
| 3 | Hybrid | main | 600 s | 0 s |

Alternative order files are listed in [CONFIGURATIONS](../CONFIGURATIONS.md).
Where profiles change by position, changing condition order does not swap the
position-specific score table. Practice blocks remain attached to their main
condition. The break follows the preceding session's result and any scheduled
questionnaire. A restart conservatively restarts the full break and records this fact.

## Before using a published-protocol template

- Historical numeric adaptation threshold, step sizes, zero-denominator and class-change conventions.
- Validated practice profiles, camera model and preprocessing configuration.
- Permitted human outcomes, original model-comparison inputs and centroid-training records.

The templates contain hash-pinned scientific configuration and named evidence
requirements. Supply only validated local files and their SHA-256 for the appropriate
requirement. File integrity alone does not establish scientific or hardware validity.
Review the method/protocol choices and the included [eight-item questionnaire](questionnaire.md)
before starting. Its wording, 1–9 scale and post-session timing come from Table 5
and Section 4.1. [protocol-schedule.json](../protocol-schedule.json) records what is
known and unknown. Original survey-platform exports and other forms are not
bundled. Synthetic examples remain demonstrations.

## During and after the session

Use **Start session** after preferences and required surveys. Follow the selected
turn protocol. Notifications and rejected offers do not create additional offers.
Duplicate or delayed commands must refer to the same session and displayed offer.
The application records agreement, deadline, withdrawal, interruption and operator
termination distinctly. A recording failure requires conductor attention before
continuing; restarting an interrupted session does not invent elapsed time.

After completion use **Build report**, or run `negotiator report PATH --output NEW_DIR`.
Keep original records and the generated report together, and export citations using
`negotiator cite PATH --format bibtex`. [Analysis guide](analysis.md).

## Materials for a new session

Each protocol requirement names its purpose. `execution` requirements cover the
model, instruments and presentation materials needed to run the configured study.
Their availability and hashes are checked before a session starts.
`historical-analysis` requirements describe evidence needed to assess the original
experiment; unavailable participant records do not prevent a new session.

This separation does not establish equivalence with the historical experiment.
A demonstration remains synthetic, and a missing runtime asset still blocks a
published-protocol run. Inspect historical requirements separately with
`protocol_readiness(spec, operation="historical-analysis")`.
