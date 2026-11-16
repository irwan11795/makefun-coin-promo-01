# Coin Promo — re-grind round 3: TOPBOT (16 Nov 2026)

## LAUNCHED — TOPFUN live on pump.fun (17:36:29 WIB, 16 Nov 2026)

- **Mint:** FBoZBbqmpmDJiPzqfUdA1wEvAmA3atP28Yn6YP2hnBKw
- **Create signature:** 5kdmiBGDtQVikCXUgZdLh42ATrsqrvRz2STGKScb4bQXyWmRvHY8L2NAbmRxjw4kxk63mo3PVbjwNCci6CjcsmUy
- **Pump URL:** https://pump.fun/coin/FBoZBbqmpmDJiPzqfUdA1wEvAmA3atP28Yn6YP2hnBKw
- **On-chain verified:** slot 470100299, err None, supply 1,000,000,000 TOPFUN
  (6 decimals); wallet holds 714,856.762158 TOPFUN from the 0.02 SOL dev buy.
  DexScreener lists it (dex pumpfun, TOPFUN). LAUNCH.json filled, main.ts
  re-run exit 0, copy byte-identical. Kit check: 4 pass (competition_open,
  snapshot 23 files, license MIT, entrypoint), 1 fail = transcripts_present
  (bundle step, after repo) — nothing else to fix.
- **Cost:** 0.030136079 SOL total (0.02 dev buy + priority 0.0005 + rent/fees);
  wallet balance now 0.000929597 SOL. NOTE: below the ~0.0035 SOL a future
  prize-claim tx needs in the signing wallet — top up C247 later IF we win.
- **Metadata detour (recorded):** pump.fun/api/ipfs is DEAD (Cloudflare 403;
  PumpDev docs confirm "no longer supported"). Metadata hosted instead at
  https://raw.githubusercontent.com/irwan11795/makefun-coin-promo-01/main/metadata.json
  (pushed, commit 713b8527); logo image at https://files.catbox.moe/cungnx.png
  (verified byte-identical to logo-01, sha256 8bd218e8…). Launch built via
  PumpPortal trade-local (single-object request returns RAW tx bytes, not
  base58 — bundle requests return base58 JSON). Confirmation via websocket
  timed out (VM egress breaks wss) — tx was verified via REST getTransaction.
- **Sessions to bundle for submit:** round-3 (main.ts etc.), round-3b
  (TOPFUN rename + banner logo), candidates (logo-01), THIS launch session
  (logo copy, DESCRIPTION/CONCEPT edits, metadata.json, LAUNCH.json, launch).

## Round 3c — USER PICKED logo-01, GAS (17:18 WIB, 16 Nov 2026)

User rejected the banner logo ("lah kok jelek amat logo nya", 17:11 WIB) and
ordered 5 distinct leaderboard logos (17:13 WIB). Five candidates were drawn
in logo-candidates/ (01 Stairway Climb, 02 Podium Pro, 03 Trophy Bot,
04 Rocket Rise, 05 Throne of Ranks). User picked **01 "Stairway Climb"** and
said GAS at 17:18 WIB — the earlier "tunggu dulu" hold is LIFTED. Launch now:
logo-01 copied to logo.png (sha256 8bd218e8…), DESCRIPTION.md + this file
updated to describe it, C247 balance re-verified on-chain 0.031065676 SOL.

## Round 3b — RENAME to TOPFUN (user order 17:07 WIB, 16 Nov 2026)

User approved TOPBOT ("gas setuju", 17:05 WIB) then immediately held the
launch ("tunggu dulu", 17:05 WIB), then ordered: rename to TOPFUN ($TOPFUN)
and redraw the logo with "make.fun" written on it. Launch is ON HOLD — do
not launch or submit; this round only prepares and reports back.

- **Collision check (live, 17:08 WIB): 0 "TOPFUN" hits** in all 490
  submissions AND all 354 graded leaderboard rows (420 unique titles
  combined). No "top…fun" variant exists at all. The word "fun" itself is
  very crowded (84/490 submissions mention fun — every entry must promote
  make.fun), but the combination TOPFUN is clean. Rename approved to proceed.
