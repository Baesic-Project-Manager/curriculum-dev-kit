# Speaker Notes Format Specification

**Used in:** Phase 4 (Production) — after slides are built
**Purpose:** Defines the structure, voice, and format requirements for speaker notes
**Companion:** `04-speaker-notes-sample.md` shows these specs in action

---

## Overview

Speaker notes are written delivery scripts that enable confident presentation without extensive preparation. They are NOT bullet points or outlines — they are conversational scripts written as you would actually speak.

**Core Principle:** Someone unfamiliar with the content should be able to deliver the presentation effectively using only the slides and speaker notes.

---

## Document Header

Every speaker notes document begins with a header block:

```
Course: {Course Number} - {Course Title}
Module: {Module Number} - {Module Title}
Duration: {Target time} ({Slide count} slides)
Activities: {List any formal activities, or "Organic discussion only"}
Version: {Date}
```

**Example:**
```
Course: Course 2 - Introduction to Planning
Module: Module 1 - Planning Fundamentals
Duration: 90 minutes (31 slides)
Activities: Organic discussion only (no formal breakout activities)
Version: January 2025
```

---

## Per-Slide Structure

Each slide follows this format:

```
---

## Slide {Number}: {Slide Title}
[{Time allocation}]

**{Section Label}:**
{Content for that section}

**{Section Label}:**
{Content for that section}

---
```

### Required Elements

| Element | Format | Required? |
|---------|--------|-----------|
| Slide number and title | `## Slide 1: Title Here` | Always |
| Time allocation | `[2 minutes]` or `[2-3 minutes]` | Always |
| At least one section label | See Section Labels below | Always |
| Transition Cue | For all slides except the last | Almost always |

---

## Section Labels

Use these standardized labels to organize content within each slide's notes:

### Opening Remarks
**Use for:** Title slide, first slide of a new major section
**Purpose:** Sets context, welcomes learners, frames what's coming

### Content Delivery
**Use for:** The main instructional content of the slide
**Purpose:** What you actually say to teach the material
**Format:** Written as spoken dialogue, natural prose

### Practical Example
**Use for:** Real-world applications, case studies, scenarios
**Purpose:** Grounds abstract concepts in concrete situations
**Note:** Not every slide needs this — use when examples add value

### Key Takeaway
**Use for:** The single most important point from this slide
**Purpose:** Reinforces retention, signals what matters most
**Format:** Usually 1-2 sentences, can be a memorable phrase

### Transition Cue
**Use for:** Bridging from this slide to the next
**Purpose:** Creates narrative flow, prevents abrupt topic shifts
**Format:** Explicit statement connecting current topic to upcoming topic

### Closing Remarks
**Use for:** Final slide only
**Purpose:** Wraps up the session, provides closure, previews next session

---

## Section Label Usage by Slide Type

| Slide Type | Typical Labels Used |
|------------|---------------------|
| Title Slide | Opening Remarks |
| Learning Objectives | Content Delivery |
| Module Overview | Content Delivery, Transition Cue |
| Standard Content | Content Delivery, Key Takeaway, Transition Cue |
| Case Study | Content Delivery, Practical Example, Key Takeaway, Transition Cue |
| Bias Check | Content Delivery, Key Takeaway, Transition Cue |
| Key Takeaways | Content Delivery, Closing Remarks |

---

## Voice and Tone Requirements

### DO — Target Voice Characteristics

| Characteristic | Example |
|----------------|---------|
| **First-person delivery** | "I want you to think about..." not "Students should think about..." |
| **Direct address** | "You'll encounter this when..." not "One encounters this when..." |
| **Conversational prose** | Written as you would actually speak, not formal writing |
| **Acknowledge complexity** | "This sounds straightforward, but here's where it gets tricky..." |
| **Honest about limitations** | "This framework is useful, but it has blind spots..." |
| **Specific metrics/data** | "Projects with clear charters are 2.5 times more likely to..." |
| **Professional but approachable** | Colleague sharing expertise, not lecturer talking down |

### AVOID — Voice Anti-Patterns

