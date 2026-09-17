# Venue Deadline Tracker

A self-contained dashboard of submission deadlines for HCI, ubiquitous computing
and machine-learning-for-health venues. Every date carries its source link, the
time zone it was stated in, and whether it was confirmed on an official page or
estimated.

**Live page:** https://emmaricci.github.io/venue-tracker

## Reading the dashboard

Deadlines appear in US Eastern with the venue's original time zone alongside,
since most academic deadlines are stated in Anywhere on Earth (UTC-12).

Each date is marked one of three ways:

| Status | Means |
| --- | --- |
| **confirmed** | The date appears on an official venue page for the correct cycle. |
| **projected** | The cycle is unannounced. The date is estimated from the previous cycle and should not be planned around. |
| **unknown** | Could not be found or reasonably estimated. The note says why. |

Urgency is tracked separately from status, so a deadline can be both imminent
and merely projected. Any venue not checked in over 30 days is flagged.

## Files

| File | Role |
| --- | --- |
| `venues.md` | The venue list. Hand-maintained input. |
| `deadlines.json` | The data store. One entry per tracked date. |
| `dashboard-template.html` | The page design, with fonts embedded and one `__DATA__` placeholder. |
| `build_dashboard.py` | Regenerates the dashboard from the template and the JSON. |
| `dashboard.html` | Generated output. Do not edit. |
| `index.html` | Identical to `dashboard.html`; the copy GitHub Pages serves. Do not edit. |
| `changelog.md` | What changed on each refresh, newest first. |

## Rebuilding

```sh
python3 build_dashboard.py
```

That is the only build step. The page has no dependencies and opens offline
straight from disk.

## Refresh cadence

A scheduled task re-checks every venue's official pages every 14 days and
rewrites `deadlines.json`, `changelog.md` and the dashboard. The date of the
next scheduled refresh is shown in the page header.

## Publishing an update

```sh
git add -A && git commit -m "Refresh deadlines" && git push
```

GitHub Pages picks up the change within a minute or so.

## A note on the data

Dates are transcribed from official venue pages and can go stale between
refreshes, and venues do extend deadlines. Check the source link on any date
you are actually planning around.
