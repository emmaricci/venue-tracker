# Changelog

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
