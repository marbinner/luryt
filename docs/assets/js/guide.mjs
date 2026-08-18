/* ============ canonical data ============ */
const LANGUAGE_URL = new URL("../../data/language.json", import.meta.url);
let LANGUAGE;
try {
  const languageResponse = await fetch(LANGUAGE_URL);
  if (!languageResponse.ok) throw new Error(`HTTP ${languageResponse.status}`);
  LANGUAGE = await languageResponse.json();
} catch (error) {
  document.body.insertAdjacentHTML("afterbegin",
    '<p role="alert" style="margin:0;padding:12px 20px;background:#7d1d1d;color:white;text-align:center">The language data could not be loaded. Please refresh the page.</p>');
  throw new Error(`Could not load ${LANGUAGE_URL}: ${error}`);
}

const languageVersion = document.querySelector("#languageVersion");
if (languageVersion) languageVersion.textContent = LANGUAGE.metadata.language_version;

const lowerPairs = entries => Object.fromEntries(
  Object.entries(entries).map(([form, values]) => [form.toLowerCase(), values])
);
const titleCase = value => value.charAt(0) + value.slice(1).toLowerCase();

const CONS = LANGUAGE.consonants.toLowerCase();
const VOWS = LANGUAGE.vowels.toLowerCase();
const NVOWS = LANGUAGE.numeric_vowels.toLowerCase();
const NUM_BASE = LANGUAGE.numeral_base;
const FINALS = LANGUAGE.final_consonants.toLowerCase();

const CONS_GUIDANCE = {
  p:["as in pat"],b:["as in bat"],m:["as in man"],f:["as in fan"],
  v:["as in van"],t:["as in top"],d:["as in dog"],n:["as in net"],
  q:["“ts” as in cats",1],s:["as in sun"],z:["as in zoo"],l:["as in let"],
  c:["“ch” as in church",1],w:["“j” as in jam",1],x:["“sh” as in shoe",1],
  j:["“y” as in yes",1],k:["as in kite"],g:["as in go"],
  r:["French/German throat r",1],h:["as in hat"]
};
const VOWEL_GUIDANCE = {
  i:"as in machine",y:"German ü — say “ee”, round your lips",
  e:"as in they (pure)",a:"as in father",o:"as in go (pure)",u:"as in moon"
};
const CONS_INFO = [...CONS].map(form => {
  const [hint, trap] = CONS_GUIDANCE[form];
  return [form, LANGUAGE.consonant_ipa[form.toUpperCase()].slice(1,-1), hint, trap];
});
const VOW_INFO = [...VOWS].map(form => [
  form,
  LANGUAGE.vowel_ipa[form.toUpperCase()].slice(1,-1),
  VOWEL_GUIDANCE[form]
]);

const SUFF = lowerPairs(LANGUAGE.head_kinds);
const DOMS = Object.fromEntries(Object.entries(LANGUAGE.domains).map(
  ([form, [label, gloss]]) => [form.toLowerCase(), [titleCase(label), gloss]]
));
const ASPS = Object.fromEntries(Object.entries(LANGUAGE.aspects).map(
  ([form, [label, gloss]]) => [form.toLowerCase(), [titleCase(label), gloss]]
));
const ROOTS = Object.fromEntries(Object.entries(LANGUAGE.core_roots).map(
  ([form, root]) => [form.toLowerCase(), [root.gloss, root.semantic_range]]
));
const ATOMS = lowerPairs(LANGUAGE.atomic_words);
const K_PREFIX = Object.fromEntries(Object.entries(LANGUAGE.derivational_prefixes).map(
  ([form, gloss]) => [form.toLowerCase(), gloss]
));

// These are teaching-layout choices, not normative language facts.
const SERIES_UI = {
  j:{grp:0,scale:"me → them",note:"No gender anywhere: <span class='lx'>jo</span> covers he, she and it."},
  d:{grp:0,scale:"near → far, one → many",note:"Read the vowels in pairs: <span class='lx'>i/y</span> near, <span class='lx'>e/a</span> in view, <span class='lx'>o/u</span> elsewhere — first of each pair singular, second plural."},
  w:{grp:0,scale:"when → how",note:"A question word opens the clause. A pivot is bare: <span class='lx'>wo zifen?</span> “who speaks?” A nonpivot keeps its role: <span class='lx'>wa re ji nifen?</span> “what do I eat?”"},
  t:{grp:1,scale:"long ago → timeless",note:"<span class='lx'>tu</span> is for timeless truths: “water flows”."},
  p:{grp:1,scale:"just starting → already done",note:"Combines freely with time: <span class='lx'>ti pu</span> “had already …”."},
  h:{grp:1,scale:"once → always",note:""},
  n:{grp:1,scale:"yes → never",note:"These double as one-word answers: <span class='lx'>ni. na. no. nu.</span>"},
  q:{grp:2,scale:"none → every single one",note:"<span class='lx'>qo</span> takes the group as one mass; <span class='lx'>qu</span> goes one by one."},
  m:{grp:2,scale:"barely → too much",note:""},
  c:{grp:2,scale:"at least → as much as possible",note:"Pairs with <span class='lx'>re</span> “than”: see chapter 07."},
  r:{grp:3,scale:"doer → path closer",note:"Normally placed <em>after</em> a noun phrase, like <span class='lx'>tokim ra</span> “with a tool”. In a path, <span class='lx'>ru</span> closes the full G (S) ground frame."},
  s:{grp:3,scale:"inside → among",note:"Static on its own; traces a path when the verb moves."},
  g:{grp:3,scale:"origin → return",note:"Orients a motion path; <span class='lx'>ru</span> closes the whole path phrase: <span class='lx'>ji go si di koryt ru pasen</span> — “I go into this house.”"},
  k:{grp:3,scale:"single → scattered",note:"Also a prefix — the only one so far: <span class='lx'>kypirim</span> “a pair of people”, <span class='lx'>kokatim</span> “a mass of rock”, <span class='lx'>kufenim</span> “animals scattered everywhere”."}
};
const SERIES_ORDER = "jdwtphnqmcrsgk";
const SERIES = [...SERIES_ORDER].map(c => {
  const canonical = c.toUpperCase();
  const ui = SERIES_UI[c];
  return {
    c,
    name: LANGUAGE.particle_series_metadata[canonical].name,
    grp: ui.grp,
    scale: ui.scale,
    rows: Object.entries(LANGUAGE.particle_series[canonical]).map(
      ([form, [label, gloss]]) => [form.toLowerCase(), label, gloss]
    ),
    note: ui.note
  };
});
const GROUPS = [
  ["People & pointing","who’s talking, and about which things"],
  ["The verb’s dashboard","when, how far along, how often, whether at all"],
  ["How much","amounts, intensity, and comparison"],
  ["Links, places, groups","roles in the event, positions in space, shapes of collections"]
];

