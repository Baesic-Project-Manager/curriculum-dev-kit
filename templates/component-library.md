# Component Library

Copy-paste ready components for HTML presentations. Each component follows the design system standards.

---

## Callout Boxes

All callout boxes share these base properties:
- **Background:** White (`#FFFFFF`)
- **Left border:** 5px solid (color varies by type)
- **Shadow:** `0 2px 8px rgba(0, 0, 0, 0.1)`
- **Padding:** `2vh 2vw`
- **Margin:** `3vh 0`

### Standard Callout (Gold Border)

**Use for:** General emphasis, supporting information

```html
<div class="callout-box">
    <h3>Callout Title</h3>
    <p>Supporting information that adds context.</p>
</div>
```

### Key Takeaway (Gold Border, Labeled)

**Use for:** Critical insights learners must remember

```html
<div class="callout-box key-takeaway">
    <h3>Key Takeaway</h3>
    <p>The most important insight from this slide.</p>
</div>
```

### Example Box (Navy Border)

**Use for:** Real-world examples, case studies

```html
<div class="callout-box example">
    <h3>Example</h3>
    <p><strong>Company X:</strong> Description of what happened and results.</p>
</div>
```

### Warning Box (Red Border)

**Use for:** Common mistakes, pitfalls to avoid

```html
<div class="callout-box warning-box">
    <h3>Warning</h3>
    <p>This common mistake can cause problems. Here's how to avoid it.</p>
</div>
```

### Bias Check (Purple Border)

**Use for:** Cognitive biases, reflection prompts

```html
<div class="callout-box bias-check">
    <h3>Bias Check</h3>
    <p><strong>What it is:</strong> Description of the cognitive bias</p>
    <p><strong>How it shows up:</strong> Example in professional context</p>
    <p><strong>Counter-strategy:</strong> What to do instead</p>
</div>
```

### Stat Callout (Green Border, Centered)

**Use for:** Single impactful statistic

```html
<div class="callout-box stat-callout">
    <p class="big-stat">76%</p>
    <p class="stat-context">of professionals report this outcome</p>
</div>
```

---

## Layout Patterns

### Two-Column Comparison

**Use for:** A vs B, pros/cons, before/after

**Prefer over tables** for concept comparisons.

```html
<div class="two-column">
    <div class="column">
        <h3>Concept A</h3>
        <ul>
            <li>First characteristic</li>
            <li>Second characteristic</li>
            <li>Third characteristic</li>
        </ul>
    </div>
    <div class="column">
        <h3>Concept B</h3>
        <ul>
            <li>First characteristic</li>
            <li>Second characteristic</li>
            <li>Third characteristic</li>
        </ul>
    </div>
</div>
```

### Stats Grid (3-Column)

**Use for:** Multiple metrics, impact data

```html
<div class="stats-grid">
    <div class="stat-item">
        <span class="stat-number">75%</span>
        <span class="stat-label">Success Rate</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">30%</span>
        <span class="stat-label">Time Saved</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">15%</span>
        <span class="stat-label">Cost Reduction</span>
    </div>
</div>
```

---

## Slide Types

### Section Header Slide

**Use for:** Major section transitions

```html
<div class="slide section-header">
    <div class="slide-header">
        <h1>Section Title</h1>
        <h2>Section Subtitle</h2>
    </div>
    <div class="slide-content">
        <p>Brief preview of what this section covers.</p>
    </div>
    <div class="slide-footer">
        <p>Course Name | Module Name</p>
        <p class="slide-number">X</p>
    </div>
</div>
```

### Hook Slide

**Use for:** Provocative statements, key revelations

```html
<div class="slide hook-slide">
    <div class="slide-header">
        <h1>The Reality Check</h1>
    </div>
    <div class="slide-content">
        <p class="hook-text">The setup statement...</p>
        <p class="hook-emphasis">The powerful conclusion.</p>
    </div>
    <div class="slide-footer">
        <p>Course Name | Module Name</p>
        <p class="slide-number">X</p>
    </div>
</div>
```

### Sources Slide

**Use for:** Citations (required for credibility)

```html
<div class="slide">
    <div class="slide-header">
        <h1>Sources</h1>
    </div>
    <div class="slide-content">
        <ul class="sources-list">
            <li>Author. (Year). <em>Title</em>. Publication.</li>
            <li>Organization. (Year). <em>Report Name</em>.</li>
        </ul>
    </div>
    <div class="slide-footer">
        <p>Course Name | Module Name</p>
        <p class="slide-number">X</p>
    </div>
</div>
```

---

## Tables

### When to Use

Tables are appropriate ONLY when you have:
- Data with more than 2 comparable dimensions
- Numerical data needing alignment
- Complex comparisons where rows and columns intersect

For simple A vs B, use two-column layout instead.

### Table Styling

```html
<table class="data-table">
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
            <td>Data 3</td>
        </tr>
    </tbody>
</table>
```

Add this CSS if using tables:

```css
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2vh 0;
    font-size: 1.6rem;
}

.data-table th {
    background: var(--primary-color);
    color: white;
    padding: 1.5vh 2vw;
    text-align: left;
}

.data-table td {
    padding: 1.5vh 2vw;
    border-bottom: 1px solid #E0E0E0;
}

.data-table tbody tr:nth-child(even) {
    background: #F8F9FA;
}
```

---

## Do's and Don'ts

### Callout Boxes

| Do | Don't |
|----|-------|
| Use white backgrounds | Use gradient backgrounds |
| Use semantic types | Use generic callouts for everything |
| Keep text concise | Put entire paragraphs in callouts |
| One callout per key point | Stack multiple callouts |

### Layouts

| Do | Don't |
|----|-------|
| Use two-column for A vs B | Use tables for simple comparisons |
| Align columns at flex-start | Force equal-height columns |
| Use stats grid for metrics | Scatter stats throughout bullets |

### Typography

| Do | Don't |
|----|-------|
| Use bold for key terms (navy) | Use bold everywhere |
| Use italic sparingly (gold) | Use italic for long phrases |
| Keep list items to one line | Write paragraph-length bullets |

---

*This library is part of the Curriculum Dev Kit.*
