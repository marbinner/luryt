// API Base URL
const API_URL = '';

// Tab Management
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabName = btn.dataset.tab;
        switchTab(tabName);
    });
});

function switchTab(tabName) {
    // Update buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

    // Update content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.getElementById(tabName).classList.add('active');

    // Load data for tab
    loadTabData(tabName);
}

function loadTabData(tabName) {
    switch(tabName) {
        case 'dictionary':
            loadDictionaryStats();
            break;
        case 'particles':
            loadParticles();
            break;
        case 'roots':
            loadRoots();
            break;
        case 'numbers':
            loadNumberTable();
            break;
    }
}

// Parser Functions
async function parseWord() {
    const input = document.getElementById('parseInput').value.trim();
    if (!input) return;

    try {
        const response = await fetch(`${API_URL}/api/parse`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ word: input })
        });

        const result = await response.json();
        displayParseResult(result);
    } catch (error) {
        document.getElementById('parseResult').innerHTML =
            `<div class="error">Error: ${error.message}</div>`;
    }
}

function parseExample(word) {
    document.getElementById('parseInput').value = word;
    parseWord();
}

function displayParseResult(result) {
    const container = document.getElementById('parseResult');
    const validClass = result.is_valid ? 'parse-valid' : 'parse-invalid';

    let html = `<div class="result-item ${validClass}">`;
    html += `<div class="parse-field"><strong>Word:</strong> ${result.original}</div>`;
    html += `<div class="parse-field"><strong>Type:</strong> ${result.word_type}</div>`;
    html += `<div class="parse-field"><strong>Valid:</strong> ${result.is_valid ? '✓ Yes' : '✗ No'}</div>`;

    if (result.errors && result.errors.length > 0) {
        html += `<div class="error-list"><strong>Errors:</strong><ul>`;
        result.errors.forEach(error => {
            html += `<li>${error}</li>`;
        });
        html += `</ul></div>`;
    }

    if (result.word_type === 'atomic') {
        if (result.particle_series) {
            html += `<div class="parse-field"><strong>Particle:</strong> ${result.particle_series}-series (${result.particle_meaning[0]})</div>`;
            html += `<div class="parse-field"><strong>Gloss:</strong> "${result.particle_meaning[1]}"</div>`;
        }
        if (result.numeric_value !== null) {
            html += `<div class="parse-field"><strong>Numeric value:</strong> ${result.numeric_value}</div>`;
        }
    } else if (result.word_type === 'content') {
        if (result.prefixes && result.prefixes.length > 0) {
            html += `<div class="parse-field"><strong>Prefixes:</strong> ${result.prefixes.join('-')}</div>`;
        }
        if (result.root) {
            html += `<div class="parse-field"><strong>Root:</strong> ${result.root}</div>`;
            if (result.domain && result.aspect) {
                html += `<div class="parse-field indent">Domain: ${result.domain} (${result.domain_name})</div>`;
                html += `<div class="parse-field indent">Aspect: ${result.aspect} (${result.aspect_name})</div>`;
            }
        }
        if (result.suffix) {
            html += `<div class="parse-field"><strong>Suffix:</strong> -${result.suffix} (${result.head_kind})</div>`;
        }
    }

    html += `</div>`;
    container.innerHTML = html;
}

// Dictionary allow Enter key
document.getElementById('parseInput')?.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') parseWord();
});

document.getElementById('searchInput')?.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') searchDictionary();
});

// Dictionary Functions
async function loadDictionaryStats() {
    try {
        const response = await fetch(`${API_URL}/api/stats`);
        const data = await response.json();

        const statsHtml = `
            <div class="stat-item">
                <div class="stat-value">${data.dictionary.total_entries}</div>
                <div class="stat-label">Total Entries</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">${data.dictionary.content_words}</div>
                <div class="stat-label">Content Words</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">${data.dictionary.atomic_words}</div>
                <div class="stat-label">Particles</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">${data.dictionary.unique_roots}</div>
                <div class="stat-label">Unique Roots</div>
            </div>
        `;

        document.getElementById('dictionaryStats').innerHTML = statsHtml;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

async function searchDictionary() {
    const query = document.getElementById('searchInput').value.trim();
    const field = document.getElementById('searchField').value;

    if (!query) {
        // Show all entries if no query
        try {
            const response = await fetch(`${API_URL}/api/dictionary?limit=50`);
            const data = await response.json();
            displaySearchResults(data.entries, `Showing ${data.returned} of ${data.total} entries`);
        } catch (error) {
            document.getElementById('searchResults').innerHTML =
                `<div class="error">Error: ${error.message}</div>`;
        }
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/dictionary/search`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, field })
        });

        const data = await response.json();
        displaySearchResults(data.results, `Found ${data.count} result(s)`);
    } catch (error) {
        document.getElementById('searchResults').innerHTML =
            `<div class="error">Error: ${error.message}</div>`;
    }
}

function displaySearchResults(results, header) {
    const container = document.getElementById('searchResults');

    if (results.length === 0) {
        container.innerHTML = '<p>No results found.</p>';
        return;
    }

    let html = `<h3>${header}</h3>`;
    results.forEach(entry => {
        html += `<div class="result-item">`;
        html += `<div class="parse-field"><strong>${entry.word}</strong> - ${entry.gloss}</div>`;
        if (entry.root) {
            html += `<div class="parse-field" style="font-size: 0.9em; color: var(--text-muted);">Root: ${entry.root}</div>`;
        }
        if (entry.notes) {
            html += `<div class="parse-field" style="font-size: 0.9em;">${entry.notes}</div>`;
        }
        if (entry.examples && entry.examples.length > 0) {
            html += `<div class="parse-field" style="font-size: 0.9em; font-style: italic;">`;
            entry.examples.forEach(ex => {
                html += `<div>• ${ex}</div>`;
            });
            html += `</div>`;
        }
        html += `</div>`;
    });

    container.innerHTML = html;
}

async function addWord() {
    const word = document.getElementById('newWord').value.trim();
    const gloss = document.getElementById('newGloss').value.trim();
    const notes = document.getElementById('newNotes').value.trim();

    if (!word || !gloss) {
        alert('Please enter both word and gloss');
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/dictionary`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ word, gloss, notes, examples: [] })
        });

        if (response.ok) {
            alert(`Word "${word}" added successfully!`);
            document.getElementById('newWord').value = '';
            document.getElementById('newGloss').value = '';
            document.getElementById('newNotes').value = '';
            loadDictionaryStats();
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
}

