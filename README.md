# MEGA School Gaming Blocklist

[![Validate Blocklists](https://github.com/CasCas2/school-gaming-dns-blocklist/actions/workflows/validate-blocklists.yml/badge.svg)](https://github.com/CasCas2/school-gaming-dns-blocklist/actions/workflows/validate-blocklists.yml)
[![Repo](https://img.shields.io/badge/GitHub-CasCas2%2Fschool--gaming--dns--blocklist-black)](https://github.com/CasCas2/school-gaming-dns-blocklist)

A focused DNS blocklist for schools that want to reduce access to browser games, unblocked game mirrors, `.io` games, soundboard distractions, and browser-based cloud gaming services.

The list is intentionally kept in simple `hosts` format so it can be dropped into most DNS filtering systems without conversion.

## Use cases

This repository is built for:

- school networks
- managed student laptops and Chromebooks
- after-school clubs or shared lab environments
- home filtering where browser gaming is the primary concern

## Compatible with

- AdGuard Home
- Pi-hole
- pfSense / pfBlockerNG
- Technitium DNS Server
- NextDNS
- any resolver or firewall that accepts `hosts`-style blocklists

## What this list targets

- major browser game portals
- `.io` game domains
- "unblocked games" brands and mirrors
- classroom-style mirror domains
- GitHub Pages mirrors commonly used to evade school filters
- browser cloud-gaming entry points
- soundboard sites often used as classroom distractions

## What this list does not try to do

- replace a full parental-control or web-filtering product
- block every gaming CDN on the internet
- block every page under broad platforms such as GitHub or Xbox
- inspect encrypted traffic

That tradeoff is intentional. The list aims to stay practical and avoid blocking large general-purpose services unless they are overwhelmingly used as direct gaming destinations.

## Included files

- [`mega-gaming-blocklist.txt`](mega-gaming-blocklist.txt) - main list in `hosts` format
- [`school-gaming-lite.txt`](school-gaming-lite.txt) - smaller starter list for the most common school gaming domains
- [`classroom-only-blocklist.txt`](classroom-only-blocklist.txt) - focused list for classroom mirrors, GitHub Pages mirrors, and unblocked game brands
- [`cheat-tools-blocklist.txt`](cheat-tools-blocklist.txt) - optional list for cheat engines, auto clickers, macros, and exploit tools
- [`vpn-software-blocklist.txt`](vpn-software-blocklist.txt) - optional list for blocking common VPN software and download portals
- [`browser-download-blocklist.txt`](browser-download-blocklist.txt) - optional list for blocking alternative browser downloads while leaving Edge and Chrome available
- [`general-software-download-blocklist.txt`](general-software-download-blocklist.txt) - optional list for blocking selected consumer software download domains such as Roblox and common game launchers
- [`aggressive-school-bypass-blocklist.txt`](aggressive-school-bypass-blocklist.txt) - optional high-impact list for blocking common mirror-hosting platforms

## Raw URLs

Use these raw GitHub URLs directly in AdGuard Home, Pi-hole, or similar tools:

- [`mega-gaming-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/mega-gaming-blocklist.txt)
- [`school-gaming-lite.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/school-gaming-lite.txt)
- [`classroom-only-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/classroom-only-blocklist.txt)
- [`cheat-tools-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/cheat-tools-blocklist.txt)
- [`vpn-software-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/vpn-software-blocklist.txt)
- [`browser-download-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/browser-download-blocklist.txt)
- [`general-software-download-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/general-software-download-blocklist.txt)
- [`aggressive-school-bypass-blocklist.txt`](https://raw.githubusercontent.com/CasCas2/school-gaming-dns-blocklist/main/aggressive-school-bypass-blocklist.txt)

## Format

Each entry uses standard `hosts` syntax:

```txt
0.0.0.0 example.com
```

The `hosts` format blocks exact hostnames only. It does not automatically block every subdomain unless those hosts are listed explicitly.

## Quick setup

### AdGuard Home

Add one of the raw file URLs from this repository as a custom filter.

### Pi-hole

Add the desired raw URL under `Group Management -> Adlists`, then run a gravity update.

### pfBlockerNG

Use the list as an external DNSBL source in `hosts` format.

### Technitium / NextDNS

Import or mirror the list through the provider's custom blocklist feature.

## Recommended profiles

- `school-gaming-lite.txt` for a conservative starter deployment
- `mega-gaming-blocklist.txt` for the default broad school gaming profile
- `classroom-only-blocklist.txt` when classroom mirrors and unblocked brands are the main problem
- `cheat-tools-blocklist.txt` when you also want to block auto clickers, macro tools, and cheat portals on managed devices
- `vpn-software-blocklist.txt` when you want to reduce access to VPN client downloads and setup portals
- `browser-download-blocklist.txt` when you want to allow Edge and Chrome but reduce downloads of other browsers
- `general-software-download-blocklist.txt` when you want a small optional profile for consumer software downloads such as Roblox and common game launchers
- `aggressive-school-bypass-blocklist.txt` only when students abuse generic hosting platforms for bypass

## Scope notes

- Some domains in this category change often. Mirrors appear and disappear regularly.
- The list prefers direct game portals and mirror domains over giant shared platforms.
- A few sites may overlap with legitimate educational use. Review locally before broad deployment.
- Some domains intentionally appear in more than one profile so each list can still be deployed on its own.

## Known limitations

- `hosts` format blocks exact domains, not wildcard subdomains — for example, `0.0.0.0 example.io` does **not** block `user.example.io`; each subdomain must be listed separately
- new mirrors appear constantly, so no static list is complete
- some educational content may share domains with entertainment content
- DNS blocking alone does not stop all app installs, DoH bypasses, or already installed software

## Optional aggressive profile

If students frequently bypass filtering through static-hosting platforms, use the separate aggressive list:

- [`aggressive-school-bypass-blocklist.txt`](aggressive-school-bypass-blocklist.txt)

It blocks broad hosting platforms commonly used for mirrors, including:

- `pages.dev`
- `vercel.app`
- `netlify.app`
- `glitch.me`

Note: `github.io` has been removed from this list because GitHub is used for legitimate school work. Use the targeted GitHub Pages mirror entries in [`classroom-only-blocklist.txt`](classroom-only-blocklist.txt) instead.

This is effective, but it can also break legitimate student projects, developer documentation, and class content hosted on those platforms.

## Maintenance approach

The list is organized by category with comments so it stays easy to review and extend.

When adding new entries, prefer:

- direct gaming domains
- official mirror domains
- common `www` variants when they resolve separately
- narrowly targeted hosts over broad parent domains

Avoid adding:

- generic CDNs unless they are gaming-only
- major developer platforms unless gaming use clearly outweighs false positives
- one-off scam/spam domains that are unlikely to persist

## Suggested companion controls

This blocklist works best together with:

- SafeSearch / YouTube Restricted Mode
- browser extension restrictions
- Chromebook or MDM app allowlisting
- firewall rules for VPN / proxy evasion domains
- DNS logging and periodic review of misses

If device abuse is also a problem, combine the main gaming list with the cheat/tools profile to reduce access to:

- auto clickers
- macro tools
- cheat engines
- exploit-download portals

If VPN evasion is common, also combine it with the VPN software profile. That helps block:

- VPN client download pages
- manual VPN setup portals
- popular consumer VPN brands

If students install alternate browsers to bypass policy, combine it with the browser download profile. That helps block:

- Firefox and Firefox forks
- Opera and Brave
- privacy-focused browsers such as Tor Browser
- smaller Chromium-based alternatives

If students install non-browser software from gaming-related vendors, combine it with the general software download profile. That helps block:

- Roblox download hosts
- major PC game launcher download portals such as Steam, Epic Games, Battle.net, EA, Ubisoft Connect, GOG, and Riot, including key Steam content hosts

## Current status

- Maintained in `hosts` format
- 163 blocked hostnames
- 43 blocked hostnames in the lite list
- 41 blocked hostnames in the classroom-only list
- 55 blocked hostnames in the cheat/tools list
- 69 blocked hostnames in the VPN software list
- 34 blocked hostnames in the browser-download list
- 26 blocked hostnames in the general software download list
- 8 additional aggressive-profile hostnames

## Contributions

Pull requests are useful when they include:

- the domain
- a short reason for inclusion
- whether it is an official site, mirror, or GitHub Pages clone
- notes on false-positive risk
