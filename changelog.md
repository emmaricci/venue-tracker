# Changelog

## 2026-11-01 — Run 2b (manual, same day)

Changes Emma asked for directly, on top of the automated Run 2 earlier the same day.

### Venues added

- **HAIC — Human-AI Interaction Conference 2027** (inaugural), June 27–30 2027, Hopkins Bloomberg Center, Washington DC. Conference dates confirmed. The submission deadline is recorded as `unknown`: the official site says only "Late January 2027" with no day, time or time zone, and the full call is still "coming soon". Nothing was estimated, because an inaugural edition has no prior cycle to project from.
- **ACM ICMI — International Conference on Multimodal Interaction.** ICMI 2026 (Napoli, Oct 5–9 2026) recorded in full across 13 tracks, all now passed. Note the page's own rule: every deadline is 23:59 PDT except the paper submission, which is AoE. Several 2026 deadlines were shown struck through or marked extended. ICMI 2027 is `unknown` and deliberately not projected — the only cycle on record had several extended deadlines, making it a poor basis for estimation, and searches surfaced only predatory aggregator listings reusing the ICMI name, which were disregarded.
- **ACM HEALTH — ACM Transactions on Computing for Healthcare**, tracked for the Special Section on Human-Centered Computing in Healthcare. Emma supplied the official call-for-papers PDF after ACM's bot protection blocked every automated attempt to read dl.acm.org, including through a real browser.

### Correction

An earlier draft of the ACM HEALTH entry inferred from indirect evidence that the special section's call had probably closed. **That was wrong.** The call Emma supplied shows it is open, rolling, with a last new submission date of **1 February 2027**. The inference had been recorded as `unknown` rather than as a date, so no false deadline ever entered the data, but the reasoning is noted here because it was wrong and the same indirect signals may recur. Also recorded from that call: authors of each submission are collectively expected to volunteer to review at least three submissions, and the corresponding author must complete a reviewer form before the guest editors will send the paper out for review. No clock time or time zone appears anywhere in the call; the stored instant assumes 23:59 AoE.

### New field: category

Every tracked date now carries a `category`, saying what sort of opportunity or obligation it is, independent of its confirmed/projected status. All 101 entries are labelled across 15 values: manuscript, rebuttal, notification, camera-ready, poster-demo, workshop-organization, workshop-participation, doctoral-consortium, student-volunteer, travel-grant, reviewing, registration, journal-cycle, panel-meetup, event.

Workshop organizing and workshop participation are deliberately separate. Two judgement calls worth knowing about: CHI 2027's Student Mentoring Program (Dissertation Research Roundtable) is filed under `doctoral-consortium`, since it may be that cycle's replacement for the DC, though nothing official says so; and "Workshops: organizer notification" is filed under `workshop-organization` rather than `notification`, to keep the organizer track together under a filter.

### Dashboard

- The top section is now **Next 30 days**, down from 60.
- Urgency labels (DUE SOON / APPROACHING) moved from beside the title to beside the date they qualify.
- Every upcoming entry now carries a direct source link.
- Category badges appear in both sections, with a Category filter in the venue toolbar. Filtering by category re-ranks each venue by its next deadline *of that category*, and highlights matching rows inside an expanded venue.
- Fixed: a deadline that had passed within the previous 24 hours could still show as due "Today", because the countdown rounded to whole days. Upcoming entries are now filtered on the exact instant. ML4H's Early Career Travel Grant (31 Oct, 23:59 AoE) was the case that exposed it.

### Also in this pass

- The three new venues were appended to `venues.md`, so the scheduled refresh keeps tracking them. That file is otherwise Emma's to edit; this was done at her request.
- The new field was first called `kind` and was renamed to `category` before anything was committed. "Track" was considered and rejected: several values (notification, camera-ready, registration) are stages rather than tracks, so the word would have been wrong for roughly a third of the entries.

### Schedule reconciled

