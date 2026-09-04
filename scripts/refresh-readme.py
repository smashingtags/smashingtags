#!/usr/bin/env python3
"""Rewrite the generated numbers in README.md from their real sources.

Every number on a public profile is a claim with a shelf life. This keeps the
ones that have a checkable source and refuses to write the ones that do not:
if a source cannot be reached, the previous value is left alone and the run
fails loudly, rather than silently publishing a guess.

A source that needs a secret is optional. Without the secret the sentence is
written without a number at all, which is the honest form.
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

README = os.path.join(os.path.dirname(__file__), "..", "README.md")
UA = {"User-Agent": "smashingtags-readme-refresh"}


def get(url, headers=None, timeout=25):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()


def ce_app_count():
    """HomelabARR CE's own README is the number the product ships with."""
    txt = get(os.environ.get(
        "CE_README_URL",
        "https://raw.githubusercontent.com/imogenlabs/homelabarr-ce/main/README.md",
    ))
    counts = re.findall(r"\b(\d{2,4})\s+apps\b", txt)
    if not counts:
        raise ValueError("no 'N apps' phrase found in the HomelabARR CE README")
    # The README states it more than once; they must agree or the source is ambiguous.
    uniq = sorted(set(counts), key=int)
    if len(uniq) > 1:
        raise ValueError(f"HomelabARR CE README disagrees with itself: {uniq}")
    return uniq[0]


def npm_downloads():
    """shields.io's npm/dt endpoint is rate limited often enough that the badge
    renders "rate limited by upstream service" on the profile. npm's own API is
    not, so the number is fetched here and baked into a static badge instead."""
    url = os.environ.get(
        "NPM_DOWNLOADS_URL",
        "https://api.npmjs.org/downloads/point/last-year/@imogenlabs/operator-kit",
    )
    n = json.loads(get(url))["downloads"]
    label = f"{n:,}".replace(",", "%2C")
    # The whole badge is emitted, never just the number: an HTML comment inside a
    # markdown image URL breaks the image.
    return (f"[![npm downloads](https://img.shields.io/badge/npm%20downloads-{label}"
            f"-crimson?style=for-the-badge)](https://www.npmjs.com/package/@imogenlabs/operator-kit)")


def jira_clause():
    """Optional. Needs JIRA_EMAIL + JIRA_API_TOKEN repo secrets.

    Without them this returns an empty string and the sentence simply carries no
    number, which is the point: no secret, no claim.
    """
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    site = os.environ.get("JIRA_SITE", "https://mjashley.atlassian.net")
    if not (email and token):
        print("jira: no credentials configured, writing the sentence without a count")
        return ""
    import base64
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    projects = "EOS,SITE,INFRA,HLCE,EP,EBS,EA,MOB,NH,TMPL,STICK,NOVAI,AGTPL,HLMOB,MPAC"
    body = json.dumps({"jql": f"project in ({projects})"}).encode()
    req = urllib.request.Request(
        f"{site}/rest/api/3/search/approximate-count",
        data=body, method="POST",
        headers={**UA, "Authorization": f"Basic {auth}",
                 "Content-Type": "application/json", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        n = json.load(r)["count"]
    return f" {n:,} tracked issues across the active projects."


def replace(text, name, value):
    pat = re.compile(rf"(<!--auto:{re.escape(name)}-->)(.*?)(<!--/auto-->)", re.S)
    if not pat.search(text):
        raise ValueError(f"marker '{name}' not found in README")
    return pat.sub(lambda m: m.group(1) + value + m.group(3), text)


def main():
    text = open(README).read()
    original = text
    failures = []

    for name, fn in (("ce-apps", ce_app_count), ("npm-dl", npm_downloads), ("jira", jira_clause)):
        try:
            text = replace(text, name, fn())
        except Exception as e:            # noqa: BLE001 - report every source, then fail once
            failures.append(f"{name}: {e}")
            print(f"FAILED {name}: {e}", file=sys.stderr)

    if failures:
        # Leave the file untouched. A stale number is bad; a wrong one is worse.
        print("no changes written because a source could not be read", file=sys.stderr)
        return 1

    text = replace(text, "checked", dt.date.today().isoformat())

    if text == original:
        print("no change")
        return 0
    open(README, "w").write(text)
    print("README updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