// Particles Functions
async function loadParticles() {
    const container = document.getElementById('particlesList');
    if (container.innerHTML) return; // Already loaded

    try {
        const response = await fetch(`${API_URL}/api/particles`);
        const data = await response.json();

        let html = '';
        const seriesNames = {
            'P': 'Phase / Event Aspect',
            'M': 'Degree / Intensity',
            'T': 'Time / Tense',
            'D': 'Demonstratives',
            'N': 'Polarity',
            'Q': 'Quantifiers',
            'S': 'Spatial Topology',
            'C': 'Comparatives',
            'W': 'Wh-/Interrogatives',
            'J': 'Personal Pronouns',
            'K': 'Configuration / Collectivity',
            'R': 'Roles / Case-like',
            'H': 'Frequency / Habituality'
        };

        Object.entries(data).forEach(([series, particles]) => {
            html += `<div class="particle-series">`;
            html += `<div class="series-header">`;
            html += `<strong>${series}-series: ${seriesNames[series] || ''}</strong>`;
            html += `</div>`;
            html += `<div class="series-content">`;

            Object.entries(particles).forEach(([particle, info]) => {
                html += `<div class="particle-item">`;
                html += `<div class="particle-word">${particle.toLowerCase()}</div>`;
                html += `<div class="particle-meaning">${info.meaning}</div>`;
                html += `<div class="particle-gloss">"${info.gloss}"</div>`;
                html += `</div>`;
            });

            html += `</div></div>`;
        });

        container.innerHTML = html;
    } catch (error) {
        container.innerHTML = `<div class="error">Error loading particles: ${error.message}</div>`;
    }
}

// Roots Functions
async function loadRoots() {
    const matrixContainer = document.getElementById('rootsMatrix');
    if (matrixContainer.innerHTML) return; // Already loaded

    try {
        const [rootsResp, domainsResp, aspectsResp] = await Promise.all([
            fetch(`${API_URL}/api/roots`),
            fetch(`${API_URL}/api/domains`),
            fetch(`${API_URL}/api/aspects`)
        ]);

        const roots = await rootsResp.json();
        const domains = await domainsResp.json();
        const aspects = await aspectsResp.json();

        // Populate filters
        const domainFilter = document.getElementById('domainFilter');
        const aspectFilter = document.getElementById('aspectFilter');

        Object.entries(domains).forEach(([vowel, info]) => {
            const option = document.createElement('option');
            option.value = vowel;
            option.textContent = `${vowel} - ${info.name}`;
            domainFilter.appendChild(option);
        });

        Object.entries(aspects).forEach(([vowel, info]) => {
            const option = document.createElement('option');
            option.value = vowel;
            option.textContent = `${vowel} - ${info.name}`;
            aspectFilter.appendChild(option);
        });

        // Store data globally for filtering
        window.rootsData = { roots, domains, aspects };
        displayRoots(roots);
    } catch (error) {
        matrixContainer.innerHTML = `<div class="error">Error loading roots: ${error.message}</div>`;
    }
}

function filterRoots() {
    const domainFilter = document.getElementById('domainFilter').value;
    const aspectFilter = document.getElementById('aspectFilter').value;

    if (!window.rootsData) return;

    const filtered = {};
    Object.entries(window.rootsData.roots).forEach(([root, info]) => {
        if (domainFilter && info.domain !== domainFilter) return;
        if (aspectFilter && info.aspect !== aspectFilter) return;
        filtered[root] = info;
    });

    displayRoots(filtered);
}

function displayRoots(roots) {
    const container = document.getElementById('rootsMatrix');

    let html = '<div class="roots-grid">';
    Object.entries(roots).forEach(([root, info]) => {
        html += `<div class="root-item">`;
        html += `<div class="root-word">${root.toLowerCase()}</div>`;
        html += `<div class="root-classification">${info.domain}${info.aspect} - ${info.domain_name} × ${info.aspect_name}</div>`;
        html += `<div class="root-gloss">${info.gloss}</div>`;
        html += `</div>`;
    });
    html += '</div>';

    container.innerHTML = html;
}

// Number Conversion Functions
async function convertNumToCV() {
    const num = parseInt(document.getElementById('numInput').value);

    if (isNaN(num)) {
        document.getElementById('numResult').innerHTML = '<p>Please enter a valid number</p>';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/number-to-cv`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ value: num })
        });

        const data = await response.json();
        document.getElementById('numResult').innerHTML =
            `<div class="result-item"><strong>${data.number}</strong> → <strong style="color: var(--primary); font-size: 1.5em;">${data.cv.toLowerCase()}</strong></div>`;
    } catch (error) {
        document.getElementById('numResult').innerHTML =
            `<div class="error">Error: ${error.message}</div>`;
    }
}

async function convertCVToNum() {
    const cv = document.getElementById('cvInput').value.trim();

    if (!cv) {
        document.getElementById('cvResult').innerHTML = '<p>Please enter a CV syllable</p>';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/cv-to-number`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cv })
        });

        if (!response.ok) {
            const error = await response.json();
            document.getElementById('cvResult').innerHTML =
                `<div class="error">${error.detail}</div>`;
            return;
        }

        const data = await response.json();
        document.getElementById('cvResult').innerHTML =
            `<div class="result-item"><strong>${data.cv.toLowerCase()}</strong> → <strong style="color: var(--primary); font-size: 1.5em;">${data.number}</strong></div>`;
    } catch (error) {
        document.getElementById('cvResult').innerHTML =
            `<div class="error">Error: ${error.message}</div>`;
    }
}

