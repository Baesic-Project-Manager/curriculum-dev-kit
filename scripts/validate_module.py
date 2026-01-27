#!/usr/bin/env python3
"""
Module Validation Script

Validates course modules before publishing. Checks schema conformance,
file existence, HTML patterns, and size limits.

Exit codes:
  0 = Valid - ready for publish
  1 = Schema validation failed
  2 = HTML validation failed
  3 = File not found

Usage:
  python validate_module.py "/path/to/module"
  python validate_module.py "/path/to/module" --schema-only
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

# =============================================================================
# CONFIGURATION
# =============================================================================

# Schema version this validator supports
SUPPORTED_SCHEMA_VERSION = "1.0"

# Required fields in module.yaml
REQUIRED_FIELDS = ["schema_version", "code", "title", "status", "score"]
REQUIRED_DELIVERABLES = ["presentation", "speaker_notes"]

# Valid status values
VALID_STATUSES = ["draft", "in_progress", "review", "published", "archived"]

# Size limits (bytes)
MAX_FILE_SIZE = 500 * 1024  # 500KB per file
MAX_MODULE_SIZE = 1024 * 1024  # 1MB total

# HTML validation patterns (banned)
BANNED_PATTERNS = [
    (r'<img\s+[^>]*src\s*=', "External/embedded image"),
    (r'<link[^>]*href\s*=', "External CSS link"),
    (r'<script[^>]*src\s*=', "External JavaScript"),
    (r'<iframe\s+[^>]*src\s*=', "Iframe source"),
    (r'<image\s+[^>]*(href|xlink:href)\s*=', "SVG image reference"),
    (r'@import\s+["\']?https?://', "CSS @import external URL"),
    (r'@import\s+url\s*\(', "CSS @import url()"),
    (r'data:image/(jpeg|png|gif|webp)', "Base64 raster image"),
]


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def log(message: str, status: str = "INFO") -> None:
    """Print formatted log message."""
    symbols = {
        "OK": "[OK]",
        "FAIL": "[FAIL]",
        "WARN": "[WARN]",
        "INFO": "->",
    }
    symbol = symbols.get(status, "->")
    print(f"{symbol} {message}")


def validate_schema(module_path: Path) -> tuple[bool, dict | None, list[str]]:
    """Validate module.yaml exists and conforms to schema."""
    errors = []
    yaml_path = module_path / "module.yaml"

    if not yaml_path.exists():
        errors.append("module.yaml not found")
        return False, None, errors

    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(f"YAML parse error: {e}")
        return False, None, errors

    if not isinstance(data, dict):
        errors.append("module.yaml must be a YAML mapping")
        return False, None, errors

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Validate schema version
    if data.get("schema_version") != SUPPORTED_SCHEMA_VERSION:
        errors.append(
            f"Unsupported schema_version: {data.get('schema_version')} "
            f"(expected {SUPPORTED_SCHEMA_VERSION})"
        )

    # Validate status
    if data.get("status") not in VALID_STATUSES:
        errors.append(
            f"Invalid status: {data.get('status')} (valid: {VALID_STATUSES})"
        )

    # Validate score
    score = data.get("score")
    if score is not None and not (isinstance(score, int) and 0 <= score <= 4):
        errors.append(f"Invalid score: {score} (must be 0-4)")

    # Validate deliverables
    deliverables = data.get("deliverables", {})
    if not isinstance(deliverables, dict):
        errors.append("deliverables must be a mapping")
    else:
        for req in REQUIRED_DELIVERABLES:
            if req not in deliverables or not deliverables[req]:
                errors.append(f"Missing required deliverable: {req}")

    return len(errors) == 0, data, errors


def validate_code_matches_path(module_path: Path, code: str) -> tuple[bool, list[str]]:
    """Validate that module code matches folder path pattern."""
    errors = []

    # Extract expected pattern from code (e.g., C1M1 -> c1, m1)
    match = re.match(r'C(\d+)M(\d+)', code.upper())
    if not match:
        errors.append(f"Invalid module code format: {code} (expected C#M#)")
        return False, errors

    course_num = match.group(1)
    module_num = match.group(2)

    # Check path contains expected folders
    path_str = str(module_path).lower().replace('\\', '/')

    # Support various naming conventions
    course_patterns = [f"c{course_num}", f"course {course_num}", f"course{course_num}"]
    module_patterns = [f"m{module_num}", f"module {module_num}", f"module{module_num}"]

    course_ok = any(p in path_str for p in course_patterns)
    module_ok = any(p in path_str for p in module_patterns)

    if not course_ok:
        errors.append(f"Code {code} expects path containing course {course_num}")
    if not module_ok:
        errors.append(f"Code {code} expects path containing module {module_num}")

    return len(errors) == 0, errors


def validate_deliverables_exist(module_path: Path, deliverables: dict) -> tuple[bool, list[str]]:
    """Check that all specified deliverable files exist."""
    errors = []

    for key, filename in deliverables.items():
        if filename:
            if isinstance(filename, list):
                for f in filename:
                    if not (module_path / f).exists():
                        errors.append(f"Deliverable not found: {key}/{f}")
            else:
                if not (module_path / filename).exists():
                    errors.append(f"Deliverable not found: {key} -> {filename}")

    return len(errors) == 0, errors


def validate_html_content(module_path: Path) -> tuple[bool, list[str]]:
    """Scan HTML files for banned patterns."""
    errors = []
    html_files = list(module_path.glob("*.html"))

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding='utf-8')
        except Exception as e:
            errors.append(f"Cannot read {html_file.name}: {e}")
            continue

        for pattern, description in BANNED_PATTERNS:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                for match in matches[:3]:  # Show first 3 matches
                    line_num = content[:match.start()].count('\n') + 1
                    snippet = content[match.start():match.start() + 60].replace('\n', ' ')
                    errors.append(f"{html_file.name} line {line_num}: {description}")
                    errors.append(f"  Found: {snippet}...")

    return len(errors) == 0, errors


def validate_size(module_path: Path) -> tuple[bool, list[str], int]:
    """Check file and total module size limits."""
    errors = []
    total_size = 0

    for file_path in module_path.rglob("*"):
        if file_path.is_file():
            size = file_path.stat().st_size
            total_size += size

            if size > MAX_FILE_SIZE:
                errors.append(
                    f"File too large: {file_path.name} "
                    f"({size // 1024}KB > {MAX_FILE_SIZE // 1024}KB)"
                )

    if total_size > MAX_MODULE_SIZE:
        errors.append(
            f"Module too large: {total_size // 1024}KB > "
            f"{MAX_MODULE_SIZE // 1024}KB limit"
        )

    return len(errors) == 0, errors, total_size


# =============================================================================
# MAIN VALIDATION
# =============================================================================

def validate_module(module_path: Path, schema_only: bool = False) -> int:
    """
    Full validation of a module.

    Returns exit code (0 = valid, 1 = schema, 2 = HTML, 3 = file)
    """
    print(f"\nValidating: {module_path}\n")

    all_errors = []
    exit_code = 0

    # Step 1: Schema validation
    valid, data, errors = validate_schema(module_path)
    if valid:
        log("module.yaml exists and parses", "OK")
        log(f"Schema valid (v{SUPPORTED_SCHEMA_VERSION})", "OK")
    else:
        for err in errors:
            log(err, "FAIL")
        all_errors.extend(errors)
        exit_code = 1

    if exit_code != 0 or data is None:
        print(f"\nRESULT: INVALID - Schema validation failed")
        return 1

    # Step 2: Code matches path
    valid, errors = validate_code_matches_path(module_path, data.get("code", ""))
    if valid:
        log(f"Code {data.get('code')} matches path", "OK")
    else:
        for err in errors:
            log(err, "FAIL")
        all_errors.extend(errors)
        exit_code = 1

    # Step 3: Deliverables exist
    deliverables = data.get("deliverables", {})
    valid, errors = validate_deliverables_exist(module_path, deliverables)
    if valid:
        log("Deliverables exist", "OK")
    else:
        for err in errors:
            log(err, "FAIL")
        all_errors.extend(errors)
        exit_code = max(exit_code, 3)

    if schema_only:
        if exit_code == 0:
            print(f"\nRESULT: VALID (schema-only check)")
        else:
            print(f"\nRESULT: INVALID - Fix {len(all_errors)} issue(s)")
        return exit_code

    # Step 4: HTML validation
    valid, errors = validate_html_content(module_path)
    if valid:
        log("HTML clean (no banned patterns)", "OK")
    else:
        log("HTML validation failed:", "FAIL")
        for err in errors:
            print(f"  {err}")
        all_errors.extend(errors)
        exit_code = max(exit_code, 2)

    # Step 5: Size check
    valid, errors, total_size = validate_size(module_path)
    if valid:
        log(f"Size: {total_size // 1024}KB (< {MAX_MODULE_SIZE // 1024}KB limit)", "OK")
    else:
        for err in errors:
            log(err, "FAIL")
        all_errors.extend(errors)
        exit_code = max(exit_code, 1)

    # Final result
    print()
    if exit_code == 0:
        print("RESULT: VALID - Ready for publish")
    else:
        print(f"RESULT: INVALID - Fix {len(all_errors)} issue(s) before publish")

    return exit_code


# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Validate a course module before publishing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit codes:
  0 = Valid - ready for publish
  1 = Schema validation failed
  2 = HTML validation failed
  3 = File not found

Examples:
  python validate_module.py "/path/to/module"
  python validate_module.py "/path/to/module" --schema-only
        """
    )
    parser.add_argument("path", help="Path to module folder")
    parser.add_argument("--schema-only", action="store_true",
                        help="Only validate schema, skip HTML checks")

    args = parser.parse_args()

    module_path = Path(args.path)
    if not module_path.exists():
        print(f"Error: Path not found: {module_path}")
        sys.exit(3)

    if not module_path.is_dir():
        print(f"Error: Path is not a directory: {module_path}")
        sys.exit(3)

    exit_code = validate_module(module_path, args.schema_only)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
