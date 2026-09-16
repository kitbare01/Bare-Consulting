# Daily Sheet

A one-page daily task list built around a paper workflow: sections down a
sheet, a checkbox per task, and whatever isn't finished carries to tomorrow.

## What it does

- **Sections** — one per client, plus work-admin and personal. Rename,
  recolour, reorder, delete.
- **Automatic carry-over** — there is no "start a new day" step. Open tasks
  stay open, and on a new day they wear a day count (`3d`) that turns amber
  at three days and red at seven. That count is the only thing the paper
  version gave you for free, by making you rewrite the task.
- **A log instead of a void** — checking a task off moves it into that day's
  record. The Log tab reads back day by day; the tally on any entry says how
  long it was carried before it got done.
- **Configurable day boundary** — a new day starts at 4:00 AM by default, so
  work past midnight still lands on the day it felt like.
- **Copy and print** — copy today's sheet (or the whole log) as plain text,
  or print the sheet with the interface stripped out.

## Files

| File | Role |
| --- | --- |
| `app.html` | Source of truth. An Artifact fragment: no `<html>`/`<head>`/`<body>` wrapper, since claude.ai supplies one. |
| `index.html` | Generated. `app.html` plus a document shell, so it also opens as a plain web page. |
| `build.py` | Regenerates `index.html` from `app.html`. |

Edit `app.html`, then:

```sh
python3 daily-sheet/build.py
```

## Storage

The app talks to one storage interface with two backends, chosen at load:

- **Published as a Claude Artifact** — uses the artifact's `db` capability,
  so the same sheet follows you between laptop and phone. Private to the
  account unless explicitly shared.
- **Opened as a plain file or web page** — falls back to `localStorage`,
  which means that browser only.

The data model keeps open work and the archive apart, which is what keeps it
inside the document budget:

- `board/state` — one document holding the sections, the open tasks (in
  order) and the settings. Small, bounded, always read together.
- `archive/YYYY-MM-DD` — one document per finished day. Roughly 365 a year
  rather than one per task.

## Note on hosting

This directory is source. The live copy is the published Artifact, which is
private; `index.html` is here so the app is yours to self-host, but anything
served from this repository is public, and browser storage is per-device.
