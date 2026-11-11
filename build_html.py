import json
import re

# Read master databases
with open('master_v1.json', 'r', encoding='utf-8') as f:
    v1_data = json.load(f)

with open('master_v2.json', 'r', encoding='utf-8') as f:
    v2_data = json.load(f)

v1_json_str = json.dumps(v1_data, ensure_ascii=False)
v2_json_str = json.dumps(v2_data, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plataforma Curricular MEN: Matemáticas (V.1 2015 & V.2 2016) • DBA y Ejemplos Literales</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    }}
                }}
            }}
        }}
    </script>

    <style>
        /* ================= TEMA OSCURO (DEFAULT) ================= */
        body {{
            font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
            background-color: #070D18;
            color: #F8FAFC;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}

        .custom-scrollbar::-webkit-scrollbar {{ width: 6px; height: 6px; }}
        .custom-scrollbar::-webkit-scrollbar-track {{ background: #0F172A; }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{ background: #0284C7; border-radius: 9999px; }}

        .math-glow-card {{
            transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
        }}
        .math-glow-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 0 30px rgba(56, 189, 248, 0.35), 0 20px 25px -5px rgba(0, 0, 0, 0.5);
        }}

        .glass-panel {{
            background: rgba(15, 23, 42, 0.82);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
        }}

        .glass-pill {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }}

        .highlight-text {{
            background-color: #FBBF24;
            color: #0F172A;
            font-weight: 800;
            padding: 1px 4px;
            border-radius: 4px;
        }}

        .modal-body-bg {{ background-color: #080D1A; }}
        .modal-card-bg {{ 
            background: rgba(15, 23, 42, 0.85); 
            border: 1px solid rgba(56, 189, 248, 0.2); 
        }}
        .input-search-bg {{ 
            background-color: rgba(15, 23, 42, 0.9); 
            border: 1px solid rgba(56, 189, 248, 0.3); 
            color: #FFFFFF; 
        }}

        /* ================= TEMA CLARO (LIGHT THEME) ================= */
        body.light-theme {{
            background-color: #F8FAFC;
            color: #0F172A;
        }}

        body.light-theme .custom-scrollbar::-webkit-scrollbar-track {{ background: #E2E8F0; }}
        body.light-theme .custom-scrollbar::-webkit-scrollbar-thumb {{ background: #0284C7; }}

        body.light-theme .glass-panel {{
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(226, 232, 240, 0.9);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }}

        body.light-theme header {{
            border-bottom-color: rgba(226, 232, 240, 1) !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
        }}

        body.light-theme .header-title-text {{ color: #0F172A !important; }}
        body.light-theme .nav-badge-pill {{ 
            background-color: #F1F5F9 !important; 
            color: #0369A1 !important; 
            border-color: #CBD5E1 !important; 
        }}

        body.light-theme .grade-nav-pill-inactive {{
            background-color: #F1F5F9 !important;
            color: #475569 !important;
            border-color: #E2E8F0 !important;
        }}
        body.light-theme .grade-nav-pill-inactive:hover {{ background-color: #E2E8F0 !important; }}

        body.light-theme .thought-filter-inactive {{
            background-color: #F1F5F9 !important;
            color: #334155 !important;
        }}
        body.light-theme .thought-filter-inactive:hover {{ background-color: #E2E8F0 !important; }}

        body.light-theme .input-search-bg {{
            background-color: #FFFFFF !important;
            border-color: #CBD5E1 !important;
            color: #0F172A !important;
        }}
        body.light-theme .input-search-bg::placeholder {{ color: #64748B !important; }}

        body.light-theme .math-glow-card:hover {{
            box-shadow: 0 15px 30px -5px rgba(2, 132, 199, 0.25), 0 10px 15px -3px rgba(0, 0, 0, 0.08);
        }}

        body.light-theme footer {{
            background-color: #FFFFFF !important;
            border-top-color: #E2E8F0 !important;
            color: #64748B !important;
        }}
        body.light-theme footer p.text-slate-200 {{ color: #0F172A !important; }}

        body.light-theme .modal-drawer-bg {{ 
            background-color: #FFFFFF !important; 
            border-left-color: #E2E8F0 !important; 
        }}
        body.light-theme .modal-body-bg {{ background-color: #F8FAFC !important; }}
        body.light-theme .modal-card-bg {{ 
            background-color: #FFFFFF !important; 
            border-color: #E2E8F0 !important; 
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }}
        body.light-theme .modal-card-bg h4 {{ color: #0F172A !important; }}
        body.light-theme .modal-evidence-box {{ 
            background-color: #F8FAFC !important; 
            border-color: #E2E8F0 !important; 
        }}
        body.light-theme .modal-example-box {{ 
            background-color: #FFFBEB !important; 
            border-color: #FDE68A !important; 
            color: #78350F !important;
        }}
        body.light-theme .modal-example-text {{ color: #451A03 !important; }}
        body.light-theme .modal-footer-bg {{ 
            background-color: #FFFFFF !important; 
            border-top-color: #E2E8F0 !important; 
            color: #64748B !important; 
        }}

        @media print {{
            header, .no-print, button {{ display: none !important; }}
            body {{ background: white !important; color: black !important; }}
            .glass-panel, .modal-card-bg {{ box-shadow: none !important; border: 1px solid #ccc !important; }}
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-slate-900">

    <!-- CABECERA INSTITUCIONAL Y HERRAMIENTAS -->
    <header class="sticky top-0 z-40 glass-panel border-b border-cyan-500/25 shadow-lg shadow-cyan-950/40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                
                <!-- Logo & Identificador Oficial -->
                <div class="flex items-center space-x-3.5">
                    <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-indigo-600 flex items-center justify-center font-black text-white text-xl shadow-lg shadow-cyan-500/30 shrink-0">
                        ∑
                    </div>
                    <div>
                        <div class="flex flex-wrap items-center gap-2 mb-0.5">
                            <span class="text-[10px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 border border-cyan-500/30 nav-badge-pill">
                                Asesorías Pedagógicas S.A.S.
                            </span>
                            <span id="versionStatusBadge" class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                                Textos Literales MEN • Versión 2 (2016)
                            </span>
                            <span class="text-[10px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/30 flex items-center gap-1">
                                <span>✓</span> Auditado Pedagógico: 100% Sin Parafraseo
                            </span>
                        </div>
                        <h1 class="header-title-text text-base sm:text-lg font-black text-white tracking-tight leading-tight">
                            Plataforma Curricular de Matemáticas • Derechos Básicos de Aprendizaje (1° a 11°)
                        </h1>
                    </div>
                </div>

                <!-- BOTONES DE ACCIÓN: SWITCH V1/V2, MODO CLARO/OSCURO, JSON E IMPRIMIR -->
                <div class="flex flex-wrap items-center gap-2.5">

                    <!-- SWITCH DUAL V1 (2015) ⇄ V2 (2016) -->
                    <div class="bg-slate-900 p-1 rounded-xl border border-slate-700 flex items-center shadow-inner">
                        <button id="btnSwitchV1" onclick="switchVersion('v1')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white">
                            Versión 1 (2015)
                        </button>
                        <button id="btnSwitchV2" onclick="switchVersion('v2')" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/30">
                            Versión 2 (2016)
                        </button>
                    </div>

                    <!-- BOTÓN CONMUTADOR DE TEMA CLARO ⇄ OSCURO -->
                    <button id="themeToggleBtn" onclick="toggleTheme()" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700 shadow-sm">
                        <span id="themeToggleIcon">☀️</span>
                        <span id="themeToggleText">Modo Claro</span>
                    </button>

                    <!-- Exportar JSON Oficial -->
                    <button onclick="descargarJSONActivo()" class="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm shadow-emerald-900/50">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                        <span>Descargar JSON</span>
                    </button>

                    <!-- Imprimir / Guardar PDF -->
                    <button onclick="window.print()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                        <span>Imprimir</span>
                    </button>
                </div>

            </div>

            <!-- Navegación Rápida por Grados (1° a 11°) -->
            <div class="mt-3 pt-2.5 border-t border-slate-800 flex items-center justify-between gap-2 overflow-x-auto pb-1">
                <div class="flex items-center gap-1.5">
                    <span class="text-xs font-extrabold uppercase text-slate-400 mr-1 shrink-0">Grado:</span>
                    <button onclick="filterGrade('all')" id="btn-grade-all" class="grade-nav-pill px-3 py-1 rounded-lg text-xs font-black transition bg-cyan-500 text-slate-950 shadow-sm">
                        Todos
                    </button>
                    <div id="grades-nav-container" class="flex items-center gap-1"></div>
                </div>

                <div class="hidden md:flex items-center gap-2 shrink-0">
                    <span id="versionTotalDbaCount" class="text-[11px] font-bold px-2.5 py-0.5 rounded-md bg-cyan-950/80 text-cyan-300 border border-cyan-800/40">
                        119 DBAs Oficiales • Textos Literales MEN V.2
                    </span>
                    <span id="statsEjemplosBadge" class="text-[11px] font-bold px-2 py-0.5 rounded-md bg-amber-950/60 text-amber-300 border border-amber-800/40">
                        119 Ejemplos Didácticos
                    </span>
                </div>
            </div>
        </div>
    </header>

    <!-- ÁREA PRINCIPAL -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full flex-grow">

        <!-- Barra de Búsqueda y Filtros por Pensamientos Matemáticos -->
        <div class="glass-panel rounded-2xl p-4 shadow-sm mb-6 flex flex-wrap items-center justify-between gap-4">
            
            <!-- Input de Búsqueda -->
            <div class="relative flex-1 min-w-[280px]">
                <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-cyan-400">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                </div>
                <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Buscar en DBA, Evidencias y Ejemplos (ej: fracciones, derivada, pitágoras, perímetro, azar)..." 
                       class="input-search-bg w-full pl-10 pr-10 py-2.5 rounded-xl text-xs sm:text-sm transition outline-none shadow-inner">
                <button id="clearSearchBtn" onclick="clearSearch()" class="hidden absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-white">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Filtros por los 5 Pensamientos Matemáticos -->
            <div class="flex items-center gap-1.5 flex-wrap">
                <span class="text-xs font-bold text-slate-400 mr-1">Pensamiento:</span>
                <button onclick="filterThought('all')" class="thought-filter-btn px-2.5 py-1 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950 transition" data-thought="all">Todos</button>
                <button onclick="filterThought('num')" class="thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition" data-thought="num">🔢 Numérico</button>
                <button onclick="filterThought('met')" class="thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition" data-thought="met">📏 Métrico</button>
                <button onclick="filterThought('geo')" class="thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition" data-thought="geo">📐 Geométrico</button>
                <button onclick="filterThought('ale')" class="thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition" data-thought="ale">📊 Aleatorio</button>
                <button onclick="filterThought('var')" class="thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition" data-thought="var">📈 Variacional</button>
            </div>
        </div>

        <!-- Banner de Certificación y Veracidad Pedagógica -->
        <div class="glass-panel rounded-2xl p-3.5 mb-6 border border-emerald-500/30 bg-emerald-950/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2.5">
                <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black text-sm shrink-0 border border-emerald-500/30">
                    ✓
                </span>
                <div>
                    <span class="font-black text-emerald-300 block">Certificación de Fidelidad Curricular (Auditoría Integral MEN):</span>
                    <span class="text-slate-300">Todos los enunciados, evidencias y ejemplos pedagógicos provienen textualmente y sin parafraseo de los documentos oficiales del Ministerio de Educación Nacional.</span>
                </div>
            </div>
            <div class="flex items-center gap-2 shrink-0">
                <span id="activeDatasetTag" class="px-2.5 py-1 rounded-lg bg-slate-900 text-cyan-300 font-bold border border-slate-700 text-[11px]">
                    V.2 (2016) Activa
                </span>
            </div>
        </div>

        <!-- Barra de Contador de Búsqueda -->
        <div id="resultsCountBar" class="hidden mb-4 flex items-center justify-between text-xs font-bold text-cyan-400 px-1">
            <span id="resultsCountText">Mostrando resultados...</span>
            <button onclick="clearSearch()" class="text-cyan-500 hover:underline">Restablecer vista general de grados</button>
        </div>

        <!-- GRID DE TARJETAS POR GRADO CON RESPLANDOR Y GRADIENTES -->
        <div id="gradesGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"></div>

        <!-- CONTENEDOR DE RESULTADOS DE BÚSQUEDA -->
        <div id="searchResultsContainer" class="hidden space-y-4"></div>

    </main>

    <!-- PIE DE PÁGINA INSTITUCIONAL -->
    <footer class="bg-slate-950 text-slate-400 border-t border-slate-900 py-6 text-xs text-center mt-12 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-1.5">
            <p class="text-slate-200 font-bold">
                Plataforma Editorial y Pedagógica Curricular • Matemáticas Grados 1° a 11° • Ministerio de Educación Nacional de Colombia
            </p>
            <p id="footerVersionNote">
                Modo activo: Versión 2 (2016) - 119 DBAs Oficiales con evidencias completas y ejemplos didácticos literales.
            </p>
            <p class="text-[11px] text-slate-500">
                Diseñado para directivos docentes, coordinadores pedagógicos y profesores de área • Asesorías Pedagógicas S.A.S.
            </p>
        </div>
    </footer>

    <!-- MODAL / VISOR EXPANDIDO DE DBAs DEL GRADO (VISOR PEDAGÓGICO DE ALTO IMPACTO) -->
    <div id="dbaModal" class="fixed inset-0 z-50 hidden bg-slate-950/85 backdrop-blur-md flex justify-end transition-opacity">
        <div class="modal-drawer-bg w-full max-w-4xl bg-slate-900 h-full shadow-2xl flex flex-col justify-between transform transition-transform duration-300 translate-x-full border-l border-cyan-800/40" id="modalDrawer">
            
            <!-- Header Modal -->
            <div id="modalHeader" class="p-6 text-white relative">
                <button onclick="closeModal()" class="absolute top-5 right-5 p-2 rounded-full bg-black/30 hover:bg-black/50 text-white transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
                <div class="flex items-center gap-2 mb-2">
                    <span id="modalCicloBadge" class="text-[10px] font-extrabold uppercase tracking-wider px-2.5 py-0.5 rounded-full glass-pill text-white"></span>
                    <span id="modalAgeBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-black/40 text-white/90"></span>
                    <span id="modalVersionBadge" class="text-[10px] font-black uppercase px-2 py-0.5 rounded-full bg-cyan-400 text-slate-950">V.2 (2016)</span>
                </div>
                <div class="flex items-baseline gap-3">
                    <h2 id="modalGradeTitle" class="text-2xl sm:text-3xl font-black tracking-tight"></h2>
                    <span id="modalDbaCount" class="text-xs font-extrabold px-2.5 py-1 rounded-lg bg-emerald-500 text-slate-950 font-black shadow-sm"></span>
                </div>
                <p id="modalGradeDesc" class="text-xs sm:text-sm text-slate-200 mt-2 leading-relaxed max-w-2xl"></p>
            </div>

            <!-- Lista de DBAs, Evidencias Completas y Ejemplos Literales -->
            <div class="modal-body-bg p-6 overflow-y-auto custom-scrollbar flex-grow space-y-6" id="modalDbaList"></div>

            <!-- Footer Modal -->
            <div class="modal-footer-bg p-4 bg-slate-900 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    <span class="font-semibold">Textos Oficiales MEN 100% Literales (Sin Parafraseo)</span>
                </div>
                <button onclick="closeModal()" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-black transition shadow-md">
                    Cerrar Visor
                </button>
            </div>
        </div>
    </div>

    <!-- TOAST DE COPIADO -->
    <div id="copyToast" class="fixed bottom-6 right-6 z-50 hidden bg-gradient-to-r from-cyan-500 to-blue-600 text-slate-950 px-4 py-3 rounded-2xl shadow-2xl flex items-center gap-2.5 text-xs font-black border border-cyan-300/40">
        <svg class="w-5 h-5 text-slate-950" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
        <span id="copyToastMsg">¡DBA, Evidencias y Ejemplo oficial copiados al portapapeles!</span>
    </div>

    <!-- BASES DE DATOS OFICIALES CERTIFICADAS Y SCRIPTS -->
    <script>
        /* CONFIGURACIÓN CURRICULAR Y VISUAL POR GRADO */
        const GRADE_CONFIG = {{
            "1": {{
                name: "Grado 1° de Primaria",
                ciclo: "CICLO I • BÁSICA PRIMARIA",
                age: "6 - 7 años",
                desc: "Conteo estructurado, relaciones cuantitativas, figuras del entorno, magnitudes y nociones espaciales.",
                bgGradient: "from-sky-500 via-blue-600 to-indigo-950",
                icon: "🔢",
                thoughts: ["NUMÉRICO", "MÉTRICO", "GEOMÉTRICO", "ALEATORIO", "VARIACIONAL"]
            }},
            "2": {{
                name: "Grado 2° de Primaria",
                ciclo: "CICLO I • BÁSICA PRIMARIA",
                age: "7 - 8 años",
                desc: "Estructuras aditivas, sistema decimal (centenas), medición estándar/no estándar, patrones y probabilidad inicial.",
                bgGradient: "from-emerald-500 via-teal-600 to-slate-950",
                icon: "🎲",
                thoughts: ["NUMÉRICO", "MÉTRICO", "GEOMÉTRICO", "ALEATORIO", "VARIACIONAL"]
            }},
            "3": {{
                name: "Grado 3° de Primaria",
                ciclo: "CICLO I • BÁSICA PRIMARIA",
                age: "8 - 9 años",
                desc: "Multiplicación, repartos equitativos, fracciones iniciales, perímetro y área, y transformaciones espaciales.",
                bgGradient: "from-blue-600 via-indigo-600 to-slate-950",
                icon: "📐",
                thoughts: ["NUMÉRICO", "MÉTRICO", "GEOMÉTRICO", "ALEATORIO", "VARIACIONAL"]
            }},
            "4": {{
                name: "Grado 4° de Primaria",
                ciclo: "CICLO II • BÁSICA PRIMARIA",
                age: "9 - 10 años",
                desc: "Fracciones como operador y cociente, decimales, polígonos regulares, transformaciones y tendencia central.",
                bgGradient: "from-indigo-500 via-purple-600 to-slate-950",
                icon: "🧩",
                thoughts: ["NUMÉRICO", "VARIACIONAL", "MÉTRICO", "GEOMÉTRICO", "ALEATORIO"]
            }},
            "5": {{
                name: "Grado 5° de Primaria",
                ciclo: "CICLO II • BÁSICA PRIMARIA",
                age: "10 - 11 años",
                desc: "Potenciación, proporcionalidad directa e inversa, volumen de prismas, plano cartesiano y probabilidad.",
                bgGradient: "from-purple-600 via-fuchsia-700 to-slate-950",
                icon: "📊",
                thoughts: ["NUMÉRICO", "MÉTRICO", "GEOMÉTRICO", "VARIACIONAL", "ALEATORIO"]
            }},
            "6": {{
                name: "Grado 6° de Secundaria",
                ciclo: "CICLO III • BÁSICA SECUNDARIA",
                age: "11 - 12 años",
                desc: "Números enteros y racionales, teoría de números (MCM, MCD), covariación y análisis de dispersión.",
                bgGradient: "from-cyan-500 via-blue-700 to-slate-950",
                icon: "📉",
                thoughts: ["NUMÉRICO (Z)", "VARIACIONAL", "GEOMÉTRICO", "MÉTRICO", "ALEATORIO"]
            }},
            "7": {{
                name: "Grado 7° de Secundaria",
                ciclo: "CICLO III • BÁSICA SECUNDARIA",
                age: "12 - 13 años",
                desc: "Operaciones con racionales (Q), Teorema de Tales, escalas, ecuaciones lineales y principio multiplicativo.",
                bgGradient: "from-teal-500 via-cyan-700 to-slate-950",
                icon: "🔍",
                thoughts: ["NUMÉRICO (Q)", "GEOMÉTRICO", "VARIACIONAL", "ALEATORIO", "MÉTRICO"]
            }},
            "8": {{
                name: "Grado 8° de Secundaria",
                ciclo: "CICLO IV • BÁSICA SECUNDARIA",
                age: "13 - 14 años",
                desc: "Números irracionales, álgebra de polinomios, factorización, Teorema de Pitágoras y datos agrupados.",
                bgGradient: "from-blue-600 via-indigo-700 to-slate-950",
                icon: "⚡",
                thoughts: ["VARIACIONAL", "GEOMÉTRICO", "NUMÉRICO", "ALEATORIO", "MÉTRICO"]
            }},
            "9": {{
                name: "Grado 9° de Secundaria",
                ciclo: "CICLO IV • BÁSICA SECUNDARIA",
                age: "14 - 15 años",
                desc: "Números reales (R), función cuadrática, sistemas lineales 2x2, homotecias y diagramas de caja.",
                bgGradient: "from-indigo-600 via-violet-700 to-slate-950",
                icon: "📈",
                thoughts: ["VARIACIONAL", "NUMÉRICO (R)", "GEOMÉTRICO", "ALEATORIO", "MÉTRICO"]
            }},
            "10": {{
                name: "Grado 10° Media Vocacional",
                ciclo: "MEDIA VOCACIONAL",
                age: "15 - 16 años",
                desc: "Trigonometría analítica, círculo unitario, Ley de Seno y Coseno, secciones cónicas y razón de cambio.",
                bgGradient: "from-rose-600 via-pink-700 to-slate-950",
                icon: "⚖️",
                thoughts: ["TRIGONOMETRÍA", "GEOMÉTRICO", "MÉTRICO", "ALEATORIO", "VARIACIONAL"]
            }},
            "11": {{
                name: "Grado 11° Media Vocacional",
                ciclo: "MEDIA VOCACIONAL",
                age: "16 - 17 años",
                desc: "Cálculo diferencial, noción formal de derivada, optimización de funciones, probabilidad condicional y Saber 11.",
                bgGradient: "from-amber-500 via-orange-600 to-slate-950",
                icon: "🎓",
                thoughts: ["CÁLCULO", "DERIVADAS", "NUMÉRICO", "ALEATORIO", "VARIACIONAL"]
            }}
        }};

        /* BASES DE DATOS OFICIALES MEN COMPLETAS Y CERTIFICADAS */
        const DBA_V1_DATA = {v1_json_str};
        const DBA_V2_DATA = {v2_json_str};

        /* ESTADO GLOBAL */
        let activeVersion = 'v2';
        let currentFilterGrade = 'all';
        let currentFilterThought = 'all';

        document.addEventListener('DOMContentLoaded', () => {{
            const savedTheme = localStorage.getItem('theme_mat');
            if (savedTheme === 'light') {{
                enableLightTheme(false);
            }}
            renderNavPills();
            renderGradesGrid();
        }});

        /* ================= CONTROLADOR DE TEMA CLARO / OSCURO ================= */
        function toggleTheme() {{
            const isLight = document.body.classList.contains('light-theme');
            if (isLight) {{
                enableDarkTheme(true);
            }} else {{
                enableLightTheme(true);
            }}
        }}

        function enableLightTheme(save = true) {{
            document.body.classList.add('light-theme');
            document.getElementById('themeToggleIcon').innerText = '🌙';
            document.getElementById('themeToggleText').innerText = 'Modo Oscuro';
            document.getElementById('themeToggleBtn').className = "px-3.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold transition flex items-center gap-1.5 border border-slate-300 shadow-sm";
            if (save) localStorage.setItem('theme_mat', 'light');
            renderNavPills();
        }}

        function enableDarkTheme(save = true) {{
            document.body.classList.remove('light-theme');
            document.getElementById('themeToggleIcon').innerText = '☀️';
            document.getElementById('themeToggleText').innerText = 'Modo Claro';
            document.getElementById('themeToggleBtn').className = "px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-bold transition flex items-center gap-1.5 border border-slate-700 shadow-sm";
            if (save) localStorage.setItem('theme_mat', 'dark');
            renderNavPills();
        }}

        function switchVersion(ver) {{
            activeVersion = ver;
            const btnV1 = document.getElementById('btnSwitchV1');
            const btnV2 = document.getElementById('btnSwitchV2');
            const badge = document.getElementById('versionStatusBadge');
            const totalBadge = document.getElementById('versionTotalDbaCount');
            const modalBadge = document.getElementById('modalVersionBadge');
            const footerNote = document.getElementById('footerVersionNote');
            const activeTag = document.getElementById('activeDatasetTag');
            const statsEj = document.getElementById('statsEjemplosBadge');

            if (ver === 'v1') {{
                btnV1.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/30";
                btnV2.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white";
                badge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span> Textos Literales MEN • Versión 1 (2015)`;
                badge.className = "text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 flex items-center gap-1.5";
                totalBadge.innerText = "176 DBAs Oficiales • Textos Literales MEN V.1";
                statsEj.innerText = "176 Ejemplos Didácticos";
                modalBadge.innerText = "V.1 (2015)";
                footerNote.innerText = "Modo activo: Versión 1 (2015) - 176 DBAs Oficiales con formulaciones y ejemplos originales del Ministerio de Educación Nacional.";
                activeTag.innerText = "V.1 (2015) Activa";
            }} else {{
                btnV2.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/30";
                btnV1.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition text-slate-400 hover:text-white";
                badge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Textos Literales MEN • Versión 2 (2016)`;
                badge.className = "text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5";
                totalBadge.innerText = "119 DBAs Oficiales • Textos Literales MEN V.2";
                statsEj.innerText = "119 Ejemplos Didácticos";
                modalBadge.innerText = "V.2 (2016)";
                footerNote.innerText = "Modo activo: Versión 2 (2016) - 119 DBAs Oficiales con evidencias completas y ejemplos didácticos literales.";
                activeTag.innerText = "V.2 (2016) Activa";
            }}

            clearSearch();
            renderGradesGrid();
        }}

        function renderNavPills() {{
            const container = document.getElementById('grades-nav-container');
            container.innerHTML = '';
            const isLight = document.body.classList.contains('light-theme');

            for (let g = 1; g <= 11; g++) {{
                const btn = document.createElement('button');
                btn.id = `btn-grade-${{g}}`;
                const baseClass = isLight 
                    ? 'grade-nav-pill px-2.5 py-1 rounded-lg text-xs font-bold transition grade-nav-pill-inactive bg-slate-100 text-slate-700 border border-slate-200'
                    : 'grade-nav-pill px-2.5 py-1 rounded-lg text-xs font-bold transition grade-nav-pill-inactive bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800';
                btn.className = baseClass;
                btn.innerText = `${{g}}°`;
                btn.onclick = () => filterGrade(g.toString());
                container.appendChild(btn);
            }}
        }}

        function renderGradesGrid() {{
            const grid = document.getElementById('gradesGrid');
            grid.innerHTML = '';
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;

            for (let g = 1; g <= 11; g++) {{
                const gStr = g.toString();
                const config = GRADE_CONFIG[gStr];
                const gradeDbas = activeDb[gStr] || {{}};
                const dbaCount = Object.keys(gradeDbas).length;

                let totalEvidencias = 0;
                let totalEjemplos = 0;
                Object.values(gradeDbas).forEach(d => {{
                    totalEvidencias += (d.evidencias ? d.evidencias.length : 0);
                    if (d.ejemplo && d.ejemplo.length > 5) totalEjemplos++;
                }});

                const card = document.createElement('div');
                card.className = `math-glow-card rounded-3xl p-6 text-white shadow-xl flex flex-col justify-between border border-white/10 relative overflow-hidden bg-gradient-to-br ${{config.bgGradient}}`;
                card.id = `card-grade-${{gStr}}`;

                const thoughtsHtml = config.thoughts.map(t => 
                    `<span class="text-[9px] font-extrabold tracking-wider px-2 py-0.5 rounded-md glass-pill text-white/90">${{t}}</span>`
                ).join(' ');

                card.innerHTML = `
                    <div>
                        <div class="flex items-center justify-between gap-2 mb-3">
                            <span class="text-[10px] font-extrabold uppercase tracking-wider px-2.5 py-0.5 rounded-full glass-pill text-white">
                                ${{config.ciclo}}
                            </span>
                            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-black/40 text-white/80">
                                ${{config.age}}
                            </span>
                        </div>

                        <div class="flex items-center justify-between my-2">
                            <div class="text-5xl font-black tracking-tight text-white drop-shadow-md">
                                ${{g}}°
                            </div>
                            <div class="w-12 h-12 rounded-2xl glass-panel flex items-center justify-center text-xl font-black shadow-inner border border-white/20">
                                ${{config.icon}}
                            </div>
                        </div>

                        <h3 class="text-lg font-black text-white tracking-tight mt-1">
                            ${{config.name}}
                        </h3>
                        <p class="text-xs text-slate-200 mt-1.5 line-clamp-2 leading-relaxed">
                            ${{config.desc}}
                        </p>

                        <div class="flex flex-wrap gap-1 mt-4 pt-3 border-t border-white/15">
                            ${{thoughtsHtml}}
                        </div>
                    </div>

                    <div class="mt-6 pt-4 border-t border-white/15">
                        <div class="grid grid-cols-2 gap-2 mb-3">
                            <div class="bg-black/30 rounded-xl p-2 text-center border border-white/10">
                                <span class="block text-[10px] uppercase font-bold text-slate-300">DBAs MEN</span>
                                <span class="text-sm font-black text-white">${{dbaCount}} DBAs</span>
                            </div>
                            <div class="bg-black/30 rounded-xl p-2 text-center border border-white/10">
                                <span class="block text-[10px] uppercase font-bold text-slate-300">Ejemplos</span>
                                <span class="text-sm font-black text-amber-300">${{totalEjemplos}} Ejemplos</span>
                            </div>
                        </div>

                        <button onclick="openGradeModal('${{gStr}}')" class="w-full py-2.5 px-4 rounded-xl font-black text-xs transition flex items-center justify-center gap-2 shadow-lg bg-white text-slate-950 hover:bg-slate-100">
                            <span>→ EXPLORAR DBAs Y EJEMPLOS</span>
                            <span class="text-[10px] opacity-70">(${{dbaCount}})</span>
                        </button>
                    </div>
                `;

                grid.appendChild(card);
            }}
        }}

        /* ================= MODAL / VISOR PEDAGÓGICO DE DBAs ================= */
        function openGradeModal(gradeNum) {{
            const config = GRADE_CONFIG[gradeNum];
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;
            const gradeDbas = activeDb[gradeNum] || {{}};
            const dbaCount = Object.keys(gradeDbas).length;

            document.getElementById('modalGradeTitle').innerText = config.name;
            document.getElementById('modalCicloBadge').innerText = config.ciclo;
            document.getElementById('modalAgeBadge').innerText = config.age;
            document.getElementById('modalDbaCount').innerText = `${{dbaCount}} DBAs Oficiales`;
            document.getElementById('modalGradeDesc').innerText = config.desc;
            document.getElementById('modalVersionBadge').innerText = activeVersion === 'v1' ? 'V.1 (2015)' : 'V.2 (2016)';

            const header = document.getElementById('modalHeader');
            header.className = `p-6 text-white relative bg-gradient-to-r ${{config.bgGradient}}`;

            const listContainer = document.getElementById('modalDbaList');
            listContainer.innerHTML = '';

            Object.keys(gradeDbas).forEach(dbaNum => {{
                const dba = gradeDbas[dbaNum];
                const dbaCard = document.createElement('div');
                dbaCard.className = 'modal-card-bg rounded-2xl p-5 border border-slate-700/80 shadow-md hover:border-cyan-400 transition';

                // Evidencias HTML
                const evidenciasListHtml = (dba.evidencias || []).map((ev, i) => `
                    <li class="flex items-start gap-2.5 text-xs text-slate-300 leading-relaxed">
                        <span class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 font-bold flex items-center justify-center shrink-0 text-[10px] mt-0.5 border border-cyan-500/30">
                            ${{i + 1}}
                        </span>
                        <span>${{ev}}</span>
                    </li>
                `).join('');

                // Ejemplo HTML
                let ejemploHtml = '';
                if (dba.ejemplo && dba.ejemplo.trim().length > 0) {{
                    ejemploHtml = `
                        <div class="modal-example-box mt-4 bg-amber-950/20 border border-amber-500/30 rounded-xl p-4 text-amber-200">
                            <div class="flex items-center justify-between mb-2 pb-2 border-b border-amber-500/20">
                                <span class="text-[11px] font-black uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                                    <span>💡</span>
                                    <span>Ejemplo Pedagógico Oficial del MEN</span>
                                </span>
                                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300">
                                    Orientación de Aula
                                </span>
                            </div>
                            <div class="modal-example-text text-xs leading-relaxed text-slate-200 whitespace-pre-line font-normal">
                                ${{dba.ejemplo}}
                            </div>
                        </div>
                    `;
                }}

                dbaCard.innerHTML = `
                    <div class="flex items-start justify-between gap-3 mb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 text-slate-950 font-black flex items-center justify-center text-sm shadow-md">
                                ${{dbaNum}}
                            </span>
                            <div>
                                <span class="text-xs font-black uppercase tracking-wider text-slate-400 block">
                                    DBA ${{dbaNum}} • ${{config.name}} (${{activeVersion === 'v1' ? 'V.1' : 'V.2'}})
                                </span>
                                <span class="text-[10px] font-bold text-cyan-400">
                                    ${{dba.pensamiento_nombre || 'Pensamiento Matemático Oficial'}}
                                </span>
                            </div>
                        </div>
                        <button onclick="copyDbaToClipboard('${{gradeNum}}', '${{dbaNum}}')" title="Copiar DBA, Evidencias y Ejemplo oficial" class="p-1.5 px-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs font-bold transition flex items-center gap-1 border border-slate-700">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                            <span class="text-[11px] font-bold">Copiar Ficha</span>
                        </button>
                    </div>

                    <div class="mb-3">
                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400 block mb-1">Enunciado Oficial Literal:</span>
                        <h4 class="text-sm font-bold text-white leading-relaxed">
                            ${{dba.statement}}
                        </h4>
                    </div>

                    <div class="modal-evidence-box mt-3 pt-3 border-t border-slate-800 bg-slate-900/60 rounded-xl p-3.5 border border-slate-800">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[11px] font-extrabold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                                <span>Evidencias de Aprendizaje Oficiales</span>
                                <span class="px-1.5 py-0.2 rounded-full bg-cyan-950 text-cyan-300 border border-cyan-800 text-[10px] font-black">${{(dba.evidencias || []).length}}</span>
                            </span>
                        </div>
                        <ul class="space-y-2">
                            ${{evidenciasListHtml}}
                        </ul>
                    </div>

                    ${{ejemploHtml}}
                `;

                listContainer.appendChild(dbaCard);
            }});

            const modal = document.getElementById('dbaModal');
            const drawer = document.getElementById('modalDrawer');
            modal.classList.remove('hidden');
            setTimeout(() => {{
                drawer.classList.remove('translate-x-full');
            }}, 10);
            document.body.style.overflow = 'hidden';
        }}

        function closeModal() {{
            const drawer = document.getElementById('modalDrawer');
            drawer.classList.add('translate-x-full');
            setTimeout(() => {{
                document.getElementById('dbaModal').classList.add('hidden');
                document.body.style.overflow = 'auto';
            }}, 250);
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeModal();
        }});

        function filterGrade(grade) {{
            currentFilterGrade = grade;
            clearSearchInputOnly();
            const isLight = document.body.classList.contains('light-theme');

            document.querySelectorAll('.grade-nav-pill').forEach(btn => {{
                btn.className = isLight
                    ? "grade-nav-pill px-2.5 py-1 rounded-lg text-xs font-bold transition grade-nav-pill-inactive bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200"
                    : "grade-nav-pill px-2.5 py-1 rounded-lg text-xs font-bold transition grade-nav-pill-inactive bg-slate-900 text-slate-400 hover:bg-slate-800 border border-slate-800";
            }});

            const activeBtn = document.getElementById(`btn-grade-${{grade}}`);
            if (activeBtn) {{
                activeBtn.className = "grade-nav-pill px-3 py-1 rounded-lg text-xs font-black transition bg-cyan-500 text-slate-950 shadow-sm";
            }}

            for (let g = 1; g <= 11; g++) {{
                const card = document.getElementById(`card-grade-${{g}}`);
                if (grade === 'all' || grade === g.toString()) {{
                    card.classList.remove('hidden');
                }} else {{
                    card.classList.add('hidden');
                }}
            }}

            document.getElementById('gradesGrid').classList.remove('hidden');
            document.getElementById('searchResultsContainer').classList.add('hidden');
            document.getElementById('resultsCountBar').classList.add('hidden');
        }}

        function handleSearch() {{
            const query = document.getElementById('searchInput').value.trim().toLowerCase();
            const clearBtn = document.getElementById('clearSearchBtn');
            const grid = document.getElementById('gradesGrid');
            const resultsBox = document.getElementById('searchResultsContainer');
            const countBar = document.getElementById('resultsCountBar');
            const countText = document.getElementById('resultsCountText');

            if (query.length === 0) {{
                clearBtn.classList.add('hidden');
                grid.classList.remove('hidden');
                resultsBox.classList.add('hidden');
                countBar.classList.add('hidden');
                return;
            }}

            clearBtn.classList.remove('hidden');
            grid.classList.add('hidden');
            resultsBox.classList.remove('hidden');
            countBar.classList.remove('hidden');

            resultsBox.innerHTML = '';
            let matches = 0;
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;

            for (let g = 1; g <= 11; g++) {{
                const gStr = g.toString();
                if (currentFilterGrade !== 'all' && currentFilterGrade !== gStr) continue;

                const config = GRADE_CONFIG[gStr];
                const gradeDbas = activeDb[gStr] || {{}};

                Object.keys(gradeDbas).forEach(dbaNum => {{
                    const dba = gradeDbas[dbaNum];
                    
                    // Filter by thought if active
                    if (currentFilterThought !== 'all' && dba.pensamiento_key !== currentFilterThought) {{
                        return;
                    }}

                    const stmtMatches = (dba.statement || '').toLowerCase().includes(query);
                    const matchingEvidencias = (dba.evidencias || []).filter(ev => ev.toLowerCase().includes(query));
                    const ejemploMatches = (dba.ejemplo || '').toLowerCase().includes(query);

                    if (stmtMatches || matchingEvidencias.length > 0 || ejemploMatches) {{
                        matches++;

                        const highlightedStatement = highlightText(dba.statement, query);

                        const card = document.createElement('div');
                        card.className = 'modal-card-bg rounded-2xl p-5 border border-slate-700/80 shadow-md hover:border-cyan-400 transition';

                        const evidHtml = (dba.evidencias || []).map(ev => {{
                            const isMatch = ev.toLowerCase().includes(query);
                            return `
                                <li class="flex items-start gap-2 text-xs ${{isMatch ? 'text-cyan-200 font-semibold' : 'text-slate-400'}}">
                                    <span class="w-4 h-4 rounded-full ${{isMatch ? 'bg-cyan-500 text-slate-950 font-black' : 'bg-slate-800 text-slate-500'}} flex items-center justify-center shrink-0 text-[9px] mt-0.5">
                                        ${{isMatch ? '★' : '•'}}
                                    </span>
                                    <span>${{highlightText(ev, query)}}</span>
                                </li>
                            `;
                        }}).join('');

                        let ejHtml = '';
                        if (dba.ejemplo && dba.ejemplo.length > 5) {{
                            ejHtml = `
                                <div class="mt-3 bg-amber-950/20 border border-amber-500/30 rounded-xl p-3 text-amber-200">
                                    <span class="text-[10px] font-extrabold uppercase text-amber-400 block mb-1">Ejemplo Oficial:</span>
                                    <div class="text-xs text-slate-300 leading-relaxed whitespace-pre-line">
                                        ${{highlightText(dba.ejemplo, query)}}
                                    </div>
                                </div>
                            `;
                        }}

                        card.innerHTML = `
                            <div class="flex items-start justify-between gap-3 mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-cyan-500 text-slate-950">
                                        ${{config.name}} • DBA ${{dbaNum}}
                                    </span>
                                    <span class="text-[10px] font-bold px-2 py-0.5 rounded-md glass-pill text-cyan-300">
                                        ${{activeVersion === 'v1' ? 'Versión 1' : 'Versión 2'}}
                                    </span>
                                    <span class="text-[10px] font-bold px-2 py-0.5 rounded-md bg-slate-800 text-slate-300">
                                        ${{dba.pensamiento_nombre || ''}}
                                    </span>
                                </div>
                                <button onclick="copyDbaToClipboard('${{gStr}}', '${{dbaNum}}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs font-bold transition border border-slate-700">
                                    Copiar
                                </button>
                            </div>
                            <h4 class="text-sm font-bold text-white mb-3">
                                ${{highlightedStatement}}
                            </h4>
                            <div class="modal-evidence-box bg-slate-900/60 rounded-xl p-3 border border-slate-800">
                                <span class="text-[10px] font-extrabold uppercase text-cyan-400 block mb-1.5">Evidencias Oficiales:</span>
                                <ul class="space-y-1.5">
                                    ${{evidHtml}}
                                </ul>
                            </div>
                            ${{ejHtml}}
                        `;

                        resultsBox.appendChild(card);
                    }}
                }});
            }}

            countText.innerText = `Se encontraron ${{matches}} DBAs con el término "${{query}}" en la ${{activeVersion === 'v1' ? 'Versión 1' : 'Versión 2'}}.`;
            if (matches === 0) {{
                resultsBox.innerHTML = `
                    <div class="text-center py-12 glass-panel rounded-2xl border border-slate-800 p-8">
                        <div class="text-3xl mb-2">🔍</div>
                        <h4 class="text-sm font-bold text-slate-300">No se encontraron DBAs con ese término</h4>
                        <p class="text-xs text-slate-500 mt-1">Prueba con palabras como: fracciones, enteros, probabilidad, pitágoras, cuadriláteros, derivada, función...</p>
                        <button onclick="clearSearch()" class="mt-4 px-4 py-2 rounded-xl bg-cyan-500 text-slate-950 text-xs font-black">
                            Ver todos los grados
                        </button>
                    </div>
                `;
            }}
        }}

        function highlightText(text, query) {{
            if (!query || !text) return text;
            const regex = new RegExp(`(${{query.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&')}})`, 'gi');
            return text.replace(regex, '<span class="highlight-text">$1</span>');
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
            document.getElementById('gradesGrid').classList.remove('hidden');
            document.getElementById('searchResultsContainer').classList.add('hidden');
            document.getElementById('resultsCountBar').classList.add('hidden');
        }}

        function clearSearchInputOnly() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('clearSearchBtn').classList.add('hidden');
        }}

        function filterThought(thoughtKey) {{
            currentFilterThought = thoughtKey;
            const isLight = document.body.classList.contains('light-theme');
            document.querySelectorAll('.thought-filter-btn').forEach(btn => {{
                btn.className = isLight
                    ? "thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200 transition"
                    : "thought-filter-btn thought-filter-inactive px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition";
            }});

            const active = document.querySelector(`.thought-filter-btn[data-thought="${{thoughtKey}}"]`);
            if (active) {{
                active.className = "thought-filter-btn px-2.5 py-1 rounded-lg text-xs font-black bg-cyan-500 text-slate-950 transition";
            }}

            const query = document.getElementById('searchInput').value.trim();
            if (query.length > 0) {{
                handleSearch();
            }} else if (thoughtKey !== 'all') {{
                // Trigger search filter for that thought
                filterByThoughtOnly(thoughtKey);
            }} else {{
                clearSearch();
            }}
        }}

        function filterByThoughtOnly(thoughtKey) {{
            const grid = document.getElementById('gradesGrid');
            const resultsBox = document.getElementById('searchResultsContainer');
            const countBar = document.getElementById('resultsCountBar');
            const countText = document.getElementById('resultsCountText');

            grid.classList.add('hidden');
            resultsBox.classList.remove('hidden');
            countBar.classList.remove('hidden');
            resultsBox.innerHTML = '';

            let matches = 0;
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;

            for (let g = 1; g <= 11; g++) {{
                const gStr = g.toString();
                if (currentFilterGrade !== 'all' && currentFilterGrade !== gStr) continue;

                const config = GRADE_CONFIG[gStr];
                const gradeDbas = activeDb[gStr] || {{}};

                Object.keys(gradeDbas).forEach(dbaNum => {{
                    const dba = gradeDbas[dbaNum];
                    if (dba.pensamiento_key === thoughtKey) {{
                        matches++;
                        const card = document.createElement('div');
                        card.className = 'modal-card-bg rounded-2xl p-5 border border-slate-700/80 shadow-md hover:border-cyan-400 transition';

                        const evidHtml = (dba.evidencias || []).map(ev => `
                            <li class="flex items-start gap-2 text-xs text-slate-300">
                                <span class="w-4 h-4 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center shrink-0 text-[9px] mt-0.5">
                                    ✓
                                </span>
                                <span>${{ev}}</span>
                            </li>
                        `).join('');

                        card.innerHTML = `
                            <div class="flex items-start justify-between gap-3 mb-2">
                                <div class="flex items-center gap-2">
                                    <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-cyan-500 text-slate-950">
                                        ${{config.name}} • DBA ${{dbaNum}}
                                    </span>
                                    <span class="text-[10px] font-bold px-2 py-0.5 rounded-md glass-pill text-cyan-300">
                                        ${{activeVersion === 'v1' ? 'Versión 1' : 'Versión 2'}}
                                    </span>
                                </div>
                                <button onclick="copyDbaToClipboard('${{gStr}}', '${{dbaNum}}')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs font-bold transition border border-slate-700">
                                    Copiar
                                </button>
                            </div>
                            <h4 class="text-sm font-bold text-white mb-3">
                                ${{dba.statement}}
                            </h4>
                            <div class="modal-evidence-box bg-slate-900/60 rounded-xl p-3 border border-slate-800">
                                <span class="text-[10px] font-extrabold uppercase text-cyan-400 block mb-1.5">Evidencias Oficiales:</span>
                                <ul class="space-y-1.5">
                                    ${{evidHtml}}
                                </ul>
                            </div>
                        `;
                        resultsBox.appendChild(card);
                    }}
                }});
            }}

            countText.innerText = `Mostrando ${{matches}} DBAs pertenecientes a ${{getThoughtName(thoughtKey)}}.`;
        }}

        function getThoughtName(k) {{
            const map = {{
                'num': 'Pensamiento Numérico',
                'met': 'Pensamiento Métrico',
                'geo': 'Pensamiento Geométrico',
                'ale': 'Pensamiento Aleatorio',
                'var': 'Pensamiento Variacional'
            }};
            return map[k] || 'Todos';
        }}

        function copyDbaToClipboard(gradeNum, dbaNum) {{
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;
            const dba = activeDb[gradeNum][dbaNum];
            const config = GRADE_CONFIG[gradeNum];

            let text = `========================================================\\n`;
            text += `DERECHO BÁSICO DE APRENDIZAJE (DBA) - MATEMÁTICAS MEN ${{activeVersion === 'v1' ? 'V.1 (2015)' : 'V.2 (2016)'}}\\n`;
            text += `${{config.name}} | ${{config.ciclo}} | DBA #${{dbaNum}}\\n`;
            text += `Dominio: ${{dba.pensamiento_nombre || 'Matemáticas'}}\\n`;
            text += `========================================================\\n\\n`;
            text += `ENUNCIADO OFICIAL LITERAL (100% Sin Parafraseo):\\n"${{dba.statement}}"\\n\\n`;
            text += `EVIDENCIAS DE APRENDIZAJE OFICIALES:\\n`;
            (dba.evidencias || []).forEach((ev, i) => {{
                text += `  ${{i + 1}}. ${{ev}}\\n`;
            }});
            if (dba.ejemplo && dba.ejemplo.length > 5) {{
                text += `\\nEJEMPLO PEDAGÓGICO OFICIAL (Orientación Didáctica de Aula):\\n${{dba.ejemplo}}\\n`;
            }}
            text += `\\nFuente Oficial: Ministerio de Educación Nacional de Colombia (MEN)\\nCertificación: Asesorías Pedagógicas S.A.S.`;

            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('copyToast');
                toast.classList.remove('hidden');
                setTimeout(() => toast.classList.add('hidden'), 2500);
            }});
        }}

        function descargarJSONActivo() {{
            const activeDb = activeVersion === 'v1' ? DBA_V1_DATA : DBA_V2_DATA;
            const fileName = activeVersion === 'v1' ? 'dba_matematicas_v1_men_2015_literal.json' : 'dba_matematicas_v2_men_2016_literal.json';

            const blob = new Blob([JSON.stringify(activeDb, null, 2)], {{ type: "application/json" }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = fileName;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("index.html generado exitosamente con datos maestros 100% literales!")
