<!--
Template: Pre-Delivery QA Checklist
Version: 2.0.0
Last Updated: 2025-01-29
Changelog: https://github.com/Baesic-Project-Manager/curriculum-dev-kit/wiki/Template-Changelog
-->

# Pre-Delivery QA Checklist

**Use when:** Before delivering any presentation
**Time required:** 30-45 minutes
**Rule:** Complete all items or document exceptions before finalizing

---

## Quick Reference

| Category | Expected Time |
|----------|---------------|
| Visual Consistency | 5-10 minutes |
| Content Completeness | 10-15 minutes |
| Speaker Notes Review | 5-10 minutes |
| Technical Testing | 5 minutes |

---

## 1. Visual Consistency

### Headers
- [ ] All H1 headers use primary color (navy)
- [ ] All H1 headers are same size (3.5rem for content, 4.5rem for title)
- [ ] All H2 subtitles use secondary color (gold)
- [ ] All H2 subtitles are same size (2rem)
- [ ] No inline font-size overrides on headers

### Callout Boxes
- [ ] All callout boxes have white background (`#FFFFFF`)
- [ ] All callout boxes have shadow (`box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1)`)
- [ ] Border colors match semantic type:
  - [ ] Standard/Key Takeaway: Gold
  - [ ] Example: Navy
  - [ ] Warning: Red (`#D32F2F`)
  - [ ] Bias Check: Purple (`#7B1FA2`)
  - [ ] Stat Callout: Green (`#388E3C`)
- [ ] No gradient backgrounds on callout boxes

### Text Emphasis
- [ ] Bold text renders in navy (primary color)
- [ ] Italic text renders in gold (secondary color)
- [ ] No other colors used for random emphasis

### Colors
- [ ] No hardcoded hex values in slide content
- [ ] All colors reference CSS variables or documented accents
- [ ] Footer text uses footer color

---

## 2. Content Completeness

### Mandatory Slides Present
- [ ] Title slide (first)
- [ ] Learning objectives (second)
- [ ] Today's roadmap/overview (third)
- [ ] Sources slide (near end)
- [ ] Bias check slide
- [ ] Key takeaways slide (near end)

### Next Session Preview (CRITICAL)

**This slide is frequently auto-generated with INCORRECT content. STOP and verify.**

- [ ] **Module title matches actual next module** in course sequence
- [ ] **Bullet points reflect actual next module content** (not fabricated)
- [ ] Cross-referenced with course syllabus or module list

If this is the **final module in a course**, the slide should preview the next course, not make up content.

### Slide Numbers
- [ ] All slide numbers are sequential
- [ ] Slide numbers in footer match actual position
- [ ] No duplicate slide numbers

### Footer Content
- [ ] Course name is correct on all slides
- [ ] Module name is correct on all slides
- [ ] Consistent format across all footers

### Sources Slide
- [ ] All cited statistics have sources
- [ ] Source formatting is consistent
- [ ] Sources are credible/verifiable

---

## 3. Fact-Check Buffer

### Statistics Verification
- [ ] All percentages are from cited sources
- [ ] Statistics are recent (within 2-3 years unless historical)
- [ ] No placeholder or made-up numbers remain

### Claims Review
- [ ] Bold claims have supporting evidence
- [ ] Industry examples are accurate
- [ ] No outdated information

### Link Validation (if applicable)
- [ ] Any referenced URLs are accessible
- [ ] QR codes scan correctly

---

## 4. Speaker Notes Review

### Completeness
- [ ] Every slide has speaker notes
- [ ] Time allocations present for each slide
- [ ] Transition cues between slides (except last)
- [ ] Timing summary table at end of document

### Quality
- [ ] Voice is first-person and conversational
- [ ] Notes expand on slides (not just repeat them)
- [ ] Examples are specific and concrete
- [ ] Key takeaways are actionable

### Math Check
- [ ] Individual slide times sum to presentation duration
- [ ] Buffer time is accounted for
- [ ] Total matches session length

---

## 5. Technical Testing

### Browser Testing
- [ ] Presentation loads without errors
- [ ] No console errors in browser dev tools
- [ ] Navigation works (arrow keys, space bar, click)

### Resolution Testing
- [ ] Test at presentation resolution (1920x1080 recommended)
- [ ] Test at smaller resolution (1366x768)
- [ ] Content remains readable at both sizes

### Print Testing (if needed)
- [ ] Print preview shows all slides
- [ ] Page breaks occur correctly
- [ ] Navigation buttons are hidden in print

---

## 6. Spacing Audit

### List Spacing
- [ ] All first-level list items have consistent margin
- [ ] All nested list items have consistent margin
- [ ] No visual jumps between list items

### Callout Spacing
- [ ] All callout boxes have consistent margin
- [ ] Consistent padding within callouts
- [ ] No inline margin overrides

### Slide Layout
- [ ] Slide padding is consistent
- [ ] Header height is consistent
- [ ] Footer height is consistent
- [ ] Content has room to breathe (not cramped)

### Inline Style Check
- [ ] Search for `style="` in HTML — should be minimal/none
- [ ] Any inline styles are documented exceptions

---

## Exception Log

Document any intentional deviations from standards:

| Slide # | Deviation | Reason |
|---------|-----------|--------|
| | | |
| | | |
| | | |

---

## Sign-Off

**Reviewer:** _______________________

**Date:** _______________________

**Status:** [ ] Approved  [ ] Approved with exceptions  [ ] Needs revision

**Notes:**

---

## Quick Fix Reference

### Gray backgrounds on callouts
```css
/* Change this */
background: #F8F9FA;
/* To this */
background: #FFFFFF;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
```

### Inconsistent list spacing
```css
/* Ensure all list items use */
margin-bottom: 2.5vh; /* First level */
margin-bottom: 1.5vh; /* Nested */
```

### Hardcoded colors
```css
/* Change this */
color: #003B7A;
/* To this */
color: var(--primary-color);
```

---

*This checklist is part of the Curriculum Dev Kit.*