The scheduled refresh runs **monthly on the 1st** (07:00 Europe/Rome). `next_update` is now 2026-12-01 and `update_cadence` reads "monthly, on the 1st", so the date in the page header matches when the task actually fires. The task's own instructions were rewritten to match; they previously described a fortnightly gate on a Monday schedule.

### IMWUT confirmed, and a missing deadline found

Emma supplied IMWUT's own submission guidance, which dl.acm.org had blocked on every previous run. Three things follow.

**The projected schedule was right.** New submissions are accepted three times a year — 1 February, 1 May, 1 November — exactly as projected since run 1. All three are upgraded from `projected` to `confirmed`. The assumed 23:59 AoE cutoff was also correct: the guidance states every IMWUT deadline closes at 23:59 AoE on the date itself, and that deadlines are firm with no extensions granted.

**A deadline was missing entirely: 1 August.** It is open only to papers that received a major-revision decision, and is closed to new submissions. A paper that receives major revisions may resubmit at either of the two deadlines following its original submission — so a 1 February submission can resubmit on 1 May or 1 August. This is now tracked as its own entry under the `rebuttal` category. Nothing in the tracker had carried it before.

**Also recorded:** the submission site (new.precisionconference.com/submissions) opens roughly two weeks before each deadline, and authors of accepted papers are invited to present at UbiComp/ISWC each year.

Source provenance is noted on every entry: the text came from Emma rather than from a page this tracker could read, since ACM's bot protection stops both automated fetches and a real browser.

The SIGCHI UbiComp 2027 page was also checked. It confirms the conference dates already recorded in Run 2 (3-7 Oct 2027, Seoul Dragon City) and carries no IMWUT deadlines, which is expected: the journal sets its own cycles and conference pages restate them only incidentally.

## 2026-11-01 — Run 2