function loadNumberTable() {
    const container = document.getElementById('numberTable');
    if (container.innerHTML) return;

    let html = '<div class="number-grid">';
    for (let i = 0; i < 100; i++) {
        // Calculate CV (we'll just show some examples)
        if (i % 5 === 0 && i < 20) {
            fetch(`${API_URL}/api/number-to-cv`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ value: i })
            }).then(r => r.json()).then(data => {
                const cell = document.querySelector(`[data-num="${i}"]`);
                if (cell) cell.querySelector('.cv-display').textContent = data.cv.toLowerCase();
            });
        }

        html += `<div class="number-cell" data-num="${i}">`;
        html += `<div class="cv-display">...</div>`;
        html += `<div class="num-display">${i}</div>`;
        html += `</div>`;
    }
    html += '</div>';

    container.innerHTML = html;

    // Load all conversions
    for (let i = 0; i < 100; i++) {
        fetch(`${API_URL}/api/number-to-cv`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ value: i })
        }).then(r => r.json()).then(data => {
            const cell = document.querySelector(`[data-num="${i}"]`);
            if (cell) cell.querySelector('.cv-display').textContent = data.cv.toLowerCase();
        }).catch(() => {});
    }
}

// Practice Mode Functions
let currentQuiz = null;
let quizScore = 0;
let quizTotal = 0;

async function startParticleQuiz() {
    const response = await fetch(`${API_URL}/api/particles`);
    const data = await response.json();

    // Flatten particles
    const particles = [];
    Object.entries(data).forEach(([series, items]) => {
        Object.entries(items).forEach(([particle, info]) => {
            particles.push({ particle, ...info, series });
        });
    });

    currentQuiz = { type: 'particle', data: particles, index: 0 };
    quizScore = 0;
    quizTotal = 0;

    showQuizQuestion();
}

async function startRootQuiz() {
    const response = await fetch(`${API_URL}/api/roots`);
    const roots = await response.json();

    const rootList = Object.entries(roots).map(([root, info]) => ({
        root,
        ...info
    }));

    currentQuiz = { type: 'root', data: rootList, index: 0 };
    quizScore = 0;
    quizTotal = 0;

    showQuizQuestion();
}

async function startNumberQuiz() {
    const numbers = [];
    for (let i = 0; i < 20; i++) {
        const num = Math.floor(Math.random() * 100);
        const response = await fetch(`${API_URL}/api/number-to-cv`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ value: num })
        });
        const data = await response.json();
        numbers.push(data);
    }

    currentQuiz = { type: 'number', data: numbers, index: 0 };
    quizScore = 0;
    quizTotal = 0;

    showQuizQuestion();
}

async function startVocabQuiz() {
    const response = await fetch(`${API_URL}/api/dictionary?limit=100`);
    const data = await response.json();

    // Filter to content words with roots
    const words = data.entries.filter(e => e.root);

    if (words.length < 4) {
        alert('Not enough words in dictionary for quiz!');
        return;
    }

    currentQuiz = { type: 'vocab', data: words, index: 0 };
    quizScore = 0;
    quizTotal = 0;

    showQuizQuestion();
}

async function startConsonantQuiz() {
    // Canonical consonant order: P B M F V T D N Q S Z L C W X J K G R H
    const consonants = 'PBMFVTDNQSZLCWXJKGRH'.split('');

    // Create quiz data (mix of letter->index and index->letter questions)
    const quizData = [];

    // Generate 5 initial questions (more will be generated as needed)
    for (let i = 0; i < 5; i++) {
        const randomIndex = Math.floor(Math.random() * consonants.length);
        const consonant = consonants[randomIndex];

        // Randomly decide if we ask for letter or index
        const askForLetter = Math.random() > 0.5;

        quizData.push({
            question: askForLetter ? randomIndex : consonant,
            answer: askForLetter ? consonant : randomIndex,
            askForLetter: askForLetter,
            consonantIndex: randomIndex  // Track which consonant this is about
        });
    }

    currentQuiz = {
        type: 'consonant',
        data: quizData,
        index: 0,
        consonants: consonants,
        incorrectIndices: new Set(),  // Track which consonant indices were answered incorrectly
        recentQuestions: []  // Track last 3 questions to avoid immediate repeats
    };
    quizScore = 0;
    quizTotal = 0;

    showQuizQuestion();
}

function generateConsonantQuestion(quiz) {
    const consonants = quiz.consonants;
    let consonantIndex;

    // Build a weighted list of consonant indices
    const weightedIndices = [];

    for (let i = 0; i < consonants.length; i++) {
        // Skip if this was asked in the last 3 questions
        if (quiz.recentQuestions.includes(i)) {
            continue;
        }

        // Add this index multiple times based on whether it was incorrect
        const weight = quiz.incorrectIndices.has(i) ? 3 : 1;
        for (let w = 0; w < weight; w++) {
            weightedIndices.push(i);
        }
    }

    // If all indices are in recent questions (shouldn't happen normally), clear recent
    if (weightedIndices.length === 0) {
        quiz.recentQuestions = [];
        // Rebuild without recent check
        for (let i = 0; i < consonants.length; i++) {
            const weight = quiz.incorrectIndices.has(i) ? 3 : 1;
            for (let w = 0; w < weight; w++) {
                weightedIndices.push(i);
            }
        }
    }

    // Pick a weighted random index
    consonantIndex = weightedIndices[Math.floor(Math.random() * weightedIndices.length)];
    const consonant = consonants[consonantIndex];

    // Track this question in recent history
    quiz.recentQuestions.push(consonantIndex);
    if (quiz.recentQuestions.length > 3) {
        quiz.recentQuestions.shift();
    }

    // Randomly decide if we ask for letter or index
    const askForLetter = Math.random() > 0.5;

    return {
        question: askForLetter ? consonantIndex : consonant,
        answer: askForLetter ? consonant : consonantIndex,
        askForLetter: askForLetter,
        consonantIndex: consonantIndex
    };
}

