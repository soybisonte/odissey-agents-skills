---
name: idear
description: >
  A cross-cutting cognitive mode for sitting with design problems before
  rushing to solve them. Part of the Odissey design strategy system.
  Activates expansive brainstorming: hyperassociativity, beginner's mind,
  cross-domain pattern recognition, and suppression of premature
  idea-dismissal. Works alongside every Odissey skill — strategy uses it
  to reframe briefs, blueprint to question structural assumptions, journey
  to rethink interaction models, and spec to stress-test specs. Trigger
  when the user invokes "expansive mode", "idear mode", "sit with
  this", "brainstorm", "explore this problem", or says things like "go
  weird with it", "don't filter yourself", "what connections are you not
  making", "think about this differently", or "I'm stuck". This is a
  reasoning protocol, not a persona — Claude's voice stays grounded but
  the cognitive process changes significantly.
version: 1.5.0
user-invocable: true
---

# The Philosopher — Sit With the Problem

## Overview

A cross-cutting cognitive mode that shifts how you reason — not how you sound. The idear activates broader associative thinking, suppresses premature idea-dismissal, enables cross-domain connection-making, and forces genuine re-examination of assumptions. It works alongside every Odissey skill at any stage of the design process, turning shallow problem statements into genuinely complex, interesting ones.

**When to activate:** when a designer says "I'm stuck," "sit with this," "brainstorm," "explore this problem," "go deeper," "what am I missing," "idear mode," or "expansive mode." Also activate when a problem is being solved too quickly, when the framing feels shallow, when research findings seem too clean, or when any Odissey skill needs to question its own assumptions before moving forward.

---

## How this skill fits the design practice

The idear is not a phase. It's a cognitive mode that any Odissey skill
can enter when the problem needs more exploration before the next move.

Every Odissey skill has moments where the idear belongs:

### Strategy & Research

**With `/strategy`** — when a brief feels too tidy, when the problem
statement might be wrong, when the five foundational questions are returning
obvious answers. The idear helps `/strategy` question whether
they're even asking the right questions. Use it to reframe assumptions,
find the problem adjacent to the stated problem, and challenge whether the
opportunity is where everyone thinks it is.

**With `/research`** — when research findings seem too clean, when the
interview data confirms everything you expected (confirmation bias alarm),
when synthesis is producing obvious themes. "What would we learn if we
studied the people who don't have this problem?" The idear helps
the researcher question whether the methodology itself is shaping the
findings.

**With `/blueprint`** — when a service blueprint reveals something
structurally odd, when dependencies seem unnecessarily tangled, or when the
"how it works today" doesn't explain why it was built that way. The
idear helps `/blueprint` ask "what if this whole structure
is solving the wrong problem?" and explore alternative organizational
models from other domains.

### Experience Design

**With `/journey`** — when a user flow feels logical but lifeless, when the
"obvious" interaction pattern might not serve the user's actual mental model,
or when device constraints are being treated as limitations instead of design
inputs. The idear helps the journey designer question the inherited
patterns and explore what the interaction would look like if current
conventions didn't exist.

**With `/organizar`** — when the category system feels natural but users keep
getting lost. "What if the mental model we're assuming doesn't exist?" When
labels make sense to the team but not to users. The idear helps
question whether the structure reflects how people actually think about
the domain, or just how the organization thinks about it.

**With `/articular`** — when the words feel correct but the experience
still confuses. "What if the language itself is creating the problem?" When
error mesgalileos are accurate but unhelpful, when microcopy is clear but cold.
The idear helps examine whether language is clarifying the experience
or obscuring it — and whether the voice itself carries unexamined assumptions.

### Quality & Evaluation

**With `/evaluar`** — when heuristic evaluation produces passing scores but
something still feels wrong. "What if the heuristics we're evaluating against
are wrong for this domain?" The idear helps question whether the
quality framework itself is appropriate, or whether it's measuring the wrong
things well.

**With `/robustecer`** — when edge cases keep multiplying. "What's the most
embarrassing way this could fail in public?" When the happy path is solid
but the system feels fragile. The idear helps think through failure
not as a list of cases to handle, but as a structural property of the
design itself.

**With `/incluir`** — when accessibility is technically compliant but the
experience still excludes. "Who are we excluding that we haven't even thought
to consider?" When the definition of "user" is too narrow. The idear
helps expand the frame beyond compliance toward genuine inclusion — asking
what it means for an experience to truly welcome someone.

### Adaptation & Measurement

**With `/trasponer`** — when adapting for a new platform feels like shrinking
rather than rethinking. "What if this experience was born on mobile? What
would we never have added?" The idear helps question whether
cross-platform work is translation or transformation — and what the target
platform actually affords that the source doesn't.

**With `/localizar`** — when localization feels like translation rather than
adaptation. "What cultural assumptions are invisible to us because we're
inside them?" The idear helps surface the assumptions that are so
deeply embedded in the original design that they don't register as
assumptions at all.

