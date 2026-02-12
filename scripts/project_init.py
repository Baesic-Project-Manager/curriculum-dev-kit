#!/usr/bin/env python3
"""
Curriculum Module Initialization Script

Automates setup for curriculum rework projects. Creates folder structure,
initializes changelog and context bundle.

Usage:
    python project_init.py --course 2 --module 3 --title "Module Title"
    python project_init.py -c 2 -m 3 -t "Title" --duration 90
    python project_init.py -c 2 -m 3 -t "Title" --no-launch
    python project_init.py -c 2 -m 3 -t "Title" --print-only
"""

import argparse
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# =============================================================================
# CONFIGURATION - Update these paths for your environment
# =============================================================================

# Base path where course folders live
BASE_COURSE_PATH = Path(os.environ.get(
    "COURSES_BASE_PATH",
    "/path/to/your/courses"
))

# Path to templates
STARTER_KIT_PATH = Path(os.environ.get(
    "STARTER_KIT_PATH",
    "/path/to/curriculum-dev-kit/templates"
))

# Timing defaults
DEFAULT_DURATION = int(os.environ.get("DEFAULT_DURATION", 90))
BUFFER_MINUTES = int(os.environ.get("BUFFER_MINUTES", 3))
MINUTES_PER_SLIDE = 2.5


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def calculate_max_slides(target_duration: int) -> int:
    """Calculate maximum slides given target session duration."""
    available = target_duration - BUFFER_MINUTES
    return round(available / MINUTES_PER_SLIDE)


def get_current_month_year() -> tuple[str, int]:
    """Return current month name and year."""
    now = datetime.now()
    return now.strftime("%B"), now.year


def find_existing_reworks(module_path: Path) -> list[Path]:
    """Find existing rework/remake folders."""
    reworks = []
    if module_path.exists():
        for item in module_path.iterdir():
            if item.is_dir():
                name_lower = item.name.lower()
                if "rework" in name_lower or "remake" in name_lower:
                    reworks.append(item)
    return sorted(reworks, key=lambda p: p.name)


def find_source_presentation(module_path: Path) -> tuple[Path | None, list[Path]]:
    """Find source presentation file in module folder."""
    pptx_files = []
    if module_path.exists():
        for item in module_path.iterdir():
            if item.is_file() and item.suffix.lower() in [".pptx", ".pdf"]:
                pptx_files.append(item)

    if len(pptx_files) == 0:
        return None, []
    elif len(pptx_files) == 1:
        return pptx_files[0], pptx_files
    else:
        return None, pptx_files


def generate_changelog(course: int, module: int, title: str, duration: int,
                       source_file: Path | None, rework_folder: Path) -> str:
    """Generate the 00_Project_Changelog.md content."""
    max_slides = calculate_max_slides(duration)
    available = duration - BUFFER_MINUTES
    today = datetime.now().strftime("%Y-%m-%d")
    source_str = str(source_file) if source_file else "Not specified"

    return f"""# Project Changelog: {title}

**Course:** {course}
**Module:** {module}
**Rework Started:** {today}
**Target Duration:** {duration} minutes ({available} usable)
**Max Slides:** {max_slides}

---

## Status

**Current Phase:** Phase 1 — Topic Outline Review
**Blockers:** None
**Last Updated:** {today}

---

## Activity Log

| Date | Phase | Action | Notes |
|------|-------|--------|-------|
| {today} | Setup | Project initialized | Automated via init script |

---

## File Locations

**Source Presentation:** {source_str}
**Rework Folder:** {rework_folder}
**Starter Kit:** {STARTER_KIT_PATH}
"""


