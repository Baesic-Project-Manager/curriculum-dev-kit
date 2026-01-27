# Topic Outline Review Template

**Purpose:** Structured document for instructor review of existing presentation content before rework begins
**When to Use:** Phase 1 of any module rework — before creating Presentation Development Brief
**Output:** Instructor-approved priorities and consolidation decisions

---

## Instructions

1. Analyst reviews existing presentation (PDF/slides) and populates structure
2. Instructor reviews each section and adds notes
3. Instructor completes Decision Points checklist
4. Decisions feed into Presentation Development Brief

---

## Document Header (Copy and Customize)

```markdown
# {Course} {Module}: Topic Outline for Priority Review

**Purpose:** Review current slide structure and assign priorities for {Month Year} rework
**Current State:** {X} slides (~{Y} min) → **Target:** {A-B} slides (~{C-D} min + buffer)
**Action Needed:** Mark each section as HIGH / MEDIUM / LOW priority

---

## Quick Math

| Metric                          | Value           |
| ------------------------------- | --------------- |
| Session Duration                | {90} minutes    |
| Buffer (transitions, questions) | {3-5} minutes   |
| Available Presentation Time     | {85-87} minutes |
| Target Slide Count              | {32-34} slides  |
| **Slides to Cut/Consolidate**   | **{X} slides**  |
```

---

## Section Template (Repeat for Each Section)

```markdown
### Section {Letter}: {Section Name} (Slides {X-Y}) — {N} slides

| Slide | Title | Content Summary | PRIORITY |
| ----- | ----- | --------------- | -------- |
| {#}   | {Title} | {Brief description} | {High/Medium/Low/Required/Redundant} |

**Observations:**
- {Analysis of redundancy, overlap, or consolidation opportunities}
- {Questions for instructor consideration}

**Instructor Notes:**
> _{Instructor fills in their thoughts, priorities, concerns}_
```

---

## Priority Labels Guide

| Label        | Meaning                                           |
| ------------ | ------------------------------------------------- |
| **Required** | Must keep — foundational or certification-aligned |
| **High**     | Important — keep unless major time pressure       |
| **Medium**   | Valuable but could be condensed                   |
| **Low**      | Nice-to-have — cut first if needed                |
| **Redundant**| Duplicate content — consolidate or remove         |

---

## Decision Points Section Template

Include at end of document for instructor to check off:

```markdown
## Instructor Decision Points

Please indicate your preferences:

### 1. {Topic/Slides in Question}
- [ ] Option A: {Description}
- [ ] Option B: {Description}
- [ ] Other: _______________

### 2. {Next Topic/Slides}
- [ ] Option A
- [ ] Option B
- [ ] Option C

{Continue for each major decision point identified}

### {Final}: Any sections to ADD depth to?
> _{Instructor notes}_
```

---

## Consolidation Opportunities Table

Include after all sections, before Decision Points:

```markdown
## Recommended Consolidation Opportunities

| Current | Proposal | Slides Saved |
| ------- | -------- | ------------ |
| Slides {X-Y} ({Topic}) | Consolidate to {N} slide(s) | {N} |

**Potential Total Saved:** {X-Y} slides → **{Target achieved/Gap remaining}**
```

---

## File Naming Convention

`01_Topic_Outline_Review.md`

- Always number as `01_` to indicate it's the first working document
- Place in module's rework folder

---

## Workflow Integration

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: ANALYSIS                                          │
│  ├── Analyze existing presentation                          │
│  ├── Create 01_Topic_Outline_Review.md  ← THIS TEMPLATE     │
│  └── Instructor completes review                            │
├─────────────────────────────────────────────────────────────┤
│  PHASE 2: PLANNING                                          │
│  ├── Create Presentation_Development_Brief.md               │
│  │   (informed by instructor decisions above)               │
│  └── Lock structure before drafting                         │
├─────────────────────────────────────────────────────────────┤
│  PHASE 3: DEVELOPMENT                                       │
│  ├── Draft speaker notes using Speaker_Notes_Format_Spec    │
│  └── Update HTML presentation                               │
├─────────────────────────────────────────────────────────────┤
│  PHASE 4: REVIEW                                            │
│  └── Quality check and timing verification                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Sample Instructor Feedback (What Good Looks Like)

**Helpful feedback:**

> "I think if the Five Factors Overview is going to remain, we should mention it at the beginning and flow logically through it. As it stands, the order doesn't make sense."

> "I just don't want a 'slide for every term or stage' if that makes sense?"

> "This is a topic I usually misspeak on — make sure the speaker notes are extra clear here."

**Why this feedback helps:**

- Reveals instructor's teaching style
- Identifies pain points in current materials
- Prioritizes speaker note clarity for difficult sections

---

*This template is part of the Curriculum Dev Kit.*