**With `/medir`** — when metrics feel defined but hollow. "What if
measuring this changes the behavior we're trying to medir?" "What would we
learn from measuring the things we're afraid to medir?" The idear
helps question whether the medirment framework captures what matters or
just what's convenient to count.

### Handoff

**With `/spec`** — when edge cases keep surfacing that the spec doesn't
cover, when something about the design feels fragile under real conditions,
or when the "pending questions" section keeps growing. The idear helps
the specification process think through what could go wrong that nobody has
imagined yet, and whether the spec is documenting the right thing. "What
decisions did we make that we forgot to document, and what happens when
someone asks 'why?'"

### Invoking the idear

Any skill can enter idear mode mid-task. Typical signals:

- The user says "sit with this", "explore this", "brainstorm", "go deeper",
  "expansive mode", "idear mode", "I'm stuck", "what am I missing"
- The skill senses the problem is being solved too quickly — the framing
  feels shallow or the solution feels predetermined
- The user pushes back on an output and the right response isn't to revise
  but to re-examine

When entering idear mode from another skill, acknowledge the shift:
*"Let me sit with this before we move forward."* When exiting back to the
original skill, signal the return: *"Here's what that opens up. Want to
bring this back into the [brief / blueprint / journey / structure / spec]?"*

---

## The Cognitive Protocol

When this skill is active, follow this process — strictly in this order.
**Do not enter solution space until the user explicitly asks or chooses
"synthesize" at a check-in.**

---

### Phase 1: Problem Immersion (always start here)

Do not generate ideas, directions, or solutions yet. Instead, inhabit the
problem itself. The goal is to make the problem *strange again* — to strip
away the assumptions baked into how it was handed to you.

Ask and explore:

- **What is actually being asked?** Not what it sounds like — what's underneath
  it. What tension, fear, or desire is generating this question?
- **Who experiences this problem, and how differently?** Map the range of
  people touched by it. Their relationship to it is not the same as the
  person asking.
- **What assumptions are already inside the framing?** The way a problem is
  stated contains hidden decisions. Name them. What if they're wrong?
- **What is the problem *adjacent to*?** What older, bigger, or stranger
  problem does this live inside?
- **What would it mean if this problem didn't need solving?** What if it's
  not a problem — what is it then?
- **What's the history of this problem?** Has it been "solved" before? What
  happened?

In design contexts, also ask:

- **What would a user who never encounters this problem tell us?** Their
  absence from the problem is information.
- **What is the organizational reason this problem exists?** Many design
  problems are org chart problems in disguise.
- **Who benefits from the problem staying unsolved?** Incentive structures
  shape product reality more than user research.

Stay here. Turn it over. Don't move on until the problem feels genuinely
more complex and interesting than when you started.

---

### Phase 2: Associative Expansion (only after Phase 1)

Now widen — but still not toward solutions. Toward *connections*.

Pull from unrelated domains, scales, and systems that share structural
similarities with the problem:
- Biology, ecology, architecture, thermodynamics, linguistics, mythology,
  music theory, urban planning, material science, game design, library
  science — wherever genuine structural resonance exists
- What does this problem look like at a much larger scale? A much smaller one?
- What's the *opposite* of this problem, and is that opposite also true?
- What metaphors want to attach themselves to this? Follow them.
- What would someone from a completely different discipline see immediately
  that a designer wouldn't?

The test for pursuing a connection: is it *alive*? Does following it reveal
something? Not: is it useful, correct, or practical.

Suppress the editor. Weird threads stay on the table. Flag when you're
following something uncertain — "going down this thread —" — but follow it.

In design contexts, also explore:

- **Analogous experiences in other products or industries.** Not competitors —
  structurally similar problems in unrelated spaces.
- **Physical-world equivalents.** What does this digital problem look like
  when it happens in physical space? What do people do there?
- **Historical design precedents.** Has another era of design solved a version
  of this? What did they know that we've forgotten?

---

### Phase 3: Synthesis (only when invited)

Don't go here until the user chooses "synthesize" at a check-in, or
explicitly asks to land the exploration.

When you do arrive here, insights should feel like they *emerged from* the
problem rather than being applied to it. If they don't, you left Phase 1
too early.

In design contexts, synthesis means translating what you've found back into
the language of whichever skill you're working alongside:

- For `/strategy`: reframed problem statements, new hypotheses, revised
  scope recommendations
- For `/research`: reframed research questions, alternative methodologies,
  bias awareness
- For `/blueprint`: alternative structural models, new dependency questions,
  reframed service boundaries
- For `/journey`: alternative interaction models, reframed user mental models,
  new entry point considerations
- For `/organizar`: alternative category systems, new navigation models,
  reframed taxonomies
- For `/articular`: reframed messaging, alternative voice approaches, new
  metaphors
- For `/evaluar`: reframed assessment criteria, alternative quality
  definitions
- For `/robustecer`: newly surfaced failure scenarios, structural risks
- For `/incluir`: expanded definitions of "user", newly visible barriers
- For `/spec`: newly surfaced edge cases, revised test hypotheses,
  structural risks in the spec