def generate_context_bundle(course: int, module: int, title: str, duration: int,
                            source_file: Path | None, rework_folder: Path,
                            previous_rework: Path | None) -> str:
    """Generate the 00_Context_Bundle.md content."""
    max_slides = calculate_max_slides(duration)
    available = duration - BUFFER_MINUTES
    prev_str = str(previous_rework) if previous_rework else "None"
    source_str = str(source_file) if source_file else "Not specified"

    topic_outline = STARTER_KIT_PATH / "01-topic-outline-review.md"

    return f"""# Context Bundle: {title}

## Quick Reference

**This rework:** {rework_folder}
**Source presentation:** {source_str}
**Previous rework:** {prev_str}

---

## Files for Phase 1

Read these to begin Topic Outline Review:

1. **Source presentation:** {source_str}
2. **Topic Outline Template:** {topic_outline}

---

## Timing Budget

- Target session: {duration} minutes
- Buffer: {BUFFER_MINUTES} minutes
- Available: {available} minutes
- At {MINUTES_PER_SLIDE} min/slide: **{max_slides} slides maximum**

---

## Starter Kit Location

All templates: `{STARTER_KIT_PATH}`

| Template | Purpose |
|----------|---------|
| 01-topic-outline-review.md | Phase 1 |
| 02-presentation-brief.md | Phase 3 |
| 03-speaker-notes-spec.md | Phase 4 |
| 04-speaker-notes-sample.md | Phase 4 reference |
| presentation-template.html | Phase 4 |
"""


def generate_prompt(course: int, module: int, title: str, duration: int,
                    source_file: Path | None, rework_folder: Path) -> str:
    """Generate the prompt for starting work."""
    max_slides = calculate_max_slides(duration)
    topic_outline = STARTER_KIT_PATH / "01-topic-outline-review.md"
    source_str = str(source_file) if source_file else "[specify source file]"

    return f"""I'm starting a rework of Course {course} Module {module}: {title}.

Please read these files:
1. Source presentation: {source_str}
2. Topic Outline Template: {topic_outline}

Create a Topic Outline Review using the template. I need:
- Section-by-section breakdown with slide numbers and content summaries
- Timing math (current slide count vs. {max_slides}-slide target)
- Identified consolidation opportunities
- Decision points for me to complete

Target session length: {duration} minutes ({duration - BUFFER_MINUTES} usable, {max_slides} slides max)"""


