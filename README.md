# Curriculum Dev Kit

A structured workflow system for creating professional course presentations with comprehensive speaker notes using AI-assisted research.

---

## What This Does

**End-to-end workflow: Existing Content OR Research → Structured Planning → Production-Ready Deliverables**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CURRICULUM DEVELOPMENT WORKFLOW                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────┐ │
│   │  REWORK     │     │   PHASE 3   │     │   PHASE 4   │     │  OUTPUT  │ │
│   │  PHASE 1    │     │   Content   │     │ Production  │     │          │ │
│   │             │ ──▶ │ Development │ ──▶ │             │ ──▶ │          │ │
│   │  Content    │     │    Brief    │     │  HTML Deck  │     │ ✓ Slides │ │
│   │   Audit     │     │  (Locked)   │     │  + Notes    │     │ ✓ Notes  │ │
│   └─────────────┘     └─────────────┘     └─────────────┘     └──────────┘ │
│         │                                                                   │
│         │  OR (for new content)                                             │
│         ▼                                                                   │
│   ┌─────────────┐     ┌─────────────┐                                       │
│   │  PHASE 1    │     │  PHASE 2    │                                       │
│   │  Research   │ ──▶ │  Dual-Tool  │ ──────────────────────────┐           │
│   │Architecture │     │  Research   │                           │           │
│   │  (Prompts)  │     │ (8 Reports) │                           ▼           │
│   └─────────────┘     └─────────────┘                     [To Phase 3]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Before:** Ad-hoc slide creation, inconsistent quality, speaker notes as bullet points, "where did I leave off?"

**After:** Template-driven consistency, conversational delivery scripts, clear handoff points, repeatable process

---

## The Problem It Solves

- **No methodology** — Slide decks get built "from vibes" with no structured planning phase
- **Speaker notes are afterthoughts** — Bullet points that don't help actual delivery
- **Research is shallow** — Single-source, single-perspective content
- **Hard to hand off** — No one else can pick up where you left off
- **Inconsistent quality** — Every module looks and feels different

---

## Key Features

| Feature | Description |
|---------|-------------|
| **4-Phase Workflow** | Separation of concerns: audit → plan → produce → deliver |
| **Brief-First Methodology** | All content decisions locked before production begins |
| **Dual-Tool Research** | NotebookLM (depth) + Gemini (breadth) for validated content |
| **Conversational Speaker Notes** | Delivery scripts written as you'd actually speak |
| **HTML Presentation System** | Full CSS design system with copy-paste components |
| **Pre-Delivery QA** | Checklist catches common issues before you present |
| **Project Scaffolding** | Scripts to initialize, validate, and publish modules |

---

## The Workflow

### For Reworking Existing Content

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  REWORK PHASE 1  │    │     PHASE 3      │    │     PHASE 4      │
│  Content Audit   │───▶│  Development     │───▶│   Production     │
│   (30-60 min)    │    │  Brief (2-3 hr)  │    │    (3-5 hr)      │
├──────────────────┤    ├──────────────────┤    ├──────────────────┤
│ • Analyze slides │    │ • Timing math    │    │ • Build slides   │
│ • Priority rank  │    │ • Slide budget   │    │ • Write notes    │
│ • Get decisions  │    │ • Lock structure │    │ • QA checklist   │
└──────────────────┘    └──────────────────┘    └──────────────────┘
        │                                                │
        ▼                                                ▼
  Topic Outline                                    HTML Presentation
  Review (approved)                                + Speaker Notes