/* ============ helpers ============ */
const $ = s => document.querySelector(s);
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function colorize(w){ // wrap vowels in colored spans
  return [...w].map(ch => VOWS.includes(ch) ? `<span class="cv-${ch}">${ch}</span>` : esc(ch)).join("");
}
const PARTICLES = {};
SERIES.forEach(s => s.rows.forEach(([f,v,g]) => PARTICLES[f] = {series:s.c, name:s.name, val:v, gloss:g}));

/* ============ responsive teaching diagrams ============ */
const ddSeries = c => SERIES.find(s => s.c === c);
const ddVColor = v => `var(--v${v.toUpperCase()})`;
const ddHead = (kicker,title,copy) => `
  <div class="dd-head">
    <div><span class="dd-kicker">${esc(kicker)}</span><div class="dd-title">${title}</div></div>
    <p class="dd-copy">${copy}</p>
  </div>`;
const ddShortRoot = r => ROOTS[r][0].split(",")[0].replace(/^to be /,"be ").replace(/^to /,"");
const ddRootsAt = (position,vowel,limit=3) =>
  Object.keys(ROOTS).filter(r => r[position] === vowel).slice(0,limit);
const ddRootPills = roots => `<div class="dd-rootlist">${roots.map(r =>
  `<span class="dd-root"><b>${colorize(r)}</b>${esc(ddShortRoot(r))}</span>`).join("")}</div>`;
const ddTokens = words => `<div class="dd-tokenrow">${words.map(([form,gloss]) =>
  `<span class="dd-token"><b>${colorize(form)}</b><small>${esc(gloss)}</small></span>`).join("")}</div>`;
const ddRows = series => `<div class="dd-rows">${series.rows.map(([f,v,g]) =>
  `<div class="dd-row" style="--ddc:${ddVColor(f[1])}"><span class="f">${colorize(f)}</span><span class="v">${esc(v)}</span><span class="g">${esc(g)}</span></div>`).join("")}</div>`;
const ddArt = (file,cls="") =>
  `<div class="dd-art ${cls}"><img src="assets/illustrations/${file}" alt="" loading="lazy" decoding="async"></div>`;
function ddNumeral(n){
  return CONS[Math.floor(n/5)] + NVOWS[n%5];
}
function ddSpatialGlyph(form){
  const common = `<svg viewBox="0 0 160 94" aria-hidden="true">`;
  const shapes = {
    si:`<rect class="ground" x="38" y="12" width="84" height="70" rx="7"/><circle class="figure" cx="80" cy="47" r="13"/>`,
    sy:`<rect class="ground" x="43" y="55" width="74" height="29" rx="5"/><circle class="figure" cx="80" cy="42" r="13"/>`,
    se:`<rect class="ground" x="28" y="25" width="62" height="57" rx="6"/><circle class="figure" cx="116" cy="54" r="13"/>`,
    sa:`<rect class="ground" x="61" y="33" width="38" height="34" rx="5"/><ellipse class="guide" cx="80" cy="50" rx="61" ry="37"/><circle class="figure" cx="130" cy="28" r="11"/>`,
    so:`<rect class="ground" x="35" y="18" width="72" height="64" rx="7"/><path class="guide" d="M27 10h88a9 9 0 0 1 9 9v66"/><circle class="figure" cx="137" cy="70" r="12"/>`,
    su:`<rect class="ground" x="18" y="17" width="30" height="25" rx="4"/><rect class="ground" x="111" y="19" width="30" height="25" rx="4"/><rect class="ground" x="25" y="62" width="30" height="24" rx="4"/><rect class="ground" x="106" y="61" width="30" height="24" rx="4"/><circle class="figure" cx="80" cy="50" r="13"/>`
  };
  return `<div class="dd-glyph">${common}${shapes[form]}</svg></div>`;
}