function showQuizQuestion() {
    const container = document.getElementById('quizContainer');
    container.classList.add('active');

    // For consonant quiz, keep generating new questions
    if (currentQuiz.type === 'consonant' && currentQuiz.index >= currentQuiz.data.length) {
        // Generate a new question using weighted selection
        const newQuestion = generateConsonantQuestion(currentQuiz);
        currentQuiz.data.push(newQuestion);
    }

    // For other quizzes, check if complete
    if (currentQuiz.type !== 'consonant' && currentQuiz.index >= Math.min(10, currentQuiz.data.length)) {
        // Quiz complete
        container.innerHTML = `
            <div class="quiz-question">Quiz Complete!</div>
            <div class="quiz-score">Score: ${quizScore} / ${quizTotal}</div>
            <button onclick="closeQuiz()">Close</button>
        `;
        return;
    }

    const item = currentQuiz.data[currentQuiz.index];
    let html = '';

    if (currentQuiz.type === 'particle') {
        html = `
            <div class="quiz-question">What does "${item.particle.toLowerCase()}" mean?</div>
            <div class="quiz-options">
        `;

        // Generate options (correct + 3 random)
        const options = [item.gloss];
        while (options.length < 4) {
            const random = currentQuiz.data[Math.floor(Math.random() * currentQuiz.data.length)];
            if (!options.includes(random.gloss)) {
                options.push(random.gloss);
            }
        }

        // Shuffle
        options.sort(() => Math.random() - 0.5);

        options.forEach(opt => {
            html += `<button class="quiz-option" onclick="checkAnswer('${opt.replace(/'/g, "\\'")}', '${item.gloss.replace(/'/g, "\\'")}')">${opt}</button>`;
        });

        html += `</div><div class="quiz-score">Question ${currentQuiz.index + 1} / 10 | Score: ${quizScore} / ${quizTotal}</div>`;

    } else if (currentQuiz.type === 'root') {
        html = `
            <div class="quiz-question">What is the gloss for root "${item.root.toLowerCase()}"?</div>
            <div class="quiz-options">
        `;

        const options = [item.gloss];
        while (options.length < 4) {
            const random = currentQuiz.data[Math.floor(Math.random() * currentQuiz.data.length)];
            if (!options.includes(random.gloss)) {
                options.push(random.gloss);
            }
        }

        options.sort(() => Math.random() - 0.5);

        options.forEach(opt => {
            html += `<button class="quiz-option" onclick="checkAnswer('${opt.replace(/'/g, "\\'")}', '${item.gloss.replace(/'/g, "\\'")}')">${opt}</button>`;
        });

        html += `</div><div class="quiz-score">Question ${currentQuiz.index + 1} / 10 | Score: ${quizScore} / ${quizTotal}</div>`;

    } else if (currentQuiz.type === 'number') {
        html = `
            <div class="quiz-question">What number is "${item.cv.toLowerCase()}"?</div>
            <div class="quiz-options">
        `;

        const options = [item.number];
        while (options.length < 4) {
            const random = Math.floor(Math.random() * 100);
            if (!options.includes(random)) {
                options.push(random);
            }
        }

        options.sort(() => Math.random() - 0.5);

        options.forEach(opt => {
            html += `<button class="quiz-option" onclick="checkAnswer(${opt}, ${item.number})">${opt}</button>`;
        });

        html += `</div><div class="quiz-score">Question ${currentQuiz.index + 1} / 10 | Score: ${quizScore} / ${quizTotal}</div>`;

    } else if (currentQuiz.type === 'vocab') {
        html = `
            <div class="quiz-question">What does "${item.word.toLowerCase()}" mean?</div>
            <div class="quiz-options">
        `;

        const options = [item.gloss];
        while (options.length < 4) {
            const random = currentQuiz.data[Math.floor(Math.random() * currentQuiz.data.length)];
            if (!options.includes(random.gloss)) {
                options.push(random.gloss);
            }
        }

        options.sort(() => Math.random() - 0.5);

        options.forEach(opt => {
            html += `<button class="quiz-option" onclick="checkAnswer('${opt.replace(/'/g, "\\'")}', '${item.gloss.replace(/'/g, "\\'")}')">${opt}</button>`;
        });

        html += `</div><div class="quiz-score">Question ${currentQuiz.index + 1} / 10 | Score: ${quizScore} / ${quizTotal}</div>`;

    } else if (currentQuiz.type === 'consonant') {
        const item = currentQuiz.data[currentQuiz.index];

        if (item.askForLetter) {
            // Given index, find letter
            html = `
                <div class="quiz-question" style="font-size: 3rem; font-weight: bold; color: var(--primary);">${item.question}</div>
                <div class="input-group" style="max-width: 400px; margin: 0 auto;">
                    <input type="text" id="consonantInput" placeholder="?"
                           style="text-align: center; font-size: 1.5rem; text-transform: uppercase;"
                           autocomplete="off" autofocus maxlength="1">
                </div>
                <div id="feedbackMessage" style="margin-top: 1rem; font-size: 1.2rem; min-height: 30px;"></div>
            `;
        } else {
            // Given letter, find index
            html = `
                <div class="quiz-question" style="font-size: 3rem; font-weight: bold; color: var(--primary);">${item.question}</div>
                <div class="input-group" style="max-width: 400px; margin: 0 auto;">
                    <input type="number" id="consonantInput" placeholder="?"
                           style="text-align: center; font-size: 1.5rem;"
                           autocomplete="off" autofocus min="0" max="19">
                </div>
                <div id="feedbackMessage" style="margin-top: 1rem; font-size: 1.2rem; min-height: 30px;"></div>
            `;
        }

        html += `
            <div class="quiz-score">
                Score: ${quizScore} / ${quizTotal} | Accuracy: ${quizTotal > 0 ? Math.round((quizScore / quizTotal) * 100) : 0}%
                <button onclick="closeQuiz()" style="margin-left: 1rem; padding: 0.5rem 1rem;">Stop</button>
            </div>`;
    }

    container.innerHTML = html;

    // Add auto-check listener for consonant quiz
    if (currentQuiz.type === 'consonant') {
        const input = document.getElementById('consonantInput');
        if (input) {
            input.focus();

            const item = currentQuiz.data[currentQuiz.index];
            const correctAnswer = String(item.answer).toUpperCase();

            input.addEventListener('input', function(e) {
                const userInput = input.value.trim().toUpperCase();

                if (!userInput) return; // Don't check empty input

                let shouldCheck = false;

                if (item.askForLetter) {
                    // For letters, check as soon as they type one character
                    shouldCheck = userInput.length === 1;
                } else {
                    // For numbers, need smarter logic
                    const inputNum = parseInt(userInput);
                    const correctNum = parseInt(correctAnswer);

                    // If they've typed a complete answer
                    if (userInput === correctAnswer) {
                        shouldCheck = true;
                    }
                    // If the input is already impossible to be correct
                    else if (inputNum > 19) {
                        // Out of range
                        shouldCheck = true;
                    }
                    // Single digit cases
                    else if (correctNum <= 9) {
                        // Answer is single digit, so check immediately
                        shouldCheck = true;
                    }
                    // Two digit cases (10-19)
                    else if (correctNum >= 10 && correctNum <= 19) {
                        // Answer is 10-19
                        if (userInput.length === 1) {
                            // First digit typed
                            if (userInput !== '1') {
                                // Wrong first digit (must be 1 for 10-19)
                                shouldCheck = true;
                            }
                            // If it's '1', wait for second digit
                        } else if (userInput.length === 2) {
                            // Two digits typed, check now
                            shouldCheck = true;
                        }
                    }
                }

                if (shouldCheck) {
                    checkConsonantAnswer(userInput, correctAnswer);
                }
            });

            // Also allow Enter key for manual submission
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    const userAnswer = input.value.trim().toUpperCase();
                    checkConsonantAnswer(userAnswer, correctAnswer);
                }
            });
        }
    }
}

