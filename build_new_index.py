import json

with open('clean_v1.json', 'r', encoding='utf-8') as f:
    v1_data = json.load(f)

with open('clean_v2.json', 'r', encoding='utf-8') as f:
    v2_data = json.load(f)

v1_json_str = json.dumps(v1_data, ensure_ascii=False)
v2_json_str = json.dumps(v2_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curriculum DBA • Matemáticas (1° a 11°)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
                    }
                }
            }
        }
    </script>

    <style>
        /* ================= TEMA OSCURO (DEFAULT) ================= */
        body {
            font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
            background-color: #070D18;
            color: #F8FAFC;
            transition: background-color 0.25s ease, color 0.25s ease;
        }

        .custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #0F172A; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #0284C7; border-radius: 9999px; }

        .card-surface {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .card-surface:hover {
            border-color: rgba(56, 189, 248, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
        }

        .glass-panel {
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .highlight-text {
            background-color: #FBBF24;
            color: #0F172A;
            font-weight: 800;
            padding: 1px 3px;
            border-radius: 3px;
        }

        .text-statement {
            color: #F8FAFC;
            font-weight: 600;
            line-height: 1.55;
        }

        .text-evidence {
            color: #CBD5E1;
            font-weight: 500;
            line-height: 1.5;
        }

        /* ================= TEMA CLARO - ALTO NIVEL DE TINTA (CONTRASTE PROFUNDO) ================= */
        body.light-theme {
            background-color: #F1F5F9;
            color: #0F172A;
        }

        body.light-theme .custom-scrollbar::-webkit-scrollbar-track { background: #E2E8F0; }
        body.light-theme .custom-scrollbar::-webkit-scrollbar-thumb { background: #0284C7; }

        body.light-theme .glass-panel {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        body.light-theme header {
            background: #FFFFFF !important;
            border-bottom-color: #CBD5E1 !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }

        body.light-theme .header-title { color: #0F172A !important; }
        body.light-theme .header-subtitle { color: #475569 !important; }

        body.light-theme .card-surface {
            background: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
        }
        body.light-theme .card-surface:hover {
            border-color: #0284C7 !important;
            box-shadow: 0 10px 20px -3px rgba(2, 132, 199, 0.15);
        }

        body.light-theme .text-statement {
            color: #0F172A !important; /* TINTA NEGRA PROFUNDA */
            font-weight: 700 !important;
        }

        body.light-theme .text-evidence {
            color: #1E293B !important; /* TINTA NEGRA/PIZARRA PROFUNDA */
            font-weight: 600 !important;
        }

        body.light-theme .evidence-box {
            background-color: #F8FAFC !important;
            border-color: #E2E8F0 !important;
        }

        body.light-theme .evidence-badge {
            background-color: #E2E8F0 !important;
            color: #0F172A !important;
            border-color: #CBD5E1 !important;
        }

        body.light-theme .badge-pill {
            background-color: #F1F5F9 !important;
            border-color: #CBD5E1 !important;
            color: #0F172A !important;
        }

        body.light-theme .input-search {
            background-color: #FFFFFF !important;
            border-color: #94A3B8 !important;
            color: #0F172A !important;
        }
        body.light-theme .input-search::placeholder { color: #64748B !important; }

        body.light-theme .filter-pill-inactive {
            background-color: #FFFFFF !important;
            color: #334155 !important;
            border-color: #CBD5E1 !important;
        }
        body.light-theme .filter-pill-inactive:hover {
            background-color: #F1F5F9 !important;
            color: #0F172A !important;
        }

        body.light-theme .master-item-inactive {
            background-color: #FFFFFF !important;
            color: #1E293B !important;
            border-color: #E2E8F0 !important;
        }
        body.light-theme .master-item-inactive:hover {
            background-color: #F8FAFC !important;
            border-color: #CBD5E1 !important;
        }

        body.light-theme footer {
            background-color: #FFFFFF !important;
            border-top-color: #CBD5E1 !important;
            color: #475569 !important;
        }
        body.light-theme footer p.text-slate-200 { color: #0F172A !important; }

        /* ================= ESTILOS DE IMPRESIÓN OFICIAL ================= */
        @media print {
            body * { visibility: hidden; }
            #printableSheet, #printableSheet * { visibility: visible; }
            #printableSheet {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                background: white !important;
                color: black !important;
                display: block !important;
            }
            .no-print { display: none !important; }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-slate-900">

    <!-- CABECERA INSTITUCIONAL LIMPIA -->
    <header class="sticky top-0 z-40 glass-panel border-b border-slate-800 shadow-sm transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                
                <!-- Logo & Título -->
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-black text-white text-lg shadow-md shrink-0">
                        ∑
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h1 class="header-title text-base sm:text-lg font-black tracking-tight leading-none text-white">
                                Curriculum DBA • Matemáticas
                            </h1>
                            <span id="versionIndicatorBadge" class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">
                                V.2 (2016)
                            </span>
                        </div>
                        <p class="header-subtitle text-xs text-slate-400 font-medium mt-0.5">
                            Educación Básica Primaria, Secundaria y Media Vocacional (1° a 11°)
                        </p>
                    </div>
                </div>

                <!-- Controles: Versión 1 / Versión 2, Modo Claro / Oscuro, Imprimir Ficha -->
                <div class="flex items-center gap-2 flex-wrap">

                    <!-- Switch V1 ⇄ V2 -->
                    <div class="bg-slate-900/90 p-0.5 rounded-xl border border-slate-700/80 flex items-center shadow-inner">
                        <button id="btnSwitchV1" onclick="switchVersion('v1')" class="px-3 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white">
                            V.1 (2015)
                        </button>
                        <button id="btnSwitchV2" onclick="switchVersion('v2')" class="px-3 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-sm">
                            V.2 (2016)
                        </button>
                    </div>

                    <!-- Modo Claro ⇄ Oscuro -->
                    <button id="themeToggleBtn" onclick="toggleTheme()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700">
                        <span id="themeToggleIcon">☀️</span>
                        <span id="themeToggleText">Modo Claro</span>
                    </button>

                    <!-- Imprimir Ficha Curricular del Grado -->
                    <button onclick="imprimirFichaGrado()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700 shadow-sm" title="Imprimir únicamente la ficha de DBAs y evidencias del grado seleccionado">
                        <svg class="w-3.5 h-3.5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                        <span>Imprimir Ficha</span>
                    </button>

                    <!-- Exportar JSON -->
                    <button onclick="descargarJSON()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                        <span class="hidden md:inline">JSON</span>
                    </button>

                </div>

            </div>

            <!-- Barra de Selección de Grados (Pills 1° a 11°) -->
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center justify-between gap-2 overflow-x-auto pb-1">
                <div class="flex items-center gap-1">
                    <span class="text-[11px] font-bold uppercase text-slate-400 mr-1 shrink-0">Grado:</span>
                    <button onclick="setGrade('all')" id="pill-grade-all" class="px-2.5 py-1 rounded-lg text-xs font-extrabold transition bg-cyan-500 text-slate-950 shadow-sm shrink-0">
                        Todos
                    </button>
                    <div id="gradesPillsContainer" class="flex items-center gap-1"></div>
                </div>

                <!-- Conmutador de Modo de Vista (Grid Compacto vs Panel Dividido) -->
                <div class="flex items-center gap-1.5 bg-slate-900/80 p-0.5 rounded-xl border border-slate-800 shrink-0">
                    <button id="btnViewGrid" onclick="setViewMode('grid')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition bg-cyan-500 text-slate-950 flex items-center gap-1">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
                        <span>Tarjetas</span>
                    </button>
                    <button id="btnViewSplit" onclick="setViewMode('split')" class="px-2.5 py-1 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white flex items-center gap-1">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2"/></svg>
                        <span>Explorador</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- ÁREA PRINCIPAL -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 w-full flex-grow">

        <!-- Barra de Búsqueda y Filtros de Pensamientos -->
        <div class="glass-panel rounded-2xl p-3.5 shadow-sm mb-5 flex flex-wrap items-center justify-between gap-3">
            
            <!-- Input de Búsqueda en tiempo real -->
            <div class="relative flex-1 min-w-[260px]">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-cyan-400">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                </div>
                <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Buscar en enunciados y evidencias (ej: fracciones, pitágoras, derivada, área, probabilidad)..." 
                       class="input-search w-full pl-9 pr-8 py-2 rounded-xl text-xs sm:text-sm transition outline-none shadow-inner bg-slate-900 border border-slate-700 text-white">
                <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-2.5 flex items-center text-slate-400 hover:text-white">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Filtros por los 5 Pensamientos Matemáticos -->
            <div class="flex items-center gap-1 flex-wrap">
                <span class="text-xs font-bold text-slate-400 mr-1">Pensamiento:</span>
                <button onclick="setThought('all')" class="filter-pill-thought px-2 py-1 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950 transition" data-thought="all">Todos</button>
                <button onclick="setThought('num')" class="filter-pill-thought filter-pill-inactive px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 transition" data-thought="num">🔢 Numérico</button>
                <button onclick="setThought('met')" class="filter-pill-thought filter-pill-inactive px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 transition" data-thought="met">📏 Métrico</button>
                <button onclick="setThought('geo')" class="filter-pill-thought filter-pill-inactive px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 transition" data-thought="geo">📐 Geométrico</button>
                <button onclick="setThought('ale')" class="filter-pill-thought filter-pill-inactive px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 transition" data-thought="ale">📊 Aleatorio</button>
                <button onclick="setThought('var')" class="filter-pill-thought filter-pill-inactive px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 transition" data-thought="var">📈 Variacional</button>
            </div>

        </div>

        <!-- Barra de Estado y Conteo de Resultados -->
        <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-3 px-1">
            <div class="flex items-center gap-2">
                <span id="activeFilterSummary">Mostrando todos los grados</span>
                <span id="totalVisibleCount" class="px-2 py-0.5 rounded-md bg-slate-800 text-cyan-400 font-extrabold border border-slate-700"></span>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="expandAllEvidences(true)" class="text-xs text-cyan-400 hover:underline font-semibold">Expandir todas</button>
                <span>•</span>
                <button onclick="expandAllEvidences(false)" class="text-xs text-cyan-400 hover:underline font-semibold">Colapsar todas</button>
            </div>
        </div>

        <!-- MODO 1: VISTA GRID COMPACTO DE TARJETAS -->
        <div id="viewGridContainer" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4"></div>

        <!-- MODO 2: VISTA EXPLORADOR / PANEL DIVIDIDO (MASTER-DETAIL) -->
        <div id="viewSplitContainer" class="hidden grid grid-cols-1 lg:grid-cols-12 gap-5">
            <!-- Columna Izquierda: Lista Maestra de DBAs -->
            <div class="lg:col-span-4 xl:col-span-3 space-y-2 max-h-[750px] overflow-y-auto pr-1 custom-scrollbar" id="splitMasterList"></div>
            
            <!-- Columna Derecha: Detalle Completo del DBA Seleccionado -->
            <div class="lg:col-span-8 xl:col-span-9" id="splitDetailPane"></div>
        </div>

    </main>

    <!-- PIE DE PÁGINA -->
    <footer class="bg-slate-950 text-slate-400 border-t border-slate-900 py-5 text-xs text-center mt-10 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-1">
            <p class="text-slate-200 font-bold">
                Derechos Básicos de Aprendizaje • Área de Matemáticas (1° a 11°)
            </p>
            <p class="text-[11px] text-slate-500">
                Herramienta interactiva para planeación docente y seguimiento curricular • Ministerio de Educación Nacional de Colombia
            </p>
        </div>
    </footer>

    <!-- DOCUMENTO OCULTO PARA IMPRESIÓN OFICIAL LIMPIA -->
    <div id="printableSheet" class="hidden p-8 text-black bg-white"></div>

    <!-- TOAST DE COPIADO -->
    <div id="copyToast" class="fixed bottom-5 right-5 z-50 hidden bg-cyan-600 text-white px-4 py-2.5 rounded-xl shadow-2xl flex items-center gap-2 text-xs font-bold border border-cyan-400">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
        <span>¡Copiado al portapapeles listo para planeador de clase!</span>
    </div>

    <!-- SCRIPTS DE INTERACCIÓN -->
    <script>
        const DBA_V1 = __V1_DATA__;
        const DBA_V2 = __V2_DATA__;

        const GRADE_METADATA = {
            "1": { name: "1° de Primaria", ciclo: "Ciclo I (Básica Primaria)" },
            "2": { name: "2° de Primaria", ciclo: "Ciclo I (Básica Primaria)" },
            "3": { name: "3° de Primaria", ciclo: "Ciclo I (Básica Primaria)" },
            "4": { name: "4° de Primaria", ciclo: "Ciclo II (Básica Primaria)" },
            "5": { name: "5° de Primaria", ciclo: "Ciclo II (Básica Primaria)" },
            "6": { name: "6° de Secundaria", ciclo: "Ciclo III (Básica Secundaria)" },
            "7": { name: "7° de Secundaria", ciclo: "Ciclo III (Básica Secundaria)" },
            "8": { name: "8° de Secundaria", ciclo: "Ciclo IV (Básica Secundaria)" },
            "9": { name: "9° de Secundaria", ciclo: "Ciclo IV (Básica Secundaria)" },
            "10": { name: "10° Media Vocacional", ciclo: "Media Vocacional" },
            "11": { name: "11° Media Vocacional", ciclo: "Media Vocacional" }
        };

        const THOUGHT_COLORS = {
            "num": { bg: "bg-blue-500/10 text-blue-400 border-blue-500/30", label: "Numérico" },
            "met": { bg: "bg-emerald-500/10 text-emerald-400 border-emerald-500/30", label: "Métrico" },
            "geo": { bg: "bg-purple-500/10 text-purple-400 border-purple-500/30", label: "Geométrico" },
            "ale": { bg: "bg-amber-500/10 text-amber-400 border-amber-500/30", label: "Aleatorio" },
            "var": { bg: "bg-rose-500/10 text-rose-400 border-rose-500/30", label: "Variacional" }
        };

        // Estado
        let activeVersion = 'v2';
        let currentGrade = 'all';
        let currentThought = 'all';
        let currentView = 'grid'; // 'grid' | 'split'
        let activeSelectedDbaKey = null; // 'grade_num'
        let cardExpandedStates = {}; // key -> boolean

        function getStored(k) {
            try { return localStorage.getItem(k); } catch(e) { return null; }
        }
        function setStored(k, v) {
            try { localStorage.setItem(k, v); } catch(e) {}
        }

        document.addEventListener('DOMContentLoaded', () => {
            const savedTheme = getStored('theme_dba_mat');
            if (savedTheme === 'light') {
                enableLightTheme(false);
            } else {
                renderGradePills();
            }
        });

        /* ================= TEMA CLARO / OSCURO ================= */
        function toggleTheme() {
            const isLight = document.body.classList.contains('light-theme');
            if (isLight) {
                enableDarkTheme(true);
            } else {
                enableLightTheme(true);
            }
        }

        function enableLightTheme(save = true) {
            document.body.classList.add('light-theme');
            const icon = document.getElementById('themeToggleIcon');
            const txt = document.getElementById('themeToggleText');
            const btn = document.getElementById('themeToggleBtn');
            if (icon) icon.innerText = '🌙';
            if (txt) txt.innerText = 'Modo Oscuro';
            if (btn) btn.className = "px-3 py-1.5 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-900 text-xs font-bold transition flex items-center gap-1.5 border border-slate-300 shadow-sm";
            if (save) setStored('theme_dba_mat', 'light');
            renderGradePills();
        }

        function enableDarkTheme(save = true) {
            document.body.classList.remove('light-theme');
            const icon = document.getElementById('themeToggleIcon');
            const txt = document.getElementById('themeToggleText');
            const btn = document.getElementById('themeToggleBtn');
            if (icon) icon.innerText = '☀️';
            if (txt) txt.innerText = 'Modo Claro';
            if (btn) btn.className = "px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700 shadow-sm";
            if (save) setStored('theme_dba_mat', 'dark');
            renderGradePills();
        }

        /* ================= CAMBIO DE VERSIÓN V1 / V2 ================= */
        function switchVersion(ver) {
            activeVersion = ver;
            const btnV1 = document.getElementById('btnSwitchV1');
            const btnV2 = document.getElementById('btnSwitchV2');
            const badge = document.getElementById('versionIndicatorBadge');

            if (ver === 'v1') {
                btnV1.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-sm";
                btnV2.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white";
                badge.innerText = "V.1 (2015)";
                badge.className = "text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/30";
            } else {
                btnV2.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-sm";
                btnV1.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white";
                badge.innerText = "V.2 (2016)";
                badge.className = "text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
            }

            activeSelectedDbaKey = null;
            renderView();
        }

        function setViewMode(mode) {
            currentView = mode;
            const btnGrid = document.getElementById('btnViewGrid');
            const btnSplit = document.getElementById('btnViewSplit');
            const gridContainer = document.getElementById('viewGridContainer');
            const splitContainer = document.getElementById('viewSplitContainer');

            if (mode === 'grid') {
                btnGrid.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-cyan-500 text-slate-950 flex items-center gap-1";
                btnSplit.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white flex items-center gap-1";
                gridContainer.classList.remove('hidden');
                splitContainer.classList.add('hidden');
            } else {
                btnSplit.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-cyan-500 text-slate-950 flex items-center gap-1";
                btnGrid.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white flex items-center gap-1";
                gridContainer.classList.add('hidden');
                splitContainer.classList.remove('hidden');
            }

            renderView();
        }

        function renderGradePills() {
            const container = document.getElementById('gradesPillsContainer');
            container.innerHTML = '';
            const isLight = document.body.classList.contains('light-theme');

            for (let g = 1; g <= 11; g++) {
                const btn = document.createElement('button');
                btn.id = `pill-grade-${g}`;
                btn.innerText = `${g}°`;
                const inactiveClass = isLight
                    ? "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-slate-200 text-slate-800 hover:bg-slate-300 border border-slate-300 shrink-0"
                    : "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 shrink-0";
                btn.className = inactiveClass;
                btn.onclick = () => setGrade(g.toString());
                container.appendChild(btn);
            }
            setGrade(currentGrade);
        }

        function setGrade(g) {
            currentGrade = g;
            const isLight = document.body.classList.contains('light-theme');

            document.querySelectorAll('#gradesPillsContainer button, #pill-grade-all').forEach(btn => {
                btn.className = isLight
                    ? "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-slate-200 text-slate-800 hover:bg-slate-300 border border-slate-300 shrink-0"
                    : "px-2.5 py-1 rounded-lg text-xs font-bold transition bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700 shrink-0";
            });

            const activeBtn = document.getElementById(g === 'all' ? 'pill-grade-all' : `pill-grade-${g}`);
            if (activeBtn) {
                activeBtn.className = "px-2.5 py-1 rounded-lg text-xs font-extrabold transition bg-cyan-500 text-slate-950 shadow-sm shrink-0";
            }

            activeSelectedDbaKey = null;
            renderView();
        }

        function setThought(t) {
            currentThought = t;
            const isLight = document.body.classList.contains('light-theme');

            document.querySelectorAll('.filter-pill-thought').forEach(btn => {
                btn.className = isLight
                    ? "filter-pill-thought px-2 py-1 rounded-lg text-xs font-semibold bg-white text-slate-800 border border-slate-300 hover:bg-slate-100 transition"
                    : "filter-pill-thought px-2 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition";
            });

            const active = document.querySelector(`.filter-pill-thought[data-thought="${t}"]`);
            if (active) {
                active.className = "filter-pill-thought px-2 py-1 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950 transition";
            }

            activeSelectedDbaKey = null;
            renderView();
        }

        function getFilteredDbas() {
            const db = activeVersion === 'v1' ? DBA_V1 : DBA_V2;
            const query = (document.getElementById('searchInput')?.value || '').trim().toLowerCase();
            const list = [];

            const gradesToScan = currentGrade === 'all' 
                ? Object.keys(db).sort((a,b) => parseInt(a) - parseInt(b))
                : [currentGrade];

            gradesToScan.forEach(gStr => {
                const gradeObj = db[gStr] || {};
                const dbaKeys = Object.keys(gradeObj).sort((a,b) => parseInt(a) - parseInt(b));

                dbaKeys.forEach(dbaNum => {
                    const dba = gradeObj[dbaNum];
                    if (currentThought !== 'all' && dba.pensamiento_key !== currentThought) {
                        return;
                    }

                    if (query.length > 0) {
                        const matchStmt = (dba.statement || '').toLowerCase().includes(query);
                        const matchEvid = (dba.evidencias || []).some(e => e.toLowerCase().includes(query));
                        if (!matchStmt && !matchEvid) return;
                    }

                    list.push({
                        grade: gStr,
                        num: dbaNum,
                        key: `${gStr}_${dbaNum}`,
                        statement: dba.statement,
                        evidencias: dba.evidencias || [],
                        pensamiento_key: dba.pensamiento_key || 'num',
                        pensamiento_nombre: dba.pensamiento_nombre || 'Pensamiento Numérico'
                    });
                });
            });

            return list;
        }

        function renderView() {
            const list = getFilteredDbas();
            const countBadge = document.getElementById('totalVisibleCount');
            const summary = document.getElementById('activeFilterSummary');

            const gradeLabel = currentGrade === 'all' ? 'todos los grados (1° a 11°)' : `Grado ${currentGrade}°`;
            const thoughtLabel = currentThought === 'all' ? '' : ` • ${currentThought.toUpperCase()}`;
            summary.innerText = `Mostrando ${gradeLabel}${thoughtLabel}`;
            countBadge.innerText = `${list.length} DBAs disponibles`;

            if (currentView === 'grid') {
                renderGridView(list);
            } else {
                renderSplitView(list);
            }
        }

        /* ================= RENDERIZADO GRID COMPACTO ================= */
        function renderGridView(list) {
            const container = document.getElementById('viewGridContainer');
            container.innerHTML = '';

            if (list.length === 0) {
                container.innerHTML = `
                    <div class="col-span-full text-center py-12 glass-panel rounded-2xl p-6">
                        <div class="text-3xl mb-2">🔍</div>
                        <h3 class="text-sm font-bold text-slate-300">No se encontraron DBAs con los filtros seleccionados</h3>
                        <p class="text-xs text-slate-500 mt-1">Prueba cambiando de grado o limpiando la barra de búsqueda.</p>
                        <button onclick="clearSearch()" class="mt-3 px-3 py-1.5 rounded-lg bg-cyan-500 text-slate-950 text-xs font-black">Restablecer filtros</button>
                    </div>
                `;
                return;
            }

            const query = (document.getElementById('searchInput')?.value || '').trim().toLowerCase();

            list.forEach(item => {
                const meta = GRADE_METADATA[item.grade] || { name: `Grado ${item.grade}°` };
                const thInfo = THOUGHT_COLORS[item.pensamiento_key] || THOUGHT_COLORS['num'];
                const isExpanded = cardExpandedStates[item.key] !== false;

                const card = document.createElement('div');
                card.className = "card-surface rounded-2xl p-4 flex flex-col justify-between";
                card.id = `card-${item.key}`;

                const highlightedStatement = highlightText(item.statement, query);

                const evidItems = item.evidencias.map((ev, idx) => `
                    <li class="flex items-start gap-2 text-xs leading-relaxed text-evidence">
                        <span class="evidence-badge w-4 h-4 rounded-full bg-slate-800 text-cyan-400 font-extrabold flex items-center justify-center shrink-0 text-[10px] mt-0.5 border border-slate-700">
                            ${idx + 1}
                        </span>
                        <span>${highlightText(ev, query)}</span>
                    </li>
                `).join('');

                card.innerHTML = `
                    <div>
                        <!-- Header de la Tarjeta Compacta -->
                        <div class="flex items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-800/80">
                            <div class="flex items-center gap-1.5">
                                <span class="px-2 py-0.5 rounded-md bg-cyan-500 text-slate-950 font-black text-xs">
                                    ${item.grade}° • DBA ${item.num}
                                </span>
                                <span class="text-[10px] font-bold px-2 py-0.5 rounded-md border ${thInfo.bg}">
                                    ${thInfo.label}
                                </span>
                            </div>
                            <div class="flex items-center gap-1">
                                <button onclick="copiarDbaIndividual('${item.grade}', '${item.num}')" title="Copiar al portapapeles para planeador" class="p-1 rounded-md hover:bg-slate-800 text-slate-400 hover:text-cyan-400 transition">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                                </button>
                                <button onclick="toggleCardEvidence('${item.key}')" class="p-1 rounded-md hover:bg-slate-800 text-slate-400 hover:text-white transition" title="Colapsar o expandir evidencias">
                                    <svg id="arrow-${item.key}" class="w-3.5 h-3.5 transform transition-transform ${isExpanded ? '' : '-rotate-90'}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
                                </button>
                            </div>
                        </div>

                        <!-- Enunciado Oficial -->
                        <div class="mb-3">
                            <h3 class="text-statement text-xs sm:text-sm">
                                ${highlightedStatement}
                            </h3>
                        </div>

                        <!-- Contenedor Colapsable de Evidencias -->
                        <div id="evid-box-${item.key}" class="${isExpanded ? '' : 'hidden'} evidence-box bg-slate-900/60 rounded-xl p-3 border border-slate-800/80 mt-2">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">
                                    Evidencias de Aprendizaje (${item.evidencias.length})
                                </span>
                            </div>
                            <ul class="space-y-2">
                                ${evidItems}
                            </ul>
                        </div>
                    </div>
                `;

                container.appendChild(card);
            });
        }

        function toggleCardEvidence(key) {
            const box = document.getElementById(`evid-box-${key}`);
            const arrow = document.getElementById(`arrow-${key}`);
            if (box) {
                const isHidden = box.classList.contains('hidden');
                if (isHidden) {
                    box.classList.remove('hidden');
                    if (arrow) arrow.classList.remove('-rotate-90');
                    cardExpandedStates[key] = true;
                } else {
                    box.classList.add('hidden');
                    if (arrow) arrow.classList.add('-rotate-90');
                    cardExpandedStates[key] = false;
                }
            }
        }

        function expandAllEvidences(expand) {
            const list = getFilteredDbas();
            list.forEach(item => {
                cardExpandedStates[item.key] = expand;
            });
            renderView();
        }

        /* ================= RENDERIZADO PANEL DIVIDIDO (MASTER-DETAIL) ================= */
        function renderSplitView(list) {
            const masterContainer = document.getElementById('splitMasterList');
            const detailPane = document.getElementById('splitDetailPane');
            masterContainer.innerHTML = '';

            if (list.length === 0) {
                masterContainer.innerHTML = '<div class="text-xs text-slate-500 p-3">No hay DBAs</div>';
                detailPane.innerHTML = '<div class="glass-panel p-6 rounded-2xl text-center text-xs text-slate-500">Sin resultados</div>';
                return;
            }

            if (!activeSelectedDbaKey || !list.some(it => it.key === activeSelectedDbaKey)) {
                activeSelectedDbaKey = list[0].key;
            }

            list.forEach(item => {
                const isSelected = item.key === activeSelectedDbaKey;
                const thInfo = THOUGHT_COLORS[item.pensamiento_key] || THOUGHT_COLORS['num'];

                const btn = document.createElement('div');
                btn.className = isSelected 
                    ? "p-3 rounded-xl cursor-pointer border transition bg-cyan-500/15 border-cyan-400 text-white shadow-sm"
                    : "master-item-inactive p-3 rounded-xl cursor-pointer border transition bg-slate-900 border-slate-800 text-slate-300 hover:border-slate-700";
                
                btn.onclick = () => {
                    activeSelectedDbaKey = item.key;
                    renderSplitView(list);
                };

                btn.innerHTML = `
                    <div class="flex items-center justify-between gap-1 mb-1">
                        <span class="text-xs font-black ${isSelected ? 'text-cyan-400' : 'text-slate-300'}">
                            ${item.grade}° • DBA ${item.num}
                        </span>
                        <span class="text-[9px] font-bold px-1.5 py-0.2 rounded border ${thInfo.bg}">
                            ${thInfo.label}
                        </span>
                    </div>
                    <p class="text-[11px] line-clamp-2 leading-relaxed text-statement">
                        ${item.statement}
                    </p>
                `;

                masterContainer.appendChild(btn);
            });

            // Render Detail Pane
            const activeItem = list.find(it => it.key === activeSelectedDbaKey) || list[0];
            const meta = GRADE_METADATA[activeItem.grade] || { name: `Grado ${activeItem.grade}°`, ciclo: "Oficial" };
            const thInfo = THOUGHT_COLORS[activeItem.pensamiento_key] || THOUGHT_COLORS['num'];

            const evidListHtml = activeItem.evidencias.map((ev, i) => `
                <li class="flex items-start gap-3 text-xs leading-relaxed text-evidence p-2.5 rounded-xl bg-slate-950/40 border border-slate-800/80">
                    <span class="evidence-badge w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 font-extrabold flex items-center justify-center shrink-0 text-xs mt-0.5 border border-cyan-500/30">
                        ${i + 1}
                    </span>
                    <span class="flex-1">${ev}</span>
                </li>
            `).join('');

            detailPane.innerHTML = `
                <div class="card-surface rounded-2xl p-6 shadow-xl border border-slate-800">
                    
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-800">
                        <div>
                            <div class="flex items-center gap-2 mb-1">
                                <span class="px-2.5 py-1 rounded-lg bg-cyan-500 text-slate-950 font-black text-xs">
                                    Grado ${activeItem.grade}° • DBA #${activeItem.num}
                                </span>
                                <span class="text-xs font-bold px-2 py-0.5 rounded-md border ${thInfo.bg}">
                                    ${activeItem.pensamiento_nombre}
                                </span>
                            </div>
                            <span class="text-xs text-slate-400 font-semibold">${meta.ciclo} • Modo ${activeVersion === 'v1' ? 'Versión 1 (2015)' : 'Versión 2 (2016)'}</span>
                        </div>

                        <div class="flex items-center gap-2">
                            <button onclick="copiarDbaIndividual('${activeItem.grade}', '${activeItem.num}')" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                                <span>Copiar para Planeador</span>
                            </button>
                        </div>
                    </div>

                    <!-- Enunciado Principal -->
                    <div class="mb-5">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider text-cyan-400 block mb-1.5">Enunciado Estructurante MEN:</span>
                        <h2 class="text-statement text-base sm:text-lg">
                            ${activeItem.statement}
                        </h2>
                    </div>

                    <!-- Lista de Evidencias -->
                    <div class="evidence-box bg-slate-900/80 rounded-xl p-4 border border-slate-800">
                        <div class="flex items-center justify-between mb-3 pb-2 border-b border-slate-800">
                            <span class="text-xs font-black uppercase tracking-wider text-cyan-400">
                                Evidencias de Aprendizaje Oficiales (${activeItem.evidencias.length})
                            </span>
                            <span class="text-[10px] text-slate-400">Directrices curriculares oficiales</span>
                        </div>
                        <ul class="space-y-2.5">
                            ${evidListHtml}
                        </ul>
                    </div>

                </div>
            `;
        }

        /* ================= BÚSQUEDA Y RESALTADOR ================= */
        function handleSearch() {
            const query = document.getElementById('searchInput').value.trim();
            const clearBtn = document.getElementById('clearSearchBtn');
            if (query.length > 0) {
                clearBtn.classList.remove('hidden');
            } else {
                clearBtn.classList.add('hidden');
            }
            renderView();
        }

        function clearSearch() {
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            renderView();
        }

        function highlightText(text, query) {
            if (!query || !text) return text;
            const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
            return text.replace(regex, '<span class="highlight-text">$1</span>');
        }

        /* ================= COPIAR AL PORTAPAPELES ================= */
        function copiarDbaIndividual(gradeNum, dbaNum) {
            const db = activeVersion === 'v1' ? DBA_V1 : DBA_V2;
            const dba = db[gradeNum][dbaNum];
            const meta = GRADE_METADATA[gradeNum] || { name: `Grado ${gradeNum}°` };

            let text = `========================================================\\n`;
            text += `DERECHO BÁSICO DE APRENDIZAJE • MATEMÁTICAS MEN\\n`;
            text += `${meta.name} • ${meta.ciclo} • DBA #${dbaNum}\\n`;
            text += `Pensamiento: ${dba.pensamiento_nombre || 'Matemático'}\\n`;
            text += `Versión: ${activeVersion === 'v1' ? 'V.1 (2015)' : 'V.2 (2016)'}\\n`;
            text += `========================================================\\n\\n`;
            text += `ENUNCIADO:\\n"${dba.statement}"\\n\\n`;
            text += `EVIDENCIAS DE APRENDIZAJE:\\n`;
            (dba.evidencias || []).forEach((ev, i) => {
                text += `  ${i + 1}. ${ev}\\n`;
            });

            const showToast = () => {
                const toast = document.getElementById('copyToast');
                if (toast) {
                    toast.classList.remove('hidden');
                    setTimeout(() => toast.classList.add('hidden'), 2200);
                }
            };

            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(text).then(showToast).catch(() => {
                    fallbackCopy(text);
                    showToast();
                });
            } else {
                fallbackCopy(text);
                showToast();
            }
        }

        function fallbackCopy(text) {
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.focus();
            ta.select();
            try { document.execCommand('copy'); } catch(e) {}
            document.body.removeChild(ta);
        }

        /* ================= IMPRESIÓN EXCLUSIVA DE FICHA CURRICULAR ================= */
        function imprimirFichaGrado() {
            const db = activeVersion === 'v1' ? DBA_V1 : DBA_V2;
            const targetGrade = currentGrade === 'all' ? '1' : currentGrade;
            const meta = GRADE_METADATA[targetGrade];
            const gradeDbas = db[targetGrade] || {};

            const sheet = document.getElementById('printableSheet');
            let contentHtml = `
                <div style="font-family: Arial, sans-serif; color: #000; padding: 20px;">
                    <div style="border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 20px;">
                        <h1 style="font-size: 20px; font-weight: bold; margin: 0; text-transform: uppercase;">
                            Ficha Curricular de Matemáticas • Derechos Básicos de Aprendizaje
                        </h1>
                        <p style="font-size: 13px; margin: 4px 0 0 0; color: #333;">
                            <strong>${meta.name}</strong> | ${meta.ciclo} | Versión MEN: ${activeVersion === 'v1' ? 'Versión 1 (2015)' : 'Versión 2 (2016)'}
                        </p>
                    </div>
            `;

            Object.keys(gradeDbas).sort((a,b) => parseInt(a) - parseInt(b)).forEach(num => {
                const dba = gradeDbas[num];
                const evidHtml = (dba.evidencias || []).map((e, idx) => `
                    <li style="margin-bottom: 4px;"><strong>${idx + 1}.</strong> ${e}</li>
                `).join('');

                contentHtml += `
                    <div style="margin-bottom: 18px; page-break-inside: avoid; border: 1px solid #ccc; padding: 12px; border-radius: 6px;">
                        <div style="margin-bottom: 6px;">
                            <span style="font-weight: bold; font-size: 13px; background: #eee; padding: 2px 6px; border-radius: 3px;">DBA #${num}</span>
                            <span style="font-size: 11px; color: #555; margin-left: 8px;">${dba.pensamiento_nombre || ''}</span>
                        </div>
                        <p style="font-size: 13px; font-weight: bold; margin: 6px 0 8px 0; line-height: 1.4;">
                            ${dba.statement}
                        </p>
                        <div style="margin-top: 6px; padding-top: 6px; border-top: 1px dashed #ccc;">
                            <span style="font-size: 11px; font-weight: bold; text-transform: uppercase; color: #444;">Evidencias de Aprendizaje:</span>
                            <ul style="font-size: 12px; margin: 4px 0 0 16px; padding: 0; line-height: 1.4;">
                                ${evidHtml}
                            </ul>
                        </div>
                    </div>
                `;
            });

            contentHtml += `
                    <div style="font-size: 10px; color: #777; text-align: center; margin-top: 25px; border-top: 1px solid #ddd; padding-top: 8px;">
                        Documento curricular oficial extraído de los Derechos Básicos de Aprendizaje • Ministerio de Educación Nacional de Colombia
                    </div>
                </div>
            `;

            sheet.innerHTML = contentHtml;
            window.print();
        }

        function descargarJSON() {
            const db = activeVersion === 'v1' ? DBA_V1 : DBA_V2;
            const fileName = activeVersion === 'v1' ? 'dba_matematicas_v1_men_2015.json' : 'dba_matematicas_v2_men_2016.json';
            const blob = new Blob([JSON.stringify(db, null, 2)], { type: "application/json" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = fileName;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }
    </script>
</body>
</html>
"""

final_html = html_template.replace('__V1_DATA__', v1_json_str).replace('__V2_DATA__', v2_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html generado exitosamente sin errores!")
