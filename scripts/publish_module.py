#!/usr/bin/env python3
"""
Module Publishing Script

Post-completion publishing tool for the curriculum dev kit.
Copies validated course modules from a source location to the Git repository
with content hashing, safety checks, and optional Qdrant indexing.

Exit codes:
  0 = Success
  1 = Validation failed
  2 = Safety check failed (requires --force)
  3 = File not found
  4 = Qdrant/Ollama connection error
  5 = Git commit failed

Usage:
  python publish_module.py C1M1 --dry-run
  python publish_module.py C1M1
  python publish_module.py C1M1 --force
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

# Configuration
WORKSPACE_ROOT = Path(os.environ.get("WORKSPACE_ROOT", "."))
COURSES_ROOT = WORKSPACE_ROOT / "courses"
ONEDRIVE_BASE = Path(os.environ.get("COURSE_BASE_PATH", "."))

# File extensions to include in hashing and copying
INCLUDE_EXTENSIONS = {'.html', '.md', '.yaml', '.yml', '.txt'}

# Retry settings for cloud-synced file locking
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def log(message: str, status: str = "INFO") -> None:
    """Print formatted log message."""
    symbols = {
        "OK": "[OK]",
        "FAIL": "[FAIL]",
        "WARN": "[WARN]",
        "INFO": "->",
        "DRY": "[DRY]",
    }
    symbol = symbols.get(status, "->")
    print(f"{symbol} {message}")


def read_file_with_retry(path: Path) -> str:
    """Read file with retry logic for cloud-synced file locks."""
    for attempt in range(MAX_RETRIES):
        try:
            return path.read_text(encoding='utf-8')
        except PermissionError:
            if attempt < MAX_RETRIES - 1:
                log(f"File locked, retrying in {RETRY_DELAY}s... ({path.name})", "WARN")
                time.sleep(RETRY_DELAY)
            else:
                raise


def calculate_content_hash(folder: Path) -> str:
    """Calculate deterministic SHA256 hash of folder contents."""
    hasher = hashlib.sha256()

    # Get files sorted alphabetically for determinism
    files = sorted([
        f for f in folder.rglob('*')
        if f.is_file() and f.suffix.lower() in INCLUDE_EXTENSIONS
        and not f.name.startswith('_')  # Exclude marker files
    ])

    for file_path in files:
        # Add relative path to hash
        rel_path = file_path.relative_to(folder)
        hasher.update(str(rel_path).encode('utf-8'))

        # Add normalized content
        try:
            content = read_file_with_retry(file_path)
            content = content.replace('\r\n', '\n').strip()
            hasher.update(content.encode('utf-8'))
        except Exception as e:
            log(f"Cannot read {file_path.name}: {e}", "WARN")

    return f"sha256:{hasher.hexdigest()}"


def discover_source_path(module_code: str) -> Path | None:
    """
    Discover source path based on module code.

    Pattern: COURSE_BASE_PATH/{year}/Course {X}/Module {Y}/.../ReWork/
    """
    match = re.match(r'C(\d+)M(\d+)', module_code.upper())
    if not match:
        return None

    course_num = int(match.group(1))
    module_num = int(match.group(2))

    # Try different year folders
    for year in ["2026", "2025"]:
        year_path = ONEDRIVE_BASE / year
        if not year_path.exists():
            continue

        # Look for course folder
        course_pattern = f"Course {course_num}"
        for course_folder in year_path.iterdir():
            if course_folder.is_dir() and course_pattern in course_folder.name:
                # Look for module folder
                module_pattern = f"Module {module_num}"
                for module_folder in course_folder.iterdir():
                    if module_folder.is_dir() and module_pattern in module_folder.name:
                        # Look for ReWork folder (most recent month)
                        rework_folders = [
                            f for f in module_folder.iterdir()
                            if f.is_dir() and "ReWork" in f.name
                        ]
                        if rework_folders:
                            # Sort by name to get most recent
                            rework_folders.sort(key=lambda x: x.name, reverse=True)
                            return rework_folders[0]

    return None


def get_dest_path(module_code: str) -> Path:
    """Get destination path in courses/ folder."""
    match = re.match(r'C(\d+)M(\d+)', module_code.upper())
    if not match:
        raise ValueError(f"Invalid module code: {module_code}")

    course_num = match.group(1)
    module_num = match.group(2)

    return COURSES_ROOT / "google-pm" / f"c{course_num}" / f"m{module_num}"


def extract_hash_from_marker(marker_path: Path) -> str | None:
    """Extract content hash from _GIT_PUBLISHED.md marker file."""
    try:
        content = read_file_with_retry(marker_path)
        match = re.search(r'Content Hash:\s*(\S+)', content)
        if match:
            return match.group(1)
    except Exception:
        pass
    return None


def check_publish_safety(source_path: Path, dest_path: Path) -> tuple[bool, str]:
    """
    Check if it's safe to publish.

    Returns (safe: bool, reason: str)
    """
    marker_path = source_path / "_GIT_PUBLISHED.md"
    marker_exists = marker_path.exists()
    dest_exists = dest_path.exists() and any(dest_path.iterdir())

    if not dest_exists:
        return True, "First-time publish to empty destination"

    if marker_exists:
        stored_hash = extract_hash_from_marker(marker_path)
        if stored_hash is None:
            return False, "Marker file exists but hash is missing/corrupted"

        git_hash = calculate_content_hash(dest_path)

        if git_hash == stored_hash:
            return True, "Destination unchanged since last publish"
        else:
            return False, f"Destination modified since last publish\n  Stored: {stored_hash[:20]}...\n  Current: {git_hash[:20]}..."
    else:
        return False, "Destination exists but no publish marker found (orphaned or manual edit?)"


def copy_module_files(source_path: Path, dest_path: Path, dry_run: bool = False) -> list[str]:
    """Copy module files from source to destination."""
    copied = []

    # Create destination if needed
    if not dry_run:
        dest_path.mkdir(parents=True, exist_ok=True)

    # Copy files with included extensions
    for file_path in source_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in INCLUDE_EXTENSIONS:
            if not file_path.name.startswith('_'):  # Skip marker files
                dest_file = dest_path / file_path.name
                if dry_run:
                    status = "update" if dest_file.exists() else "new"
                    copied.append(f"+ {file_path.name} ({status})")
                else:
                    shutil.copy2(file_path, dest_file)
                    copied.append(file_path.name)

    return copied


def create_marker_file(source_path: Path, dest_path: Path, commit_hash: str = "pending") -> None:
    """Create _GIT_PUBLISHED.md marker file in source directory."""
    content_hash = calculate_content_hash(dest_path)

    marker_content = f"""# Published to Git Repository

