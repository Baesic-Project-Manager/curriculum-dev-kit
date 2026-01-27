# Getting Started

> Time to orient: 5 minutes

---

## TL;DR — The Fast Path

1. **Decide your path:** Reworking existing content? Or building new?
2. **Start with a template:** `01-topic-outline-review.md` (rework) or `05-prompt-templates.md` (new)
3. **Always complete Phase 3:** The brief is non-negotiable
4. **Build from templates:** Use `presentation-template.html` and speaker notes spec
5. **QA before delivery:** Run `06-qa-checklist.md`

---

## Choose Your Path

### Path A: Reworking Existing Content

You have slides/materials that need updating.

```
Rework Phase 1 → Phase 3 → Phase 4
   (audit)       (brief)    (build)
```

**Start with:** `templates/01-topic-outline-review.md`

### Path B: Building New Content

You're creating a module from scratch.

```
Phase 1 → Phase 2 → Phase 3 → Phase 4
(prompts) (research)  (brief)   (build)
```

**Start with:** `templates/05-prompt-templates.md`

### Path C: Quick Build (Expert Mode)

You know the content deeply and need to move fast.

```
Phase 3 → Phase 4
(brief)   (build)
```

**Start with:** `templates/02-presentation-brief.md`

**Warning:** Skipping research phases means you're relying entirely on existing knowledge. Appropriate for revisions or deep expertise only.

---

## Folder Setup

Create a folder structure for your module:

```
{Course}/{Module}/
├── 01_Topic_Outline_Review.md      # If reworking
├── 02_Presentation_Brief.md        # Always required
├── 03_Speaker_Notes.md             # Or .docx
├── {Module}_Presentation.html      # Final deliverable
├── Research/                       # If doing full research
│   ├── NotebookLM_Report_1.md
│   ├── NotebookLM_Report_2.md
│   ├── Gemini_Report_1.md
│   └── ...
└── Prompts/                        # If doing full research
    ├── Research_Prompts.md
    └── Reporting_Prompts.md
```

---

## Template Checklist

Copy these templates to your module folder as needed:

| Template | Required? | When |
|----------|-----------|------|
| `01-topic-outline-review.md` | If reworking | Rework Phase 1 |
| `02-presentation-brief.md` | **Always** | Phase 3 |
| `03-speaker-notes-spec.md` | Reference | Phase 4 |
| `04-speaker-notes-sample.md` | Reference | Phase 4 |
| `05-prompt-templates.md` | If new content | Phase 1-2 |
| `06-qa-checklist.md` | **Always** | Before delivery |
| `presentation-template.html` | **Always** | Phase 4 |

---

## First Module Walkthrough

### Step 1: Set Up Your Module Folder

```bash
mkdir -p "Course 1/Module 1"
cd "Course 1/Module 1"
```

### Step 2: Copy Required Templates

At minimum, copy:
- `02-presentation-brief.md`
- `presentation-template.html`
- `06-qa-checklist.md`

### Step 3: Complete the Brief

Open `02-presentation-brief.md` and fill out:

1. **Module Identification** — What are you building?
2. **Timing Calculations** — How many slides can you have?
3. **Priority Rankings** — What gets the most attention?
4. **Case Study Selection** — What's your anchor example?
5. **Voice and Tone** — How should it sound?

**Do not skip sections.** The brief forces decisions that prevent problems later.

### Step 4: Lock the Brief

When complete, mark status as LOCKED:

```markdown
**Brief Status:** [x] LOCKED
```

From this point forward, follow the brief. No improvising.

### Step 5: Build the Presentation

1. Copy `presentation-template.html` and rename it
2. Update the `<title>` tag
3. Build slides following your brief's structure
4. Check slide count against your budget

### Step 6: Write Speaker Notes

Using the brief and `03-speaker-notes-spec.md`:

1. Create notes document with header block
2. Write each slide's notes as conversational script
3. Include time allocations
4. Add transition cues between slides
5. End with timing summary table

### Step 7: QA Check

Run through `06-qa-checklist.md`:

- [ ] Visual consistency
- [ ] Mandatory slides present
- [ ] Speaker notes complete
- [ ] Timing adds up
- [ ] HTML clean

---

## Common First-Timer Mistakes

### Mistake 1: Skipping the Brief

"I'll just start making slides."

**Problem:** You'll run out of time, exceed your slide budget, or miss key content.

**Fix:** Complete Phase 3 first. Always.

### Mistake 2: Bullet Point Speaker Notes

```
• Cover project charter
• Explain stakeholders
• Discuss timeline
```

**Problem:** These don't help you deliver. They're outlines, not scripts.

**Fix:** Write as you would speak. Full sentences, conversational tone.

### Mistake 3: Ignoring the Timing Math

"I'll just see how many slides I need."

**Problem:** You'll end up with 50 slides for a 45-minute session.

**Fix:** Calculate your slide budget first. Allocations must sum to maximum.

### Mistake 4: Research Without Prompts

"I'll just ask the AI about the topic."

**Problem:** Shallow, unfocused responses. Missing perspectives.

**Fix:** Design your prompts in Phase 1 before executing research in Phase 2.

---

## Using the Scripts (Optional)

If you have Python 3.10+ installed:

### Initialize a New Module

```bash
python scripts/project_init.py \
  --course 2 \
  --module 3 \
  --title "Project Planning Fundamentals" \
  --duration 90
```

This creates:
- Folder structure
- Changelog file
- Context bundle with file references

### Validate Before Publish

```bash
python scripts/validate_module.py "path/to/module"
```

Checks:
- Required files exist
- HTML has no banned patterns
- Size limits respected

See `scripts/README.md` for full documentation.

---

## Next Steps

1. **Read the full workflow:** [workflow.md](workflow.md)
2. **Understand the research method:** [research-methodology.md](research-methodology.md)
3. **Learn the quality standards:** [quality-standards.md](quality-standards.md)

---

*Start with the brief. Everything else follows.*
