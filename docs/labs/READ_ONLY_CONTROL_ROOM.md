# A human-first control room with no hidden authority

**Paper UI specification and accessibility exercise. NOT an installed dashboard, monitor, background agent, browser controller or source of live status.** Based on publicly discussed visibility principles in the [September progress report](https://docs.google.com/document/d/1EtINjScE_enRNPv6g1tciIa0k4GUV697TFY4z56x3JE/edit) and the repository's [human control-room architecture chapter](../architecture/chapters/09-human-control-room.md).

## Goal

Let an ordinary person answer five questions without knowing the private mechanics of an AI system:

1. What mission and source revision are we looking at?
2. Which bounded work items are genuinely **verified**, still proposed, blocked, or not run?
3. Which evidence is fresh, stale, contradictory or missing?
4. Is a worker merely reachable or actually producing qualified work?
5. Which protected next action is waiting for a **new human decision**?

Start with a text mockup. Do not link the display directly to filesystem edits, command execution, remote accounts or publication.

## A minimum status card

```text
Fictional workshop — read-only status
Data type: SYNTHETIC              Refreshed: [actual timestamp / UNKNOWN]
Mission: draft an accurate workshop schedule (NO PUBLICATION)
Source revision: R1-A / R1-B        Reconciliation: CONFLICT OPEN

Task                     Evidence                 Status
Draft flyer text         local draft exists       DRAFT ONLY
Verify workshop time     conflicting notes        BLOCKED
Print flyer              worker said "printed"    UNVERIFIED
Publish schedule         no authority             NEEDS APPROVAL

Worker/session: [unobserved / reachable / recently acted, with time]
Health: not equal to qualified progress
Safe next action: human resolves time conflict; no action executed
```

The illustrative statuses above are **not a live feed**. In a real system, every time-bearing field should come from an actual current source or read `UNKNOWN`.

## Truth in interface design

| Dimension | Good visible label | Dangerous shortcut |
| --- | --- | --- |
| Connection | "Last response observed at [time]" | "ONLINE" based on remembered subscription |
| Work | "Output inspected and tests run on revision X" | "DONE" based on an AI promise |
| Review | "Review returned by provider Y on exact packet Z" | "AI COUNCIL APPROVED" with no receipts |
| Recovery | "Next worker has verified the current source" | "HANDOFF COMPLETE" because text was pasted |
| Authorization | "Needs current owner approval before publication" | Button that grants approval through a status view |
| Freshness | "As-of 12:00; not rechecked since" | Permanent green indicator |
| Costs | "Current API price/quota UNKNOWN" | Assume paid model access is included |

Never represent a source-provided field, check mark or old timestamp as authentication. Read-only observers should not gain write power by loading the page.

## Accessibility and progressive disclosure

- Present mission, result and unresolved blockers in ordinary language before technical details.
- Provide readable text labels **in addition to color** for PASS, FAIL, HOLD and UNKNOWN.
- Make keyboard navigation, screen-reader names and high contrast part of future implementation requirements.
- Avoid motion or animations whose meaning depends on continuous attention.
- Put source versions, raw receipts and failure history behind an optional *read-only* details view when a real UI is implemented.
- Distinguish "there is no new work" from "the monitor cannot currently observe the work".
- Voice input, if later offered, is not identity proof or permission to perform protected actions.

## Paper acceptance checklist (not tested)

| ID | Test | Required behavior |
| --- | --- | --- |
| UI-01 | Source is stale | Show source age and uncertainty |
| UI-02 | Worker is alive but idle | Do not mark useful work complete |
| UI-03 | Previous test was invalidated | Show both old receipt and current HOLD |
| UI-04 | Two sources conflict | Show both; do not auto-select a preferred one |
| UI-05 | Tool returns no data | Show UNKNOWN instead of a fictional heartbeat |
| UI-06 | Reviewer identity is unavailable | Do not claim named independent review |
| UI-07 | User clicks a descriptive status card | No protected external action |
| UI-08 | Required approval absent | Display "approval needed"; do not synthesize a grant |
| UI-09 | Screen reader cannot distinguish statuses | Accessibility check FAIL |
| UI-10 | Dashboard only exists on paper | Mark `DESIGN ONLY / NOT RUN` |

## Scope and next step

The current repository contains educational text and schemas, **not this live dashboard**. A future executable UI would require independent code review, confinement of any computer tools, real telemetry controls, no hidden callbacks, privacy compliance, clean-machine tests, explicit licenses and owner approval before release.

Try [the fictional casebook](../examples/CONTINUITY_CASEBOOK.md) for sample tasks and [measuring continuity](../MEASURING_CONTINUITY.md) for meaningful metrics.
