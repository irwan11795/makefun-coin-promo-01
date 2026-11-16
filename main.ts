// TOPFUN — makefun-coin-promo-01 entry program (Node 22, stdlib only).
// Copies LAUNCH.json from the repository root to /output, after validating
// its shape. The house reads the coin itself from pump.fun; nothing this
// program writes about the coin is judged.
//
// Run it locally the way the kit does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// The grader runs it with the repository mounted at /bot and /output as the
// output directory, so both paths are overridable by environment.
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

// Base58 alphabet: no 0, O, I or l.
const BASE58 = /^[1-9A-HJ-NP-Za-km-z]+$/;
const MAX_BYTES = 16384;

function fail(message: string): never {
  console.error(`TOPFUN main.ts: ${message}`);
  process.exit(1);
}

const botDir = process.env.MAKEFUN_BOT_DIR ?? process.cwd();
const launchPath = join(botDir, "LAUNCH.json");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

let raw: Buffer;
try {
  raw = readFileSync(launchPath);
} catch {
  fail("LAUNCH.json not found at the repository root");
}
if (raw.length > MAX_BYTES) {
  fail(`LAUNCH.json is ${raw.length} bytes, over the ${MAX_BYTES} cap`);
}

let launch: unknown;
try {
  launch = JSON.parse(raw.toString("utf8"));
} catch {
  fail("LAUNCH.json is not valid JSON");
}
if (typeof launch !== "object" || launch === null || Array.isArray(launch)) {
  fail("LAUNCH.json must be a JSON object");
}
const { mint, create_signature } = launch as Record<string, unknown>;

if (
  (typeof mint === "string" && mint.includes("PLACEHOLDER")) ||
  (typeof create_signature === "string" &&
    create_signature.includes("PLACEHOLDER"))
) {
  fail(
    "LAUNCH.json still holds placeholders — fill in the real mint and create_signature",
  );
}
if (
  typeof mint !== "string" ||
  !BASE58.test(mint) ||
  mint.length < 32 ||
  mint.length > 44
) {
  fail("mint must be a base58 Solana address, 32 to 44 characters");
}
const sigOk =
  typeof create_signature === "string" &&
  BASE58.test(create_signature) &&
  ((create_signature.length >= 64 && create_signature.length <= 88) ||
    (create_signature.length >= 32 && create_signature.length <= 44));
if (!sigOk) {
  fail(
    "create_signature must be a base58 transaction signature (64-88 chars) or key (32-44 chars)",
  );
}

mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "LAUNCH.json");
copyFileSync(launchPath, outPath);
const copied = readFileSync(outPath);
if (!copied.equals(raw)) {
  fail("copied LAUNCH.json differs from the source");
}
console.log(
  `TOPFUN main.ts: LAUNCH.json copied to ${outPath} (${raw.length} bytes, mint ${mint})`,
);