```

### For New Content (Full Research)

```
Phase 1: Research Architecture (1-2 hr) → Define what you need to learn
Phase 2: Dual-Tool Research (2-4 hr)    → 8 reports from 2 AI perspectives
Phase 3: Content Development (2-3 hr)   → Lock the brief
Phase 4: Production (3-5 hr)            → Build deliverables
```

---

## Repository Structure

```
curriculum-dev-kit/
├── README.md                      # You are here
├── docs/
│   ├── workflow.md                # Full 4-phase process
│   ├── getting-started.md         # Quick start guide
│   ├── research-methodology.md    # Dual-tool AI research
│   └── quality-standards.md       # Design system + QA
├── templates/
│   ├── 01-topic-outline-review.md # Rework Phase 1
│   ├── 02-presentation-brief.md   # Phase 3 planning
│   ├── 03-speaker-notes-spec.md   # Notes format spec
│   ├── 04-speaker-notes-sample.md # Example notes
│   ├── 05-prompt-templates.md     # AI research prompts
│   ├── 06-qa-checklist.md         # Pre-delivery QA
│   ├── presentation-template.html # HTML slide template
│   ├── component-library.md       # UI components
│   └── design-system.md           # CSS + colors
├── scripts/
│   ├── project_init.py            # Scaffold new module
│   ├── validate_module.py         # Validate before publish
│   └── README.md                  # Script docs
├── examples/
│   ├── sample-topic-outline.md    # Filled example
│   ├── sample-brief.md            # Filled example
│   └── sample-speaker-notes.md    # Voice/format example
└── lessons-learned.md             # What we discovered
```

---

## Quick Start

### Option 1: Start a New Module (with script)

```bash
# Set up environment
export MODULE_PATH="/path/to/your/courses"
export STARTER_KIT_PATH="/path/to/curriculum-dev-kit/templates"

# Initialize a new module rework
python scripts/project_init.py --course 2 --module 3 --title "Project Planning Fundamentals"
```

### Option 2: Manual Start

1. **Copy the templates** you need to your module folder
2. **Start with Phase 1** — Fill out `01-topic-outline-review.md` (for rework) or research prompts (for new)
3. **Complete Phase 3** — Lock your `02-presentation-brief.md` before building
4. **Build in Phase 4** — Use `presentation-template.html` and speaker notes spec
5. **QA before delivery** — Run through `06-qa-checklist.md`

---

## Template Overview

| Template | When to Use | Time |
|----------|-------------|------|
| `01-topic-outline-review.md` | Reworking existing content | 30-60 min |
| `02-presentation-brief.md` | Planning any module (required) | 2-3 hours |
| `03-speaker-notes-spec.md` | Writing delivery scripts | Reference |
| `05-prompt-templates.md` | New content needing research | 3-6 hours |
| `06-qa-checklist.md` | Before any delivery | 30-45 min |

---

## The Brief-First Principle

> *"The Presentation Development Brief is a locked document. Creative deviation during production is scope creep."*

The most important template is `02-presentation-brief.md`. It forces you to:

- Calculate timing backwards from delivery reality
- Assign slide budgets that sum to your maximum
- Make case study and example choices explicit
- Define voice and tone with examples
- Identify cognitive biases to address

**Once locked, follow it.** This prevents the "just one more slide" problem that derails timing.

---

## Speaker Notes Philosophy

Speaker notes in this system are **conversational delivery scripts**, not bullet points.

```
❌ AVOID:
• Explain project charter
• Discuss stakeholder importance
• Cover success criteria

✓ USE:
"We've established why initiation matters — now let's get specific about
what you actually produce during this phase. There are six key components,
and I want to be clear: you don't always create all six on every project.
Context matters. But you should know what they are so you can make
informed decisions about what to include."
```

See `03-speaker-notes-spec.md` for full format and `04-speaker-notes-sample.md` for examples.

---

## Requirements

| Dependency | Purpose | Required? |
|------------|---------|-----------|
| Python 3.10+ | Script automation | For scripts only |
| Modern browser | HTML presentations | Yes |
| NotebookLM | Research (depth) | For full workflow |
| Gemini | Research (breadth) | For full workflow |

---

## Context

This system was developed for professional certificate curriculum at scale.

**Scale:**
- 50+ modules developed with this methodology
- 6-course certificate program
- 90-minute session format
- Consistent quality across different content areas

**Proven outcomes:**
- First-draft presentations require minimal revision
- Speaker notes enable confident delivery without extensive prep
- Timing works out in actual delivery
- System transfers between instructors

---

## Documentation

- [Full Workflow Guide](docs/workflow.md)
- [Getting Started](docs/getting-started.md)
- [Research Methodology](docs/research-methodology.md)
- [Quality Standards](docs/quality-standards.md)

---

## Related

This is part of a broader teaching methodology documented in [teaching-at-scale](https://github.com/Baesic-Project-Manager/teaching-at-scale).

| Related Repo | What It Covers |
|--------------|----------------|
| [recording-pipeline](https://github.com/Baesic-Project-Manager/recording-pipeline) | Post-recording automation (after you record) |
| curriculum-dev-kit | Pre-recording content development (this repo) |

---

*Built for real workflows. Designed for scale.*
