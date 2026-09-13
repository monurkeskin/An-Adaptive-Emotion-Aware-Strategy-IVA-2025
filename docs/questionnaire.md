# The negotiation questionnaire

The [IVA 2025 paper](https://doi.org/10.1145/3717511.3747087) reports eight
negotiation-experience questions in Table 5. The items below preserve that wording.
The response scale is **1 = strongly disagree** to **9 = strongly agree**.

| Item | Published wording |
| --- | --- |
| Q1 | Nao negotiated fairly. |
| Q2 | Nao negotiated with me like a human. |
| Q3 | Nao determined her next offer according to my emotional state. |
| Q4 | Nao tried to find the best deal for us. |
| Q5 | Nao cared about my preferences. |
| Q6 | Nao considers my behavior. |
| Q7 | I'm satisfied with my performance. |
| Q8 | Nao often made very unfair offers. |

Section 4.1 places the questionnaire after a main negotiation, before the
ten-minute break and the next session. Both order configurations schedule these
items after each main session and exclude practice. Responses refer to the
particular session, preserving Solver/Hybrid condition and session position.

The [instrument file](../instruments/iva-2025-post-session.json) records the item
identifiers, wording, scale and timing. The two [protocol configurations](../CONFIGURATIONS.md)
embed the same items, so importing a configuration also imports its questionnaire.
The shared GUI displays the numeric scale and both endpoint descriptions.

## Interpreting the answers

Keep the items separate. Q8 has negative wording; the paper does not specify an
automatic reversal or a composite score. Table 5's published means and standard
deviations are references for reading the paper, not inputs for reconstructing
individual responses.

This implementation lets people skip questions. The paper does not state whether
the original form forced a response, so this is a documented software choice.
Skipped items retain `null` with `not_answered`; an eligible questionnaire that
was never reached retains `not_administered`. A practice session has no scheduled
items and therefore contributes no missing-response rows. CSV cells for missing
values are blank; they are never scored as zero.

The tests traverse both session orders, retry a submission, replay the journal
and inspect JSON/CSV exports. They use synthetic session endings and responses.
The original form export, demographics/consent forms and participant responses
are not part of this recovered instrument.

## Changing the instrument for a new study

Import the paper configuration and review the wording and timing in **Advanced
settings and questionnaires**. Changes to wording, scale descriptions or timing
change the protocol fingerprint. Record a new study/protocol revision when you
change the instrument; the original Table 5 wording remains available here.
