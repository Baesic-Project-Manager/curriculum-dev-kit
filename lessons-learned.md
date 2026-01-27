# Lessons Learned

Discoveries from building and using this curriculum development system at scale.

---

## What We Discovered

### The Brief-First Principle Works

The most important insight from this project: **completing the Presentation Development Brief before building anything prevents most problems.**

When we let ourselves "just start making slides," we consistently:
- Exceeded slide budgets by 30-50%
- Made conflicting design decisions
- Had to rework significant portions
- Ran over time in delivery

When we locked the brief first:
- Slide counts matched targets within 1-2 slides
- Design decisions were consistent
- Rework was minimal
- Timing worked in actual delivery

**The discipline of the brief isn't bureaucracy — it's the thing that makes everything else easier.**

---

### Timing Math Is Non-Negotiable

Early versions of this system didn't enforce timing calculations. We thought experienced instructors would "feel" the right length.

They didn't. Everyone optimistically added "just one more slide" until modules ran 20-30 minutes over.

The formula that worked:

```
(Session time - buffer - activities) ÷ 2.5 = max slides
```

The 2.5 minutes/slide factor accounts for:
- Slide transitions (~10 seconds each)
- Natural pauses for emphasis
- Occasional audience questions
- Brief elaborations beyond notes

Faster-paced sessions might work at 2 min/slide. Interactive sessions might need 3 min/slide. But 2.5 is a reliable default.

---

### Dual-Tool Research Catches Blind Spots

Initially we used only NotebookLM for research. It worked, but reports had a consistent perspective — whatever sources we happened to provide.

Adding Gemini as a second research stream changed the quality:

| What We Found | Why It Mattered |
|---------------|-----------------|
| NotebookLM gave depth | Strong synthesis of provided sources |
| Gemini gave breadth | Practitioner perspectives we didn't think to seek |
| Contradictions surfaced | When tools disagreed, we investigated further |
| Coverage improved | Topics we thought we'd covered had gaps |

The investment of running both tools paid back in content that felt complete.

---

### Speaker Notes Are Scripts, Not Outlines

The biggest mistake in our early modules: treating speaker notes as bullet point outlines.

```
❌ What we wrote:
• Cover project charter
• Explain stakeholders
• Discuss success criteria

✓ What actually helped:
"We've established why initiation matters — now let's get
specific about what you actually produce during this phase.
There are six key components, and I want to be clear: you
don't always create all six on every project."
```

The shift to conversational prose meant:
- Instructors could deliver confidently without extensive prep
- Timing was predictable (you can time prose; you can't time bullets)
- Substitute instructors could step in effectively
- Consistency across multiple deliveries improved

**Write for the ear, not the eye.**

---

### The Next Session Preview Is A Trap

AI tools consistently generate plausible but incorrect "Next Session Preview" content. They'll write confident bullet points about topics that don't exist in the next module.

We added explicit warnings to the template after this happened multiple times:

```html
<!--
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
STOP - THIS CONTENT IS A PLACEHOLDER
DO NOT TRUST AUTO-GENERATED CONTENT HERE.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-->
```

**Always verify against the actual course syllabus.**

---

### White Backgrounds Print Better

Our original design used gradient backgrounds on callout boxes. They looked nice on screen but printed terribly — muddy gradients that obscured text.

The switch to white backgrounds with subtle shadows:
- Prints cleanly in grayscale
- Looks modern on screen
- Reduces visual complexity
- Works across different projectors/displays

**Design for the worst display environment you'll encounter.**

---

### QA Checklists Catch Obvious Errors

We resisted formal QA at first. "We'll just review it."

Then we shipped a module with:
- Slide numbers out of sequence
- Footer text referencing the wrong course
- A hardcoded hex color that didn't match the design system
- A "Next Session Preview" about a nonexistent topic

The checklist catches the things you stop seeing after staring at a document for hours.

---

### The Bias Check Adds Genuine Value

We initially included bias checks because best practices said to include them. Then we discovered they're one of the most-discussed elements in student feedback.

What works:
- One bias per module (focus, don't overwhelm)
- Connect to module content specifically
- Provide a counter-strategy (not just "be aware")
- Make it practical ("Where might this affect your current work?")

The Planning Fallacy bias check generates more "aha" moments than almost any other content.

---

### Handoff Is The Real Test

The true test of documentation isn't whether the original creator can follow it. It's whether someone new can pick it up and produce the same quality.

We validated this system by having different team members:
1. Follow the templates without additional guidance
2. Produce complete modules
3. Have those modules reviewed blind

When outputs were consistent regardless of who created them, we knew the system worked.

---

## What We'd Do Differently

### Start with the templates earlier

We built templates after creating several modules "freeform." This meant retrofitting inconsistent early modules to match the eventual standards.

**Build templates from day one, even if they're rough.**

### Enforce the brief lock more strictly

We sometimes let production start before briefs were fully locked "because we knew what we wanted." This always led to mid-production changes that cost more than waiting would have.

**The brief isn't locked until it's locked.**

### Track time-to-production

We didn't measure how long each phase actually took. This made it hard to plan future development or identify bottlenecks.

**Measure the process, not just the outputs.**

### Include more worked examples

Early versions of templates had explanations but few examples. Adding realistic examples significantly improved adoption.

**Examples > explanations.**

---

## Metrics That Mattered

| Metric | Before System | After System |
|--------|---------------|--------------|
| Slide budget adherence | 60% within target | 95% within target |
| Timing accuracy | ±15 minutes | ±3 minutes |
| First-draft approval rate | ~40% | ~85% |
| Time to complete module | Highly variable | Predictable within 20% |
| Handoff success | Required extensive knowledge transfer | Self-service with templates |

---

## Principles Worth Remembering

1. **Constraints enable creativity.** Slide budgets and timing limits force better decisions.

2. **Separate concerns.** Research, synthesis, planning, and production are different activities. Do them separately.

3. **Lock before building.** The brief-first principle prevents the most common problems.

4. **Write for delivery.** Speaker notes should sound like speech, not read like documentation.

5. **Validate with handoff.** If someone new can follow the system, it works.

6. **Checklists catch fatigue.** Use them for the obvious things you stop seeing.

7. **Two perspectives beat one.** Dual-tool research surfaces blind spots.

---

*"A system that works once is an accident. A system that works repeatedly is a process worth documenting."*
