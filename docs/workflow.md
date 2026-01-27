# The Four-Phase Workflow

> Complete each phase before moving to the next. Skipping or combining phases degrades output quality.

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              WORKFLOW PATHS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  REWORK PATH (existing content):                                            │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │ Rework Ph. 1 │────▶│   Phase 3    │────▶│   Phase 4    │                │
│  │ Content Audit│     │    Brief     │     │  Production  │                │
│  └──────────────┘     └──────────────┘     └──────────────┘                │
│                                                                             │
│  NEW CONTENT PATH (from scratch):                                           │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌────────┐ │
│  │   Phase 1    │────▶│   Phase 2    │────▶│   Phase 3    │────▶│Phase 4 │ │
│  │  Research    │     │  Dual-Tool   │     │    Brief     │     │  Build │ │
│  │ Architecture │     │   Research   │     │   (Locked)   │     │        │ │
│  └──────────────┘     └──────────────┘     └──────────────┘     └────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Rework Phase 1: Content Audit & Instructor Review

**Time:** 30-60 minutes
**Use when:** Revising existing presentations
**Output:** Completed Topic Outline Review with locked decisions

### Goal

Before any development, get instructor decisions on what to keep, cut, and prioritize.

### Actions

1. Analyze existing presentation (PDF/slides) structure
2. Create Topic Outline Review using `01-topic-outline-review.md` template
3. Instructor completes priority ratings and decision checkboxes
4. Review instructor feedback for consolidation decisions

### Why This Matters

- Prevents wasted work on content instructor wants cut
- Identifies problem areas ("I misspeak on this section")
- Catches structural issues ("the order doesn't make sense")
- Gets instructor buy-in before production begins

**After completing Rework Phase 1:** Skip to Phase 3 — your instructor review replaces the research phases.

---

## Phase 1: Research Architecture (New Content Only)

**Time:** 1-2 hours
**Use when:** Building new modules from scratch
**Output:** Three sets of prompts ready for execution

### Goal

Define what you need to learn before you try to learn it.

### Actions

1. Open `05-prompt-templates.md`
2. Customize Research Prompts for your topic
3. Customize Reporting Prompts for your synthesis needs
4. Customize External Research Prompts for practitioner validation

### Key Principle

Don't start researching until you know what questions you're answering. Prompts should cover:

- Core concepts and frameworks
- Common distinctions that confuse learners
- Practitioner reality vs. textbook theory
- Concrete examples and case studies

---

## Phase 2: Dual-Tool Research Execution (New Content Only)

**Time:** 2-4 hours
**Use when:** After Phase 1 prompts are ready
**Output:** 8 research reports (4 from each tool)

### Goal

Generate comprehensive research from complementary AI perspectives.

### Stream A: NotebookLM (Internal Analyst)

1. Create a new NotebookLM notebook
2. Use Research Prompts to gather 70-80 sources via web search
3. Use Reporting Prompts to generate 4 synthesis reports (3-5 pages each)
4. Export reports as markdown

### Stream B: Gemini Deep Research (External Researcher)

1. Use External Research Prompts to generate 4 parallel reports
2. Save reports as markdown

### Why Two Tools?

| Tool | Strength | Perspective |
|------|----------|-------------|
| NotebookLM | Synthesizes from curated sources | Depth — what the literature says |
| Gemini | Researches from the open web | Breadth — what practitioners say |

**Combined:** 8 reports covering the same 4 topics from different angles.

### Naming Convention

```
{Tool}_Report_{Number}_{Topic}.md

Examples:
- NotebookLM_Report_1_Stakes_of_Project_Initiation.md
- Gemini_Report_3_Six_Components.md
```

---

## Phase 3: Content Development

**Time:** 2-3 hours
**Use when:** After Rework Phase 1 OR Phase 2 is complete
**Output:** Completed Presentation Development Brief (LOCKED)

### Goal

Make ALL strategic content decisions before any formatting or slide creation.

### Actions

1. Open `02-presentation-brief.md`
2. Complete ALL sections:
   - Module identification
   - Timing calculations (work backwards from delivery reality)
   - Content priorities with specific slide allocations
   - Mandatory elements checklist
   - Case study selection with justification
   - Voice and tone definition (including what to AVOID)
   - Bias check topics
3. Review and lock the brief — no changes during production

### The Timing Math

Always calculate backwards from actual delivery:

```
Total session time:           _____ minutes
Minus planned activities:     -_____ minutes
Minus discussion time:        -_____ minutes
Minus transitions/buffer:     -_____ minutes
= Actual presentation time:   _____ minutes

÷ 2.5 minutes per slide =     _____ slides maximum
```

### The Priority Budget

| Priority | Coverage Depth | Typical Allocation |
|----------|---------------|-------------------|
| HIGH | Comprehensive, multiple examples | 8-12 slides |
| MEDIUM | Solid coverage, key concepts | 4-6 slides |
| LOW | Overview only, essential points | 2-4 slides |

**The discipline:** Allocations must sum to your slide maximum. This forces hard choices.

### Critical Rule

> *The brief is a locked document. Creative deviation during production is scope creep.*

---

## Phase 4: Production

**Time:** 3-5 hours
**Use when:** After Phase 3 brief is LOCKED
**Output:** HTML presentation + Speaker notes document

### Goal

Transform the locked brief into final deliverables.

### For the Presentation

1. Copy `presentation-template.html`
2. Rename for your module
3. Customize colors using design system (optional)
4. Build slides following your brief's structure and allocations
5. **Verify slide count matches brief**

### For the Speaker Notes

1. Open `03-speaker-notes-spec.md` for structure requirements
2. Reference `04-speaker-notes-sample.md` for execution examples
3. Write speaker notes following the standard format
4. Include timing summary at end

### Quality Check

Before considering the module complete, run through `06-qa-checklist.md`:

- [ ] Visual consistency (colors, spacing, callout styles)
- [ ] All mandatory slides present
- [ ] Slide numbers sequential
- [ ] HTML clean (no banned patterns)
- [ ] Timing adds up

---

## Quick Start (Minimum Viable Workflow)

If you already have content knowledge and face time pressure:

1. **Skip to Phase 3** — Complete the Presentation Development Brief (non-negotiable)
2. Build slides from the HTML template
3. Write speaker notes using the format specification

**What you lose:** Dual-perspective research validation, comprehensive source coverage

**When acceptable:** Topic you know deeply, tight deadline, revision of existing content

---

## Key Principles

### Separation of Concerns

Research, synthesis, content strategy, and production are distinct activities. Do them separately.

### Constraint-Driven Design

Establish hard limits (slide budgets, timing allocations) BEFORE creative work begins. Constraints force clarity.

### Brief-First Methodology

The Presentation Development Brief is a locked document. Creative deviation during production is scope creep.

### Dual-Perspective Validation

NotebookLM synthesizes from curated sources (depth). Gemini researches from the web (breadth). Both perspectives strengthen content.

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Slides feel unfocused | Brief wasn't completed or followed | Return to Phase 3, revise brief, rebuild |
| Running out of time | Timing calculations optimistic | Recalculate with realistic buffers; reduce slides |
| Speaker notes feel generic | Voice/tone not defined | Review spec; revise with specific audience in mind |
| Research feels thin | Single-tool research | Execute full dual-tool methodology |

---

*"A system that works once is an accident. A system that works repeatedly is a process worth documenting."*
