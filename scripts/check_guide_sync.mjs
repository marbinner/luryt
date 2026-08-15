// Checks that the interactive guide (docs/index.html) agrees with the
// canonical language data (src/conlang_tools/data/language.json).
//
// The guide intentionally rewords glosses for teaching, so only structural
// facts are compared: alphabets, root spellings and their matrix cells, and
// particle forms per series.
//
// Usage: node scripts/check_guide_sync.mjs

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const canon = JSON.parse(
  readFileSync(join(repo, "src/conlang_tools/data/language.json"), "utf8")
);
const html = readFileSync(join(repo, "docs/index.html"), "utf8");
const js = html.match(/<script>([\s\S]*)<\/script>/)[1];

// Run the guide script with a stub DOM so only the data definitions matter.
const noopEl = new Proxy(function () {}, {
  get: (t, p) => {
    if (p === "innerHTML" || p === "value") return "";
    if (p === "querySelectorAll") return () => [];
    return noopEl;
  },
  apply: () => noopEl,
});
const documentStub = new Proxy(
  {},
  { get: (t, p) => (p === "querySelectorAll" ? () => [] : () => noopEl) }
);
const guide = new Function(
  "document",
  "window",
  js + "\nreturn {CONS, VOWS, NVOWS, FINALS, ROOTS, SERIES};"
)(documentStub, {});

const failures = [];
const eq = (name, a, b) => {
  if (JSON.stringify(a) !== JSON.stringify(b))
    failures.push(`${name}:\n  guide: ${JSON.stringify(a)}\n  canon: ${JSON.stringify(b)}`);
};

eq("consonant order", guide.CONS.toUpperCase(), canon.consonants);
eq("vowel order", guide.VOWS.toUpperCase(), canon.vowels);
eq("numeric vowels", guide.NVOWS.toUpperCase(), canon.numeric_vowels);
eq("final consonants", [...guide.FINALS.toUpperCase()].sort(), [...canon.final_consonants].sort());

const guideRoots = Object.keys(guide.ROOTS).map((r) => r.toUpperCase()).sort();
eq("root inventory", guideRoots, Object.keys(canon.core_roots).sort());

for (const [root, info] of Object.entries(canon.core_roots)) {
  const g = root.toLowerCase();
  if (guide.ROOTS[g] && (root[1] !== info.domain || root[3] !== info.aspect))
    failures.push(`root ${root}: canonical cell ${info.domain}x${info.aspect} disagrees with spelling`);
}

const bySeries = (entries) =>
  Object.fromEntries(entries.sort((a, b) => a[0].localeCompare(b[0])));
const guideSeries = bySeries(
  guide.SERIES.map((s) => [s.c.toUpperCase(), s.rows.map((r) => r[0].toUpperCase())])
);
const canonSeries = bySeries(
  Object.entries(canon.particle_series).map(([c, forms]) => [c, Object.keys(forms)])
);
eq("particle series", guideSeries, canonSeries);

if (failures.length) {
  console.error("guide/data sync check FAILED:\n\n" + failures.join("\n\n"));
  process.exit(1);
}
console.log(
  `guide/data sync check passed: ${guideRoots.length} roots, ` +
    `${Object.keys(canonSeries).length} series, alphabets match.`
);