const DD_RENDERERS = {
  overview(){
    const dots = Array.from({length:36},() => "<i></i>").join("");
    return `
      ${ddHead("system map","Four layers, one computation","Every symbol has a fixed job. Read left to right to see sound become meaning, then a word, then a clause.")}
      <div class="dd-counts">
        <div class="dd-count"><b>20 + 6</b><span>consonants + vowels</span></div>
        <div class="dd-count"><b>6 × 6</b><span>semantic root cells</span></div>
        <div class="dd-count"><b>6</b><span>content-word endings</span></div>
        <div class="dd-count"><b>14 × 6</b><span>particle forms</span></div>
      </div>
      <div class="dd-flow">
        <div class="dd-card dd-step" data-v="i"><span class="dd-num">01 · SOUND</span>
          <div class="dd-card-head"><span class="dd-code">CV</span><span><b class="dd-name">legal syllables</b><span class="dd-meta">p…h · i…u</span></span></div>
          <p class="dd-desc"><span class="lx">ka · pi · rim</span><br>no vowel onset; no consonant cluster</p>
        </div>
        <div class="dd-card dd-step" data-v="y"><span class="dd-num">02 · ROOT ADDRESS</span>
          <div class="dd-mini-matrix">${dots}</div>
          <p class="dd-desc"><span class="lx">p<span class="cv-i">i</span>r<span class="cv-i">i</span></span> = Person × Individual → person</p>
        </div>
        <div class="dd-card dd-step" data-v="e"><span class="dd-num">03 · WORD ASSEMBLY</span>
          <div class="dd-form"><span class="cv-a">ka</span> + <span class="cv-i">piri</span> + m<br>→ <b>kapirim</b></div>
          <p class="dd-desc">group + person + entity → a crowd</p>
        </div>
        <div class="dd-card dd-step" data-v="o"><span class="dd-num">04 · CLAUSE TRACK</span>
          ${ddTokens([["te","now"],["py","in progress"],["na","not"],["ji","I"],["zifen","speak"]])}
          <p class="dd-desc" style="margin-top:6px">operators → pivot → <b>event last</b></p>
        </div>
      </div>`;
  },

  sounds(){
    const consonants = CONS_INFO.map(([letter,ipa,hint,trap],i) => `
      <div class="dd-sound" title="${esc(hint)}">
        <span class="letter">${letter}</span><span class="ipa">/${esc(ipa)}/${trap ? " · !" : ""}</span>
        <span class="hint">${esc(hint)}</span><span class="index">${i}</span>
      </div>`).join("");
    const vowels = VOW_INFO.map(([letter,ipa,hint]) => `
      <div class="dd-vowel dd-card" data-v="${letter}"><b>${letter}</b><span>/${esc(ipa)}/ · ${esc(hint)}</span></div>`).join("");
    const traps = CONS_INFO.filter(x => x[3]).map(x => `<span class="lx">${x[0]} /${esc(x[1])}/</span>`).join(" · ");
    return `
      ${ddHead("complete inventory","26 sounds in canonical order","The tiny corner number is the consonant’s numeral index. An exclamation mark flags letters whose sound may surprise an English reader.")}
      <div class="dd-sounds">${consonants}</div>
      <div class="dd-vowels">${vowels}</div>
      <div class="dd-grid two" style="margin-top:10px">
        <div class="dd-card" data-v="i"><div class="dd-card-head"><span class="dd-code">CV(C)</span><span><b class="dd-name">syllable shape</b><span class="dd-meta">open or one final</span></span></div>
          <div class="dd-form">ka · pi · rim &nbsp; / &nbsp; zi · fen</div><p class="dd-detail">Never begins with a vowel. Consonants never cluster.</p></div>
        <div class="dd-card" data-v="o"><div class="dd-card-head"><span class="dd-code">ˈ</span><span><b class="dd-name">automatic stress</b><span class="dd-meta">first root syllable</span></span></div>
          <div class="dd-form">ka · <b>PI</b> · rim</div><p class="dd-detail">English traps: ${traps}</p></div>
      </div>`;
  },

  word(){
    return `
      ${ddHead("content-word anatomy","One legal cut, read outside-in","A content word has one four-letter root, exactly one final ending, and zero or more two-letter prefixes.")}
      <div class="dd-form big">(CV)* &nbsp;+&nbsp; C<span class="cv-i">V₁</span>C<span class="cv-o">V₂</span> &nbsp;+&nbsp; { m · t · n · s · l · r }</div>
      <div class="dd-formula">
        <div class="dd-seg"><b class="cv-a">ka</b><span>prefix · group</span></div><span class="dd-op">+</span>
        <div class="dd-seg"><b class="cv-i">piri</b><span>root · person</span></div><span class="dd-op">+</span>
        <div class="dd-seg"><b>m</b><span>ending · entity</span></div><span class="dd-op">→</span>
        <div class="dd-seg"><b>kapirim</b><span>a crowd</span></div>
      </div>
      <div class="dd-grid two">
        <div class="dd-card" data-v="e">
          <div class="dd-card-head"><span class="dd-code">read</span><span><b class="dd-name">deterministic algorithm</b><span class="dd-meta">from the right edge</span></span></div>
          <div class="dd-rows">
            <div class="dd-row"><span class="f">1</span><span class="v">last letter</span><span class="g"><b>m</b> is a legal ending</span></div>
            <div class="dd-row"><span class="f">2</span><span class="v">previous four</span><span class="g"><b>piri</b> is the root</span></div>
            <div class="dd-row"><span class="f">3</span><span class="v">remainder</span><span class="g"><b>ka</b> is one CV prefix</span></div>
          </div>
        </div>
        <div class="dd-card" data-v="u">
          <div class="dd-card-head"><span class="dd-code">why</span><span><b class="dd-name">the seams are unique</b><span class="dd-meta">shape carries structure</span></span></div>
          <p class="dd-desc">Particle-family forms are exactly CV; <span class="lx">num</span> is the sole longer fixed atom. Roots are exactly CVCV. Only six consonants can close content words. Every leftover prefix is read two letters at a time.</p>
          <div class="dd-note">Guide notation <span class="lx">ka-piri-m</span> exposes the seams; normal writing is solid: <span class="lx">kapirim</span>.</div>
        </div>
      </div>`;
  },

  endings(){
    const cards = Object.entries(SUFF).map(([s,[name,desc]],i) => `
      <div class="dd-card" data-v="${VOWS[i]}">
        <div class="dd-card-head"><span class="dd-code">−${s}</span><span><b class="dd-name">${esc(name)}</b><span class="dd-meta">${colorize("zife"+s)}</span></span></div>
        <p class="dd-desc">${esc(desc)}</p>
        <p class="dd-detail"><span class="lx">zife</span> “speak / talk” + <b class="lx">−${s}</b> → <b class="lx">${colorize("zife"+s)}</b></p>
      </div>`).join("");
    return `
      ${ddHead("six grammatical lenses","One root enters a clause six ways","The semantic neighborhood stays “speech”; the last consonant declares the result’s grammatical kind.")}
      <div class="dd-formula"><div class="dd-seg"><b class="cv-e">zife</b><span>speech root</span></div><span class="dd-op">×</span><div class="dd-seg"><b>6 endings</b><span>one required</span></div></div>
      <div class="dd-grid six">${cards}</div>`;
  },

  domains(){
    const cards = [...VOWS].map(v => `
      <div class="dd-card" data-v="${v}">
        <div class="dd-card-head"><span class="dd-code">${v}−</span><span><b class="dd-name">${esc(DOMS[v][0])}</b><span class="dd-meta">first root vowel · V₁</span></span></div>
        ${ddArt(`scene-domain-${v}.webp`,"dd-domain-art")}
        <p class="dd-desc">${esc(DOMS[v][1])}</p>
        ${ddRootPills(ddRootsAt(1,v,3))}
      </div>`).join("");
    return `
      ${ddHead("coordinate 1 of 2","First vowel chooses the world","Read C–V₁–C–V₂: the first vowel sets the broad semantic domain; the second will choose an aspect inside it.")}
      <div class="dd-form" style="margin-bottom:10px">C <b>V₁</b> C V₂ → Person · Society · Life · Physical · Artefact · Abstract</div>
      <div class="dd-grid six">${cards}</div>`;
  },

  aspects(){
    const cards = [...VOWS].map(v => `
      <div class="dd-card" data-v="${v}">
        <div class="dd-card-head"><span class="dd-code">−${v}</span><span><b class="dd-name">${esc(ASPS[v][0])}</b><span class="dd-meta">second root vowel · V₂</span></span></div>
        <div class="dd-form">C V₁ C <b style="color:${ddVColor(v)}">${v}</b></div>
        <p class="dd-desc" style="margin-top:7px">${esc(ASPS[v][1])}</p>
        ${ddRootPills(ddRootsAt(3,v,3))}
      </div>`).join("");
    return `
      ${ddHead("coordinate 2 of 2","Second vowel chooses the angle","The same six aspects repeat across every domain, turning each row of the lexicon into a predictable conceptual family.")}
      <div class="dd-form" style="margin-bottom:10px">C V₁ C <b>V₂</b> → Individual · Config · Process · State · Relation · Quantity</div>
      <div class="dd-grid six">${cards}</div>`;
  },

  grid(){
    const byCell = {};
    Object.keys(ROOTS).forEach(r => byCell[r[1]+r[3]] = r);
    let matrix = `<div class="dd-matrix"><div class="dd-mx-head"><b>V₁ ↓</b><span>domain / aspect →</span></div>`;
    for (const a of VOWS) matrix += `<div class="dd-mx-head" style="border-top:3px solid ${ddVColor(a)}"><b style="color:${ddVColor(a)}">${a}</b><span>${esc(ASPS[a][0])}</span></div>`;
    for (const d of VOWS){
      matrix += `<div class="dd-mx-row" style="border-left:3px solid ${ddVColor(d)}"><b style="color:${ddVColor(d)}">${d}</b><span>${esc(DOMS[d][0])}</span></div>`;
      for (const a of VOWS){
        const r = byCell[d+a];
        matrix += `<div class="dd-mx-cell" style="--ddc:${ddVColor(a)}"><b>${colorize(r)}</b><span>${esc(ddShortRoot(r))}</span></div>`;
      }
    }
    matrix += "</div>";
    return `
      ${ddHead("all 36 addresses","The complete semantic map","Rows are first-vowel domains; columns are second-vowel aspects. Every cell already has one root, shown with a compact gloss.")}
      <div class="dd-scroll">${matrix}</div>
      <div class="dd-grid three" style="margin-top:10px">
        <div class="dd-card" data-v="i"><div class="dd-form"><b>p-i-r-i</b></div><p class="dd-detail">Person × Individual → person</p></div>
        <div class="dd-card" data-v="e"><div class="dd-form"><b>p-a-s-e</b></div><p class="dd-detail">Physical × Process → move / flow</p></div>
        <div class="dd-card" data-v="u"><div class="dd-form"><b>b-y-r-u</b></div><p class="dd-detail">Society × Quantity → wealth</p></div>
      </div>`;
  },

  time(){
    const s = ddSeries("t");
    const cards = s.rows.map(([f,v,g]) => `
      <div class="dd-card dd-time" data-v="${f[1]}" style="--ddc:${ddVColor(f[1])}">
        <div class="dd-card-head"><span class="dd-code">${colorize(f)}</span><span><b class="dd-name">${esc(g)}</b><span class="dd-meta">${esc(v)}</span></span></div>
        <div class="dd-form">${colorize(f)} + zifen</div>
      </div>`).join("");
    return `
      ${ddHead("T-family · six values","Place an event in time","Five values run from remote past through future. The sixth, tu, leaves the timeline for general or timeless truths.")}
      <div class="dd-scroll"><div class="dd-timeline">${cards}</div></div>
      <div class="dd-note"><span class="lx">te py ji zifen</span> = now + in-progress + I + speak. Time comes before phase; <span class="lx">tu</span> is gnomic, not “later than <span class="lx">to</span>.”</div>`;
  },

  grouping(){
    const s = ddSeries("k");
    const cards = s.rows.map(([f,v,g]) => `
      <div class="dd-card" data-v="${f[1]}">
        <div class="dd-card-head"><span class="dd-code">${colorize(f)}</span><span><b class="dd-name">${esc(g)}</b><span class="dd-meta">${esc(v)}</span></span></div>
        <div class="dd-form">${colorize(f)} + pirim → <b>${colorize(f+"pirim")}</b></div>
        <p class="dd-detail">${esc(K_PREFIX[f])}</p>
      </div>`).join("");
    return `
      ${ddHead("K-family · particle and prefix","Six configurations, two altitudes","A spaced K-form precedes a noun phrase and configures its selected participants. The same syllable glued before a root builds a grouped content word.")}
      <div class="dd-grid six">${cards}</div>
      <div class="dd-split" style="margin-top:10px">
        <div class="dd-card" data-v="a"><span class="dd-meta">free particle · space</span><div class="dd-form">ka pirim pasen</div><p class="dd-detail">people travel <b>as a group</b> · configures the participant phrase</p></div>
        <div class="dd-card" data-v="a"><span class="dd-meta">bound prefix · no space</span><div class="dd-form">kapirim pasen</div><p class="dd-detail"><b>a crowd</b> travels · builds the noun</p></div>
      </div>`;
  },

  numbers(){
    const consonants = [...CONS].map((c,i) => `<span class="dd-index"><b>${c}</b><span>${i}</span></span>`).join("");
    const vowels = [...NVOWS].map((v,i) => `<span class="dd-index"><b style="color:${ddVColor(v)}">${v}</b><span>+${i}</span></span>`).join("");
    const examples = [0,27,42,99].map((n,i) => {
      const f = ddNumeral(n), ci = CONS.indexOf(f[0]), vi = NVOWS.indexOf(f[1]);
      return `<div class="dd-card" data-v="${f[1]}"><div class="dd-card-head"><span class="dd-code">${colorize(f)}</span><span><b class="dd-name">${n}</b><span class="dd-meta">5 × ${ci} + ${vi}</span></span></div><div class="dd-form">num ${colorize(f)}</div></div>`;
    }).join("");
    return `
      ${ddHead("base 5 × 20 blocks","One syllable encodes 0–99","The consonant chooses a five-number bank; one of five numeral vowels adds 0–4. One or more blocks after num compose positionally in base 100.")}
      <div class="dd-form big">value = 5 × index(C) + index(V)</div>
      <div class="dd-panel" style="margin-top:9px"><span class="dd-meta">consonant index · bank 0–19</span><div class="dd-index-grid" style="margin-top:7px">${consonants}</div></div>
      <div class="dd-panel" style="margin-top:7px"><span class="dd-meta">numeral vowel index · offset 0–4 · u is not used</span><div class="dd-index-grid" style="grid-template-columns:repeat(5,1fr);margin-top:7px">${vowels}</div></div>
      <div class="dd-grid four" style="margin-top:9px">${examples}</div>
      <div class="dd-note"><span class="lx">te</span> alone is the present-time particle; <span class="lx">num te</span> announces 27. Larger values reuse the same blocks: <span class="lx">num py pi</span> is 100 and <span class="lx">num py pi pi</span> is 10,000. Inside an NP, K/Q/D come before <span class="lx">num</span> and the noun closes the numeral run.</div>`;
  },

  clause(){
    const slots = [
      ["w– (+ r–)","question + role","optional","var(--vY)"],["t–","time","optional","var(--vY)"],["p–","phase","optional","var(--vY)"],
      ["h–","frequency","optional","var(--vY)"],["m–","degree","optional","var(--vY)"],["n–","polarity","optional","var(--vY)"],
      ["pivot","unmarked NP","optional","var(--accent)"],["NP + role / space","other frame","optional","var(--accent)"],
      ["manner−l","event manner","optional · one","var(--vA)"],["na","narrow polarity","optional","var(--vO)"],
      ["event−n","event","required · last","var(--vO)"]
    ];
    const track = slots.map(([f,label,state,color],i) => `<div class="dd-slot" style="--ddc:${color}"><b>${esc(f)}</b><span>${esc(label)}</span><small>${String(i+1).padStart(2,"0")} · ${esc(state)}</small></div>`).join("");
    return `
      ${ddHead("canonical event clause","Operators first; event last","Six optional operator families have a fixed order. After participants and spatial frames, one optional manner and narrow na form the event tail.")}
      <div class="dd-scroll"><div class="dd-clause">${track}</div></div>
      <div class="dd-split" style="margin-top:10px">
        <div class="dd-card" data-v="i"><span class="dd-meta">smallest pivoted · 2 words</span>${ddTokens([["ji","pivot"],["zifen","event"]])}<p class="dd-detail">“I speak.”</p></div>
        <div class="dd-card" data-v="o"><span class="dd-meta">three dials added · 5 words</span>${ddTokens([["te","time"],["py","phase"],["na","polarity"],["ji","pivot"],["zifen","event"]])}<p class="dd-detail">“Right now, I am not speaking.”</p></div>
      </div>
      <div class="dd-note"><span class="lx">ji koryt re tokim ra gusel gosen</span> keeps every participant frame before the single manner slot; <span class="lx">ji gusel na zifen</span> shows the fixed manner + narrow polarity + event tail.</div>`;
  },

  scope(){
    return `
      ${ddHead("same words, different reach","Position changes what “not” controls","Operators bind everything to their right. The matched scenes show one possible world for each reading.")}
      <div class="dd-scene-grid">
        <div class="dd-scene-card" style="--ddc:var(--vO)">
          <div class="dd-scene"><img src="assets/illustrations/scene-scope-not-all.webp" alt="" loading="lazy" decoding="async"></div>
          <div class="dd-scene-copy"><span class="dd-meta">negation scopes over “all”</span><div class="dd-form"><b>na</b> [ qo pirim · pasen ]</div>
          <div class="dd-verdict"><b>&lt; 6</b><span>not everyone goes; zero to five may go</span></div></div>
        </div>
        <div class="dd-scene-card" style="--ddc:var(--vI)">
          <div class="dd-scene"><img src="assets/illustrations/scene-scope-none.webp" alt="" loading="lazy" decoding="async"></div>
          <div class="dd-scene-copy"><span class="dd-meta">“all” scopes over negation</span><div class="dd-form"><b>qo pirim</b> [ na · pasen ]</div>
          <div class="dd-verdict"><b>0 / 6</b><span>the whole group is established; none goes</span></div></div>
        </div>
      </div>`;
  },

  roles(){
    const s = ddSeries("r");
    const scene = {ri:"builder · doer",ry:"recipient · affected experiencer",re:"house · affected object",ra:"hammer · instrument",ro:"building site · location",ru:"footprints · path"};
    const roles = s.rows.map(([f,v,g]) => `<div class="dd-role" style="--ddc:${ddVColor(f[1])}"><b>${colorize(f)}</b><strong>${esc(v)}</strong><span>${esc(g)} · ${esc(scene[f])}</span></div>`).join("");
    return `
      ${ddHead("R-family · six participant links","Read the role after its noun phrase","The scene separates who acts, what is affected, what tool is used, who experiences it, where it happens, and the path through it.")}
      <div class="dd-role-layout">
        <div class="dd-role-art"><img src="assets/illustrations/scene-role-builder.webp" alt="" loading="lazy" decoding="async"></div>
        <div class="dd-role-list">${roles}</div>
      </div>
      <div class="dd-note"><span class="dd-meta">worked clause · pivot may stay unmarked</span>${ddTokens([["ji","I · pivot"],["koryt","house"],["re","object"],["tokim","tool"],["ra","instrument"],["gosen","build"]])}</div>`;
  },

  relations(){
    const s = ddSeries("s");
    const cards = s.rows.map(([f,v,g]) => `
      <div class="dd-card" data-v="${f[1]}">
        <div class="dd-card-head"><span class="dd-code">${colorize(f)}</span><span><b class="dd-name">${esc(v)}</b><span class="dd-meta">${esc(g)}</span></span></div>
        ${ddSpatialGlyph(f)}
        <div class="dd-form">figure · ${colorize(f)} · ground</div>
        <p class="dd-detail">path-neutral: <span class="lx">figure · ${f} ground · pasen</span></p>
      </div>`).join("");
    return `
      ${ddHead("S-family · figure versus ground","Six reusable spatial relations","The colored dot is the figure; the outlined shape or collection is its ground. A G-particle can orient the same relation as a path.")}
      <div class="dd-grid six">${cards}</div>`;
  },

  "space-grammar"(){
    const items = [
      ["i","scene-space-static.webp","static location","S relation stands alone","di pirit · si · di koryt","this person · inside · this house"],
      ["a","scene-space-setting.webp","event setting","ro closes a location role","ji · si di koryt ro · zifen","I · inside this house · speak"],
      ["o","scene-space-path.webp","directed motion","G orients; ru closes the path","ji · go si di koryt ru · pasen","I · into this house · go"]
    ];
    const cards = items.map(([v,img,name,rule,form,gloss]) => `
      <div class="dd-scene-card" style="--ddc:${ddVColor(v)}">
        <div class="dd-scene"><img src="assets/illustrations/${img}" alt="" loading="lazy" decoding="async"></div>
        <div class="dd-scene-copy"><div class="dd-card-head"><span class="dd-code" style="--ddc:${ddVColor(v)};--ddbg:var(--v${v.toUpperCase()}bg)">${v==="i"?"S":v==="a"?"S+ro":"G+S+ru"}</span><span><b class="dd-name">${esc(name)}</b><span class="dd-meta">${esc(rule)}</span></span></div>
        <div class="dd-form">${colorize(form)}</div><p class="dd-detail">${esc(gloss)}</p></div>
      </div>`).join("");
    return `
      ${ddHead("one house, three constructions","Location, setting, or path","The scene stays constant. What changes is the grammatical level at which the spatial relation is closed.")}
      <div class="dd-space-grid">${cards}</div>`;
  },

  questions(){
    const w = ddSeries("w"), c = ddSeries("c");
    return `
      ${ddHead("two six-value scales","Ask for a slot; compare a degree","The W-family names the missing value. A nonpivot participant or event setting keeps its R-role immediately after W; a questioned pivot is bare.")}
      <div class="dd-split">
        <div class="dd-panel">
          <div class="dd-panel-title"><span class="dd-code">w−</span><span><b>Question words</b><span class="dd-meta">missing value → answer</span></span></div>
          ${ddRows(w)}
          <div class="dd-note"><span class="lx">wo zifen?</span> → “who speaks?” · <span class="lx">wa re ji nifen?</span> → “what do I eat?”</div>
        </div>
        <div class="dd-panel">
          <div class="dd-panel-title"><span class="dd-code">c−</span><span><b>Comparison</b><span class="dd-meta">bound → less → equal → more → most → extreme</span></span></div>
          ${ddRows(c)}
          <div class="dd-note"><span class="lx">je ca hisas ji re</span> → “you are healthier than I am.”</div>
        </div>
      </div>
      <div class="dd-note"><span class="lx">di koryt vosas</span> is the zero-copula base “this house is broken.” An overt C-form instead selects the existing comparison or superlative construction.</div>`;
  },

  parser(){
    return `
      ${ddHead("outside-in segmentation","The ending fixes every seam","For a content word, peel one legal final, reserve exactly four letters for the root, then split the remainder into CV pairs.")}
      <div class="dd-form big">k a p i r i m</div>
      <div class="dd-parse">
        <div class="dd-parse-step"><span class="n">01 · PEEL FINAL</span><span class="word">kapiri<b style="color:var(--vO)">m</b></span><p class="dd-desc"><span class="lx">m ∈ {m t n s l r}</span><br>ending = Entity</p></div>
        <div class="dd-parse-step"><span class="n">02 · TAKE 4</span><span class="word">ka<b style="color:var(--vI)">piri</b>m</span><p class="dd-desc"><span class="lx">CVCV</span><br>root = Person × Individual</p></div>
        <div class="dd-parse-step"><span class="n">03 · SPLIT REST</span><span class="word"><b style="color:var(--vA)">ka</b>pirim</span><p class="dd-desc"><span class="lx">CV</span><br>prefix = K-family group</p></div>
      </div>
      <div class="dd-formula"><div class="dd-seg"><b class="cv-a">ka</b><span>prefix</span></div><span class="dd-op">+</span><div class="dd-seg"><b class="cv-i">piri</b><span>root</span></div><span class="dd-op">+</span><div class="dd-seg"><b>m</b><span>ending</span></div><span class="dd-op">→</span><div class="dd-seg"><b>kapirim</b><span>valid content word</span></div></div>
      <div class="dd-checks">
        <div class="dd-check"><b>ji ✓</b>exactly CV → atomic pronoun; do not search for an ending</div>
        <div class="dd-check"><b>piri △</b>well-formed bare root → add one of <span class="lx">m t n s l r</span></div>
        <div class="dd-check"><b>pirix ✕</b><span class="lx">x</span> cannot close a content word → illegal final</div>
      </div>`;
  }
};

