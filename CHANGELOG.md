# Changelog

All notable repository changes should be summarized here.

## Unreleased

- Removed `github.io` and `www.github.io` from `aggressive-school-bypass-blocklist.txt` — GitHub is used for legitimate school work; use targeted entries in `classroom-only-blocklist.txt` instead.
- Updated README aggressive profile section to reflect the removal.

## 2026-03-12

- Added a `LICENSE` file using `CC0-1.0`.
- Reduced false-positive risk in the browser download profile by removing broad Mozilla root domains.
- Added more conservative browser-game and `.io` targets to the mega gaming list.
- Documented exact-hostname limitations in the README.
- Added an informational cross-file duplicate warning to CI.
- Added `CONTRIBUTING.md` with contribution rules and local validation guidance.
- Added a pull request template for domain additions and list maintenance.
- Added `scripts/update_readme_counts.py` and CI enforcement for README count accuracy.
- Added `playtoria.com` to the mega gaming blocklist.
- Added `general-software-download-blocklist.txt` for Roblox and common game launcher download hosts.
- Expanded the cheat/tools blocklist with additional low-maintenance domains.
- Added Cloudflare WARP and Arc Browser coverage.
- Improved README raw links and profile guidance.
- Fixed false-positive: replaced `one.one.one.one` in VPN list with correct Cloudflare WARP domains.
- Added missing `www` variants for several browser game portals in the mega gaming list.
- Improved CI hostname validation regex to reject invalid hostname formats.
- Clarified wildcard limitation in README and aggressive bypass list.
- Fixed `wave.gg` category comment in cheat/tools list.
- Added `www.geo-fs.com` and context comment to mega gaming list.