Second run, about five weeks late (the schedule's `next_update` had been 2026-09-28; this run processes all changes since the 2026-09-16 baseline in one pass).

### Changed dates (flagged per policy)

- **ML4H 2026 — "Decisions released" moved from Oct 22, 2026 to Oct 26, 2026** on the official call-for-papers page (ml4h.ahli.cc). Both dates are already in the past as of today, so this has no forward-looking effect, but it's a change to a previously confirmed date and is flagged as required.

### Newly confirmed / resolved

- **CHIL 2027 call for papers is now published.** Submission deadline Feb 3, 2027 — upgraded from `projected` to `confirmed` (the projection made last run matched exactly). Also added: author/reviewer discussion (Mar 26, 2027), meta-review deadline (Apr 2, 2027), notification (Apr 12, 2027). No time zone stated on the page for any of these; `instant_utc` assumes 23:59 AoE as before. Doctoral symposium still has no dates.
- **UbiComp/ISWC 2027 is now announced**: Oct 3–7, 2027, Seoul Dragon City, Seoul, South Korea. No call-for-papers or deadlines yet. Venue-level fields in `deadlines.json` now point at this 2027 cycle instead of the completed 2026 one; IMWUT remains the real submission path for long papers.
- **MLHC open item partially resolved.** `mlhc.org` is reachable again and is the genuine official site (previous runs found it unreachable, or showing unrelated content). It confirms MLHC 2027 will be Aug 11–13, 2027 at ETH Zurich, Switzerland, but says the call for papers is "details coming soon" — so submission deadlines are still `unknown`. Will keep checking each run as instructed.
- **ACM CHI 2027** — two newly published dates: conference registration deadline and video presentation deadline, both Mar 4, 2027. Also found a new **Student Mentoring Program: Dissertation Research Roundtable** track (submission Jan 21, 2027; notification Feb 18, 2027), which may be CHI 2027's replacement for the traditional Doctoral Consortium — not confirmed as such, so DC itself remains recorded as `unknown`.

### Could not verify this run

- **MLHC papers / clinical abstracts submission deadlines** — site is up but CFP isn't published yet. Per the task's standing instruction, will try again next run.
- **ACM CHI 2027 Doctoral Consortium, Student Volunteers, and Travel Grants** — no pages found for any of the three (the DC URL now 404s). SV and travel grant pages have never existed for this cycle.
- **IMWUT November 2026 cycle deadline** — dl.acm.org/journal/imwut still returns a client error on every attempt, so the Nov 1, 2026 date remains `projected`, not `confirmed`, and its time zone is still unstated. Note: today is Nov 1, 2026 — if this is in fact the live deadline, Emma should verify the exact cutoff directly in the submission system rather than relying on the assumed AoE time here.
- **ML4H Early Career Travel Grant** (previously Oct 31, 2026) — no longer findable on the current call-for-papers page, which now mentions an "Author, Reviewer and Career Mentorship Program" instead with no date given. Left the old date in place since it's already past and there's no live risk either way; flagging the discrepancy for the record.
- **ACM DIS 2027 Doctoral Consortium** — still no dates; the page now at least gives a contact address (dc@dis2027.acm.org) and a 16-participant cap.

### Unchanged, re-verified

ACM CHI papers/workshops core dates, ACM DIS papers & pictorials dates, ACM CSCW rolling-submission status and 2026 DC, ACM UIST 2026 (all passed) and projected UIST 2027 dates, ML4H camera-ready (still "tentative"), ACM Interactive Health (IH'27 still not announced) — all re-checked against their official pages with no changes found.


## 2026-09-16 — Run 1 (first run)

First run. `deadlines.json`, `dashboard.html` and this changelog created from scratch against the ten venues in `venues.md`.

### Venue name resolved

- **ACM Interactive Health** — confirmed as a real venue at the URL you supplied, `https://ih.acm.org/`. Official title: ACM Interactive Health Conference (IH). The 2026 edition was the inaugural one, held July 5–8, 2026 in Porto, Portugal. The `NAME UNVERIFIED` note in `venues.md` can be considered resolved, though `venues.md` is yours to edit.

### New dates recorded — confirmed

**ACM CHI (CHI 2027, Pittsburgh, May 10–14 2027)** — full cycle confirmed from chi2027.acm.org:
papers Sep 10 2026 (passed), reviews Nov 5, resubmission Dec 3, final notification Dec 17 2026, camera-ready chain Jan 7 / Jan 14 / Feb 18 2027. Workshops juror application Sep 28 2026, workshop proposals Oct 1 2026. Posters, Interactive Demos and SRC all Jan 21 2027. Panels Nov 19 2026. Meet-Ups Oct 1 2026. All AoE.

**ACM DIS (DIS 2027, Stockholm, Jun 28 – Jul 2 2027)** — abstract Jan 11 2027, papers and pictorials Jan 18 2027, notification Mar 19 2027, workshop proposals Feb 1 2027. All AoE.

**ML4H 2026 (Sydney, Dec 6–7 2026)** — papers Sep 10 2026 (passed), author response closes Oct 12, decisions Oct 22, early-career travel grant Oct 31, camera-ready Nov 7 2026 (tentative). All AoE.

**ACM UIST (UIST 2026, Detroit, Nov 2–5 2026)** — full 2026 cycle recorded; every submission deadline has passed. Conference is upcoming.

**ACM UbiComp (UbiComp/ISWC 2026, Shanghai, Oct 11–15 2026)** — ISWC Notes & Briefs May 24 2026 and Doctoral Colloquium Jun 19 2026, both passed and both already extended from their original dates. Registration regular rate ends Oct 1 2026.

**ACM CSCW (CSCW 2026, Salt Lake City, Oct 10–14 2026)** — Doctoral Consortium May 15 2026, passed.

**CHIL 2026 (Seattle, Jun 28–30 2026)** — full 2026 cycle recorded, all passed.

### Structural changes worth your attention

1. **CSCW has moved to rolling submission.** The official page at `cscw.acm.org/rolling.html` states plainly that there are no submission deadlines for any year's conference from CSCW 2027 onward. Papers go through PACM HCI (CSCW) or TOCHI, and on acceptance authors are emailed to request a presentation slot at whichever conference the timing allows. This answers the "verify current submission cycle" note in `venues.md`: there is no cycle to track anymore for the papers track. Workshops, DC and SV for CSCW 2027 presumably still have deadlines, but no CSCW 2027 site exists yet.

2. **CHI 2027 appears to have no Late-Breaking Work track.** The author-tracks page lists Papers, Posters, Interactive Demos, Panels, Workshops, Meet-Ups and Student Research Competition, and nothing else. Posters (Jan 21 2027) may be the replacement for LBW, but nothing on the site says so, so LBW is recorded as `unknown` rather than mapped onto Posters. Worth watching.

3. **CHI 2027 replaced the rebuttal with a revise-and-resubmit window.** Reviews land Nov 5 2026 and the resubmission is due Dec 3 2026, a four-week revision period rather than a short rebuttal.

4. **IMWUT may have dropped from four cycles to three.** The official ISWC 2026 call for papers states IMWUT now has three deadlines a year: 1 February, 1 May, 1 November. This conflicts with the older quarterly schedule. See "could not verify" below.

5. **ISWC long papers now route through IMWUT.** ISWC's own track is Notes & Briefs only; anything longer goes to the IMWUT journal system. That makes the IMWUT cycle the real submission path for UbiComp work.

### Could not verify

- **MLHC — nothing recorded at all.** Every official domain I tried was unreachable. `mlforhc.org` and `mlhc.org/2026-conference` both failed on robots.txt, and `mlhc.org` itself returned content from an unrelated Milwaukee community organization, which suggests the domain is not what it appears to be. Aggregator listings exist but I will not use them as a source. MLHC is recorded as `unknown` with no dates. This one needs a manual look in a browser.
- **IMWUT cycle dates — recorded as projected, not confirmed.** The journal's own page at `dl.acm.org/journal/imwut` returned HTTP 403 on every attempt. The 1 Feb / 1 May / 1 Nov schedule comes from the official ISWC 2026 CFP describing the journal, not from the journal itself, and no clock time or time zone is stated anywhere I could reach. Treat Nov 1 2026 as indicative.
- **CHI 2027 Doctoral Consortium, Student Volunteers, travel grants** — no pages exist on the CHI 2027 site yet.
- **DIS 2027 Doctoral Consortium** — page exists and confirms the DC runs in person at KTH, but carries no dates.
- **UbiComp/ISWC 2026 workshops, posters/demos, student volunteers, travel grants** — track pages exist but the specific deadlines were not retrievable. The 2026 cycle has closed regardless.
- **UbiComp/ISWC 2027, CSCW 2027, UIST 2027, CHIL 2027, IH 2027** — no sites or calls announced yet.
- **Time zones for CHIL 2026 and IH 2026** — neither site stated a time zone. Stored instants assume 23:59 AoE and are flagged in the JSON notes.

### Projected dates added

- **UIST 2027** papers: abstract Mar 23 2027, full Mar 30 2027. Projected from the UIST 2026 pattern of an abstract on the last Tuesday of March with the paper a week later.
- **CHIL 2027** papers: Feb 3 2027. Projected from CHIL 2026's first-Wednesday-of-February deadline.
- **IMWUT** Feb 1 and May 1 2027 cycles, on the same unverified basis as the Nov 1 2026 cycle.
- **IH 2027** — deliberately not projected. 2026 was the inaugural edition, so there is no multi-year pattern to estimate from.

### Extensions flagged

Two UbiComp/ISWC 2026 deadlines were already extended before this run and are stored at their extended values, with the original date noted: ISWC Notes & Briefs moved May 17 → May 24 2026, and the Doctoral Colloquium moved Jun 15 → Jun 19 2026 (with notification and camera-ready shifting to Jul 15 and Jul 22).
