#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CURRENT_SPRINT = ROOT / "project_management" / "Current_Sprint.md"
DEBT_DIR = ROOT / "project_management" / "debt_checks"
LOG_DIR = ROOT / "project_management" / "log"

DATE_RE = re.compile(r"^Date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
GATE_RE = re.compile(r"^Gate Result:\s*(PASS|FAIL)\s*$", re.MULTILINE)


class ValidationError(RuntimeError):
    pass


def _run_git(*args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise ValidationError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def _extract_sprint_number(text: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() == "## Sprint Number" and idx + 1 < len(lines):
            sprint = lines[idx + 1].strip()
            if sprint:
                return sprint
    raise ValidationError("Could not parse sprint number from Current_Sprint.md")


def _get_last_change_date(repo_path: Path) -> str:
    rel = repo_path.relative_to(ROOT).as_posix()
    date = _run_git("log", "-1", "--format=%cs", "--", rel)
    if not date:
        raise ValidationError(f"No git history found for {rel}")
    return date


def _parse_table_rows(report_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in report_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 6:
            continue
        marker_row = all(set(cell) <= {"-", ":"} for cell in cells)
        if marker_row:
            continue
        if cells[0].lower() == "id":
            continue
        rows.append(cells)
    return rows


def _validate_debt_report(sprint: str, sprint_change_date: str) -> None:
    report_path = DEBT_DIR / f"{sprint}.md"
    if not report_path.exists():
        raise ValidationError(
            f"Missing required debt preflight report: {report_path.relative_to(ROOT)}"
        )

    report_text = report_path.read_text(encoding="utf-8")
    date_match = DATE_RE.search(report_text)
    if not date_match:
        raise ValidationError(
            f"Debt report {report_path.relative_to(ROOT)} must include 'Date: YYYY-MM-DD'"
        )

    report_date = date_match.group(1)
    if report_date != sprint_change_date:
        raise ValidationError(
            "Debt report date does not match Current_Sprint.md last change date: "
            f"{report_date} != {sprint_change_date}"
        )

    gate_match = GATE_RE.search(report_text)
    if not gate_match:
        raise ValidationError(
            f"Debt report {report_path.relative_to(ROOT)} must include 'Gate Result: PASS|FAIL'"
        )

    if gate_match.group(1) != "PASS":
        raise ValidationError(f"Debt gate is not passing for {sprint} (Gate Result is FAIL)")

    rows = _parse_table_rows(report_text)
    if not rows:
        raise ValidationError(
            f"Debt report {report_path.relative_to(ROOT)} must include at least one findings row"
        )

    valid_severity = {"low", "medium", "high", "critical"}
    for row in rows:
        severity = row[1].strip().lower()
        owner = row[2].strip()
        target_sprint = row[3].strip()
        if severity not in valid_severity:
            raise ValidationError(
                f"Invalid severity '{row[1]}' in findings row: {' | '.join(row)}"
            )
        if not owner or owner.upper() == "TBD":
            raise ValidationError(f"Owner missing in findings row: {' | '.join(row)}")
        if not target_sprint or target_sprint.upper() == "TBD":
            raise ValidationError(
                f"Target Sprint missing in findings row: {' | '.join(row)}"
            )


def _validate_same_day_log_entry(sprint: str, sprint_change_date: str) -> None:
    log_path = LOG_DIR / f"story_management_{sprint_change_date}.log"
    if not log_path.exists():
        raise ValidationError(
            "Missing same-day log file for sprint change: "
            f"{log_path.relative_to(ROOT)}"
        )

    found = False
    for raw_line in log_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"Invalid JSON in {log_path.name}: {exc}") from exc

        entity_id = str(entry.get("entity_id", ""))
        summary = str(entry.get("summary", "")).lower()
        if sprint in entity_id and "debt" in summary:
            found = True
            break

    if not found:
        raise ValidationError(
            "Expected at least one same-day audit entry mentioning debt for "
            f"{sprint} in {log_path.relative_to(ROOT)}"
        )


def main() -> int:
    if not CURRENT_SPRINT.exists():
        raise ValidationError(f"Missing {CURRENT_SPRINT.relative_to(ROOT)}")

    sprint_text = CURRENT_SPRINT.read_text(encoding="utf-8")
    sprint = _extract_sprint_number(sprint_text)
    sprint_change_date = _get_last_change_date(CURRENT_SPRINT)

    _validate_debt_report(sprint, sprint_change_date)
    _validate_same_day_log_entry(sprint, sprint_change_date)

    print(
        "Sprint governance check passed:",
        f"sprint={sprint}",
        f"change_date={sprint_change_date}",
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
