# MEGA School Gaming Blocklist

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

## Included file

- [`mega-gaming-blocklist.txt`](mega-gaming-blocklist.txt) - main list in `hosts` format

## Format

Each entry uses standard `hosts` syntax:

```txt
0.0.0.0 example.com
```

## Quick setup

### AdGuard Home

Add the raw file URL from this repository as a custom filter.

### Pi-hole

Add the list under `Group Management -> Adlists`, then run a gravity update.

### pfBlockerNG

Use the list as an external DNSBL source in `hosts` format.

### Technitium / NextDNS

Import or mirror the list through the provider's custom blocklist feature.

## Scope notes

- Some domains in this category change often. Mirrors appear and disappear regularly.
- The list prefers direct game portals and mirror domains over giant shared platforms.
- A few sites may overlap with legitimate educational use. Review locally before broad deployment.

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

## Current status

- Maintained in `hosts` format
- 131 blocked hostnames
- Reviewed and expanded on March 11, 2026

## Contributions

Pull requests are useful when they include:

- the domain
- a short reason for inclusion
- whether it is an official site, mirror, or GitHub Pages clone
- notes on false-positive risk
