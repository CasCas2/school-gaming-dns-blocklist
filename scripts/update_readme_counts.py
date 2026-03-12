from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

COUNT_MAP = {
    "mega-gaming-blocklist.txt": "blocked hostnames",
    "school-gaming-lite.txt": "blocked hostnames in the lite list",
    "classroom-only-blocklist.txt": "blocked hostnames in the classroom-only list",
    "cheat-tools-blocklist.txt": "blocked hostnames in the cheat/tools list",
    "vpn-software-blocklist.txt": "blocked hostnames in the VPN software list",
    "browser-download-blocklist.txt": "blocked hostnames in the browser-download list",
    "general-software-download-blocklist.txt": "blocked hostnames in the general software download list",
    "aggressive-school-bypass-blocklist.txt": "additional aggressive-profile hostnames",
}


def count_hosts(path: Path) -> int:
    if not path.is_file():
        raise SystemExit(f"Blocklist file not found: {path}")
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("0.0.0.0 "))


def expected_counts() -> dict[str, int]:
    return {label: count_hosts(ROOT / filename) for filename, label in COUNT_MAP.items()}


def rewrite_readme(text: str, counts: dict[str, int]) -> str:
    updated = text
    for label, count in counts.items():
        pattern = rf"^- \d+ {re.escape(label)}$"
        replacement = f"- {count} {label}"
        updated, num = re.subn(pattern, replacement, updated, flags=re.MULTILINE)
        if num != 1:
            raise SystemExit(f"Could not uniquely update README line for: {label}")
    return updated


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Rewrite README.md with current counts")
    parser.add_argument("--check", action="store_true", help="Fail if README.md counts do not match current files")
    args = parser.parse_args()

    if not args.write and not args.check:
        parser.error("Specify --write or --check")

    counts = expected_counts()
    original = README.read_text(encoding="utf-8")
    updated = rewrite_readme(original, counts)

    if args.write:
        if updated != original:
            README.write_text(updated, encoding="utf-8")
            print("Updated README.md counts")
        else:
            print("README.md counts already up to date")
        return 0

    if updated != original:
        print("README.md count lines are out of date. Run: python scripts/update_readme_counts.py --write")
        return 1

    print("README.md counts are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