document.querySelectorAll(".dense-diagram[data-diagram]").forEach(el => {
  const render = DD_RENDERERS[el.dataset.diagram];
  if (render) el.innerHTML = render();
});

/* ============ hero anatomy ============ */
(function(){
  const segs = [["pre","ka"],["root","piri"],["suf","m"]];
  $("#anWord").innerHTML = segs.map(([k,t]) =>
    `<span class="an-seg" data-k="${k}" tabindex="0">${colorize(t)}</span>`).join("");
  const all = document.querySelectorAll("#anatomy [data-k]");
  all.forEach(el => {
    const k = el.dataset.k;
    const on = () => all.forEach(e => e.classList.toggle("hl", e.dataset.k === k));
    const off = () => all.forEach(e => e.classList.remove("hl"));
    el.addEventListener("mouseenter", on); el.addEventListener("mouseleave", off);
    el.addEventListener("focus", on);      el.addEventListener("blur", off);
  });
})();

/* ============ ch1: sound grids ============ */
$("#congrid").innerHTML = CONS_INFO.map(([L,ipa,hint,trap]) =>
  `<div class="con${trap?" trap":""}"><span class="L">${L}</span><span class="p ipa">/${ipa}/</span>
   <span class="hint">${hint}</span></div>`).join("");
$("#vowrow").innerHTML = VOW_INFO.map(([L,ipa,hint]) =>
  `<div class="vow vow-${L}"><span class="L cv-${L}">${L}</span><span class="p ipa">/${ipa}/</span>
   <span class="hint">${hint}</span></div>`).join("");