- **Published:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
- **Git Path:** {dest_path.relative_to(WORKSPACE_ROOT)}
- **Git Commit:** {commit_hash}
- **Content Hash:** {content_hash}

---

*This file marks this module as published. Do not delete.*
*If you edit this module, republish using: `python publish_module.py {dest_path.name.upper()}`*
"""

    marker_path = source_path / "_GIT_PUBLISHED.md"
    marker_path.write_text(marker_content, encoding='utf-8')


def git_commit(dest_path: Path, module_code: str, module_title: str, is_first: bool) -> tuple[bool, str]:
    """Create git commit for the published module."""
    action = "Publish" if is_first else "Update"
    message = f"[courses] {action} {module_code}: {module_title}"

    try:
        # Add files
        subprocess.run(
            ["git", "add", str(dest_path)],
            cwd=WORKSPACE_ROOT,
            check=True,
            capture_output=True
        )

        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=WORKSPACE_ROOT,
            capture_output=True
        )

        if result.returncode == 0:
            return True, "No changes to commit"

        # Commit
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=WORKSPACE_ROOT,
            check=True,
            capture_output=True
        )

        # Get commit hash
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=WORKSPACE_ROOT,
            check=True,
            capture_output=True,
            text=True
        )
        commit_hash = result.stdout.strip()[:12]

        return True, commit_hash

    except subprocess.CalledProcessError as e:
        return False, f"Git error: {e.stderr.decode() if e.stderr else str(e)}"


def run_validation(source_path: Path) -> int:
    """Run validate_module.py on source path."""
    validate_script = Path(__file__).parent / "validate_module.py"

    if not validate_script.exists():
        log("validate_module.py not found, skipping validation", "WARN")
        return 0

    result = subprocess.run(
        [sys.executable, str(validate_script), str(source_path)],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    return result.returncode


def run_indexing(module_code: str) -> bool:
    """Run index_courses.py for the module."""
    index_script = Path(__file__).parent / "index_courses.py"

    if not index_script.exists():
        log("index_courses.py not found, skipping indexing", "WARN")
        return True

    result = subprocess.run(
        [sys.executable, str(index_script), module_code],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        log("Qdrant index updated", "OK")
        return True
    else:
        log(f"Indexing failed: {result.stderr}", "WARN")
        return False


def publish_module(module_code: str, dry_run: bool = False, force: bool = False) -> int:
    """
    Main publish workflow.

    Returns exit code.
    """
    module_code = module_code.upper()
    print(f"\n{'DRY RUN - ' if dry_run else ''}Publishing {module_code}\n")

    # Step 1: Discover source
    source_path = discover_source_path(module_code)
    if source_path is None:
        log(f"Cannot find source for {module_code}", "FAIL")
        log("Expected: COURSE_BASE_PATH/{year}/Course X/Module Y/.../ReWork/", "INFO")
        return 3

    log(f"Source: {source_path}", "OK" if not dry_run else "DRY")

    # Step 2: Get destination
    dest_path = get_dest_path(module_code)
    log(f"Destination: {dest_path.relative_to(WORKSPACE_ROOT)}", "OK" if not dry_run else "DRY")

    # Step 3: Validate source
    print("\n--- Validation ---")
    if dry_run:
        log("Would run validation on source", "DRY")
    else:
        exit_code = run_validation(source_path)
        if exit_code != 0:
            if force:
                log("Validation failed but proceeding due to --force", "WARN")
            else:
                log("Validation failed - cannot publish", "FAIL")
                log("Use --force to publish despite validation errors", "INFO")
                return 1

    # Step 4: Safety check
    print("\n--- Safety Check ---")
    is_first_publish = not dest_path.exists() or not any(dest_path.iterdir())
    safe, reason = check_publish_safety(source_path, dest_path)

    if safe:
        log(reason, "OK" if not dry_run else "DRY")
    else:
        log(reason, "WARN")
        if force:
            log("Proceeding due to --force flag", "WARN")
        elif dry_run:
            log("Would require --force to proceed", "DRY")
        else:
            log("Use --force to override", "INFO")
            return 2

    # Step 5: Copy files
    print("\n--- File Copy ---")
    copied = copy_module_files(source_path, dest_path, dry_run)
    for f in copied:
        log(f, "OK" if not dry_run else "DRY")

    if not copied:
        log("No files to copy", "WARN")
        return 0

    # Step 6: Read module metadata for commit message
    yaml_path = source_path / "module.yaml"
    module_title = module_code
    if yaml_path.exists():
        try:
            data = yaml.safe_load(yaml_path.read_text(encoding='utf-8'))
            module_title = data.get("title", module_code)
        except Exception:
            pass

    # Step 7: Git commit
    print("\n--- Git Commit ---")
    if dry_run:
        action = "Publish" if is_first_publish else "Update"
        log(f"Would commit: [courses] {action} {module_code}: {module_title}", "DRY")
        commit_hash = "dry-run"
    else:
        success, result = git_commit(dest_path, module_code, module_title, is_first_publish)
        if success:
            if result == "No changes to commit":
                log(result, "OK")
                commit_hash = "unchanged"
            else:
                log(f"Committed: {result}", "OK")
                commit_hash = result
        else:
            log(result, "FAIL")
            return 5

    # Step 8: Create marker file
    print("\n--- Marker File ---")
    if dry_run:
        log("Would create _GIT_PUBLISHED.md in source", "DRY")
    else:
        create_marker_file(source_path, dest_path, commit_hash)
        log("Created _GIT_PUBLISHED.md", "OK")

    # Step 9: Index to Qdrant
    print("\n--- Qdrant Index ---")
    if dry_run:
        log("Would update Qdrant course_content collection", "DRY")
    else:
        run_indexing(module_code)

    # Final summary
    print("\n" + "=" * 40)
    if dry_run:
        print("DRY RUN COMPLETE - No changes made")
        print("Run without --dry-run to execute")
    else:
        print(f"SUCCESS: {module_code} published")
        print(f"Git path: {dest_path.relative_to(WORKSPACE_ROOT)}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Publish course modules to the Git repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python publish_module.py C1M1 --dry-run    # Preview changes
  python publish_module.py C1M1              # Publish
  python publish_module.py C1M1 --force      # Force overwrite
        """
    )
    parser.add_argument("module", help="Module code (e.g., C1M1, C2M3)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without executing")
    parser.add_argument("--force", action="store_true",
                        help="Force publish even if destination modified")

    args = parser.parse_args()

    exit_code = publish_module(args.module, args.dry_run, args.force)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
