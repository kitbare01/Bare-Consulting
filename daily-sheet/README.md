# Daily Sheet

A one-page daily task list built around a paper workflow: sections down a
sheet, a checkbox per task, and whatever isn't finished carries to tomorrow.

## What it does

- **Sections** — one card per client, plus a few general cards for admin
  and personal work. Rename, recolour, collapse, delete, and set the card
  type. Order is a rule rather than a preference: **Admin** first,
  **Personal** last, everything else alphabetical between them, re-sorting
  the moment a card is renamed or retyped — so there is nothing to drag and
  no manual move. The client/general distinction is not decorative:
  dictation is told which cards are clients, so a task for a client gets
  that client's own card, creating it when the client is new, instead of
  landing in a catch-all.
- **Marking a line for today** — on the paper sheet, drawing a checkbox
  beside an item is the commitment: it means *I intend to do this today*,
  as distinct from the running list around it. That mark is its own thing
  here, and it is independent of importance: `▸` puts a line on today's
  list, `★` makes it high priority, and a line may carry either, both, or
  neither. Marked lines take a rail down the left edge (cyan, gold, or split
  when both), the **Today** tab shows today's list with high priority first,
  and anything high priority but *not* on today's list is gathered at the
  foot of that tab so it cannot quietly disappear. A line still on today's
  list days later says so, in gold and then red.
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
- **Dictate a list** — the one feature that uses Claude. Get words into the
  box by pasting, by the browser's own recogniser where the frame allows a
  microphone, or by the OS dictation key; Claude then sorts the run-on into
  sections with the marks set, for review before anything is written. It
  spends the viewer's own Claude usage and asks consent on first use; where
  the capability is absent the button is hidden and the rest of the app is
  unaffected.
- **Copy and print** — copy today's sheet (or the whole log) as plain text,
  or print the sheet with the interface stripped out.

## Layout

Sections are cards laid into balanced columns: three on a laptop or a tablet
held sideways (≥1150px), two at middling widths, one on a phone held
upright. The columns are real elements rather than CSS multicol, so a menu
opening inside one is never fragmented across the gap.

They read like a newspaper: down column one, then column two. Because the
order is a rule, the split may only choose *where* to break between columns,
never which card goes where — each card lands in the column its own midpoint
falls into, and an outsized card that would strand a later column pushes its
neighbours along instead. Balancing heights by reordering, which an earlier
version did, makes "first" and "last" meaningless.

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

## Panels and focus

Panels render into their own container, rebuilt only when their own state
changes, rather than into `#main` alongside the sheet. `#main` is replaced
wholesale on every render, and a sync snapshot arriving mid-sentence would
otherwise tear the textarea out from under whatever was typing into it —
which is precisely what dictation is. The box also takes focus when the
panel opens and keeps its caret across a rebuild.

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

## One artifact, one URL

Publishing an update redeploys to the same address; the artifact has had a
single URL since its first version. The database below is keyed to that
artifact, not to a version, so data survives every republish. A *new* URL
would be a different artifact with an empty database — which is why updates
always go to this one.

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
