# Contributing

This repository accepts focused additions that improve school-oriented DNS blocking for gaming, bypass, cheat, VPN, browser-download, and related software-install scenarios.

## Before you open a PR

- Make sure the domain is a direct gaming, bypass, cheat, VPN, browser-download, or related software-install destination.
- Avoid broad platforms, generic CDNs, and major services unless false-positive risk is clearly acceptable.
- Add common `www` variants when they resolve separately and are part of the same user flow.
- Update `# Last reviewed:` in every blocklist file you modify.
- If list counts change, update `README.md` or run `python scripts/update_readme_counts.py --write`.

## PR expectations

Include:

- the domain you are adding or removing
- a short reason for the change
- whether it is an official site, mirror, download host, or bypass host
- any known false-positive risk

## Local checks

Before submitting:

- run the existing validation workflow logic locally if possible
- run `python scripts/update_readme_counts.py --check`
- confirm there are no duplicate domains in the file you changed

## Scope guidance

Good candidates:

- official game portals
- unblocked game mirrors
- classroom bypass mirrors
- cheat or exploit portals
- VPN client download portals
- browser or launcher download hosts

Usually avoid:

- generic shared hosting unless it belongs in the aggressive profile
- generic download portals with heavy collateral risk
- domains with unclear or weak ties to the list purpose