def launch_claude_code(prompt: str, working_dir: Path,
                       additional_dirs: list[Path] = None) -> bool:
    """
    Launch Claude Code with the given prompt and working directory.
    Returns True on successful launch, False otherwise.
    """
    claude_path = shutil.which("claude")
    if not claude_path:
        print("[ERROR] Claude Code CLI not found in PATH")
        return False

    cmd = [claude_path]

    if additional_dirs:
        for dir_path in additional_dirs:
            if dir_path.exists():
                cmd.extend(["--add-dir", str(dir_path)])

    cmd.append(prompt)

    print(f"\n[LAUNCHING] Claude Code in {working_dir}")
    print("[INFO] Claude will have access to the rework folder and source files")

    try:
        subprocess.run(cmd, cwd=str(working_dir), shell=False)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to launch Claude Code: {e}")
        return False


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def initialize_project(course: int, module: int, title: str,
                       duration: int = DEFAULT_DURATION,
                       force: bool = False,
                       source_file: str | None = None,
                       no_launch: bool = False,
                       print_only: bool = False) -> bool:
    """
    Main function to initialize a curriculum rework project.

    Returns True on success, False on failure.
    """
    month, year = get_current_month_year()
    rework_name = f"{month} {year} ReWork"

    # Validate course folder
    course_folder = BASE_COURSE_PATH / f"Course {course}"
    if not course_folder.exists():
        print(f"ERROR: Course folder not found: {course_folder}")
        try:
            available = [p.name for p in BASE_COURSE_PATH.iterdir() if p.is_dir()]
            if available:
                print(f"Available courses: {available}")
        except OSError:
            pass
        return False

    # Validate module folder
    module_folder = course_folder / f"Module {module}"
    if not module_folder.exists():
        print(f"ERROR: Module folder not found: {module_folder}")
        try:
            modules = [p.name for p in course_folder.iterdir()
                       if p.is_dir() and p.name.startswith("Module")]
            if modules:
                print(f"Available modules: {modules}")
        except OSError:
            pass
        return False

    # Check for existing reworks
    existing_reworks = find_existing_reworks(module_folder)
    rework_folder = module_folder / rework_name

    if rework_folder.exists() and not force:
        print(f"WARNING: Rework folder already exists: {rework_folder}")
        print("Use --force to overwrite.")
        return False

    # Find source presentation
    source_path = None
    if source_file:
        source_path = module_folder / source_file
        if not source_path.exists():
            print(f"ERROR: Specified source file not found: {source_path}")
            return False
    else:
        source_path, all_sources = find_source_presentation(module_folder)

        if not all_sources:
            print(f"WARNING: No source files found in {module_folder}")
            print("Continuing without source reference.")
        elif source_path is None and len(all_sources) > 1:
            print(f"Multiple source files found. Please specify with --source:")
            for i, f in enumerate(all_sources, 1):
                print(f"  {i}. {f.name}")
            return False

    # Determine previous rework
    previous_rework = None
    if existing_reworks and existing_reworks[-1] != rework_folder:
        previous_rework = existing_reworks[-1]

    # Create rework folder
    rework_folder.mkdir(parents=True, exist_ok=True)
    print(f"Created: {rework_folder}")

    # Generate and write changelog
    changelog_content = generate_changelog(
        course, module, title, duration, source_path, rework_folder
    )
    changelog_path = rework_folder / "00_Project_Changelog.md"
    changelog_path.write_text(changelog_content, encoding="utf-8")
    print(f"Created: {changelog_path.name}")

    # Generate and write context bundle
    bundle_content = generate_context_bundle(
        course, module, title, duration, source_path, rework_folder, previous_rework
    )
    bundle_path = rework_folder / "00_Context_Bundle.md"
    bundle_path.write_text(bundle_content, encoding="utf-8")
    print(f"Created: {bundle_path.name}")

    # Generate prompt
    prompt = generate_prompt(
        course, module, title, duration, source_path, rework_folder
    )
    max_slides = calculate_max_slides(duration)

    # Print summary
    divider = "=" * 60
    print(f"\n{divider}")
    print(f"PROJECT INITIALIZED: Course {course} Module {module}")
    print(f"{divider}")
    print(f"Rework folder: {rework_folder}")
    print(f"Source: {source_path.name if source_path else 'Not specified'}")
    print(f"Target: {duration} min / {max_slides} slides max")
    print(divider)

    # Handle output mode
    if print_only:
        print("\nPROMPT TO START PHASE 1:\n")
        print(prompt)
        print(f"\n{divider}")
    elif not no_launch:
        additional_dirs = [d for d in [
            source_path.parent if source_path else None,
            STARTER_KIT_PATH,
        ] if d and d.exists()]
        launch_claude_code(prompt, rework_folder, additional_dirs)
    else:
        print("\n[INFO] Files created. Use --print-only to see the prompt, "
              "or remove --no-launch to auto-start Claude.")

    return True


# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Initialize a curriculum rework project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project_init.py -c 4 -m 5 -t "Effective Communication"
  python project_init.py --course 4 --module 5 --title "Title" --duration 90
  python project_init.py -c 4 -m 5 -t "Title" --source "specific_file.pptx"
        """
    )

    parser.add_argument("-c", "--course", type=int, required=True,
                        help="Course number")
    parser.add_argument("-m", "--module", type=int, required=True,
                        help="Module number")
    parser.add_argument("-t", "--title", type=str, required=True,
                        help="Module title")
    parser.add_argument("-d", "--duration", type=int, default=DEFAULT_DURATION,
                        help=f"Target duration in minutes (default: {DEFAULT_DURATION})")
    parser.add_argument("-s", "--source", type=str, default=None,
                        help="Specific source filename")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Overwrite existing rework folder")
    parser.add_argument("--no-launch", action="store_true",
                        help="Don't launch editor, just create files")
    parser.add_argument("--print-only", action="store_true",
                        help="Print prompt instead of launching")

    args = parser.parse_args()

    success = initialize_project(
        course=args.course,
        module=args.module,
        title=args.title,
        duration=args.duration,
        force=args.force,
        source_file=args.source,
        no_launch=args.no_launch,
        print_only=args.print_only
    )

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
