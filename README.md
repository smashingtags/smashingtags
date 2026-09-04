<!--
  Numbers in this file are generated. Do not hand-edit anything between
  <!--auto:NAME--> and <!--/auto--> markers; .github/workflows/refresh-readme.yml
  rewrites them daily from the real source and commits only when one changes.

  A number nothing can check is worse than no number, so anything without a live
  source was removed rather than typed in and left to rot.
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

**A real SDLC, not a story about one.**<!--auto:jira--> 2,864 tracked issues across the active projects.<!--/auto--> Every change starts as a Jira ticket with acceptance criteria and story points, moves through a sprint, and stops at QA for a human. Architecture decisions, runbooks and process manuals live in Confluence and render at [docs.mjashley.com](https://docs.mjashley.com).

**AI does the typing. I own the architecture.** Scope, sequencing and acceptance criteria are mine. Agents implement inside a written contract that caps file size, forces decomposition and bars them from pushing to main. Every change is reviewed in a browser against the running dev environment before it ships, and a second model audits the result.

**Guardrails that have actually fired.** Automated gates block a merge on unformatted code, oversized files, undocumented work and unverified claims. I fire each new gate at a real broken case before I keep it, because a guard that cannot fire looks exactly like a guard with nothing to report.

**My own infrastructure, on my own operating system.** Two bare-metal production nodes running Eight.ly OS, which took over from the Proxmox cluster and Unraid array they replaced. Multi-node Docker, Traefik reverse proxy, Cloudflare zero-trust tunnels, self-hosted GitHub Actions runners, and multi-architecture builds for amd64 and arm64.

### Stack

Go · TypeScript · React · SwiftUI · Python · SQLite · Docker · KVM/QEMU · nftables · GitHub Actions · Jira

---

[![Contribution graph](https://ghchart.rshah.org/409ba5/smashingtags)](https://github.com/smashingtags)

<sub>Counts above are refreshed daily from their sources by <a href="https://github.com/smashingtags/smashingtags/actions/workflows/refresh-readme.yml">a workflow in this repo</a>. Last checked <!--auto:checked-->2026-09-03<!--/auto-->.</sub>