/* ============ ch4: matrix ============ */
(function(){
  const byCell = {};
  Object.keys(ROOTS).forEach(r => byCell[r[1] + r[3]] = r);
  let html = `<div class="mx-corner">domain ↓ · aspect →</div>`;
  for (const a of VOWS) html += `<div class="mx-h"><b class="cv-${a}">${a}</b>${ASPS[a][0]}</div>`;
  for (const d of VOWS){
    html += `<div class="mx-r"><b class="cv-${d}">${d}</b>${DOMS[d][0]}</div>`;
    for (const a of VOWS){
      const r = byCell[d + a];
      const short = ROOTS[r][0].split(",")[0].replace(/^to be /,"be ").replace(/^to /,"");
      html += `<button class="mx-c" data-r="${r}" aria-label="root ${r}: ${esc(ROOTS[r][0])}">
        <span class="r">${colorize(r)}</span><span class="g">${esc(short)}</span></button>`;
    }
  }
  const mx = $("#matrix");
  mx.innerHTML = html;
  function show(r){
    mx.querySelectorAll(".mx-c").forEach(b => b.classList.toggle("on", b.dataset.r === r));
    const d = r[1], a = r[3];
    $("#mxDetail").innerHTML = `
      <span class="dr">${colorize(r)}</span>
      <p class="dg">${esc(ROOTS[r][0])}</p>
      <dl>
        <dt>cell</dt><dd><b>${DOMS[d][0]}</b> × <b>${ASPS[a][0]}</b> — ${DOMS[d][1]}; ${ASPS[a][1]}</dd>
        <dt>zone</dt><dd>future roots in this cell will mean things like: ${esc(ROOTS[r][1])}</dd>
        <dt>forms</dt><dd><span class="lx">${r}m</span> thing · <span class="lx">${r}t</span> the thing ·
          <span class="lx">${r}n</span> verb · <span class="lx">${r}s</span> adjective ·
          <span class="lx">${r}l</span> adverb · <span class="lx">${r}r</span> relation</dd>
      </dl>`;
  }
  mx.addEventListener("click", e => {
    const b = e.target.closest(".mx-c");
    if (b) show(b.dataset.r);
  });
  show("piri");
})();

