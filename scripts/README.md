# Scripts

Supporting automation for the curriculum development workflow.

---

## Overview

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `project_init.py` | Scaffold a new module rework folder | Starting a new module |
| `validate_module.py` | Validate module completeness | Before publishing |

---

## Requirements

- Python 3.10+
- PyYAML (`pip install pyyaml`)

---

## Environment Variables

Set these in your environment or `.env` file:

```bash
# Required paths
export COURSES_BASE_PATH="/path/to/your/courses"
export STARTER_KIT_PATH="/path/to/curriculum-dev-kit/templates"

# Optional
export DEFAULT_DURATION=90  # Session length in minutes
export BUFFER_MINUTES=3     # Buffer for transitions
```

---

## project_init.py

Scaffolds a new module rework folder with changelog and context bundle.

### Usage

```bash
# Basic usage
python project_init.py --course 2 --module 3 --title "Module Title"

# With custom duration
python project_init.py -c 2 -m 3 -t "Module Title" --duration 60

# Just create files (don't launch editor)
python project_init.py -c 2 -m 3 -t "Module Title" --no-launch

# Print prompt only (for manual copy-paste)
python project_init.py -c 2 -m 3 -t "Module Title" --print-only
```

### What It Creates

```
{Course}/{Module}/{Month} {Year} ReWork/
├── 00_Project_Changelog.md    # Track what changed
└── 00_Context_Bundle.md       # File references for session
```

### Arguments

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| `--course` | `-c` | Yes | Course number |
| `--module` | `-m` | Yes | Module number |
| `--title` | `-t` | Yes | Module title |
| `--duration` | `-d` | No | Session duration (default: 90) |
| `--source` | `-s` | No | Specific source filename |
| `--force` | `-f` | No | Overwrite existing folder |
| `--no-launch` | | No | Don't launch editor |
| `--print-only` | | No | Just print the prompt |

---

## validate_module.py

Validates a module folder before publishing.

### Usage

```bash
# Full validation
python validate_module.py "/path/to/module"

# Schema only (skip HTML checks)
python validate_module.py "/path/to/module" --schema-only
```

### What It Checks

1. **Schema validation** — `module.yaml` exists and conforms to schema
2. **Code matches path** — Module code matches folder structure
3. **Deliverables exist** — All specified files are present
4. **HTML validation** — No banned patterns (external resources, etc.)
5. **Size limits** — Files and total module under limits

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Valid — ready for publish |
| 1 | Schema validation failed |
| 2 | HTML validation failed |
| 3 | File not found |

### module.yaml Schema

Modules must include a `module.yaml` file:

```yaml
schema_version: "1.0"
code: "C1M1"
title: "Module Title"
status: "published"  # draft, in_progress, review, published, archived
score: 3             # 0-4 quality score

deliverables:
  presentation: "presentation.html"
  speaker_notes: "speaker_notes.md"
```

### Banned HTML Patterns

The validator rejects HTML files containing:

- External images (`<img src=...>`)
- External CSS (`<link href=...>`)
- External JavaScript (`<script src=...>`)
- Iframes
- CSS `@import url()`
- Base64 raster images (file size bloat)

### Size Limits

- Single file: 500 KB
- Total module: 1 MB

---

## Adapting for Your Environment

These scripts were designed for a specific folder structure. To adapt:

1. **Update paths** in the configuration section at the top of each script
2. **Adjust naming conventions** if your courses use different patterns
3. **Modify validation rules** if you have different requirements

The scripts are intentionally simple and readable for easy customization.

---

## Example Workflow

```bash
# 1. Initialize a new module rework
python scripts/project_init.py -c 4 -m 2 -t "Stakeholder Communication"

# 2. Work through the phases...
#    - Complete topic outline review
#    - Lock presentation brief
#    - Build HTML presentation
#    - Write speaker notes

# 3. Validate before considering it done
python scripts/validate_module.py "Course 4/Module 2/January 2025 ReWork"

# 4. If validation passes, module is ready
```

---

*These scripts are part of the Curriculum Dev Kit.*