- **Logo redrawn in THIS session** (draw_logo.py updated, logo.png
  regenerated — authorship clean): same design (teal robot on gold #1 podium,
  #1 flag, coral robot on #2, leaderboard rows 2–9) + a gold "make.fun"
  banner across the top, bold navy text. Verified by eye at full size and at
  256px thumbnail: banner legible at both sizes. 1024x1024, 99 KB.
- **Docs renamed:** DESCRIPTION.md, README.md, main.ts — TOPBOT → TOPFUN
  throughout (same length, description still 709 chars, all required
  elements present). LAUNCH.json had no name in it, unchanged.
  TOPBOT is set aside (approved-then-held, then renamed by the user); do not
  launch it. RANKBOT remains an unused backup name.

User order 16:59 WIB: grind again with a TOP BOARD / leaderboard concept, logo =
robots in the style of the top 10 leaderboard feed. The $LEAK concept is SET
ASIDE (user never approved it — do not launch it). Margin Five is also dead.
This file replaces the round-2 concept; all artifacts in this directory are the
round-3 build, written in this session.

## Field intel (live leaderboard API, 16 Nov ~17:00 WIB)

- 354 graded entries (491 submissions total, field still growing); prize zone =
  top 50; cutoff #50 = 87.95% ("The Judge"), #51 = 87.95%. #1 USE THIS ONE
  93.15%. Top 10: USE THIS ONE, Doxxed Dev ($DOXXED), Agent Cheque ($CHEQUE),
  The Snitch ($TAPE), Human Not Included ($NOHUMAN), The Wanted Poster, Feed
  The Bot ($FEED), Copycat, Escrow Goblin, The Replay.
- The board's top is sharp, self-referential concepts built on make.fun's own
  mechanics: cheque, invoice/paystub, escrow, grading, doxxing, snitching,
  wanted posters, replays.
- Dev rate is provisional (11 games vs house coins only; draws hurt — the
  reference entry 7W 4D 0L = 85.06% landed #73). The final re-judges ALL coins
  head-to-head from scratch (10 Swiss rounds + playoff for the top 52) right
  after entries close. Optimize for pairwise wins vs other entrants' coins.
- Bounty page checked directly (make.fun/bounty/makefun-coin-promo-01): $1,000
  in escrow, 50 places, deadline 17 Nov 13:00 WIB.

## Top-10 feed study — honest note on what I could and could not see

The feed's cover images are rendered client-side: the page text fetch returns
only the static brief, and the API exposes no coin image URLs (source
withheld; the leaderboard's `image` fields are submitter avatars or null).
So I studied the top 10 through the leaderboard data itself — titles,
tickers, scores — plus the user's own description of the feed: robots
dominate the top-10 feed. The logo below is drawn in that robot-mascot
style (chunky friendly robot, flat vector, bold outlines, bright accents on
dark navy) as the user described it — but the artwork itself is mine, drawn
with code in this session. No existing coin's logo was copied: copying
another entry's art fails the copy scan and kills the entry.

What the data says about robots on the board: "robot" appears in only 3 of
845 scanned titles (Robot Wages $WAGES #38 — the paycheck angle; The Roast
$ROAST — robot comic; Code Alchemist — robot alchemist) and "bot" in 17
(Feed The Bot $FEED #7, Bounty Bot x2, Forgi, Pip, Bread Bot, Stamp Bot,
BOTJOB, Bounty Hunter Bot). No coin is a robot ON a leaderboard. The robot
slot is open; the board slot is crowded (see below) — the fusion is the
originality.

## Collision scan (845 titles: 491 submissions + 354 leaderboard rows)

| Candidate | Hits | Verdict |
|---|---|---|
| **TOPBOT ($TOPBOT)** | 0 | **PICK** — "top" + "bot" in one short word; both words are crowded alone, the combination is clean |
| RANKBOT ($RANKBOT) | 0 | Backup — clean, but "rank" is less punchy than "top" |
| BOARDBOT ($BOARDBOT) | 0 | Backup — clean, but "board" is the crowded word (11 hits) |
| LEADERBOT ($LEADERBOT) | 0 | Clean but long; $TOPBOT says it in 6 letters |
| The Leaderboard (BOARD) | — | TAKEN — ticker BOARD is held; "board" has 11 hits (Bounty Board, Verdict Board, SCOREBOARD) |
| RANK ONE ($TOP1) | — | TAKEN — "top" + rank angle held at #2 territory; $TOP1/$TOP5 taken |
| Trophy ($TROPHY) | — | TAKEN — 7 hits; trophy angle held |
| Podium | — | TAKEN — "Podium" exists (low score, ~#300) |
| Robot Wages ($WAGES) | — | Different story (paycheck), #38 — a robot coin, but not a top-board robot |

## The pick: TOPFUN ($TOPFUN) — renamed from TOPBOT per user order 17:07 WIB

- Name: TOPFUN · Ticker: $TOPFUN · Logo: logo.png (agent-drawn in this
  session, verified by eye at full size and at 256px thumbnail: chunky teal
  robot climbing leaderboard steps 5 to 1 toward a gold #1 step, gold "#1"
  star above, "make.fun" engraved on the gold #1 step; 1024x1024, 21 KB —
  under the 5 MiB / 16 MP limits) — this is logo-01 "Stairway Climb", picked
  by the user at 17:18 WIB 16 Nov 2026 from 5 candidates (the earlier banner
  logo was rejected by the user as ugly at 17:11 WIB)
- Website: https://make.fun/bounty/makefun-coin-promo-01
- Description: see DESCRIPTION.md (hook first line, the climb story, what
  make.fun is, "made for the make.fun coin bounty", full link at the end,
  "The board is public. The bot is #1. Buy the top.")
- Story: the leaderboard is make.fun's core — every agent's work is scored
  and ranked in the open. This bot climbed it by building, one bounty at a
  time, and now sits at #1. The coin IS the robot at the top of the board.
- Why it wins pairwise: criterion 1 — the concept fuses the two things the
  user asked for (top board + robots) into one character no one else holds;
  criterion 2 — the description explains make.fun through its own leaderboard
  mechanic; criterion 3 — a chunky robot on a gold #1 podium with a flag is
  the most readable thumbnail possible, and $TOPFUN is short and memorable —
  and the "make.fun" banner on the logo literally brands the platform on the
  coin itself. Built to win decisively, not to draw.

## What is ready (in ~/workspace/makefun/new-bounties/makefun-coin-promo-01/)

- main.ts (written in THIS session: copies LAUNCH.json to /output, validates
  mint/signature base58 shapes + 16384-byte cap, refuses placeholders with
  exit 1, verifies the copy is byte-identical; placeholder run exits 1,
  valid-shape run exits 0)
- package.json ({"private":true,"type":"module"})
- README.md (3 make.fun badges as LINKS, per the requirements template)
- LICENSE (MIT, from the starter)
- LAUNCH.json (placeholders — filled with the real mint + create_signature
  after launch)
- logo.png (1024x1024, 91 KB — agent-drawn in this session, draw_logo.py kept
  beside it) + DESCRIPTION.md (exact launch metadata) + this file

## What is NOT done (needs parent / user)

1. CONCEPT APPROVAL (this report): user reviews TOPFUN first. $LEAK is set
   aside — do not launch it. TOPBOT was approved then held and renamed by
   the user — do not launch it either. Backup if the user rejects this too:
   RANKBOT ($RANKBOT), same logo family, name/ticker swapped.
2. GitHub repo makefun-coin-promo-01 (owner irwan11795, public, created after
   the competition opened) + push + About (website
   https://make.fun/bounty/makefun-coin-promo-01, topics
   makefun, ai-agents, bounties, growth) — parent does this via browser.
3. LAUNCH on pump.fun from C247 (balance verified on-chain 0.031065676 SOL
   at 17:08 WIB, unchanged; launch ~0.02 SOL + ~0.00001 fee; ~0.011 SOL
   spare — enough for the launch plus one failed-attempt retry, nothing
   more; do not waste transactions). Metadata: name "TOPFUN", symbol
   "TOPFUN", description + website + logo.png exactly as in DESCRIPTION.md.
   No human step in the launch itself.
4. Fill LAUNCH.json with the real mint + create_signature, re-run main.ts,
   run the kit check, bundle transcripts (this session + the launch session),
   submit with --keypair ~/workspace/makefun/makefun-keypair.json.
   Quota: entries_kept=0, can_submit=true, day cap 3 left. Deadline 13:00 WIB
   17 Nov. Max 5/day, 10 total; last submission before the deadline is final.
