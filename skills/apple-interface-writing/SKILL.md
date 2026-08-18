---
name: apple-interface-writing
description: Draft, rewrite, or audit concise interface text using an independently expressed reference-only interpretation of Apple's Human Interface Guidelines for writing. Use for buttons, labels, settings, alerts, errors, onboarding, notifications, permissions, empty states, and multi-screen app flows where wording must make actions and consequences clear in limited space.
---

# Apple interface writing

Use language as part of the interaction. Make each screen's purpose, choice, and
result understandable with minimal text.

## Protect interaction truth

- Preserve the actual action, consequence, permission, data state, and recovery path.
- Do not make a destructive action sound reversible.
- Do not claim data is saved, private, secure, or recoverable without evidence.
- Respect supplied character, localization, platform, and accessibility constraints.

## Define voice, then adapt tone

Choose a stable app voice from its audience and purpose. Adapt the tone to the moment:

- Routine action: neutral and direct.
- Success: specific and proportionate.
- Delay or interruption: calm and informative.
- Error or loss risk: serious, plain, and recovery-focused.
- Permission request: transparent about purpose and user benefit.

Do not copy a recognizable corporate personality. Apply the interaction principles
to the product's own voice.

## Write each screen

1. State the screen's single purpose and the decision or action it supports.
2. Put the most important information before explanation.
3. Use a verb for an action label and make the label predict the result.
4. Keep terminology and navigation labels consistent across the flow.
5. Use supporting text only for a consequence, requirement, unfamiliar concept, or
   choice that the label cannot carry.
6. Make completion, cancellation, and the next step explicit.

## Write errors and alerts

- Name the problem in terms the person can observe.
- Give the most useful recovery action and preserve state information when known.
- Use specific button labels for consequential choices. Avoid generic confirmation
  when the action itself can be named.
- Put irreversible consequences beside the action that triggers them.
- Remove interjections, jokes, and apologies that do not help recovery.
- Do not use `we` when it is unclear whether it means the app, company, device, or team.

## Write for the device and everyone

- Use the correct interaction verb for the platform and input method.
- Prefer plain, inclusive language that localizes without relying on wordplay.
- Do not rely on color, position, sound, or vision alone to explain an action.
- Remove unnecessary possessives when the interface already establishes ownership.
- Test expansion: translated text may need more space than the source.

## Avoid

- cute labels that hide the result, such as a celebratory phrase instead of `Send`
- `click here`, vague `OK`, and labels that require reading a paragraph to decode
- inconsistent terms for the same screen, object, or action
- exposing implementation details that do not help the choice
- blame, fake empathy, false reassurance, and difficulty judgments
- a wall of explanation on a screen that supports one decision

## Final pass

Read the flow as a sequence of choices. Confirm that each label predicts the next
state, risky consequences are visible in time, errors support recovery, terms stay
consistent, and the text works without an assumed visual cue.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