/* ============ ch5: series cards ============ */
(function(){
  let html = "";
  GROUPS.forEach(([gname, gsub], gi) => {
    html += `<div class="sgroup"><h3>${gname}</h3><p class="gsub">${gsub}</p><div class="series-grid">`;
    SERIES.filter(s => s.grp === gi).forEach(s => {
      html += `<div class="scard"><header><span class="sc">${s.c}–</span><span class="sn">${s.name}</span></header>
        <p class="scale">${esc(s.scale)}</p><table><tbody>`;
      s.rows.forEach(([f,v,g]) => {
        html += `<tr><td class="f">${colorize(f)}</td><td class="v">${esc(v)}</td><td>${esc(g)}</td></tr>`;
      });
      html += `</tbody></table>`;
      if (s.note) html += `<p class="snote">${s.note}</p>`;
      html += `</div>`;
    });
    html += `</div></div>`;
  });
  $("#seriesHost").innerHTML = html;
  $("#refSeries").innerHTML = SERIES.map(s =>
    `<li><span class="lx">${s.c}–</span> ${s.name.toLowerCase()} <span class="small">(${esc(s.scale)})</span></li>`).join("");
})();

/* ============ ch6: number grid + converter ============ */
(function(){
  let html = `<table class="numgrid num"><thead><tr><th></th>`;
  NVOWS.split("").forEach((v,i) => html += `<th class="c"><span class="lx cv-${v}">${v}</span> +${i}</th>`);
  html += `</tr></thead><tbody>`;
  for (let ci = 0; ci < 20; ci++){
    html += `<tr><td class="rl">${CONS[ci]} <span>×5=${ci*5}</span></td>`;
    for (let vi = 0; vi < 5; vi++){
      const n = ci * 5 + vi;
      html += `<td><span class="lx">${CONS[ci]}${NVOWS[vi]}</span><span class="nn">${String(n).padStart(2,"0")}</span></td>`;
    }
    html += `</tr>`;
  }
  html += `</tbody></table>`;
  $("#numgridHost").innerHTML = html;

  const blockValue = block => {
    if (block.length !== 2 || !CONS.includes(block[0]) || !NVOWS.includes(block[1])){
      return null;
    }
    return 5 * CONS.indexOf(block[0]) + NVOWS.indexOf(block[1]);
  };
  const encodeNumber = value => {
    if (value === 0n) return ["pi"];
    const blocks = [], base = BigInt(NUM_BASE);
    while (value > 0n){
      const digit = Number(value % base);
      blocks.push(CONS[Math.floor(digit / 5)] + NVOWS[digit % 5]);
      value /= base;
    }
    return blocks.reverse();
  };

  const n2cvOut = $("#n2cvOut"), cv2nOut = $("#cv2nOut");
  $("#n2cv").addEventListener("input", e => {
    const t = e.target.value.trim();
    if (!t){ n2cvOut.innerHTML = ""; return; }
    if (!/^\d+$/.test(t)){
      n2cvOut.innerHTML = `<span class="err">needs a nonnegative whole number</span>`; return;
    }
    const n = BigInt(t), blocks = encodeNumber(n), payload = blocks.join(" ");
    n2cvOut.innerHTML = `${n} → <span class="big">num ${payload}</span>
      <span class="small">(${blocks.length} base-100 block${blocks.length === 1 ? "" : "s"})</span>`;
  });
  $("#cv2n").addEventListener("input", e => {
    const t = e.target.value.trim().toLowerCase();
    if (!t){ cv2nOut.innerHTML = ""; return; }
    const blocks = t.split(/\s+/), values = blocks.map(blockValue);
    if (values.some(value => value === null)){
      cv2nOut.innerHTML = `<span class="err">each block needs consonant + one of i y e a o</span>`; return;
    }
    if (values.length > 1 && values[0] === 0){
      cv2nOut.innerHTML = `<span class="err">a multi-block numeral cannot start with pi</span>`; return;
    }
    let n = 0n;
    for (const value of values) n = n * BigInt(NUM_BASE) + BigInt(value);
    const payload = blocks.join(" ");
    cv2nOut.innerHTML = `<span class="lx">num ${payload}</span> → <span class="big">${n}</span>
      <span class="small">(${blocks.length} base-100 block${blocks.length === 1 ? "" : "s"})</span>`;
  });
})();

