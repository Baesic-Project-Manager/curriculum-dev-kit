#!/usr/bin/env python3
"""
Validate a presentation brief for completeness.

This script checks that a brief document contains all required sections
and follows the Teaching at Scale methodology standards.

Usage:
    python validate_brief.py path/to/brief.md
    python validate_brief.py path/to/brief.md --strict
    python validate_brief.py path/to/brief.md --json

Exit codes:
    0 - Validation passed
    1 - Validation failed (missing required elements)
    2 - File not found or read error
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import NamedTuple


class ValidationResult(NamedTuple):
    """Result of a single validation check."""
    passed: bool
    message: str
    severity: str  # 'error', 'warning', 'info'


class BriefValidator:
    """Validates presentation brief documents."""

    # Required sections that must be present
    REQUIRED_SECTIONS = [
        "Module Identification",
        "Timing Calculations",
        "Priority Rankings",
        "Case Study",
        "Voice and Tone",
        "Brief Status",
    ]

    # Required fields with their regex patterns
    REQUIRED_FIELDS = {
        "Course Title": r"Course\s*Title\s*:",
        "Module Number": r"Module\s*(Number|Code|ID)\s*:",
        "Target Audience": r"Target\s*Audience\s*:",
        "Delivery Format": r"Delivery\s*Format\s*:",
        "Slide Budget": r"(\d+)\s*slides?\s*(maximum|budget|total)",
        "Brief Locked": r"Brief\s*Status\s*:.*LOCKED",
    }

    # Warning-level checks (nice to have)
    RECOMMENDED_SECTIONS = [
        "Bias Check",
        "Mandatory Elements",
        "Voice.*AVOID",
    ]

    def __init__(self, filepath: str, strict: bool = False):
        self.filepath = Path(filepath)
        self.strict = strict
        self.content = ""
        self.results: list[ValidationResult] = []

    def load_file(self) -> bool:
        """Load the brief file content."""
        try:
            self.content = self.filepath.read_text(encoding='utf-8')
            return True
        except FileNotFoundError:
            self.results.append(ValidationResult(
                passed=False,
                message=f"File not found: {self.filepath}",
                severity='error'
            ))
            return False
        except Exception as e:
            self.results.append(ValidationResult(
                passed=False,
                message=f"Error reading file: {e}",
                severity='error'
            ))
            return False

    def check_required_sections(self) -> None:
        """Check that all required sections are present."""
        for section in self.REQUIRED_SECTIONS:
            pattern = re.compile(rf"##?\s*{re.escape(section)}", re.IGNORECASE)
            if pattern.search(self.content):
                self.results.append(ValidationResult(
                    passed=True,
                    message=f"Section found: {section}",
                    severity='info'
                ))
            else:
                self.results.append(ValidationResult(
                    passed=False,
                    message=f"Missing required section: {section}",
                    severity='error'
                ))

    def check_required_fields(self) -> None:
        """Check that all required fields are present."""
        for field_name, pattern in self.REQUIRED_FIELDS.items():
            if re.search(pattern, self.content, re.IGNORECASE):
                self.results.append(ValidationResult(
                    passed=True,
                    message=f"Field found: {field_name}",
                    severity='info'
                ))
            else:
                self.results.append(ValidationResult(
                    passed=False,
                    message=f"Missing or incomplete field: {field_name}",
                    severity='error'
                ))

    def check_recommended_sections(self) -> None:
        """Check for recommended (but not required) sections."""
        for section in self.RECOMMENDED_SECTIONS:
            pattern = re.compile(section, re.IGNORECASE)
            if pattern.search(self.content):
                self.results.append(ValidationResult(
                    passed=True,
                    message=f"Recommended section found: {section}",
                    severity='info'
                ))
            else:
                severity = 'error' if self.strict else 'warning'
                self.results.append(ValidationResult(
                    passed=not self.strict,
                    message=f"Missing recommended section: {section}",
                    severity=severity
                ))

    def check_timing_math(self) -> None:
        """Verify timing calculations are internally consistent."""
        # Look for timing calculation block
        timing_section = re.search(
            r"Timing\s*Calculations.*?slides?\s*(maximum|budget)",
            self.content,
            re.IGNORECASE | re.DOTALL
        )

        if not timing_section:
            return  # Already flagged by required fields check

        timing_text = timing_section.group(0)

        # Extract numbers from timing calculation
        total_match = re.search(r"Total\s*session.*?(\d+)\s*min", timing_text, re.IGNORECASE)
        budget_match = re.search(r"(\d+)\s*slides?\s*(maximum|budget)", timing_text, re.IGNORECASE)

        if total_match and budget_match:
            total_time = int(total_match.group(1))
            slide_budget = int(budget_match.group(1))

            # Check if math is roughly correct (2-3 min per slide)
            min_expected = total_time // 4  # Allows for activities/discussion
            max_expected = total_time // 1.5

            if slide_budget < min_expected:
                self.results.append(ValidationResult(
                    passed=True,
                    message=f"Slide budget ({slide_budget}) is conservative for {total_time} min session",
                    severity='info'
                ))
            elif slide_budget > max_expected:
                self.results.append(ValidationResult(
                    passed=False,
                    message=f"Slide budget ({slide_budget}) may be too high for {total_time} min session",
                    severity='warning'
                ))
            else:
                self.results.append(ValidationResult(
                    passed=True,
                    message=f"Timing math looks reasonable: {slide_budget} slides for {total_time} min",
                    severity='info'
                ))

    def check_priority_allocations(self) -> None:
        """Check that priority allocations sum correctly."""
        # Look for slide allocation table
        allocation_pattern = re.compile(
            r"\|\s*(\w+[\w\s]*)\s*\|\s*(HIGH|MEDIUM|LOW|Required|-)\s*\|\s*(\d+)\s*\|",
            re.IGNORECASE
        )

        allocations = allocation_pattern.findall(self.content)

        if allocations:
            total_allocated = sum(int(a[2]) for a in allocations)

            # Get stated budget
            budget_match = re.search(r"(\d+)\s*slides?\s*(maximum|budget)", self.content, re.IGNORECASE)

            if budget_match:
                budget = int(budget_match.group(1))

                if total_allocated > budget:
                    self.results.append(ValidationResult(
                        passed=False,
                        message=f"Allocation ({total_allocated}) exceeds budget ({budget})",
                        severity='error'
                    ))
                elif total_allocated < budget - 5:
                    self.results.append(ValidationResult(
                        passed=True,
                        message=f"Allocation ({total_allocated}) under budget ({budget}) - {budget - total_allocated} slides unallocated",
                        severity='warning'
                    ))
                else:
                    self.results.append(ValidationResult(
                        passed=True,
                        message=f"Allocation ({total_allocated}) matches budget ({budget})",
                        severity='info'
                    ))

    def check_version_header(self) -> None:
        """Check for template version header."""
        version_pattern = re.compile(r"<!--\s*\n?\s*Template:", re.IGNORECASE)

        if version_pattern.search(self.content):
            self.results.append(ValidationResult(
                passed=True,
                message="Version header found",
                severity='info'
            ))
        else:
            self.results.append(ValidationResult(
                passed=not self.strict,
                message="Missing version header (template may be v1.x)",
                severity='warning' if not self.strict else 'error'
            ))

    def validate(self) -> bool:
        """Run all validation checks."""
        if not self.load_file():
            return False

        self.check_required_sections()
        self.check_required_fields()
        self.check_recommended_sections()
        self.check_timing_math()
        self.check_priority_allocations()
        self.check_version_header()

        # Return True if no errors
        errors = [r for r in self.results if r.severity == 'error' and not r.passed]
        return len(errors) == 0

    def get_summary(self) -> dict:
        """Get validation summary as dict."""
        errors = [r for r in self.results if r.severity == 'error' and not r.passed]
        warnings = [r for r in self.results if r.severity == 'warning' and not r.passed]
        passed = [r for r in self.results if r.passed]

        return {
            'file': str(self.filepath),
            'valid': len(errors) == 0,
            'error_count': len(errors),
            'warning_count': len(warnings),
            'passed_count': len(passed),
            'errors': [r.message for r in errors],
            'warnings': [r.message for r in warnings],
        }

    def print_results(self) -> None:
        """Print validation results to console."""
        print(f"\nValidating: {self.filepath}\n")
        print("-" * 50)

        errors = []
        warnings = []
        passed = []

        for result in self.results:
            if result.severity == 'error' and not result.passed:
                errors.append(result)
            elif result.severity == 'warning' and not result.passed:
                warnings.append(result)
            elif result.passed:
                passed.append(result)

        if errors:
            print("\nERRORS:")
            for r in errors:
                print(f"  [X] {r.message}")

        if warnings:
            print("\nWARNINGS:")
            for r in warnings:
                print(f"  [!] {r.message}")

        print(f"\n{'-' * 50}")
        print(f"Errors: {len(errors)} | Warnings: {len(warnings)} | Passed: {len(passed)}")

        if len(errors) == 0:
            print("\nBrief validation PASSED!")
        else:
            print("\nBrief validation FAILED - fix errors before proceeding")


def main():
    parser = argparse.ArgumentParser(
        description='Validate a presentation brief for completeness.'
    )
    parser.add_argument(
        'filepath',
        help='Path to the brief markdown file'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )

    args = parser.parse_args()

    validator = BriefValidator(args.filepath, strict=args.strict)
    is_valid = validator.validate()

    if args.json:
        print(json.dumps(validator.get_summary(), indent=2))
    else:
        validator.print_results()

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
