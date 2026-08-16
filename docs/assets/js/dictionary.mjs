const $ = selector => document.querySelector(selector);
const esc = value => String(value)
  .replace(/&/g, "&amp;")
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;");
const lower = value => String(value).toLowerCase();

const LANGUAGE_URL = new URL("../../data/language.json", import.meta.url);
let language;
try {
  const response = await fetch(LANGUAGE_URL);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  language = await response.json();
} catch (error) {
  $("#snapshot").textContent = "Language data unavailable";
  $("#resultCount").textContent = "Dictionary unavailable";
  $("#entries").removeAttribute("aria-busy");
  $("#entries").innerHTML = `
    <article class="entry">
      <h2 class="form">Unable to load dictionary</h2>
      <p class="detail">The generated language bundle could not be read. Please refresh the page.</p>
    </article>`;
  throw new Error(`Could not load ${LANGUAGE_URL}: ${error}`);
}

const domainName = code => language.domains[code]?.[0] ?? code;
const aspectName = code => language.aspects[code]?.[0] ?? code;
const headName = code => language.head_kinds[code]?.[0] ?? code;
const entries = [];

for (const [suffix, [label, gloss]] of Object.entries(language.head_kinds)) {
  entries.push({
    id: `head-${lower(suffix)}`,
    form: `-${lower(suffix)}`,
    kind: "head",
    definition: label,
    detail: gloss,
    meta: ["word-building suffix"],
  });
}

for (const [series, forms] of Object.entries(language.particle_series)) {
  const seriesName = language.particle_series_metadata[series].name;
  for (const [form, [label, gloss]] of Object.entries(forms)) {
    const prefixGloss = language.derivational_prefixes[form];
    entries.push({
      id: `particle-${lower(form)}`,
      form: lower(form),
      kind: "particle",
      definition: label,
      detail: prefixGloss
        ? `${gloss}. Bound-prefix use: ${prefixGloss}.`
        : gloss,
      meta: [`${series}-series · ${seriesName}`, ...(prefixGloss ? ["also a prefix"] : [])],
    });
  }
}

for (const [form, [label, gloss]] of Object.entries(language.atomic_words)) {
  entries.push({
    id: `atom-${lower(form)}`,
    form: lower(form),
    kind: "atom",
    definition: label,
    detail: gloss,
    meta: ["fixed atomic word"],
  });
}

for (const [form, root] of Object.entries(language.core_roots)) {
  const productiveForms = [...language.final_consonants].map(
    suffix => lower(form + suffix)
  );
  entries.push({
    id: `root-${lower(form)}`,
    form: lower(form),
    kind: "root",
    definition: root.gloss,
    detail: `Semantic range: ${root.semantic_range}.`,
    domain: root.domain,
    aspect: root.aspect,
    meta: [
      `${root.domain} · ${domainName(root.domain)}`,
      `${root.aspect} · ${aspectName(root.aspect)}`,
    ],
    productiveForms,
  });
}

for (const lexeme of language.lexemes) {
  const root = language.core_roots[lexeme.analysis.root];
  entries.push({
    id: lexeme.id.replace(/[^a-z0-9_-]/g, "-"),
    form: lower(lexeme.form),
    kind: "lexeme",
    definition: lexeme.senses[0].definition,
    detail: `${lower(lexeme.analysis.root)} + -${lower(lexeme.analysis.head)} · ${headName(lexeme.analysis.head)}`,
    domain: root.domain,
    aspect: root.aspect,
    meta: [`${domainName(root.domain)} × ${aspectName(root.aspect)}`],
    senses: lexeme.senses,
  });
}

const kindOrder = {lexeme: 0, root: 1, particle: 2, atom: 3, head: 4};
entries.sort((left, right) =>
  left.form.localeCompare(right.form) || kindOrder[left.kind] - kindOrder[right.kind]
);
for (const entry of entries) {
  entry.searchText = lower([
    entry.form,
    entry.definition,
    entry.detail,
    ...(entry.meta ?? []),
    ...(entry.productiveForms ?? []),
    ...(entry.senses ?? []).flatMap(sense => [
      sense.definition,
      sense.gloss,
      sense.notes ?? "",
    ]),
  ].join(" "));
}

