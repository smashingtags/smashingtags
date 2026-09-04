<!--
  Numbers in this file are generated. Do not hand-edit anything between the
  auto markers; .github/workflows/refresh-readme.yml rewrites them daily from
  the real source and commits only when one changes.

  A number nothing can check is worse than no number, so anything without a
  live source was removed rather than typed in and left to rot.
-->

# Michael Ashley

**I build my own tools, ship them, and run production on them.**

Fourteen products, zero investors. A NAS operating system, a deduplicating backup server, an iOS wellness app, a homelab dashboard. My own infrastructure runs on the operating system I wrote, which replaced the Proxmox and Unraid installs it grew out of.

Open to Senior IC through Director roles in product, program, or technical project management. Duluth, GA. Remote, hybrid, or open to relocation.

[mjashley.com](https://mjashley.com) · [LinkedIn](https://www.linkedin.com/in/mjashley/) · [michael@mjashley.com](mailto:michael@mjashley.com)

---

### Before this

Twelve years in technical program and product management. Software PM at Neptune Technology Group, running twelve Scrum teams on a .NET MAUI platform. Senior TPM at Healthcare Integrations across a SaaS portfolio. TPM at G5 TEK. PSM, CSPO, SA.

### Shipping now

**[Eight.ly OS](https://eight.ly)** — One Go binary that replaces Unraid, Portainer and Proxmox on any Linux box. Docker, KVM/QEMU virtual machines, LXC, SnapRAID and MergerFS storage, SMB and NFS shares, and a local AI assistant with forty-one tools that never leaves the machine. A one-click app catalogue, three editions, bootable ISO with the top one.

**[Eight.ly Backup Server](https://eight.ly)** — Deduplicating backup with content-defined chunking, AES-256-GCM encryption, retention policies and integrity verification. Free with every Eight.ly licence.

**[Eight.ly Agent](https://hub.docker.com/r/smashingtags/eightly-agent)** — Manage Docker on a machine you are not sitting at. Apache 2.0, signed binaries with provenance and an SBOM, six security reviews passed.

**[NeuroHelper](https://apps.apple.com/us/app/neurohelper-daily-wellness/id6760686710)** — A daily wellness companion for neurodivergent minds. Native SwiftUI, AI chat, breathing and grounding exercises, brain games, HealthKit. Live on the App Store. I am autistic and have ADHD; I built the thing I wanted to exist.

**[HomelabARR CE](https://github.com/imogenlabs/homelabarr-ce)** — Your homelab on one dashboard. <!--auto:ce-apps-->117<!--/auto--> self-hosted apps, one click each, three deploy modes. MIT licensed, [live demo](https://ce-demo.homelabarr.com), and an [iOS app](https://apps.apple.com/us/app/homelabarr-mobile/id6761244772).

**[Operator Kit](https://github.com/imogenlabs/operator-kit)** — Scaffolds an AI operator with identity, three-layer memory, scheduled jobs and multi-agent roles. On [npm](https://www.npmjs.com/package/@imogenlabs/operator-kit). The methodology behind it, [IPAC](https://github.com/smashingtags/ipac), is public.

**[CF Companion](https://github.com/smashingtags/cf-companion)** — Watches Docker events and creates Cloudflare DNS records when a Traefik-labelled container starts, so nobody edits DNS by hand.

### How I work

**A real SDLC, not a story about one.**<!--auto:jira--> 2,865 tracked issues across the active projects.<!--/auto--> Every change starts as a Jira ticket with acceptance criteria and story points, moves through a sprint, and stops at QA for a human. Architecture decisions, runbooks and process manuals live in Confluence and render at [docs.mjashley.com](https://docs.mjashley.com).

**AI does the typing. I own the architecture.** Scope, sequencing and acceptance criteria are mine. Agents implement inside a written contract that caps file size, forces decomposition and bars them from pushing to main. Every change is reviewed in a browser against the running dev environment before it ships, and a second model audits the result.

**Guardrails that have actually fired.** Automated gates block a merge on unformatted code, oversized files, undocumented work and unverified claims. I fire each new gate at a real broken case before I keep it, because a guard that cannot fire looks exactly like a guard with nothing to report.

**My own infrastructure, on my own operating system.** Two bare-metal production nodes running Eight.ly OS, which took over from the Proxmox cluster and Unraid array they replaced. Multi-node Docker, Traefik reverse proxy, Cloudflare zero-trust tunnels, self-hosted GitHub Actions runners, and multi-architecture builds for amd64 and arm64.

### By the numbers

Every badge below reads its own live source, so none of them can go stale. The two
that used to be typed in by hand are gone: a 99.9% uptime figure nothing could check,
and a services-in-production count that had drifted.

[![Contributions](https://github-readme-streak-stats.herokuapp.com/?user=smashingtags&theme=transparent&hide_border=true&date_format=M%20j%5B%2C%20Y%5D)](https://github.com/smashingtags)

[![Contribution graph](https://ghchart.rshah.org/409ba5/smashingtags)](https://github.com/smashingtags)

#### GitHub
![Followers](https://img.shields.io/github/followers/smashingtags?label=followers&style=for-the-badge&color=blue) ![Public repos](https://img.shields.io/badge/dynamic/json?label=public%20repos&query=%24.public_repos&url=https%3A%2F%2Fapi.github.com%2Fusers%2Fsmashingtags&style=for-the-badge&color=blueviolet) ![On GitHub since](https://img.shields.io/github/created-at/smashingtags/smashingtags?label=on%20github%20since&style=for-the-badge&color=success) ![Profile views](https://komarev.com/ghpvc/?username=smashingtags&label=profile%20views&color=orange&style=for-the-badge) ![Total stars](https://img.shields.io/github/stars/smashingtags?affiliations=OWNER&style=for-the-badge&label=total%20stars&color=yellow)

#### Shipped
![Products shipped](https://img.shields.io/badge/products%20shipped-14-success?style=for-the-badge) ![Investors](https://img.shields.io/badge/investors-0-lightgrey?style=for-the-badge) [![GHCR](https://img.shields.io/badge/GHCR-packages-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/smashingtags?tab=packages)

#### npm
[![npm version](https://img.shields.io/npm/v/@imogenlabs/operator-kit?style=for-the-badge&label=npm&color=red)](https://www.npmjs.com/package/@imogenlabs/operator-kit) [![npm downloads](https://img.shields.io/npm/dt/@imogenlabs/operator-kit?style=for-the-badge&label=npm%20downloads&color=crimson)](https://www.npmjs.com/package/@imogenlabs/operator-kit)

#### Docker Hub
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-smashingtags-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/smashingtags) [![Agent pulls](https://img.shields.io/docker/pulls/smashingtags/eightly-agent?style=for-the-badge&label=eightly-agent%20pulls&color=2496ED&logo=docker&logoColor=white)](https://hub.docker.com/r/smashingtags/eightly-agent) [![HomelabARR backend pulls](https://img.shields.io/docker/pulls/smashingtags/homelabarr-backend?style=for-the-badge&label=homelabarr-backend%20pulls&color=2496ED&logo=docker&logoColor=white)](https://hub.docker.com/r/smashingtags/homelabarr-backend) [![HomelabARR frontend pulls](https://img.shields.io/docker/pulls/smashingtags/homelabarr-frontend?style=for-the-badge&label=homelabarr-frontend%20pulls&color=2496ED&logo=docker&logoColor=white)](https://hub.docker.com/r/smashingtags/homelabarr-frontend)

#### Hugging Face
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-smashingtags-yellow?style=for-the-badge)](https://huggingface.co/smashingtags) [![HF model downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2Fsmashingtags%2Feightly-agent&query=%24.downloads&label=HF%20model%20downloads&style=for-the-badge&color=orange)](https://huggingface.co/smashingtags/eightly-agent)

### Stack

#### Front end
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

#### Backend
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

#### Mobile
![SwiftUI](https://img.shields.io/badge/SwiftUI-0066CC?style=for-the-badge&logo=swift&logoColor=white) ![React Native](https://img.shields.io/badge/React%20Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

#### Infrastructure
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![KVM/QEMU](https://img.shields.io/badge/KVM%2FQEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white) ![SnapRAID](https://img.shields.io/badge/SnapRAID-1F4E79?style=for-the-badge) ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=for-the-badge&logo=traefikproxy&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

#### Tooling
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white) ![Confluence](https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white) ![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)

---

<sub>Counts above are refreshed daily from their sources by <a href="https://github.com/smashingtags/smashingtags/actions/workflows/refresh-readme.yml">a workflow in this repo</a>. Last checked <!--auto:checked-->2026-09-03<!--/auto-->.</sub>
