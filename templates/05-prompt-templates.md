<!--
Template: Prompt Templates
Version: 2.0.0
Last Updated: 2025-01-29
Changelog: https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki/Template-Changelog
-->

# Prompt Templates

**Used in:** Phase 1 (Research Architecture) and Phase 2 (Dual-Tool Research Execution)
**Purpose:** Pre-structured prompts for AI-assisted research with blanks to customize
**Format:** Each prompt type includes a blank template AND worked examples

---

## Overview: Prompt Types

| Prompt Type | Tool | Purpose | Phase |
|-------------|------|---------|-------|
| **Rework Analysis** | Claude/ChatGPT | Analyze existing presentation for instructor review | Rework Phase 1 |
| **Research Prompts** | NotebookLM | Gather sources on specific topics | Phase 1 → Phase 2 |
| **Reporting Prompts** | NotebookLM | Synthesize gathered sources into focused reports | Phase 2 |
| **External Research** | Gemini Deep Research | Validate and expand with practitioner perspectives | Phase 2 |

---

## How They Work Together

```
Research Prompts (NotebookLM)
    ↓
Sources gathered (70-100+ sources across topics)
    ↓
Reporting Prompts (NotebookLM)          External Research Prompts (Gemini)
    ↓                                        ↓
Internal synthesis reports (4)          External validation reports (4)
    ↓                                        ↓
    └──────────── Combined ────────────────┘
                    ↓
         8 research reports covering same 4 topics
         from complementary perspectives
```

---

## Rework Analysis Prompt

**Purpose:** Generate a structured Topic Outline Review from existing materials
**Tool:** Claude, ChatGPT, or similar
**Use when:** Revising existing content (not building new)

### Template

```
I need to rework {Course Module}: {Module Title} for {Month Year}.

**Materials:**
- Existing presentation: {file path or attachment}
- Existing speaker notes: {file path or attachment}
- Supporting brief/outline: {file path if available}

**Constraints:**
- Target session duration: {X} minutes
- Current slide count: {X} slides (~{Y} minutes estimated)
- Target slide count: {X-Y} slides OR reduce by {X} slides
- Must preserve: {any non-negotiable content}

**Please:**
1. Analyze the existing presentation structure
2. Create a Topic Outline Review document using the template format
3. Identify redundant or consolidation opportunities
4. Flag sections that need instructor priority decisions
5. Include decision point checkboxes for each major choice

Save the output to: {target file path}
```

### What This Generates

- Quick Math table (session duration, buffer, target slides)
- Section-by-section breakdown with slide tables and observations
- Consolidation opportunities table
- Decision point checkboxes for instructor

---

## Research Prompts (NotebookLM)

**Purpose:** Gather sources on specific topics
**Tool:** NotebookLM's "Search the web for sources" feature

### Template

```
**Prompt {Number}: {Topic Name}**

Find sources on {broad topic area} and {specific focus}. I'm looking for
content covering: {content area 1}, {content area 2}, {content area 3},
{content area 4}, {content area 5}, and {how these elements connect or
work together}. Include {source type 1} as well as {source type 2}.
Sources should address {key question or concern}. {Methodological note
if applicable}.
```

### Fill-in Guide

| Placeholder | What to Include |
|-------------|-----------------|
| `{Number}` | Sequential number (1, 2, 3...) |
| `{Topic Name}` | Descriptive name for this prompt's focus |
| `{broad topic area}` | The general domain |
| `{specific focus}` | The particular angle within that domain |
| `{content area 1-5}` | Specific subtopics to cover |
| `{source type 1-2}` | Practitioner guides, academic research, industry publications |
| `{key question}` | What problem should these sources help solve? |
| `{Methodological note}` | Any framework preferences or constraints |

### Example

```
**Prompt 1: Core Planning Components**

Find sources on project planning fundamentals and the essential components
that define successful project starts. I'm looking for content covering:
defining project goals and objectives, establishing project scope boundaries,
identifying deliverables, setting success criteria and metrics, stakeholder
identification, and understanding how these components work together as a
framework. Include practitioner-oriented content from management publications
as well as foundational academic perspectives. Sources should address why
planning matters for overall project success and common reasons projects fail
during or due to poor planning.
```

---

## Reporting Prompts (NotebookLM)

**Purpose:** Synthesize gathered sources into focused reports
**Tool:** NotebookLM (run AFTER source library is built)

### Template

```
**Report {Number}: {Report Title}**

Synthesize what these sources say about {main topic}. Include:

- {Content requirement 1 - what specific aspect to address}
- {Content requirement 2 - what specific aspect to address}
- {Content requirement 3 - what specific aspect to address}
- {Content requirement 4 - what specific aspect to address}
- {Content requirement 5 - what specific aspect to address}
- {Content requirement 6 - connection or synthesis element}

{Framing note - who is the audience, what's the context}. Aim for {X-X} pages.
```

### Fill-in Guide

