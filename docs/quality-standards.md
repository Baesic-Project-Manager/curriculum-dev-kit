# Quality Standards

> Design system, voice guidelines, and QA principles

---

## Visual Design System

### Color Scheme (Default)

The default scheme is Navy Blue + Gold, proven for professional presentations:

```css
:root {
    --primary-color: #003B7A;      /* Navy - headings, accents */
    --secondary-color: #F4B41A;    /* Gold - subheadings, highlights */
    --text-color: #2C3E50;         /* Dark gray-blue - body text */
    --background-color: #FFFFFF;   /* White - slide background */
    --footer-color: #7F8C8D;       /* Medium gray - footer text */
}
```

### Typography Hierarchy

| Element | Size | Color | Weight |
|---------|------|-------|--------|
| H1 (Title slide) | 4.5rem | Primary | 700 |
| H1 (Content) | 3.5rem | Primary | 700 |
| H2 (Subtitle) | 2rem | Secondary | 600 |
| Body text | 1.8rem | Text | 400 |
| List items | 1.8rem | Text | 400 |
| Footer | 1.2rem | Footer | 400 |

### Spacing Scale

| Element | Value |
|---------|-------|
| Slide padding | `4vh 6vw` |
| Header height | `15vh` |
| Footer height | `8vh` |
| Content spacing | `3vh` |
| List item margin | `2.5vh` (first level), `1.5vh` (nested) |
| Callout margin | `3vh 0` |
| Callout padding | `2vh 2vw` |

---

## Callout Box Standards

All callout boxes share these properties:

```css
.callout-box {
    background: #FFFFFF;           /* White, not gray */
    border-left: 5px solid;        /* Color varies by type */
    padding: 2vh 2vw;
    margin: 3vh 0;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

### Callout Types

| Type | Border Color | Use For |
|------|--------------|---------|
| Standard | Gold (`--secondary-color`) | General emphasis, context |
| Key Takeaway | Gold | Critical insights to remember |
| Example | Navy (`--primary-color`) | Real-world applications, case studies |
| Warning | Red (`#D32F2F`) | Common mistakes, pitfalls |
| Bias Check | Purple (`#7B1FA2`) | Cognitive biases, reflection prompts |
| Stat Callout | Green (`#388E3C`) | Impact data, key metrics |

### Callout Do's and Don'ts

| Do | Don't |
|----|-------|
| Use white backgrounds with shadows | Use gradient backgrounds |
| Use semantic types (warning, example) | Use generic callouts for everything |
| Keep text concise | Put entire paragraphs in callouts |
| One callout per key point | Stack multiple callouts |

---

## Speaker Notes Voice

### Target Voice

> Experienced colleague sharing practical wisdom — professional but approachable, honest about challenges, connects theory to workplace reality.

### Voice Characteristics — DO

- **First-person delivery:** "I want you to think about..."
- **Direct address:** "You'll encounter this when..."
- **Conversational prose:** Written as you would speak
- **Acknowledge complexity:** "This sounds straightforward, but here's where it gets tricky..."
- **Honest about limitations:** "This framework is useful, but it has blind spots..."
- **Specific metrics/data:** "Projects with clear charters are 2.5 times more likely to..."

### Voice Characteristics — AVOID

- **Marketing language:** "This revolutionary framework will transform..."
- **Hedging that undermines:** "I think maybe this might be important..."
- **Academic jargon without explanation:** Using terms without defining them
- **Condescension:** "As you probably don't know..."
- **Robotic listing:** "Point one. Point two. Point three."
- **Reading slides verbatim:** Notes should expand, not repeat

### Tone Comparison

**AVOID this:**
> "This slide covers the six components of project initiation. Component one is the project charter. Component two is the stakeholder analysis. Component three is..."

**USE this:**
> "We've established why initiation matters — now let's get specific about what you actually produce during this phase. There are six key components, and I want to be clear: you don't always create all six on every project. Context matters. But you should know what they are so you can make informed decisions about what to include."

---

## Mandatory Slide Elements

Every presentation must include:

### Opening Sequence (Slides 1-3)

1. **Title slide** — Module name, course context, branding
2. **Learning objectives** — What learners will be able to do
3. **Module overview/roadmap** — What we'll cover today

### Closing Sequence (Final slides)

1. **Sources slide** — Citations for statistics and claims
2. **Bias check slide** — Cognitive biases or reflection prompts
3. **Key takeaways** — 3-5 most important points
4. **Next session preview** (if applicable) — What's coming next

---

## HTML Validation Rules

The following patterns are banned in HTML presentations:

| Pattern | Reason |
|---------|--------|
| External images (`<img src=...>`) | Breaks offline, privacy concerns |
| External CSS (`<link href=...>`) | Dependency on external resources |
| External JavaScript (`<script src=...>`) | Security, offline reliability |
| Iframes | Security, unpredictable behavior |
| CSS `@import url()` | External dependency |
| Base64 raster images | File size bloat |

**Allowed:** Inline SVG, inline CSS, inline JavaScript for navigation.

---

## Size Limits

| Metric | Limit | Rationale |
|--------|-------|-----------|
| Single file | 500 KB | Performance, version control |
| Total module | 1 MB | Repository size management |
| Slide count | Based on timing math | Delivery quality |

---

## Pre-Delivery QA Checklist Summary

### Visual Consistency
- [ ] All H1 headers use primary color
- [ ] All callout boxes have white backgrounds
- [ ] Bold text renders in navy
- [ ] No hardcoded hex values in content

### Content Completeness
- [ ] Title slide present
- [ ] Learning objectives present
- [ ] Sources slide present
- [ ] Bias check slide present
- [ ] Key takeaways slide present
- [ ] Next session preview verified (if applicable)

### Technical Quality
- [ ] Slide numbers sequential
- [ ] Footer content consistent
- [ ] No console errors
- [ ] Navigation works

### Speaker Notes
- [ ] Every slide has notes
- [ ] Time allocations present
- [ ] Transition cues between slides
- [ ] Timing summary at end

See `06-qa-checklist.md` for the complete checklist.

---

## Layout Guidelines

### Two-Column Comparison

Use for A vs. B comparisons, pros/cons, before/after:

```html
<div class="two-column">
    <div class="column">
        <h3>Concept A</h3>
        <ul>...</ul>
    </div>
    <div class="column">
        <h3>Concept B</h3>
        <ul>...</ul>
    </div>
</div>
```

**Prefer two-column layouts over tables** for concept comparisons.

### When to Use Tables

Tables are appropriate only when you have:
- Data with more than 2 comparable dimensions
- Numerical data that needs alignment
- Complex comparisons where columns and rows intersect

### Stats Grid

For displaying multiple metrics:

```html
<div class="stats-grid">
    <div class="stat-item">
        <span class="stat-number">75%</span>
        <span class="stat-label">Success Rate</span>
    </div>
    <!-- More stat items -->
</div>
```

---

## Common Quality Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| Gray callout backgrounds | Looks dated, prints poorly | Change to white + shadow |
| Inconsistent spacing | Visual "jumpiness" | Use spacing scale consistently |
| Generic examples | "A company might..." | Use specific, named examples with data |
| Missing transitions | Abrupt topic changes | Add transition cues to speaker notes |
| Timing doesn't add up | Over/under time in delivery | Verify math before finalizing |
| Next session preview wrong | AI hallucinated content | **Always verify against course syllabus** |

---

*Quality is not an accident. It's the result of following standards consistently.*