| Anti-Pattern | Example to Avoid |
|--------------|------------------|
| **Marketing language** | "This revolutionary framework will transform..." |
| **Hedging that undermines** | "I think maybe this might be important..." |
| **Academic jargon without explanation** | Using terms without defining them |
| **Condescension** | "As you probably don't know..." |
| **Robotic listing** | "Point one. Point two. Point three." |
| **Reading the slide verbatim** | Notes should expand on slides, not repeat them |

### Sample Tone Comparison

**AVOID this:**
> "This slide covers the six components. Component one is the charter. Component two is the stakeholder analysis. Component three is..."

**USE this:**
> "We've established why this matters — now let's get specific about what you actually produce during this phase. There are six key components, and I want to be clear: you don't always create all six on every project. Context matters. But you should know what they are so you can make informed decisions about what to include."

---

## Time Allocation Guidelines

### Format
- Single time: `[2 minutes]`
- Range: `[2-3 minutes]`
- Always in brackets, always after the slide title line

### Typical Allocations

| Slide Type | Typical Time |
|------------|--------------|
| Title Slide | [1 minute] |
| Learning Objectives | [2 minutes] |
| Module Overview | [2-3 minutes] |
| Standard Content (light) | [2 minutes] |
| Standard Content (dense) | [3-4 minutes] |
| Case Study | [3-5 minutes] |
| Bias Check | [3-4 minutes] |
| Key Takeaways | [2-3 minutes] |

### Reality Check
- Total of all slide times should equal presentation duration (minus buffer)
- Build in 3-5 minutes buffer for questions, technical issues, pacing variation
- If times don't add up, adjust before finalizing

---

## Timing Summary (End of Document)

Every speaker notes document ends with a timing summary:

```
---

## Timing Summary

| Part | Slides | Duration |
|------|--------|----------|
| Opening (Title, Objectives, Overview) | 1-3 | 5 minutes |
| {Section Name} | X-X | XX minutes |
| {Section Name} | X-X | XX minutes |
| {Section Name} | X-X | XX minutes |
| Closing (Takeaways, Bias Check) | X-X | X minutes |

**Total Presentation Time:** XX minutes
**Buffer:** X minutes
**Session Duration:** XX minutes
```

---

## Formatting Standards

### Document Format
- **Preferred:** Word document (.docx) for delivery use
- **Alternative:** Markdown (.md) for version control and portability
- Speaker notes are a delivery tool — format for easy reading during presentation

### Text Formatting
- **Bold** for section labels
- *Italics* for emphasis within content (use sparingly)
- Horizontal rules (`---`) between slides for visual separation
- Consistent heading levels: H2 for slide titles, bold for section labels

### Length Guidelines
- Title/Overview slides: 100-200 words
- Standard content slides: 150-300 words
- Case study/complex slides: 200-400 words
- Bias check slides: 200-350 words

---

## Quality Checklist

Before finalizing speaker notes, verify:

- [ ] Document header is complete with all required fields
- [ ] Every slide has a number, title, and time allocation
- [ ] Every slide (except last) has a Transition Cue
- [ ] Voice is first-person and conversational throughout
- [ ] No slide simply repeats bullet points from the slide itself
- [ ] Practical examples are concrete and specific (not generic)
- [ ] Key takeaways are memorable and actionable
- [ ] Timing allocations sum to presentation duration (minus buffer)
- [ ] Timing summary table is included at end
- [ ] Someone unfamiliar with content could deliver using these notes

---

## Common Mistakes to Avoid

| Mistake | Problem | Fix |
|---------|---------|-----|
| Bullet point notes | Not a delivery script | Write as conversational prose |
| Reading slides aloud | Boring, adds no value | Expand, contextualize, add examples |
| Missing transitions | Abrupt topic changes | Add explicit Transition Cue to each slide |
| Inconsistent timing | Times don't add up | Verify math before finalizing |
| Generic examples | "For example, a company might..." | Use specific, named examples with data |
| Forgetting the header | No context for document | Always include full header block |

---

*"Speaker notes are not what you write — they're what you say. Write for the ear, not the eye."*
