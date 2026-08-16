// Checks that the interactive guide (docs/index.html) agrees with the
// canonical language data (src/conlang_tools/data/language.json).
//
// Structural inventories and canonical semantic labels are contracts. Longer
// teaching glosses may be reworded, but pronunciations, head/domain/aspect
// names, root glosses, fixed atoms, and particle meanings must not drift.
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
const converterElements = Object.fromEntries(
  ["#n2cv", "#n2cvOut", "#cv2n", "#cv2nOut"].map((selector) => [
    selector,
    {
      innerHTML: "",
      value: "",
      listeners: {},
      addEventListener(event, listener) {
        this.listeners[event] = listener;
      },
    },
  ])
);
const documentStub = new Proxy(
  {},
  {
    get: (t, p) => {
      if (p === "querySelectorAll") return () => [];
      if (p === "querySelector")
        return (selector) => converterElements[selector] ?? noopEl;
      return () => noopEl;
    },
  }
);
const guide = new Function(
  "document",
  "window",
  js + "\nreturn {CONS, VOWS, NVOWS, NUM_BASE, FINALS, CONS_INFO, VOW_INFO, " +
    "SUFF, DOMS, ASPS, ROOTS, SERIES, ATOMS, parseWord};"
)(documentStub, {});

const failures = [];
const eq = (name, a, b) => {
  if (JSON.stringify(a) !== JSON.stringify(b))
    failures.push(`${name}:\n  guide: ${JSON.stringify(a)}\n  canon: ${JSON.stringify(b)}`);
};

eq("consonant order", guide.CONS.toUpperCase(), canon.consonants);
eq("vowel order", guide.VOWS.toUpperCase(), canon.vowels);
eq("numeric vowels", guide.NVOWS.toUpperCase(), canon.numeric_vowels);
eq("numeral base", guide.NUM_BASE, canon.numeral_base);
eq("final consonants", [...guide.FINALS.toUpperCase()].sort(), [...canon.final_consonants].sort());

const pronunciationMap = (rows) =>
  Object.fromEntries(rows.map(([form, ipa]) => [form.toUpperCase(), `/${ipa}/`]));
eq("consonant IPA", pronunciationMap(guide.CONS_INFO), canon.consonant_ipa);
eq("vowel IPA", pronunciationMap(guide.VOW_INFO), canon.vowel_ipa);

const guidePrimary = (entries, upper = false) =>
  Object.fromEntries(
    Object.entries(entries).map(([form, values]) => [
      form.toUpperCase(),
      upper ? values[0].toUpperCase() : values[0],
    ])
  );
const canonicalPrimary = (entries) =>
  Object.fromEntries(
    Object.entries(entries).map(([form, values]) => [form, values[0]])
  );
eq("head-kind labels", guidePrimary(guide.SUFF), canonicalPrimary(canon.head_kinds));
eq("domain labels", guidePrimary(guide.DOMS, true), canonicalPrimary(canon.domains));
eq("aspect labels", guidePrimary(guide.ASPS, true), canonicalPrimary(canon.aspects));

const guideAtoms = Object.fromEntries(
  Object.entries(guide.ATOMS).map(([form, values]) => [form.toUpperCase(), values])
);
eq("fixed atomic words", guideAtoms, canon.atomic_words);
const parsedNum = guide.parseWord("num");
eq("num parser type", parsedNum?.type, "atomic");
eq("num parser numeric value", parsedNum?.numval, null);
eq("num parser errors", parsedNum?.errors, []);

const converterOutput = (inputSelector, outputSelector, value) => {
  const input = converterElements[inputSelector];
  const output = converterElements[outputSelector];
  output.innerHTML = "";
  input.listeners.input({ target: { value } });
  return output.innerHTML;
};
const includes = (name, actual, expected) => {
  if (!actual.includes(expected))
    failures.push(name + ": expected output to contain " + JSON.stringify(expected));
};
includes(
  "guide converter encodes 100",
  converterOutput("#n2cv", "#n2cvOut", "100"),
  "num py pi"
);
includes(
  "guide converter encodes 12345678",
  converterOutput("#n2cv", "#n2cvOut", "12345678"),
  "num me do ly ja"
);
includes(
  "guide converter decodes 10001",
  converterOutput("#cv2n", "#cv2nOut", "py pi py"),
  ">10001<"
);
includes(
  "guide converter rejects a leading zero",
  converterOutput("#cv2n", "#cv2nOut", "pi py"),
  "cannot start with pi"
);
includes(
  "guide converter rejects U-vowel blocks",
  converterOutput("#cv2n", "#cv2nOut", "py qu"),
  "each block needs"
);

const guideRoots = Object.keys(guide.ROOTS).map((r) => r.toUpperCase()).sort();
eq("root inventory", guideRoots, Object.keys(canon.core_roots).sort());

for (const [root, info] of Object.entries(canon.core_roots)) {
  const g = root.toLowerCase();
  if (guide.ROOTS[g] && (root[1] !== info.domain || root[3] !== info.aspect))
    failures.push(`root ${root}: canonical cell ${info.domain}x${info.aspect} disagrees with spelling`);
  eq(`${root} primary gloss`, guide.ROOTS[g]?.[0], info.gloss);
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

for (const [series, particles] of Object.entries(canon.particle_series)) {
  const guideRows = guide.SERIES.find(
    (item) => item.c.toUpperCase() === series
  )?.rows;
  for (const [form, [meaning]] of Object.entries(particles)) {
    const guideRow = guideRows?.find((row) => row[0].toUpperCase() === form);
    eq(`${form} semantic label`, guideRow?.[1], meaning);
  }
}

if (failures.length) {
  console.error("guide/data sync check FAILED:\n\n" + failures.join("\n\n"));
  process.exit(1);
}
console.log(
  `guide/data sync check passed: ${guideRoots.length} roots, ` +
    `${Object.keys(canonSeries).length} series, structural and semantic contracts match.`
);