/* ============ ch8: drills ============ */
(function(){
  const drills = [
    ["ji zifen.", "“I speak.”",
     [["ji","I"],["zifen","speak"]]],
    ["te py jo gusen.", "“He (or she) is thinking right now.”",
     [["te","now"],["py","-ing"],["jo","he/she/it"],["gusen","think"]]],
    ["ho qa pirim gyfen.", "“Most people usually socialize.”",
     [["ho","usually"],["qa","most"],["pirim","people"],["gyfen","mingle"]]],
    ["dy fenit si di koryt.", "“These animals are inside this house.”",
     [["dy","these"],["fenit","animals"],["si","inside"],["di","this"],["koryt","house"]]],
    ["ti jy go do saryt ru pasen.", "“Long ago, we traveled to that faraway region.”",
     [["ti","long ago"],["jy","we"],["go","endpoint"],["do","that (far)"],["saryt","the region"],["ru","path closer"],["pasen","go"]]],
    ["je ca hisas ji re.", "“You are healthier than I am.”",
     [["je","you"],["ca","more"],["hisas","healthy"],["ji","I"],["re","than"]]],
    ["pu ju qo koryt re gosen.", "“They have already built all the houses.”",
     [["pu","already"],["ju","they"],["qo","all"],["koryt","the houses"],["re","object"],["gosen","build"]]],
    ["num pa pirim pasen.", "“Three people go.”",
     [["num","number:"],["pa","3"],["pirim","people"],["pasen","go"]]],
    ["qu dy num pa koryt re gosen.", "“Each of these three houses was built.”",
     [["qu","each"],["dy","these"],["num","number:"],["pa","3"],["koryt","houses"],["re","patient"],["gosen","build"]]],
    ["wa re ji nifen?", "“What do I eat?”",
     [["wa","what?"],["re","patient"],["ji","I"],["nifen","eat"]]],
    ["ty di koryt re gosen.", "“This house was built recently.”",
     [["ty","recently"],["di","this"],["koryt","house"],["re","object"],["gosen","build"]]]
  ];
  $("#drills").innerHTML = drills.map(([q, t, ws], i) => `
    <div class="drill" id="drill${i}">
      <button aria-expanded="false" aria-controls="drillA${i}">
        <span class="q">${esc(q)}</span><span class="tog">reveal</span>
      </button>
      <div class="a" id="drillA${i}">
        <div class="ix tight"><div class="ix-s">${
          ws.map(([w,g]) => `<div class="ix-w"><span class="lx">${esc(w)}</span><span class="g">${esc(g)}</span></div>`).join("")
        }</div></div>
        <p class="ix-t" style="margin:6px 0 4px">${esc(t)}</p>
      </div>
    </div>`).join("");
  document.querySelectorAll(".drill>button").forEach(b => b.addEventListener("click", () => {
    const d = b.parentElement, open = d.classList.toggle("open");
    b.setAttribute("aria-expanded", open);
    b.querySelector(".tog").textContent = open ? "hide" : "reveal";
  }));
})();