function addOptions(selector, source) {
  const select = $(selector);
  for (const [code, [label]] of Object.entries(source)) {
    const option = document.createElement("option");
    option.value = code;
    option.textContent = `${code.toLowerCase()} · ${label.toLowerCase()}`;
    select.append(option);
  }
}
addOptions("#domain", language.domains);
addOptions("#aspect", language.aspects);

const filters = {
  query: $("#query"),
  kind: $("#kind"),
  domain: $("#domain"),
  aspect: $("#aspect"),
};
const params = new URLSearchParams(location.search);
for (const [name, input] of Object.entries(filters)) {
  input.value = params.get(name === "query" ? "q" : name) ?? "";
}

function renderSenses(senses) {
  if (!senses) return "";
  return senses.map(sense => `
    <div class="sense">
      <span class="sense-status">${esc(sense.status)} · established</span>
      <p class="definition">${esc(sense.definition)}</p>
      <p class="detail"><b>${esc(sense.gloss)}</b>${sense.notes ? ` · ${esc(sense.notes)}` : ""}</p>
    </div>`).join("");
}

function renderEntry(entry) {
  const metadata = entry.meta?.length
    ? `<div class="meta">${entry.meta.map(item => `<span>${esc(item)}</span>`).join("")}</div>`
    : "";
  const productive = entry.productiveForms
    ? `<div class="forms">${entry.productiveForms.map(form => `<code>${esc(form)}</code>`).join("")}</div>`
    : "";
  const mainDefinition = entry.senses
    ? renderSenses(entry.senses)
    : `<p class="definition">${esc(entry.definition)}</p><p class="detail">${esc(entry.detail)}</p>`;
  return `
    <article class="entry" id="${esc(entry.id)}">
      <div class="entry-head">
        <h2 class="form">${esc(entry.form)}</h2>
        <span class="badge ${esc(entry.kind)}">${esc(entry.kind)}</span>
      </div>
      ${mainDefinition}
      ${metadata}
      ${productive}
    </article>`;
}

function updateUrl() {
  const next = new URLSearchParams();
  if (filters.query.value.trim()) next.set("q", filters.query.value.trim());
  for (const name of ["kind", "domain", "aspect"]) {
    if (filters[name].value) next.set(name, filters[name].value);
  }
  const query = next.toString();
  history.replaceState(null, "", query ? `?${query}` : location.pathname);
}

function render() {
  const terms = lower(filters.query.value).trim().split(/\s+/).filter(Boolean);
  const matches = entries.filter(entry =>
    (!filters.kind.value || entry.kind === filters.kind.value)
    && (!filters.domain.value || entry.domain === filters.domain.value)
    && (!filters.aspect.value || entry.aspect === filters.aspect.value)
    && terms.every(term => entry.searchText.includes(term))
  );
  $("#entries").innerHTML = matches.map(renderEntry).join("");
  $("#resultCount").textContent =
    `${matches.length} ${matches.length === 1 ? "entry" : "entries"} shown`;
  $("#empty").hidden = matches.length !== 0;
  updateUrl();
}

for (const input of Object.values(filters)) {
  input.addEventListener(input.tagName === "INPUT" ? "input" : "change", render);
}
$("#clear").addEventListener("click", () => {
  for (const input of Object.values(filters)) input.value = "";
  filters.query.focus();
  render();
});

const particleCount = Object.values(language.particle_series)
  .reduce((total, series) => total + Object.keys(series).length, 0);
$("#snapshot").textContent =
  `${Object.keys(language.core_roots).length} roots · ${particleCount} particles · `
  + `${language.lexemes.length} established words`;
$("#schemaVersion").textContent = language.metadata.schema_version;
$("#languageVersion").textContent = language.metadata.language_version;
$("#entries").removeAttribute("aria-busy");
render();
