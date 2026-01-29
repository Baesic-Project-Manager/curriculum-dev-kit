# Curriculum Dev Kit

A structured workflow system for creating professional course presentations with comprehensive speaker notes using AI-assisted research.

**Before:** Ad-hoc slide creation, inconsistent quality, speaker notes as bullet points.
**After:** Template-driven consistency, conversational delivery scripts, repeatable process.

---

## The Core Principle

> *"The Presentation Development Brief is a locked document. Creative deviation during production is scope creep."*

All content decisions are made **before** production begins.

---

## Key Features

- **4-Phase Workflow** — Audit → Plan → Produce → Deliver
- **Brief-First Methodology** — Lock all decisions before building
- **Dual-Tool Research** — NotebookLM (depth) + Gemini (breadth)
- **Conversational Speaker Notes** — Delivery scripts, not bullet points
- **HTML Presentation System** — Full CSS design system with components
- **Pre-Delivery QA** — Checklist catches issues before you present

---

## Choose Your Path

**Reworking existing content:**
```
Content Audit → Brief → Production
```

**Building new content:**
```
Research Architecture → Dual-Tool Research → Brief → Production
```

📖 **Full workflow:** [Wiki → Four-Phase-Workflow](https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki/Four-Phase-Workflow)

---

## Quick Start

```bash
# Initialize a new module
python scripts/project_init.py --course 2 --module 3 --title "Project Planning"
```

Or manually:
1. Copy `02-presentation-brief.md` to your module folder
2. Complete the brief (non-negotiable)
3. Build slides using `presentation-template.html`
4. Run `06-qa-checklist.md` before delivery

📖 **Full setup guide:** [Wiki → Getting-Started](https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki/Getting-Started)

---

## Templates

| Template | Purpose |
|----------|---------|
| `02-presentation-brief.md` | Lock content decisions (required) |
| `01-topic-outline-review.md` | Content audit for rework |
| `05-prompt-templates.md` | AI research prompts |
| `06-qa-checklist.md` | Pre-delivery QA |

📖 **All templates:** [Wiki → Templates-Guide](https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki/Templates-Guide)

---

## Documentation

| Resource | Description |
|----------|-------------|
| **[Wiki](https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki)** | Guides, tutorials, FAQ |
| [docs/](docs/) | Technical reference |
| [templates/](templates/) | All templates |
| [examples/](examples/) | Filled-out samples |

---

## Scale

- 50+ modules developed with this methodology
- 90-minute session format
- Consistent quality across content areas

---

## Related

Part of [teaching-at-scale](https://github.com/Baesic-Project-Manager/teaching-at-scale) methodology.

| Repo | What It Covers |
|------|----------------|
| **curriculum-dev-kit** | Pre-recording content development (this repo) |
| [recording-pipeline](https://github.com/Baesic-Project-Manager/recording-pipeline) | Post-recording automation |

---

*Built for real workflows. Designed for scale.*
