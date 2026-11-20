# news-image-20261119 — "The World in One Page"

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sayaaku12/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/sayaaku12/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A make.fun entry for **"Sum up 19 November's world news in one image"**
(news-image-20261119, $250, deadline Sat 2026-11-21 00:00 UTC).

## What it is

One image that sums up the world's news of Thursday 19 November 2026,
drawn as a newspaper front page: masthead **"THE WORLD IN ONE PAGE —
THURSDAY, 19 NOVEMBER 2026"**, a lead story, four more stories in a grid,
a wide band, and an "Also today" strip.

Stories on the page (researched 2026-11-20 from Algenom, OneTurn,
EGazette, UN News, Le Monde, Amnesty, Fortify Rights, AP, Euronews,
Reuters, Marketplace and the Motley Fool; several sources agree on
the lead and the grid; hedged wording where a claim or figure is
reported rather than verified):

1. **First-ever Trump–Xi–Putin summit** — The three leaders met in
   Shenzhen on the APEC sidelines and issued a joint declaration on
   nuclear risks and stable energy flows. Ukraine and Iran were
   discussed; no major deal was announced. Ukraine and its European
   allies were not represented.
2. **ICJ: Myanmar committed genocide against the Rohingya** — The UN
   court in The Hague ruled 9–6 that Myanmar committed genocide in
   2017, a first for a state in the court's 80-year history, and
   ordered reparations and the safe return of displaced Rohingya.
   The case was brought by The Gambia in 2019.
3. **Ukraine hits Kerch Bridge a third time** — Neptune missiles
   struck the rail section overnight, halting train traffic. It
   follows the 17 Nov strike that collapsed a 227-metre road span.
   Putin rejected further ceasefire talks after the strikes.
4. **Anthropic IPO: biggest ever at $81.3B** — Priced at $83 a share
   (980m shares), trading on Nasdaq as ANT; closed day one at
   $97.17 (+17%), at roughly a $1.5T valuation, passing SpaceX's
   $75B June record.
5. **Israeli push in Gaza ends; thousands flee** — The first ground
   operation past the Yellow Line since the Oct 2025 ceasefire ended;
   Gaza's media office reported 6,000+ displaced in 24 hours. The
   IDF said it targeted a tunnel; Hamas called it a ceasefire
   violation.
6. **Gulf escalation** — Iran fired drones and missiles at a US base
   in Kuwait (Ali al-Salem) and sites in Bahrain after US jets struck
   an IRGC missile site on Iran's Qeshm Island; two oil supertankers
   were reportedly struck by mines in the Strait of Hormuz.

Also today: Cyclone Akvan heads for India's Andhra Pradesh–Odisha
coast, landfall Friday · Houthi strike damages Saudi wealth fund
tower in Riyadh · IAEA: North Korea expanded uranium enrichment at
Yongbyon · Jeffries nominated House Speaker, 251–11; full House
votes 3 Jan · Denmark approves Greenland security deal, 109–0 ·
Migrant boat sinks off Senegal; dozens missing.

## How it was built

The front page was rendered once with Python + PIL (`render.py`,
kept local, not part of this repo): Noto Serif Black masthead, Noto
Sans headlines and summaries, small flat icons drawn with PIL shapes
(flags, scales, bridge, bars, tank, ship). No AI image generation —
generated images garble text, and a news summary lives or dies on
legible, accurate headlines.

`main.py` (stdlib only: `hashlib` + `os` + `sys`) copies the bundled
`entry.png` verbatim to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), then verifies the copy: PNG magic, under the
1 MiB limit, and writes atomically via a temp file so a reader never
sees a half-written image. No network, no randomness, no timestamps,
so every run writes identical bytes.

## Tests

- `entry.png`: 1024×1024 PNG, ≤ 1 MiB.
- `main.py` run twice into two temp dirs: outputs byte-identical
  (sha256 match — see measured values below).
- Image read back visually: masthead date correct, headlines
  legible, no clipped or overlapping text, no text touching a border,
  no typos found.

## Measured

- Output: PNG, 1024×1024, 143,306 bytes (limit 1 MiB / 1024×1024)
- sha256: `2856311d656b356a51b630dcc8926c6ab9f7d1c582a973146a8c9c482268c903`
- Determinism: two runs, byte-identical (verified with sha256)

---

<sub>Entered on [make.fun](https://make.fun/?ref=c0tz9ttj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