/* ============ ch9: parser ============ */
function parseWord(raw){
  const w = raw.trim().toLowerCase();
  const out = {word:w, errors:[], type:null, numval:null};
  if (!w) return null;
  if (/[^a-z]/.test(w)){ out.type="content"; out.errors.push("Only the letters a–z occur in Luryt."); return out; }
  if (ATOMS[w]){
    const [name, gloss] = ATOMS[w];
    out.type = "atomic";
    out.fixedGloss = `${name} — ${gloss}`;
    return out;
  }
  const isCV = s => s.length===2 && CONS.includes(s[0]) && VOWS.includes(s[1]);

  if (w.length === 2 && isCV(w)){
    out.type = "atomic";
    out.particle = PARTICLES[w] || null;
    out.numval = NVOWS.includes(w[1]) ? 5*CONS.indexOf(w[0]) + NVOWS.indexOf(w[1]) : null;
    if (!out.particle && out.numval === null)
      out.errors.push(`“${w}” is a well-formed syllable, but no particle family uses it yet and it isn’t a numeral.`);
    return out;
  }

  out.type = "content";
  if (!FINALS.includes(w[w.length-1])){
    out.errors.push(`A content word must end in one of ${[...FINALS].join(" ")} — “${w[w.length-1]}” can’t close a word.`);
    if (w.length === 4 && CONS.includes(w[0]) && VOWS.includes(w[1]) && CONS.includes(w[2]) && VOWS.includes(w[3])){
      out.hint = `“${w}” is a bare root${ROOTS[w] ? ` (${ROOTS[w][0]})` : ""} — give it an ending: ${w}m, ${w}n, ${w}s…`;
    }
    return out;
  }
  out.suffix = w[w.length-1];
  if (w.length < 5){
    out.errors.push("Too short: a content word needs at least a four-letter root plus its ending.");
    return out;
  }
  out.root = w.slice(-5, -1);
  const r = out.root;
  const pos = ["first","second","third","fourth"];
  [CONS, VOWS, CONS, VOWS].forEach((set, i) => {
    if (!set.includes(r[i])) out.errors.push(
      `Root “${r}”: ${pos[i]} letter must be a ${set===CONS?"consonant":"vowel"}, but “${r[i]}” isn’t.`);
  });
  const pre = w.slice(0, -5);
  out.prefixes = [];
  if (pre){
    if (pre.length % 2) out.errors.push(`“${pre}” can’t be split into two-letter prefixes (odd length).`);
    else for (let i = 0; i < pre.length; i += 2){
      const p = pre.slice(i, i+2);
      if (!isCV(p)) out.errors.push(`“${p}” isn’t a valid consonant-vowel prefix.`);
      else {
        out.prefixes.push(p);
        if (!K_PREFIX[p])
          out.errors.push(`“${p}” has no standardized prefix use; only K-family forms are defined as prefixes.`);
      }
    }
  }
  return out;
}

(function(){
  const samples = ["kapirim","zifes","te","num","qe","kykatim","gusan","koryt","piri","ho"];
  $("#pchips").innerHTML = samples.map(s => `<button class="chip" data-w="${s}">${s}</button>`).join("");
  const pin = $("#pin"), pout = $("#pout");
  $("#pchips").addEventListener("click", e => {
    const b = e.target.closest(".chip");
    if (b){ pin.value = b.dataset.w; render(); pin.focus(); }
  });
  pin.addEventListener("input", render);

  function dt(k, v){ return `<dt>${k}</dt><dd>${v}</dd>`; }
  function render(){
    const p = parseWord(pin.value);
    if (!p){ pout.innerHTML = ""; return; }
    const ok = p.errors.length === 0;
    let html = `<p class="verdict ${ok?"good":"bad"}">${ok ? "✓ well-formed" : "✗ not a word"} · ${p.type === "atomic" ? "particle / numeral" : "content word"}</p>`;

    if (p.type === "atomic"){
      html += `<div class="an-word"><span class="an-seg" data-k="root">${colorize(p.word)}</span></div><dl class="det">`;
      if (p.fixedGloss) html += dt("fixed form", esc(p.fixedGloss));
      if (p.particle) html += dt("particle", `${p.particle.series}-family <b>${p.particle.name}</b> — ${esc(p.particle.val)}: “${esc(p.particle.gloss)}”`);
      if (p.numval !== null) html += dt("numeral", `the number <b>${p.numval}</b> (5×${CONS.indexOf(p.word[0])} + ${NVOWS.indexOf(p.word[1])})`);
      if (p.particle && p.numval !== null) html += dt("note", "both readings exist — context picks one");
      html += `</dl>`;
    } else {
      if (p.root){
        const segs = [];
        (p.prefixes || []).forEach(x => segs.push(["pre", x]));
        segs.push(["root", p.root]); segs.push(["suf", p.suffix]);
        html += `<div class="an-word">${segs.map(([k,t]) => `<span class="an-seg" data-k="${k}">${colorize(t)}</span>`).join("")}</div>`;
      }
      if (ok){
        const r = p.root, d = r[1], a = r[3];
        html += `<dl class="det">`;
        (p.prefixes || []).forEach(x => {
          const kp = K_PREFIX[x];
          html += dt(`prefix ${x}`, `K-family: <b>${esc(kp.replace("X", "…"))}</b>`);
        });
        html += dt(`root ${r}`, ROOTS[r] ? `<b>${esc(ROOTS[r][0])}</b> (core root)` :
          `not in the core 36 — but its cell is fixed by its vowels`);
        html += dt("cell", `<b>${DOMS[d][0]}</b> × <b>${ASPS[a][0]}</b>`);
        html += dt(`ending ${p.suffix}`, `<b>${SUFF[p.suffix][0]}</b> — ${SUFF[p.suffix][1]}`);
        html += `</dl>`;
      } else {
        html += `<ul class="errs">${p.errors.map(e => `<li>${esc(e)}</li>`).join("")}</ul>`;
        if (p.hint) html += `<p class="hint">${esc(p.hint)}</p>`;
      }
    }
    pout.innerHTML = html;
  }
  pin.value = "kapirim"; render();
})();

/* ============ nav scroll-spy ============ */
(function(){
  const links = [...document.querySelectorAll(".navlink")];
  const secs = links.map(l => document.querySelector(l.getAttribute("href")));
  if (!("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver(es => {
    es.forEach(en => {
      if (en.isIntersecting){
        links.forEach(l => l.classList.toggle("on", l.getAttribute("href") === "#" + en.target.id));
      }
    });
  }, {rootMargin: "-20% 0px -70% 0px"});
  secs.forEach(s => s && io.observe(s));
})();
