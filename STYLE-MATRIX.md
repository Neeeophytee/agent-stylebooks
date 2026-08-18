# Style matrix

| Skill | Audience | Optimizes for | Distinctive behavior | Avoids |
| --- | --- | --- | --- | --- |
| `google-developer-docs` | Technical practitioners, often global | Clarity and successful implementation | Direct address, explicit actors, consistent terms, clean procedures | Idioms, assumed ease, vague pronouns |
| `govuk` | People completing a public-service task | Fast comprehension and confident decisions | User need first, front-loaded headings, concrete eligibility and actions | Department-first framing, policy jargon, promotional language |
| `gitlab-docs` | Product users and contributors | Searchability, precision, and trust | Brief conversational voice, topic types, customer perspective | Marketing claims, self-referential intros, ambiguity |
| `github-docs` | Developers using a product or workflow | Goal completion and approachable support | Prerequisites, outcome-led steps, useful troubleshooting | Unexplained context, blame, "obvious" assumptions |
| `kubernetes-docs` | Cluster operators and cloud-native developers | Technical accuracy across versions | Feature-state context, explicit resources, verification and cleanup | Future promises, stale time words, ambiguous `we` |
| `mdn-web-docs` | Web developers from beginner to expert | Clear reference and transferable learning | Audience-aware definitions, runnable examples, standards context | Missing assumptions, decorative examples, blurred facts |
| `red-hat-docs` | Enterprise administrators and developers | Modular, reusable, supportable documentation | Concept/procedure/reference separation, prerequisites and verification | Mixed topic types, hidden state, ornamental prose |
| `18f-content` | People using government digital services | Inclusive task completion | Plain language, service recovery, accessible labels, evidence-based order | Bureaucratese, agency-centric explanations, shame or blame |
| `microsoft-writing-style` | Product users and support audiences | Friendly, scannable help | Important point first, direct action, solution-oriented errors | Formal distance, unnecessary detail, user blame |
| `mailchimp-content` | Small-business and marketing customers | Clear, encouraging education | Familiar voice, situation-aware tone, restrained humor | Hype, forced jokes, condescension, B2B fog |
| `apple-interface-writing` | People moving through an app | Clear choices in limited space | Verb-led labels, consistent flows, tone matched to context | Cute labels, vague errors, unnecessary possessives, device mismatch |

## Selection rule

Select by artifact and user need, not by which organization the subject mentions.
A Kubernetes tutorial usually benefits from `kubernetes-docs`; a government form
about Kubernetes might benefit from `govuk`. If two styles both fit, state which
one governs structure and which one contributes a narrow secondary constraint.
