# Design System

CSS variables, color schemes, and typography standards for HTML presentations.

---

## Default Color Scheme (Navy + Gold)

The proven default scheme for professional presentations:

```css
:root {
    /* Core Colors */
    --primary-color: #003B7A;      /* Navy Blue - headings, accents */
    --secondary-color: #F4B41A;    /* Gold - subheadings, highlights */
    --text-color: #2C3E50;         /* Dark Gray-Blue - body text */
    --background-color: #FFFFFF;   /* White - slide background */
    --footer-color: #7F8C8D;       /* Medium Gray - footer text */
}
```

### Color Usage

| Element | Color Variable | Hex Value |
|---------|---------------|-----------|
| H1 Headings | `--primary-color` | #003B7A |
| H2 Subtitles | `--secondary-color` | #F4B41A |
| Body text | `--text-color` | #2C3E50 |
| Bullet points | `--secondary-color` | #F4B41A |
| Bold text | `--primary-color` | #003B7A |
| Italic text | `--secondary-color` | #F4B41A |
| Footer | `--footer-color` | #7F8C8D |

---

## Alternative Color Schemes

### Teal + Coral

```css
:root {
    --primary-color: #00796B;      /* Teal */
    --secondary-color: #FF7043;    /* Coral */
    --text-color: #37474F;         /* Blue Gray */
    --background-color: #FFFFFF;
    --footer-color: #78909C;
}
```

### Purple + Gold

```css
:root {
    --primary-color: #512DA8;      /* Deep Purple */
    --secondary-color: #FFC107;    /* Amber */
    --text-color: #424242;         /* Gray */
    --background-color: #FFFFFF;
    --footer-color: #9E9E9E;
}
```

### Forest + Orange

```css
:root {
    --primary-color: #2E7D32;      /* Green */
    --secondary-color: #FF9800;    /* Orange */
    --text-color: #33691E;         /* Light Green Dark */
    --background-color: #FFFFFF;
    --footer-color: #8D6E63;
}
```

---

## Typography

### Font Stack

```css
:root {
    --font-main: 'Segoe UI', 'Arial', sans-serif;
    --font-code: 'Consolas', 'Courier New', monospace;
}
```

### Size Hierarchy

| Element | Size | Weight |
|---------|------|--------|
| H1 (Title slide) | 4.5rem | 600 |
| H1 (Content) | 3.5rem | 600 |
| H2 (Subtitle) | 2rem | 500 |
| H3 (Section) | 2rem | 500 |
| Body text | 1.8rem | 400 |
| List items (L1) | 2rem | 400 |
| List items (L2) | 1.6rem | 400 |
| Callout text | 1.6rem | 400 |
| Footer | 1.2rem | 400 |

---

## Spacing Scale

### Slide Layout

```css
:root {
    --slide-padding: 4vh 6vw;
    --header-height: 15vh;
    --footer-height: 8vh;
    --content-spacing: 3vh;
}
```

### Component Spacing

| Element | Property | Value |
|---------|----------|-------|
| List items (L1) | margin-bottom | 2.5vh |
| List items (L2) | margin-bottom | 1.5vh |
| Nested lists | margin-left | 2rem |
| Callout boxes | margin | 3vh 0 |
| Callout boxes | padding | 2vh 2vw |
| Two-column gap | gap | 4vw |
| Stats grid gap | gap | 3vw |

---

## Callout Box Borders

| Type | Border Color | Use Case |
|------|--------------|----------|
| Standard | `--secondary-color` (Gold) | General emphasis |
| Key Takeaway | `--secondary-color` (Gold) | Critical insights |
| Example | `--primary-color` (Navy) | Real-world cases |
| Warning | `#D32F2F` (Red) | Mistakes to avoid |
| Bias Check | `#7B1FA2` (Purple) | Cognitive biases |
| Stat Callout | `#388E3C` (Green) | Impact metrics |

---

## Shadows

Standard shadow for elevated elements:

```css
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
```

Used on:
- Callout boxes
- Stat items
- SVG containers

---

## Borders

### Header Border
```css
border-bottom: 3px solid var(--primary-color);
```

### Footer Border
```css
border-top: 2px solid #E0E0E0;
```

### Callout Border
```css
border-left: 5px solid [color];
border-radius: 4px;
```

---

## Customizing Your Presentation

### Step 1: Choose a Scheme

Copy one of the color schemes above, or create your own following the pattern.

### Step 2: Update CSS Variables

In your HTML file, replace the `:root` variables:

```css
:root {
    --primary-color: #YOUR_PRIMARY;
    --secondary-color: #YOUR_SECONDARY;
    --text-color: #YOUR_TEXT;
    --background-color: #FFFFFF;
    --footer-color: #YOUR_FOOTER;
}
```

### Step 3: Test

Check that:
- Headers are readable
- Bold/italic emphasis is visible
- Callout borders match semantic meaning
- Footer is subtle but legible

---

## Accessibility Notes

### Contrast Ratios

The default Navy + Gold scheme provides:
- Navy on white: 10.5:1 (AAA)
- Gold on white: 2.8:1 (decorative only)
- Text on white: 10.7:1 (AAA)

### Recommendations

- Never use gold for body text (contrast too low)
- Use gold for decorative elements only (borders, bullets, emphasis)
- Test custom schemes with a contrast checker

---

## Print Considerations

The design system uses white backgrounds specifically for clean printing:

- Callout boxes print clearly without gradient artifacts
- Navy text prints well in grayscale
- Shadows are subtle enough to not create heavy marks

If printing, test a few slides first.

---

*This design system is part of the Curriculum Dev Kit.*