| Placeholder | What to Include |
|-------------|-----------------|
| `{Number}` | Should match your topic numbering |
| `{Report Title}` | Clear, descriptive title |
| `{main topic}` | The synthesis focus |
| `{Content requirement 1-6}` | Specific aspects the report must address |
| `{Framing note}` | Audience description, context, tone guidance |
| `{X-X pages}` | Target length (typically 3-5 pages) |

### Example

```
**Report 1: The Stakes of Planning**

Synthesize what these sources say about why project planning matters and
what happens when it's done poorly. Include:

- The relationship between planning quality and overall project success
- Statistics or research on project failure rates tied to planning problems
- Common root causes of poor planning (rushed timelines, unclear objectives)
- The "foundation" concept - how planning decisions compound throughout delivery
- Why organizations underinvest in planning despite its importance
- The cost of correcting planning mistakes later versus addressing them early

Frame this for adult learners who may be new to formal project management
but have workplace experience. Aim for 3-4 pages.
```

---

## External Research Prompts (Gemini)

**Purpose:** Validate and expand with practitioner perspectives
**Tool:** Gemini Deep Research

### Template

```
**Gemini Report {Number}: {Report Title}**

Conduct deep research on {topic} with emphasis on {specific angle - usually
practical challenges or gap between theory and practice}. This is for
{audience description} in {context}.

Analyze:

- {Research question 1 - current state or data}
- {Research question 2 - why problems persist}
- {Research question 3 - how issues manifest in practice}
- {Research question 4 - what experienced practitioners do differently}
- {Research question 5 - current or emerging perspectives}
- {Research question 6 - tensions or tradeoffs}
- {Research question 7 - practical guidance}

{Grounding note - connect to learner experience}. {Scope note if applicable}.
```

### Fill-in Guide

| Placeholder | What to Include |
|-------------|-----------------|
| `{Number}` | Should match your topic numbering |
| `{Report Title}` | Should match NotebookLM report titles |
| `{topic}` | Same topic as corresponding NotebookLM report |
| `{specific angle}` | The "Gemini difference" - practitioner reality |
| `{audience description}` | Who will use this |
| `{context}` | The setting (course, workshop, training) |
| `{Research questions}` | Open-ended questions that invite depth |
| `{Grounding note}` | How to connect to learner experience |
| `{Scope note}` | Any boundaries |

### Example

```
**Gemini Report 1: The Stakes of Planning**

Conduct deep research on why project planning remains a persistent challenge
despite widespread understanding of its importance. This is for a professional
development course serving adult learners who may be transitioning careers or
upskilling.

Analyze:

- Current research on project failure rates attributable to planning problems
- Why organizations continue to underinvest in planning even when they know better
- The compounding effect of planning decisions throughout project delivery
- What experienced practitioners say they wish they'd understood earlier
- How thinking about project planning has evolved in recent years
- The tension between "move fast" cultures and thorough planning practices
- Practical advice for learners entering planning-intensive roles

Ground this in practical realities that working professionals will recognize
from their own experience, even if they haven't formally managed projects.
```

---

## Designing Your Prompt Set

### Step 1: Identify Your Topics

What 4-5 major topics will your module cover?

### Step 2: Create Matching Prompts

For each topic:
- 1 Research Prompt (NotebookLM source gathering)
- 1 Reporting Prompt (NotebookLM synthesis)
- 1 External Research Prompt (Gemini validation)

### Step 3: Number Consistently

```
Research Prompt 1: Topic A → Reporting Prompt 1 → Gemini Prompt 1
Research Prompt 2: Topic B → Reporting Prompt 2 → Gemini Prompt 2
Research Prompt 3: Topic C → Reporting Prompt 3 → Gemini Prompt 3
Research Prompt 4: Topic D → Reporting Prompt 4 → Gemini Prompt 4
```

---

## Quality Check Before Running

- [ ] Each Research Prompt specifies source types to find
- [ ] Each Reporting Prompt specifies target length
- [ ] Each Gemini Prompt asks about practitioner reality, not just theory
- [ ] Prompts are numbered consistently across all three types
- [ ] Audience is specified in Reporting and Gemini prompts

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Too many topics | Report sprawl, redundancy | Consolidate to 4-5 max |
| Prompts too vague | Generic, unhelpful results | Add specific content areas |
| Prompts too narrow | Misses important context | Include connections |
| Forgetting audience | Wrong complexity level | Always specify who |
| Skipping Gemini | One-sided perspective | Always run both tools |

---

## File Naming Convention

```
/Prompts/
    NotebookLM_Research_Prompts.md
    NotebookLM_Reporting_Prompts.md
    Gemini_Research_Prompts.md

/Research/
    NotebookLM_Report_1_{Topic}.md
    NotebookLM_Report_2_{Topic}.md
    Gemini_Report_1_{Topic}.md
    Gemini_Report_2_{Topic}.md
```

---

*"Good prompts are specific enough to get useful results and flexible enough to allow the AI to surface things you didn't think to ask for."*
