# Lunar Tracker Widget

A single-page, client-side moon tracker with natal chart integration.
Everything is computed in the browser with
[Astronomy Engine](https://github.com/cosinekitty/astronomy) — no backend,
no API keys, no build step.

**Features:** daily moonrise/moonset & sunrise/sunset, moon phase (SVG icon)
and illumination, the Moon's zodiac sign (tropical / sidereal-Lahiri toggle),
transiting-Moon conjunctions to natal planets (5° orb), the Moon's natal
Placidus house, a 2026 eclipse badge, personalized interpretive text, and a
date picker covering the current year.

## Files

| File | Purpose |
|---|---|
| `index.html` | page structure |
| `styles.css` | styling (light + dark mode) |
| `app.js` | all runtime logic |
| `data.js` | **configuration & content** — location, natal chart, eclipses, interpretive text |
| `astronomy.browser.js` | vendored Astronomy Engine v2 |
| `tools/derive-natal.html` | dev-time script that derived the hardcoded natal longitudes & Placidus cusps |

## Deploy to GitHub Pages

1. Create a GitHub repository and push these files to its root
   (or put them in a `/docs` folder).
2. In the repo: **Settings → Pages → Source: Deploy from a branch**,
   pick `main` and `/ (root)` (or `/docs`), then **Save**.
3. After a minute your widget is live at
   `https://<username>.github.io/<repo>/`.

## Embed in Notion

1. In Notion type `/embed` and choose **Embed**.
2. Paste your GitHub Pages URL.
3. Drag the embed's handles to size it — the layout is designed for
   400–700 px wide and stays usable down to 360 px.

## Change the location

Edit the clearly-marked block at the top of `data.js` — nothing else:

```js
// ── LOCATION CONFIG ─ edit these three values if you relocate ──
const LOCATION = {
  latitude: 43.65,
  longitude: -79.38,
  timezone: "America/Toronto", // IANA timezone name
};
```

All rise/set times and day boundaries follow this timezone. The natal chart
never changes with relocation.

## Paste in the interpretive content

Open `data.js` and fill the `CONTENT` constant: 8 categories × 12 entries
(sign entries keyed `aries`…`pisces`, house entries keyed `1`…`12`). Each
entry sits between a pair of backticks — paste the whole text exactly as
you have it, line breaks and all. `fullMoonInHouse: 12` is a filled-in
example. Formatting is automatic: lines starting with ◗ become styled
sub-headings, the first line becomes the entry's title line. Only two
characters need escaping inside an entry (both rare): type a backtick as
`` \` `` and `${` as `\${`. Any entry left empty (` `` `) shows
"— content pending —" in the widget. Solar eclipses automatically reuse the
new moon texts; lunar eclipses reuse the full moon texts.

`newMoonAffirmations` holds 3 affirmations per house (no quote marks —
they're added automatically). They display as cursive quotes above the
readings from the exact instant of each New Moon until 28 days later,
keyed by the natal house that New Moon fell in.

## Update the eclipse table annually

Each January, replace the `ECLIPSES` array in `data.js` with the new year's
solar and lunar eclipses from
[NASA's eclipse site](https://eclipse.gsfc.nasa.gov/eclipse.html)
(use the UTC time of greatest eclipse). The date-picker range follows the
year in the visitor's clock automatically; only the eclipse table needs a
manual update.

## Verification notes

- Moonrise/moonset and sunrise/sunset matched timeanddate.com for Toronto on
  Jul 14, 20, 28, 2026 (all eight times exact to the minute).
- Natal planet longitudes matched JPL Horizons within 0.004° and
  astro-seek.com within 13 arcseconds; all 12 Placidus cusps matched
  astro-seek within 1 arcsecond. GAST/RAMC for the birth instant matched an
  independent computation to 6 decimals.
- Sidereal mode matched Drik Panchang (Lahiri): e.g. the Moon's sidereal
  Cancer ingress on Jul 14, 2026 at ~9:18 am Toronto time.
- All four 2026 eclipse badges verified against the NASA catalog.