function checkConsonantAnswer(selected, correct) {
    const input = document.getElementById('consonantInput');
    const feedback = document.getElementById('feedbackMessage');

    if (!input || !feedback) return;
    if (input.disabled) return; // Already checked this question

    quizTotal++;
    const isCorrect = selected === correct;

    // Track the current question's consonant index
    const currentQuestion = currentQuiz.data[currentQuiz.index];
    const consonantIndex = currentQuestion.consonantIndex;

    if (isCorrect) {
        quizScore++;
        feedback.innerHTML = `<span style="color: var(--secondary); font-weight: bold;">✓ Correct!</span>`;
        input.style.borderColor = 'var(--secondary)';
        input.style.background = '#d1fae5';
    } else {
        feedback.innerHTML = `<span style="color: var(--danger); font-weight: bold;">✗ Wrong! Correct: ${correct}</span>`;
        input.style.borderColor = 'var(--danger)';
        input.style.background = '#fee2e2';

        // Mark this consonant index as incorrect for weighted sampling
        currentQuiz.incorrectIndices.add(consonantIndex);
    }

    input.disabled = true;

    // Update score display
    const scoreDiv = document.querySelector('.quiz-score');
    if (scoreDiv) {
        const accuracy = quizTotal > 0 ? Math.round((quizScore / quizTotal) * 100) : 0;
        scoreDiv.innerHTML = `
            Score: ${quizScore} / ${quizTotal} | Accuracy: ${accuracy}%
            <button onclick="closeQuiz()" style="margin-left: 1rem; padding: 0.5rem 1rem;">Stop</button>
        `;
    }

    // Next question after delay
    setTimeout(() => {
        currentQuiz.index++;
        showQuizQuestion();
    }, 250);
}

function checkAnswer(selected, correct) {
    quizTotal++;

    // Convert to strings for comparison
    selected = String(selected);
    correct = String(correct);

    if (selected === correct) {
        quizScore++;
        event.target.classList.add('correct');
    } else {
        event.target.classList.add('incorrect');
        // Highlight correct answer
        document.querySelectorAll('.quiz-option').forEach(btn => {
            if (btn.textContent === correct) {
                btn.classList.add('correct');
            }
        });
    }

    // Disable all buttons
    document.querySelectorAll('.quiz-option').forEach(btn => {
        btn.disabled = true;
        btn.style.cursor = 'not-allowed';
    });

    // Next question after delay (faster for consonant quiz)
    const delay = currentQuiz.type === 'consonant' ? 250 : 1500;
    setTimeout(() => {
        currentQuiz.index++;
        showQuizQuestion();
    }, delay);
}

function closeQuiz() {
    document.getElementById('quizContainer').classList.remove('active');
    document.getElementById('quizContainer').innerHTML = '';
    currentQuiz = null;
}

// Visualization Functions
let vizState = {
    selectedRoot: null,
    selectedPrefixes: [],
    selectedSuffix: null
};

let networkData = null;
let networkSimulation = null;