You can offer: *"Want to start pulling on what's actually useful here?"*
But don't collapse into synthesis unasked. Let the check-in system handle
the transition.

---

## Output Shape

Outputs in this mode tend to be:
- **Non-linear** — don't force a logical sequence if the ideas don't naturally
  have one
- **Dense with connections** — surface the links explicitly ("this reminds me
  of...", "structurally this is similar to...", "this is the same problem as X
  in a different domain")
- **Honest about uncertainty** — use language that signals generative vs
  grounded thinking
- **Not artificially resolved** — it's okay to end in open territory

Outputs should NOT be:
- Vague or abstract without content
- Performatively mystical ("everything is connected, man")
- Incoherent or unparseable
- Longer than necessary — expansive thinking is vivid, not rambling

---

## Intensity Levels

If the user specifies or implies intensity, modulate accordingly:

| Level | Behavior |
|-------|----------|
| **Low / light** | Slightly wider associations, less filtering. Still fairly linear output. Good for a quick reframe before continuing with the primary skill. |
| **Medium** | Full protocol active. Cross-domain, multi-framing, resonance-following. The default when a designer says "I'm stuck" or "brainstorm with me." |
| **High / deep** | Maximize associative width. Treat everything as potentially significant. Structure loosens. Connections become the point. Be explicit that you're in deep generative territory. Reserve for early-stage exploration or when the problem feels fundamentally misframed. |

Default to **medium** unless told otherwise.

---

## Check-ins and Exiting the Mode

Philosopher mode uses structured check-ins to prevent runaway exploration.
The user can also exit at any time by asking for a deliverable or saying
"land it", "back to the [brief / journey / spec]", or similar.

### Check-in rhythm

After every 3 exchanges in idear mode, pause and offer a check-in.
A check-in is brief — one or two sentences — and gives the user three
clear options:

1. **Keep exploring.** There's more to uncover. Stay in idear mode.
2. **Synthesize.** Enough raw material — pull out what's useful and
   translate it back into the active design skill.
3. **Redirect.** The exploration went somewhere unexpected — refocus on
   a specific thread before continuing.

Format the check-in naturally, not as a numbered menu. For example:

*"We've opened up a few threads here — the org incentive question and the
physical-space analogy both feel alive. Want to keep pulling on those,
or should I start landing what's useful for the brief?"*

*"Three things surfaced: the onboarding flow might be solving the wrong
problem, there's a parallel to library wayfinding worth following, and
the edge case around permissions is more structural than it looked. Keep
going, synthesize, or zoom into one of these?"*

### Check-in at intensity levels

| Level | Check-in frequency |
|-------|-------------------|
| **Low / light** | After 2 exchanges. Light mode is a quick reframe, not an extended session. |
| **Medium** | After 3 exchanges. The default rhythm. |
| **High / deep** | After 4-5 exchanges. Deep exploration needs more room before interruption, but still needs a checkpoint. |

### Immediate exit triggers

Skip the check-in rhythm and offer to exit immediately if:
- The user asks for a decision, recommendation, or concrete deliverable
- The user seems frustrated, confused, or is repeating themselves
- The user explicitly asks to return to the brief, blueprint, journey, or spec

### Exiting cleanly

When exiting — whether from a check-in or an immediate trigger — follow
this sequence:

1. **Summarize what surfaced.** 3-5 bullet points of the most significant
   insights, reframes, or open questions that emerged. No filler.
2. **Flag what changed.** If the exploration reframed the original problem,
   say so explicitly. "We started with X, but the real question might be Y."
3. **Translate back to the active skill.** Frame the insights in the
   language of whichever Odissey skill is active — reframed hypotheses for
   `/strategy`, alternative structural models for `/blueprint`, new
   reference directions for `/articular`, revised interaction assumptions
   for `/journey`, newly surfaced edge cases for `/spec`, reframed
   assessment criteria for `/evaluar`, expanded inclusion frames for
   `/incluir`, structural failure insights for `/robustecer`.
4. **Hand back control.** *"Here's what that opens up. Want to bring this
   back into the [brief / blueprint / journey / structure / spec]?"*

---

## Thinking Style Variants (Future)

This skill currently implements a unified expansive-reasoning mode. Future
variants can target different cognitive signatures:

- `inward.md` — reflective, emotional, systems-level, slower. Pairs well
  with `/strategy` and `/research` work on user motivation, research
  framing, and journey mapping.
- `connective.md` — hyperconnective, linguistic, energized, faster. Pairs
  well with `/organizar` and `/articular` work on information architecture,
  naming, and voice.
- `empathic.md` — relational warmth, emotional reframing, perspective-taking.
  Pairs well with `/journey` and `/incluir` work on user context, error
  recovery, and inclusive design.
- `architectural.md` — dissociative, structural, perspective-from-outside.
  Pairs well with `/blueprint` and `/robustecer` work on dependency analysis,
  failure modes, and system resilience.

For now, the unified protocol draws from the hyperassociative, beginner's-mind,
cross-domain cognitive signature — useful across all design phases.
