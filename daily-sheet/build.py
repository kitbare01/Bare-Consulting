#!/usr/bin/env python3
"""Wrap app.html (the Artifact fragment) into a standalone index.html.

app.html is the single source of truth. Published as a Claude Artifact it
gets a document skeleton automatically; this script adds an equivalent one
so the same file also opens as a plain web page with no runtime attached,
falling back to browser storage.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<style>
  :root {
    color-scheme: light dark;
    padding-top: env(safe-area-inset-top, 0px);
    padding-bottom: env(safe-area-inset-bottom, 0px);
  }
  body { margin: 0; font: 14px system-ui, sans-serif; background: #faf9f7; }
  img { max-width: 100%; }
  [hidden] { display: none !important; }
</style>
</head>
<body>
@@FRAGMENT@@
</body>
</html>
"""


def main():
    fragment = io.open(os.path.join(HERE, "app.html"), encoding="utf-8").read()
    out = os.path.join(HERE, "index.html")
    io.open(out, "w", encoding="utf-8").write(SHELL.replace("@@FRAGMENT@@", fragment.strip()))
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))


if __name__ == "__main__":
    main()