function showViz(vizType) {
    // Update button states
    document.querySelectorAll('.viz-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Update panel visibility
    document.querySelectorAll('.viz-panel').forEach(panel => panel.classList.remove('active'));
    document.getElementById(`viz-${vizType}`).classList.add('active');

    // Load data for the visualization
    if (vizType === 'network') {
        loadInteractiveNetwork();
    } else if (vizType === 'matrix') {
        loadSemanticMatrix();
    } else if (vizType === 'vowel-gradient') {
        loadVowelGradient();
    } else if (vizType === 'word-builder') {
        loadWordBuilder();
    } else if (vizType === 'series-explorer') {
        loadSeriesNetwork();
    }
}

async function loadSemanticMatrix() {
    const container = document.getElementById('matrixViz');
    if (container.innerHTML) return; // Already loaded

    const [domainsResp, aspectsResp, rootsResp] = await Promise.all([
        fetch(`${API_URL}/api/domains`),
        fetch(`${API_URL}/api/aspects`),
        fetch(`${API_URL}/api/roots`)
    ]);

    const domains = await domainsResp.json();
    const aspects = await aspectsResp.json();
    const roots = await rootsResp.json();

    const domainOrder = ['I', 'Y', 'E', 'A', 'O', 'U'];
    const aspectOrder = ['I', 'Y', 'E', 'A', 'O', 'U'];

    let html = '<div></div>'; // Top-left corner

    // Column headers (Aspects)
    aspectOrder.forEach(aspectVowel => {
        const aspect = aspects[aspectVowel];
        html += `<div class="matrix-header">${aspectVowel}<br><small>${aspect.name}</small></div>`;
    });

    // Rows
    domainOrder.forEach(domainVowel => {
        const domain = domains[domainVowel];

        // Row header
        html += `<div class="matrix-row-header">${domainVowel}<br><small>${domain.name}</small></div>`;

        // Cells
        aspectOrder.forEach(aspectVowel => {
            const cellKey = domainVowel + aspectVowel;

            // Find root with these vowels
            let rootData = null;
            for (const [root, info] of Object.entries(roots)) {
                if (info.domain === domainVowel && info.aspect === aspectVowel) {
                    rootData = { root, ...info };
                    break;
                }
            }

            if (rootData) {
                html += `
                    <div class="matrix-cell" onclick="showRootDetail('${rootData.root}')">
                        <div class="matrix-cell-vowels">${cellKey}</div>
                        <div class="matrix-cell-root">${rootData.root.toLowerCase()}</div>
                    </div>
                `;
            } else {
                html += `
                    <div class="matrix-cell">
                        <div class="matrix-cell-vowels">${cellKey}</div>
                        <div class="matrix-cell-root">—</div>
                    </div>
                `;
            }
        });
    });

    container.innerHTML = html;
}

function showRootDetail(root) {
    alert(`Root: ${root}\nClick on Word Builder to create words with this root!`);
}

async function loadVowelGradient() {
    const series = document.getElementById('seriesSelect').value;
    const container = document.getElementById('vowelGradientViz');

    const response = await fetch(`${API_URL}/api/particles/${series}`);
    const data = await response.json();

    const vowelOrder = ['I', 'Y', 'E', 'A', 'O', 'U'];

    let html = '<div class="vowel-gradient-container">';

    vowelOrder.forEach(vowel => {
        const particle = series + vowel;
        const particleData = data.particles[particle];

        if (particleData) {
            html += `
                <div class="gradient-item">
                    <div class="gradient-vowel">${vowel}</div>
                    <div class="gradient-particle">${particle.toLowerCase()}</div>
                    <div class="gradient-meaning">${particleData.meaning}</div>
                    <div class="gradient-gloss">"${particleData.gloss}"</div>
                </div>
            `;
        }
    });

    html += '</div>';
    container.innerHTML = html;
}

async function loadWordBuilder() {
    // Load roots into selector
    const rootSelector = document.getElementById('rootSelector');
    if (rootSelector.options.length <= 1) {
        const response = await fetch(`${API_URL}/api/roots`);
        const roots = await response.json();

        Object.entries(roots).forEach(([root, info]) => {
            const option = document.createElement('option');
            option.value = root;
            option.textContent = `${root.toLowerCase()} - ${info.gloss}`;
            rootSelector.appendChild(option);
        });
    }

    // Load K-series prefixes
    const prefixSelector = document.getElementById('prefixSelector');
    if (!prefixSelector.innerHTML) {
        const kPrefixes = {
            'KI': 'single',
            'KY': 'pair',
            'KE': 'small group',
            'KA': 'group',
            'KO': 'large collective',
            'KU': 'scattered'
        };

        let html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">';
        Object.entries(kPrefixes).forEach(([prefix, meaning]) => {
            html += `
                <button class="suffix-btn" onclick="togglePrefix('${prefix}')" id="prefix-${prefix}">
                    ${prefix.toLowerCase()}<br><small>${meaning}</small>
                </button>
            `;
        });
        html += '</div>';
        prefixSelector.innerHTML = html;
    }
}

function togglePrefix(prefix) {
    const btn = document.getElementById(`prefix-${prefix}`);
    const index = vizState.selectedPrefixes.indexOf(prefix);

    if (index > -1) {
        vizState.selectedPrefixes.splice(index, 1);
        btn.classList.remove('selected');
    } else {
        vizState.selectedPrefixes.push(prefix);
        btn.classList.add('selected');
    }

    updateWordPreview();
}

function selectSuffix(suffix) {
    // Deselect all
    document.querySelectorAll('.suffix-btn[data-suffix]').forEach(btn => {
        btn.classList.remove('selected');
    });

    // Select this one
    event.target.classList.add('selected');
    vizState.selectedSuffix = suffix;

    updateWordPreview();
}

function updateWordPreview() {
    const root = document.getElementById('rootSelector').value;
    vizState.selectedRoot = root;

    const wordDisplay = document.getElementById('wordDisplay');
    const wordAnalysis = document.getElementById('wordAnalysis');

    if (!root || !vizState.selectedSuffix) {
        wordDisplay.innerHTML = '<span style="color: var(--text-muted);">Select root and suffix</span>';
        wordAnalysis.innerHTML = '';
        return;
    }

    // Build the word
    let word = '';
    let partsHtml = '';

    // Add prefixes
    if (vizState.selectedPrefixes.length > 0) {
        vizState.selectedPrefixes.forEach(prefix => {
            word += prefix;
            partsHtml += `<span class="word-part prefix">${prefix.toLowerCase()}</span>`;
        });
    }

    // Add root
    word += root;
    partsHtml += `<span class="word-part root">${root.toLowerCase()}</span>`;

    // Add suffix
    word += vizState.selectedSuffix;
    partsHtml += `<span class="word-part suffix">${vizState.selectedSuffix.toLowerCase()}</span>`;

    wordDisplay.innerHTML = partsHtml;

    // Analyze
    let analysis = `<strong>Complete word:</strong> ${word.toLowerCase()}<br>`;
    if (vizState.selectedPrefixes.length > 0) {
        analysis += `<strong>Prefixes:</strong> ${vizState.selectedPrefixes.map(p => p.toLowerCase()).join('-')}<br>`;
    }
    analysis += `<strong>Root:</strong> ${root.toLowerCase()}<br>`;
    analysis += `<strong>Suffix:</strong> -${vizState.selectedSuffix.toLowerCase()}`;

    wordAnalysis.innerHTML = analysis;
}

async function loadSeriesNetwork() {
    const container = document.getElementById('seriesNetworkViz');
    if (container.innerHTML) return;

    const seriesInfo = {
        'P': 'Phase/Aspect',
        'M': 'Degree',
        'T': 'Time',
        'D': 'Demonstratives',
        'N': 'Polarity',
        'Q': 'Quantifiers',
        'S': 'Spatial',
        'C': 'Comparatives',
        'W': 'Interrogatives',
        'J': 'Pronouns',
        'K': 'Configuration',
        'R': 'Roles',
        'H': 'Frequency'
    };

    let html = '';
    Object.entries(seriesInfo).forEach(([consonant, name]) => {
        html += `
            <div class="series-node" onclick="showSeriesDetail('${consonant}')">
                <div class="series-node-consonant">${consonant}</div>
                <div class="series-node-name">${name}</div>
            </div>
        `;
    });

    html += '<div id="seriesDetailPanel" class="series-detail" style="grid-column: 1 / -1;"></div>';

    container.innerHTML = html;
}

async function showSeriesDetail(consonant) {
    const panel = document.getElementById('seriesDetailPanel');

    const response = await fetch(`${API_URL}/api/particles/${consonant}`);
    const data = await response.json();

    let html = `<h3>${consonant}-series</h3>`;
    html += '<div class="vowel-gradient-container">';

    const vowelOrder = ['I', 'Y', 'E', 'A', 'O', 'U'];
    vowelOrder.forEach(vowel => {
        const particle = consonant + vowel;
        const particleData = data.particles[particle];

        if (particleData) {
            html += `
                <div class="gradient-item">
                    <div class="gradient-vowel">${vowel}</div>
                    <div class="gradient-particle">${particle.toLowerCase()}</div>
                    <div class="gradient-meaning">${particleData.meaning}</div>
                    <div class="gradient-gloss">"${particleData.gloss}"</div>
                </div>
            `;
        }
    });

    html += '</div>';
    panel.innerHTML = html;
}

// D3 Interactive Network Visualization
async function loadInteractiveNetwork() {
    const container = document.getElementById('networkViz');

    // Only load once
    if (networkData) {
        updateNetworkFilters();
        return;
    }

    // Fetch all data
    const [domainsResp, aspectsResp, rootsResp, particlesResp] = await Promise.all([
        fetch(`${API_URL}/api/domains`),
        fetch(`${API_URL}/api/aspects`),
        fetch(`${API_URL}/api/roots`),
        fetch(`${API_URL}/api/particles`)
    ]);

    const domains = await domainsResp.json();
    const aspects = await aspectsResp.json();
    const roots = await rootsResp.json();
    const particles = await particlesResp.json();

    // Build nodes and links
    const nodes = [];
    const links = [];

    // Domain nodes
    const domainNodes = {};
    Object.entries(domains).forEach(([vowel, info]) => {
        const node = {
            id: `domain-${vowel}`,
            type: 'domain',
            label: vowel,
            name: info.name,
            vowel: vowel,
            description: `Domain: ${info.name}`
        };
        nodes.push(node);
        domainNodes[vowel] = node;
    });

    // Aspect nodes
    const aspectNodes = {};
    Object.entries(aspects).forEach(([vowel, info]) => {
        const node = {
            id: `aspect-${vowel}`,
            type: 'aspect',
            label: vowel,
            name: info.name,
            vowel: vowel,
            description: `Aspect: ${info.name}`
        };
        nodes.push(node);
        aspectNodes[vowel] = node;
    });

    // Root nodes
    Object.entries(roots).forEach(([root, info]) => {
        const node = {
            id: `root-${root}`,
            type: 'root',
            label: root.toLowerCase(),
            gloss: info.gloss,
            domain: info.domain,
            aspect: info.aspect,
            description: `${root.toLowerCase()}: ${info.gloss}`
        };
        nodes.push(node);

        // Link to domain and aspect
        links.push({
            source: node.id,
            target: `domain-${info.domain}`,
            type: 'domain-link'
        });
        links.push({
            source: node.id,
            target: `aspect-${info.aspect}`,
            type: 'aspect-link'
        });
    });

    // Particle series nodes
    const seriesInfo = {
        'P': 'Phase/Aspect',
        'M': 'Degree',
        'T': 'Time',
        'D': 'Demonstratives',
        'N': 'Polarity',
        'Q': 'Quantifiers',
        'S': 'Spatial',
        'C': 'Comparatives',
        'W': 'Interrogatives',
        'J': 'Pronouns',
        'K': 'Configuration',
        'R': 'Roles',
        'H': 'Frequency'
    };

    Object.entries(seriesInfo).forEach(([consonant, name]) => {
        const node = {
            id: `particle-${consonant}`,
            type: 'particle',
            label: consonant,
            name: name,
            description: `${consonant}-series: ${name}`
        };
        nodes.push(node);
    });

    networkData = { nodes, links };
    renderNetwork();
}

function renderNetwork() {
    const container = document.getElementById('networkViz');
    container.innerHTML = '';

    const width = container.clientWidth;
    const height = 700;

    // Create SVG
    const svg = d3.select('#networkViz')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    // Add zoom behavior
    const g = svg.append('g');

    const zoom = d3.zoom()
        .scaleExtent([0.1, 4])
        .on('zoom', (event) => {
            g.attr('transform', event.transform);
        });

    svg.call(zoom);

    // Filter nodes and links based on checkboxes
    const showDomains = document.getElementById('showDomains').checked;
    const showAspects = document.getElementById('showAspects').checked;
    const showParticles = document.getElementById('showParticles').checked;
    const showRoots = document.getElementById('showRoots').checked;

    const filteredNodes = networkData.nodes.filter(node => {
        if (node.type === 'domain') return showDomains;
        if (node.type === 'aspect') return showAspects;
        if (node.type === 'particle') return showParticles;
        if (node.type === 'root') return showRoots;
        return true;
    });

    const nodeIds = new Set(filteredNodes.map(n => n.id));
    const filteredLinks = networkData.links.filter(link =>
        nodeIds.has(link.source.id || link.source) &&
        nodeIds.has(link.target.id || link.target)
    );

    // Create force simulation
    networkSimulation = d3.forceSimulation(filteredNodes)
        .force('link', d3.forceLink(filteredLinks)
            .id(d => d.id)
            .distance(d => {
                // Shorter distances for root connections
                if (d.type === 'domain-link' || d.type === 'aspect-link') return 100;
                return 150;
            })
        )
        .force('charge', d3.forceManyBody().strength(-300))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(30));

    // Create links
    const link = g.append('g')
        .selectAll('line')
        .data(filteredLinks)
        .enter()
        .append('line')
        .attr('class', d => `d3-link ${d.type}`);

    // Create nodes
    const node = g.append('g')
        .selectAll('circle')
        .data(filteredNodes)
        .enter()
        .append('circle')
        .attr('class', d => `d3-node ${d.type}`)
        .attr('r', d => {
            if (d.type === 'domain' || d.type === 'aspect') return 20;
            if (d.type === 'particle') return 18;
            return 10;
        })
        .attr('fill', d => {
            if (d.type === 'domain') return '#10b981';
            if (d.type === 'aspect') return '#f59e0b';
            if (d.type === 'particle') return '#8b5cf6';
            if (d.type === 'root') return '#4f46e5';
            return '#6b7280';
        })
        .call(d3.drag()
            .on('start', dragStarted)
            .on('drag', dragged)
            .on('end', dragEnded)
        )
        .on('click', (event, d) => {
            showNodeInfo(d);
        })
        .on('mouseover', function(event, d) {
            highlightConnected(d, true);
        })
        .on('mouseout', function(event, d) {
            highlightConnected(d, false);
        });

    // Create labels
    const label = g.append('g')
        .selectAll('text')
        .data(filteredNodes)
        .enter()
        .append('text')
        .attr('class', d => `d3-label ${d.type === 'domain' || d.type === 'aspect' || d.type === 'particle' ? 'large' : ''}`)
        .text(d => d.label)
        .attr('text-anchor', 'middle')
        .attr('dy', d => {
            if (d.type === 'domain' || d.type === 'aspect') return 30;
            if (d.type === 'particle') return 28;
            return 20;
        });

    // Update positions on tick
    networkSimulation.on('tick', () => {
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);

        node
            .attr('cx', d => d.x)
            .attr('cy', d => d.y);

        label
            .attr('x', d => d.x)
            .attr('y', d => d.y);
    });

    function dragStarted(event, d) {
        if (!event.active) networkSimulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragEnded(event, d) {
        if (!event.active) networkSimulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    function highlightConnected(targetNode, highlight) {
        // Find connected node IDs
        const connectedIds = new Set();
        connectedIds.add(targetNode.id);

        filteredLinks.forEach(link => {
            const sourceId = link.source.id || link.source;
            const targetId = link.target.id || link.target;

            if (sourceId === targetNode.id) {
                connectedIds.add(targetId);
            }
            if (targetId === targetNode.id) {
                connectedIds.add(sourceId);
            }
        });

        // Update node opacity
        node.style('opacity', d => {
            if (!highlight) return 1;
            return connectedIds.has(d.id) ? 1 : 0.2;
        });

        // Update link opacity and width
        link.style('opacity', d => {
            if (!highlight) return 0.6;
            const sourceId = d.source.id || d.source;
            const targetId = d.target.id || d.target;
            return (sourceId === targetNode.id || targetId === targetNode.id) ? 1 : 0.1;
        })
        .attr('stroke-width', d => {
            if (!highlight) return 1.5;
            const sourceId = d.source.id || d.source;
            const targetId = d.target.id || d.target;
            return (sourceId === targetNode.id || targetId === targetNode.id) ? 3 : 1.5;
        });

        // Update label opacity
        label.style('opacity', d => {
            if (!highlight) return 1;
            return connectedIds.has(d.id) ? 1 : 0.2;
        });
    }
}

function showNodeInfo(node) {
    const panel = document.getElementById('nodeInfo');

    let html = `<h4>${node.description}</h4>`;

    if (node.type === 'root') {
        html += `<p><strong>Domain:</strong> ${node.domain} (${networkData.nodes.find(n => n.id === `domain-${node.domain}`).name})</p>`;
        html += `<p><strong>Aspect:</strong> ${node.aspect} (${networkData.nodes.find(n => n.id === `aspect-${node.aspect}`).name})</p>`;
    } else if (node.type === 'domain' || node.type === 'aspect') {
        // Count connected roots
        const connectedRoots = networkData.nodes.filter(n =>
            n.type === 'root' &&
            (n.domain === node.vowel || n.aspect === node.vowel)
        );
        html += `<p><strong>Connected roots:</strong> ${connectedRoots.length}</p>`;
        html += `<p><em>Examples: ${connectedRoots.slice(0, 3).map(r => r.label).join(', ')}</em></p>`;
    } else if (node.type === 'particle') {
        html += `<p><em>Particle series for ${node.name.toLowerCase()}</em></p>`;
    }

    panel.innerHTML = html;
}

function updateNetworkFilters() {
    if (networkData) {
        renderNetwork();
    }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    loadDictionaryStats();
});
