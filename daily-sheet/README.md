# Daily Sheet

A one-page daily task list built around a paper workflow: sections down a
sheet, a checkbox per task, and whatever isn't finished carries to tomorrow.

## What it does

- **Sections** — one per client, plus admin. Rename, recolour, reorder,
  collapse, delete.
- **Marking a line for today** — on the paper sheet, drawing a checkbox
  beside an item is the commitment: it means *I intend to do this today*,
  as distinct from the running list around it. That mark is its own thing
  here, the `▸` on each line, which cycles: nothing, on today's list,
  high priority. Marked lines carry a rail down the left edge on the full
  sheet, and the **Today** tab shows only them, high priority first. A line
  still marked days later says so, in amber and then red.
- **Every line is checkable**, and can carry an *in prog* or *waiting*
  status. A line can also be demoted to a note, which drops its checkbox and
  keeps it out of the tally, for reference text that is never "done". Any
  line can be a sub-line under the one above it.
- **Automatic carry-over** — there is no "start a new day" step. Open tasks
  stay open, and on a new day they wear a day count (`3d`) that turns amber
  at three days and red at seven. That count is the only thing the paper
  version gave you for free, by making you rewrite the task.
- **A log instead of a void** — checking a task off moves it into that day's
  record. The Log tab reads back day by day; the tally on any entry says how
  long it was carried before it got done.
- **Configurable day boundary** — a new day starts at 4:00 AM by default, so
  work past midnight still lands on the day it felt like.
- **Import** — paste a whole sheet in at once: `#` starts a section, `/`
  marks a task in progress, `-` makes a note, `x` files a line straight into
  today's log, `!` marks it for today, and two leading spaces make a
  sub-line. The same prefixes work
  when typing a single line into a section.
- **Copy and print** — copy today's sheet (or the whole log) as plain text,
  or print the sheet with the interface stripped out.

## Colour

One deliberate look, not a light/dark pair: a deep UCLA navy ground
(`#001A28` behind the sheet, `#00304A` for the sheet itself) with warm gold
type. Body text is a pale gold (`#F2E6C4`) at 11:1 against the sheet rather
than saturated gold, which is legible but tiring down a long list; full UCLA
gold (`#FFC72C`, 8.8:1) carries the structure — the date, section names,
focus rings, in-progress marks.

Priority reads on two levels. A line on today's list takes a cyan rail and
checkbox (`#4DD0E1`, 7.5:1), the one non-UCLA hue in the app. High priority
takes full UCLA gold with a wider rail and bolder text, which is why gold is
kept off the section names — reserving the brightest colour for the few
lines that have to happen makes it mean something. Gold also escalates an
ageing mark, and a soft red is held for a week stale.

Every foreground/background pair clears WCAG AA; the weakest is a secondary
count at 5.3:1 and body text sits at 11.1:1. Printing overrides the whole
palette to black on white.

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
