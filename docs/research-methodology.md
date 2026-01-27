# Research Methodology

> Dual-tool AI research for comprehensive, validated content

---

## The Problem with Single-Source Research

When you ask one AI tool "tell me about project initiation," you get:

- One perspective
- One set of sources
- One framing of the topic
- Blind spots you don't know about

**Result:** Content that feels thin, misses practitioner reality, or oversimplifies.

---

## The Dual-Tool Approach

Use two AI research tools with different strengths:

```
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐           ┌─────────────────┐             │
│  │   NotebookLM    │           │     Gemini      │             │
│  │  (Internal)     │           │   (External)    │             │
│  ├─────────────────┤           ├─────────────────┤             │
│  │ Curated sources │           │ Open web search │             │
│  │ Deep synthesis  │           │ Practitioner    │             │
│  │ Academic rigor  │           │   perspectives  │             │
│  │ "What the       │           │ "What actually  │             │
│  │  literature     │           │  happens in     │             │
│  │  says"          │           │  the field"     │             │
│  └────────┬────────┘           └────────┬────────┘             │
│           │                             │                       │
│           └──────────┬──────────────────┘                       │
│                      ▼                                          │
│           ┌─────────────────┐                                   │
│           │  8 Reports on   │                                   │
│           │  4 Topics from  │                                   │
│           │  2 Perspectives │                                   │
│           └─────────────────┘                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tool Strengths

| Aspect | NotebookLM | Gemini Deep Research |
|--------|------------|---------------------|
| **Source type** | You curate the sources | Searches the open web |
| **Depth** | Deep synthesis of provided material | Broad coverage across many sources |
| **Perspective** | Academic/foundational | Practitioner/current |
| **Best for** | "What does the research say?" | "What do people actually do?" |
| **Blind spot** | Limited to what you provide | May surface low-quality sources |

---

## The Three Prompt Types

### 1. Research Prompts (NotebookLM)

**Purpose:** Gather sources on specific topics

**Characteristics:**
- Frame as source requests ("Find sources on...")
- Specify content areas to cover
- Include source type guidance (practitioner, academic, etc.)
- Note methodological preferences

**Template:**
```
Find sources on [broad topic] and [specific focus]. I'm looking for
content covering: [area 1], [area 2], [area 3], [area 4], [area 5],
and [how these connect]. Include [source type 1] as well as
[source type 2]. Sources should address [key question].
```

### 2. Reporting Prompts (NotebookLM)

**Purpose:** Synthesize gathered sources into focused reports

**Characteristics:**
- Frame as synthesis requests ("Synthesize what these sources say about...")
- Specify report structure
- Include content requirements for each section
- Specify target length and audience

**Template:**
```
Synthesize what these sources say about [main topic]. Include:

- [Content requirement 1]
- [Content requirement 2]
- [Content requirement 3]
- [Content requirement 4]
- [Content requirement 5]
- [Synthesis element]

[Audience framing]. Aim for [X-X] pages.
```

### 3. External Research Prompts (Gemini)

**Purpose:** Validate and expand with practitioner perspectives

**Characteristics:**
- Frame as research requests ("Conduct deep research on...")
- Emphasize practitioner reality (what actually happens vs. textbooks)
- Ask for tensions and challenges (not just best practices)
- Specify audience context
- Request concrete examples

**Template:**
```
Conduct deep research on [topic] with emphasis on [practical angle].
This is for [audience] in [context].

Analyze:
- [Current state or data]
- [Why problems persist]
- [How issues manifest in practice]
- [What experienced practitioners do differently]
- [Current or emerging perspectives]
- [Tensions or tradeoffs]
- [Practical guidance]

[Grounding note connecting to learner experience].
```

---

## Designing Your Prompt Set

### Step 1: Identify Your Topics

What 4-5 major topics will your module cover?

Example for a Project Initiation module:
1. Stakes of project initiation (why it matters)
2. Goals vs. scope distinction
3. Six components of initiation
4. Cost-benefit analysis

### Step 2: Create Matching Prompts

For each topic, create:
- 1 Research Prompt (NotebookLM source gathering)
- 1 Reporting Prompt (NotebookLM synthesis)
- 1 External Research Prompt (Gemini validation)

### Step 3: Number Consistently

```
Research Prompt 1: Stakes
Reporting Prompt 1: Stakes
Gemini Prompt 1: Stakes

Research Prompt 2: Goals vs. Scope
Reporting Prompt 2: Goals vs. Scope
Gemini Prompt 2: Goals vs. Scope
```

Same topic, same number, different tools.

---

## Execution Workflow

### Phase 1: Research Architecture (1-2 hours)

1. Define your 4-5 topics
2. Write all Research Prompts
3. Write all Reporting Prompts
4. Write all External Research Prompts
5. Review for completeness

### Phase 2: Research Execution (2-4 hours)

**Stream A: NotebookLM**
1. Create new notebook
2. Run Research Prompts to gather 70-100 sources
3. Run Reporting Prompts to generate 4 synthesis reports
4. Export as markdown

**Stream B: Gemini**
1. Run External Research Prompts
2. Save 4 reports as markdown

**Output:** 8 reports covering 4 topics from 2 perspectives

---

## File Organization

```
{Module}/
├── Prompts/
│   ├── NotebookLM_Research_Prompts.md
│   ├── NotebookLM_Reporting_Prompts.md
│   └── Gemini_Research_Prompts.md
└── Research/
    ├── NotebookLM_Report_1_{Topic}.md
    ├── NotebookLM_Report_2_{Topic}.md
    ├── NotebookLM_Report_3_{Topic}.md
    ├── NotebookLM_Report_4_{Topic}.md
    ├── Gemini_Report_1_{Topic}.md
    ├── Gemini_Report_2_{Topic}.md
    ├── Gemini_Report_3_{Topic}.md
    └── Gemini_Report_4_{Topic}.md
```

---

## Quality Indicators

### Good Research Output

- Both tools agree on fundamentals
- Gemini surfaces practitioner nuances NotebookLM missed
- NotebookLM provides depth Gemini glossed over
- You discover things you didn't think to ask about
- Reports cite specific examples, data, and frameworks

### Warning Signs

- Reports are generic and could apply to any topic
- No specific examples or data points
- Tools contradict each other on basics (investigate!)
- Everything sounds like marketing copy
- No acknowledgment of limitations or tradeoffs

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Too many topics | Report sprawl, redundancy | Consolidate to 4-5 max |
| Prompts too vague | Generic, unhelpful results | Add specific content areas |
| Prompts too narrow | Misses important context | Include connections to related topics |
| Forgetting audience | Wrong complexity level | Always specify who content is for |
| Skipping Gemini | One-sided perspective | Always run both tools |
| Running prompts without review | Wasted research cycles | Review all prompts before execution |

---

## When to Skip Research

You can skip Phases 1-2 if:

- You're reworking existing content (use Rework Phase 1 instead)
- You have deep expertise in the topic
- You're under severe time pressure
- The content is highly standardized (compliance training, etc.)

**What you lose:** External validation, breadth of perspective, sources you didn't know about

**Mitigate by:** Having the brief reviewed by a subject matter expert

---

*"Good prompts are specific enough to get useful results and flexible enough to allow the AI to surface things you didn't think to ask for."*
