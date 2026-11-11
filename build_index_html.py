import os

html_code = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asesorías Pedagógicas S.A.S. • Portal Curricular Multiárea</title>

    <!-- Seguridad Institucional Gatekeeper -->
    <script src="auth-gatekeeper.js"></script>

    <!-- Base de Datos Maestra Multiárea Literal MEN -->
    <script src="dbas_master_data.js"></script>

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#F0F9FF',
                            100: '#E0F2FE',
                            500: '#0EA5E9',
                            600: '#0284C7',
                            700: '#0369A1',
                            900: '#0C4A6E',
                        }
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

        .custom-scrollbar::-webkit-scrollbar { height: 7px; width: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.6); border-radius: 8px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #38BDF8; border-radius: 8px; }

        .glass-header {
            background: rgba(11, 19, 38, 0.88);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .glass-card {
            background: rgba(15, 23, 42, 0.82);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.22s ease, border-color 0.22s ease;
        }
        .glass-card:hover {
            transform: translateY(-4px);
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.5), 0 0 20px rgba(56, 189, 248, 0.15);
        }

        .glass-bar {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.2s ease;
        }
        .glass-bar:hover {
            border-color: rgba(56, 189, 248, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.4);
        }

        /* ================= TEMA CLARO (ALTO CONTRASTE DE TINTA) ================= */
        body.light-theme {
            background-color: #F1F5F9;
            color: #0F172A;
        }

        body.light-theme .glass-header {
            background: rgba(255, 255, 255, 0.92);
            border-bottom: 1px solid #CBD5E1;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
        }

        body.light-theme .glass-card {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        }
        body.light-theme .glass-card:hover {
            border-color: #0284C7;
            box-shadow: 0 12px 24px -4px rgba(2, 132, 199, 0.15);
        }

        body.light-theme .glass-bar {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
        }
        body.light-theme .glass-bar:hover {
            border-color: #0284C7;
            box-shadow: 0 6px 16px rgba(2, 132, 199, 0.12);
        }

        body.light-theme .text-slate-100 { color: #0F172A !important; }
        body.light-theme .text-slate-200 { color: #1E293B !important; }
        body.light-theme .text-slate-300 { color: #334155 !important; }
        body.light-theme .text-slate-400 { color: #475569 !important; }
        body.light-theme .bg-slate-900\\/80 { background-color: #F8FAFC !important; }
        body.light-theme .bg-slate-800 { background-color: #E2E8F0 !important; }
        body.light-theme .border-slate-800 { border-color: #CBD5E1 !important; }
        body.light-theme .border-slate-700 { border-color: #94A3B8 !important; }
        body.light-theme .custom-scrollbar::-webkit-scrollbar-track { background: #E2E8F0; }
        body.light-theme .custom-scrollbar::-webkit-scrollbar-thumb { background: #0284C7; }

        /* Highlight de búsqueda */
        .search-match {
            background-color: #FACC15;
            color: #0F172A;
            font-weight: 700;
            padding: 0 3px;
            border-radius: 2px;
        }

        /* Estilos de impresión para modal pedagógico */
        @media print {
            body * { visibility: hidden; }
            #printable-modal-content, #printable-modal-content * { visibility: visible; }
            #printable-modal-content {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                color: #000000 !important;
                background: #FFFFFF !important;
                padding: 16px;
            }
            .no-print { display: none !important; }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-sky-500 selection:text-white">

    <!-- ==============================================================
         1. ENCABEZADO INSTITUCIONAL SUPERIOR
         ============================================================== -->
    <header class="sticky top-0 z-40 glass-header">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                
                <!-- Identidad Institucional y Titularidad -->
                <div class="flex items-center gap-3.5">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-sky-500/25 ring-2 ring-white/10 shrink-0">
                        <span class="text-xl font-black text-white">AP</span>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h1 class="text-base sm:text-lg font-black tracking-tight text-white leading-tight">
                                Asesorías Pedagógicas S.A.S.
                            </h1>
                            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-sky-500/20 text-sky-400 border border-sky-500/30">
                                Portal Curricular
                            </span>
                        </div>
                        <p class="text-xs text-slate-400 font-medium">
                            Derechos Básicos de Aprendizaje (DBA) • 1° a 11° • Saber Check
                        </p>
                    </div>
                </div>

                <!-- Controles Globales Superiores: Switcher Versión, PMA y Tema -->
                <div class="flex items-center flex-wrap gap-2.5">
                    
                    <!-- Switcher de Versiones (V1 2015 ⇄ V2 2016) -->
                    <div id="version-switch-container" class="flex items-center bg-slate-900/90 p-1 rounded-xl border border-slate-700/60 shadow-inner">
                        <button id="btn-v1" onclick="setVersion('v1')" class="px-2.5 py-1 text-xs font-bold rounded-lg transition-all text-slate-400 hover:text-white">
                            V.1 (2015)
                        </button>
                        <button id="btn-v2" onclick="setVersion('v2')" class="px-2.5 py-1 text-xs font-bold rounded-lg transition-all bg-sky-500 text-white shadow-md shadow-sky-500/30">
                            V.2 (2016)
                        </button>
                    </div>
                    <div id="version-badge-container" class="hidden px-3 py-1 rounded-xl bg-slate-900/90 border border-slate-700/60 text-[11px] font-bold text-sky-400">
                        <!-- Texto dinámico para áreas con versión única -->
                    </div>

                    <!-- Botón Saber Check PMA Modal -->
                    <button onclick="openPmaModal()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-500/15 text-amber-300 border border-amber-500/30 hover:bg-amber-500/25 transition-all shadow-sm">
                        <span>📑</span>
                        <span>Saber Check PMA</span>
                        <span class="px-1.5 py-0.2 rounded-full text-[10px] bg-amber-400/20 text-amber-200 font-extrabold">33</span>
                    </button>

                    <!-- Botón Alternar Tema (Dark / Light) -->
                    <button id="theme-toggle-btn" onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 border border-slate-700/60 transition-all flex items-center justify-center shadow-sm" title="Alternar Modo Claro / Oscuro">
                        <span id="theme-icon" class="text-sm">☀️</span>
                    </button>
                </div>
            </div>

            <!-- Selector Global de Área Curricular (Pestañas) -->
            <div class="mt-3.5 pt-3 border-t border-slate-800/60 flex items-center justify-between flex-wrap gap-2">
                <div class="flex items-center gap-1.5 overflow-x-auto pb-1 custom-scrollbar w-full sm:w-auto">
                    <button onclick="setArea('matematicas')" id="tab-matematicas" class="area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-sky-500/20 text-sky-400 border-sky-500/40 shadow-sm">
                        <span class="text-sm">📐</span>
                        <span>Matemáticas</span>
                    </button>
                    <button onclick="setArea('lenguaje')" id="tab-lenguaje" class="area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-slate-800/60 text-slate-400 border-slate-700/50 hover:text-white">
                        <span class="text-sm">📖</span>
                        <span>Lenguaje</span>
                    </button>
                    <button onclick="setArea('sociales')" id="tab-sociales" class="area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-slate-800/60 text-slate-400 border-slate-700/50 hover:text-white">
                        <span class="text-sm">🌍</span>
                        <span>Ciencias Sociales</span>
                    </button>
                    <button onclick="setArea('naturales')" id="tab-naturales" class="area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-slate-800/60 text-slate-400 border-slate-700/50 hover:text-white">
                        <span class="text-sm">🔬</span>
                        <span>Ciencias Naturales</span>
                    </button>
                    <button onclick="setArea('ingles')" id="tab-ingles" class="area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-slate-800/60 text-slate-400 border-slate-700/50 hover:text-white">
                        <span class="text-sm">🌐</span>
                        <span>Inglés</span>
                    </button>
                </div>

                <!-- Tres (3) Modos de Visualización Dinámica -->
                <div class="flex items-center gap-1 bg-slate-900/90 p-1 rounded-xl border border-slate-700/60 shadow-inner">
                    <span class="text-[10px] uppercase font-extrabold text-slate-400 px-2 hidden sm:inline">Vista:</span>
                    <button id="view-mode-carousel" onclick="setViewMode('carousel')" class="view-btn px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-all text-slate-400 hover:text-white" title="Modo 1: Carrusel Horizontal">
                        <span>↔️</span>
                        <span class="hidden md:inline">Carrusel</span>
                    </button>
                    <button id="view-mode-grid" onclick="setViewMode('grid')" class="view-btn px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-all bg-sky-500 text-white shadow-sm" title="Modo 2: Malla Vertical Tradicional">
                        <span>⊞</span>
                        <span class="hidden md:inline">Malla</span>
                    </button>
                    <button id="view-mode-bars" onclick="setViewMode('bars')" class="view-btn px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-all text-slate-400 hover:text-white" title="Modo 3: Barras Colapsadas">
                        <span>☰</span>
                        <span class="hidden md:inline">Barras</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- ==============================================================
         2. BARRA DE FILTROS Y SELECTOR RÁPIDO DE GRADOS
         ============================================================== -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-5 pb-3 w-full">
        <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3.5 bg-slate-900/60 p-3 sm:p-4 rounded-2xl border border-slate-800/80">
            
            <!-- Selector Rápido de Grados (1° a 11° y Todos) -->
            <div class="flex items-center gap-1.5 overflow-x-auto pb-1 custom-scrollbar">
                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider shrink-0 mr-1">Grados:</span>
                <button onclick="setGradeFilter('all')" id="grade-btn-all" class="grade-pill px-3 py-1 rounded-lg text-xs font-extrabold transition-all bg-sky-500 text-white shadow-sm shrink-0">
                    Todos
                </button>
                <button onclick="setGradeFilter('1')" id="grade-btn-1" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">1°</button>
                <button onclick="setGradeFilter('2')" id="grade-btn-2" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">2°</button>
                <button onclick="setGradeFilter('3')" id="grade-btn-3" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">3°</button>
                <button onclick="setGradeFilter('4')" id="grade-btn-4" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">4°</button>
                <button onclick="setGradeFilter('5')" id="grade-btn-5" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">5°</button>
                <button onclick="setGradeFilter('6')" id="grade-btn-6" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">6°</button>
                <button onclick="setGradeFilter('7')" id="grade-btn-7" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">7°</button>
                <button onclick="setGradeFilter('8')" id="grade-btn-8" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">8°</button>
                <button onclick="setGradeFilter('9')" id="grade-btn-9" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">9°</button>
                <button onclick="setGradeFilter('10')" id="grade-btn-10" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">10°</button>
                <button onclick="setGradeFilter('11')" id="grade-btn-11" class="grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">11°</button>
            </div>

            <!-- Campo de Búsqueda Rápida en Vivo -->
            <div class="relative w-full lg:w-72 shrink-0">
                <input type="text" id="search-input" oninput="handleSearch(this.value)" placeholder="Buscar en DBA o evidencias..." class="w-full pl-9 pr-8 py-2 rounded-xl text-xs bg-slate-950/80 border border-slate-700/80 text-white placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all">
                <span class="absolute left-3 top-2.5 text-xs text-slate-400">🔍</span>
                <button id="search-clear-btn" onclick="clearSearch()" class="hidden absolute right-2.5 top-2 text-xs text-slate-400 hover:text-white">✕</button>
            </div>
        </div>

        <!-- Barra de Estado Dinámico -->
        <div class="mt-2.5 px-2 flex items-center justify-between text-xs text-slate-400 font-medium">
            <div id="status-stats" class="flex items-center gap-2">
                <span>Cargando datos...</span>
            </div>
            <div id="search-results-count" class="hidden text-sky-400 font-bold">
                <!-- Conteo de coincidencias -->
            </div>
        </div>
    </section>

    <!-- ==============================================================
         3. CONTENEDOR PRINCIPAL DE CONTENIDO (DINÁMICO SEGÚN MODO)
         ============================================================== -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex-1 w-full">
        <!-- Contenedor dinámico que renderiza Carrusel, Malla o Barras -->
        <div id="content-container"></div>
    </main>

    <!-- ==============================================================
         4. MODAL DETALLE PEDAGÓGICO DE GRADO / DBA (LITERAL 100%)
         ============================================================== -->
    <div id="detail-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-black/75 backdrop-blur-md hidden opacity-0 transition-opacity duration-200">
        <div id="modal-box" class="w-full max-w-4xl max-h-[92vh] flex flex-col rounded-2xl bg-slate-900 border border-slate-700 shadow-2xl overflow-hidden transform scale-95 transition-transform duration-200">
            
            <!-- Encabezado Modal -->
            <div class="p-4 sm:p-5 border-b border-slate-800 flex items-center justify-between gap-3 bg-slate-950/70">
                <div class="flex items-center gap-3">
                    <span id="modal-grade-icon" class="text-2xl sm:text-3xl">📘</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 id="modal-title" class="text-base sm:text-lg font-black text-white">Grado X°</h3>
                            <span id="modal-version-tag" class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">V.2</span>
                        </div>
                        <p id="modal-subtitle" class="text-xs text-slate-400">Transcripción Oficial Literal MEN</p>
                    </div>
                </div>
                
                <!-- Acciones del Modal: Copiar, Imprimir y Cerrar -->
                <div class="flex items-center gap-2 no-print">
                    <button onclick="copyModalContent()" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-1 transition-all" title="Copiar texto de este grado">
                        <span>📋</span>
                        <span class="hidden sm:inline">Copiar</span>
                    </button>
                    <button onclick="printModalContent()" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-1 transition-all" title="Imprimir DBAs y Evidencias de este grado">
                        <span>🖨️</span>
                        <span class="hidden sm:inline">Imprimir</span>
                    </button>
                    <button onclick="closeModal()" class="p-2 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-bold transition-all" title="Cerrar ventana">
                        ✕
                    </button>
                </div>
            </div>

            <!-- Cuerpo Scrolleable con los DBAs y Evidencias Literales -->
            <div id="printable-modal-content" class="p-4 sm:p-6 overflow-y-auto custom-scrollbar space-y-4 flex-1">
                <!-- Se llena dinámicamente con las tarjetas de DBAs -->
            </div>

            <!-- Pie de Modal -->
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/70 flex items-center justify-between text-xs text-slate-400 no-print">
                <span id="modal-counter-tag">Total DBAs: 0</span>
                <button onclick="closeModal()" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold transition-all">
                    Entendido / Cerrar
                </button>
            </div>
        </div>
    </div>

    <!-- ==============================================================
         5. MODAL SABER CHECK PMA (CATÁLOGO DE PLANES DE MEJORAMIENTO)
         ============================================================== -->
    <div id="pma-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-black/80 backdrop-blur-md hidden opacity-0 transition-opacity duration-200">
        <div class="w-full max-w-5xl max-h-[92vh] flex flex-col rounded-2xl bg-slate-900 border border-amber-500/30 shadow-2xl overflow-hidden transform scale-95 transition-transform duration-200">
            
            <!-- Encabezado PMA -->
            <div class="p-4 sm:p-5 border-b border-slate-800 flex items-center justify-between gap-3 bg-gradient-to-r from-slate-950 via-slate-900 to-amber-950/40">
                <div class="flex items-center gap-3">
                    <span class="text-3xl">📑</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 class="text-base sm:text-lg font-black text-amber-300">
                                Planes de Mejoramiento Saber Check • 33 Módulos
                            </h3>
                            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-200 border border-amber-500/40">
                                1° a 11°
                            </span>
                        </div>
                        <p class="text-xs text-slate-400">
                            Planes pedagógicos organizados por componentes matemáticos articulados a los DBA y Estándares Básicos de Competencias.
                        </p>
                    </div>
                </div>
                <button onclick="closePmaModal()" class="p-2 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-bold transition-all">
                    ✕
                </button>
            </div>

            <!-- Filtro de Grado en PMA -->
            <div class="px-4 sm:px-6 py-2.5 bg-slate-950/50 border-b border-slate-800/80 flex items-center gap-2 overflow-x-auto custom-scrollbar">
                <span class="text-xs font-bold text-slate-400 uppercase tracking-wider shrink-0">Filtrar Grado:</span>
                <button onclick="renderPmaCards('all')" id="pma-filter-all" class="pma-filter-pill px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 shrink-0">Todos</button>
                <button onclick="renderPmaCards('1')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">1°</button>
                <button onclick="renderPmaCards('2')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">2°</button>
                <button onclick="renderPmaCards('3')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">3°</button>
                <button onclick="renderPmaCards('4')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">4°</button>
                <button onclick="renderPmaCards('5')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">5°</button>
                <button onclick="renderPmaCards('6')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">6°</button>
                <button onclick="renderPmaCards('7')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">7°</button>
                <button onclick="renderPmaCards('8')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">8°</button>
                <button onclick="renderPmaCards('9')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">9°</button>
                <button onclick="renderPmaCards('10')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">10°</button>
                <button onclick="renderPmaCards('11')" class="pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0">11°</button>
            </div>

            <!-- Cuerpo Scrolleable con los 33 Planes -->
            <div id="pma-cards-container" class="p-4 sm:p-6 overflow-y-auto custom-scrollbar grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5 flex-1">
                <!-- Tarjetas dinámicas de planes -->
            </div>

            <!-- Pie de Modal PMA -->
            <div class="p-3 sm:p-4 border-t border-slate-800 bg-slate-950/70 flex items-center justify-between text-xs text-slate-400">
                <span class="text-amber-400 font-semibold">Planes de Mejoramiento Pedagógico de Asesorías Pedagógicas S.A.S.</span>
                <button onclick="closePmaModal()" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold transition-all">
                    Cerrar
                </button>
            </div>
        </div>
    </div>

    <!-- ==============================================================
         6. PIE DE PÁGINA INSTITUCIONAL
         ============================================================== -->
    <footer class="mt-auto border-t border-slate-800/80 bg-slate-950/60 py-4 text-center text-xs text-slate-400">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
            <p>© 2026 Asesorías Pedagógicas S.A.S. • Todos los derechos reservados.</p>
            <p class="text-slate-400">Integración Curricular Literal MEN • Colombia</p>
        </div>
    </footer>

    <!-- ==============================================================
         7. LÓGICA DE APLICACIÓN MULTIÁREA Y CONTROLADORES INTERACTIVOS
         ============================================================== -->
    <script>
        /* ================= ESTADO GLOBAL ================= */
        let currentArea = 'matematicas';
        let currentVersion = 'v2'; // 'v1' o 'v2'
        let currentGradeFilter = 'all'; // 'all' o '1'..'11'
        let currentViewMode = 'grid'; // 'carousel', 'grid', 'bars'
        let searchQuery = '';
        let isLightMode = false;

        // Metadatos temáticos y ciclos pedagógicos
        const CICLOS_INFO = {
            1: { ciclo: "Ciclo 1: Primaria Temprana", color: "from-blue-500/20 to-cyan-500/10", border: "border-cyan-500/30", icon: "🌱" },
            2: { ciclo: "Ciclo 1: Primaria Temprana", color: "from-blue-500/20 to-cyan-500/10", border: "border-cyan-500/30", icon: "🌱" },
            3: { ciclo: "Ciclo 1: Primaria Temprana", color: "from-blue-500/20 to-cyan-500/10", border: "border-cyan-500/30", icon: "🌱" },
            4: { ciclo: "Ciclo 2: Primaria Superior", color: "from-emerald-500/20 to-teal-500/10", border: "border-emerald-500/30", icon: "🌿" },
            5: { ciclo: "Ciclo 2: Primaria Superior", color: "from-emerald-500/20 to-teal-500/10", border: "border-emerald-500/30", icon: "🌿" },
            6: { ciclo: "Ciclo 3: Secundaria Básica", color: "from-amber-500/20 to-orange-500/10", border: "border-amber-500/30", icon: "📘" },
            7: { ciclo: "Ciclo 3: Secundaria Básica", color: "from-amber-500/20 to-orange-500/10", border: "border-amber-500/30", icon: "📘" },
            8: { ciclo: "Ciclo 4: Secundaria Media", color: "from-purple-500/20 to-indigo-500/10", border: "border-purple-500/30", icon: "🔭" },
            9: { ciclo: "Ciclo 4: Secundaria Media", color: "from-purple-500/20 to-indigo-500/10", border: "border-purple-500/30", icon: "🔭" },
            10: { ciclo: "Ciclo 5: Educación Media", color: "from-rose-500/20 to-pink-500/10", border: "border-rose-500/30", icon: "🎓" },
            11: { ciclo: "Ciclo 5: Educación Media", color: "from-rose-500/20 to-pink-500/10", border: "border-rose-500/30", icon: "🎓" }
        };

        const AREA_TITLES = {
            matematicas: "Matemáticas",
            lenguaje: "Lenguaje",
            sociales: "Ciencias Sociales",
            naturales: "Ciencias Naturales",
            ingles: "Inglés"
        };

        /* ================= INICIALIZACIÓN ================= */
        document.addEventListener('DOMContentLoaded', () => {
            // Verificar si hay tema guardado
            if (localStorage.getItem('theme_preference') === 'light') {
                toggleTheme();
            }
            updateVersionVisibility();
            renderMainContent();
        });

        /* ================= CAMBIO DE TEMA CLARO / OSCURO ================= */
        function toggleTheme() {
            isLightMode = !isLightMode;
            const body = document.body;
            const icon = document.getElementById('theme-icon');
            if (isLightMode) {
                body.classList.add('light-theme');
                icon.textContent = '🌙';
                localStorage.setItem('theme_preference', 'light');
            } else {
                body.classList.remove('light-theme');
                icon.textContent = '☀️';
                localStorage.setItem('theme_preference', 'dark');
            }
        }

        /* ================= CAMBIO DE ÁREA ================= */
        function setArea(areaKey) {
            currentArea = areaKey;

            // Actualizar botones de área
            document.querySelectorAll('.area-tab').forEach(btn => {
                btn.className = "area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-slate-800/60 text-slate-400 border-slate-700/50 hover:text-white";
            });
            const activeTab = document.getElementById(`tab-${areaKey}`);
            if (activeTab) {
                activeTab.className = "area-tab px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border bg-sky-500/20 text-sky-400 border-sky-500/40 shadow-sm";
            }

            // Ajustar versión por defecto según el área
            if (areaKey === 'matematicas' || areaKey === 'lenguaje') {
                if (currentVersion !== 'v1' && currentVersion !== 'v2') {
                    currentVersion = 'v2';
                }
            } else if (areaKey === 'sociales') {
                currentVersion = 'v2';
            } else {
                currentVersion = 'v1';
            }

            updateVersionVisibility();
            renderMainContent();
        }

        /* ================= CONTROLADOR DE VERSIÓN ================= */
        function setVersion(vKey) {
            if (currentArea !== 'matematicas' && currentArea !== 'lenguaje') return;
            currentVersion = vKey;
            
            const btnV1 = document.getElementById('btn-v1');
            const btnV2 = document.getElementById('btn-v2');

            if (vKey === 'v1') {
                btnV1.className = "px-2.5 py-1 text-xs font-bold rounded-lg transition-all bg-sky-500 text-white shadow-md shadow-sky-500/30";
                btnV2.className = "px-2.5 py-1 text-xs font-bold rounded-lg transition-all text-slate-400 hover:text-white";
            } else {
                btnV2.className = "px-2.5 py-1 text-xs font-bold rounded-lg transition-all bg-sky-500 text-white shadow-md shadow-sky-500/30";
                btnV1.className = "px-2.5 py-1 text-xs font-bold rounded-lg transition-all text-slate-400 hover:text-white";
            }
            renderMainContent();
        }

        function updateVersionVisibility() {
            const switchContainer = document.getElementById('version-switch-container');
            const badgeContainer = document.getElementById('version-badge-container');

            if (currentArea === 'matematicas' || currentArea === 'lenguaje') {
                switchContainer.classList.remove('hidden');
                badgeContainer.classList.add('hidden');
            } else {
                switchContainer.classList.add('hidden');
                badgeContainer.classList.remove('hidden');
                if (currentArea === 'sociales') {
                    badgeContainer.textContent = "Versión Oficial Vigente (2016)";
                } else if (currentArea === 'naturales') {
                    badgeContainer.textContent = "Versión Oficial Vigente (2016 - V1)";
                } else if (currentArea === 'ingles') {
                    badgeContainer.textContent = "Currículo Sugerido MEN";
                }
            }
        }

        /* ================= CONTROLADOR DE MODO DE VISTA (LOS 3 MODOS) ================= */
        function setViewMode(mode) {
            currentViewMode = mode;
            ['carousel', 'grid', 'bars'].forEach(m => {
                const btn = document.getElementById(`view-mode-${m}`);
                if (btn) {
                    if (m === mode) {
                        btn.className = "view-btn px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-all bg-sky-500 text-white shadow-sm";
                    } else {
                        btn.className = "view-btn px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1 transition-all text-slate-400 hover:text-white";
                    }
                }
            });
            renderMainContent();
        }

        /* ================= CONTROLADOR DE FILTRO DE GRADO ================= */
        function setGradeFilter(gKey) {
            currentGradeFilter = gKey;
            document.querySelectorAll('.grade-pill').forEach(btn => {
                btn.className = "grade-pill px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0";
            });
            const activeBtn = document.getElementById(`grade-btn-${gKey}`);
            if (activeBtn) {
                activeBtn.className = "grade-pill px-3 py-1 rounded-lg text-xs font-extrabold transition-all bg-sky-500 text-white shadow-sm shrink-0";
            }
            renderMainContent();
        }

        /* ================= CONTROLADOR DE BÚSQUEDA EN VIVO ================= */
        function handleSearch(val) {
            searchQuery = val.trim().toLowerCase();
            const clearBtn = document.getElementById('search-clear-btn');
            if (searchQuery.length > 0) {
                clearBtn.classList.remove('hidden');
            } else {
                clearBtn.classList.add('hidden');
            }
            renderMainContent();
        }

        function clearSearch() {
            document.getElementById('search-input').value = '';
            handleSearch('');
        }

        /* ================= OBTENCIÓN DE DATOS ACTIVOS ================= */
        function getActiveDataset() {
            if (!window.CURRICULO_DATA || !CURRICULO_DATA[currentArea]) return {};
            const areaObj = CURRICULO_DATA[currentArea];
            if (areaObj[currentVersion]) {
                return areaObj[currentVersion];
            }
            // Fallback al primer conjunto disponible
            const availableKeys = Object.keys(areaObj);
            return availableKeys.length > 0 ? areaObj[availableKeys[0]] : {};
        }

        /* ================= RENDERIZADOR PRINCIPAL ================= */
        function renderMainContent() {
            const container = document.getElementById('content-container');
            const data = getActiveDataset();
            const grades = Object.keys(data).sort((a, b) => parseInt(a) - parseInt(b));

            let totalDbaCount = 0;
            let totalEvidCount = 0;
            let matchingDbasCount = 0;

            // Filtrar grados a renderizar
            const targetGrades = currentGradeFilter === 'all' 
                ? grades 
                : grades.filter(g => g === currentGradeFilter);

            // Preparar conteo global
            grades.forEach(g => {
                const gradeDbas = data[g] || {};
                const dbaKeys = Object.keys(gradeDbas);
                totalDbaCount += dbaKeys.length;
                dbaKeys.forEach(k => {
                    totalEvidCount += (gradeDbas[k].evidencias || []).length;
                });
            });

            // Actualizar status stats
            const statsEl = document.getElementById('status-stats');
            const areaName = AREA_TITLES[currentArea] || currentArea;
            const versionLabel = (currentArea === 'matematicas' || currentArea === 'lenguaje') 
                ? `Versión ${currentVersion.toUpperCase()}` 
                : 'Oficial MEN';
            statsEl.innerHTML = `
                <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md bg-slate-800 text-sky-400 font-bold">
                    ${areaName} • ${versionLabel}
                </span>
                <span>${totalDbaCount} DBAs</span>
                <span>•</span>
                <span>${totalEvidCount} Evidencias oficiales</span>
            `;

            if (targetGrades.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-16 bg-slate-900/40 rounded-2xl border border-slate-800">
                        <span class="text-4xl">📂</span>
                        <p class="text-slate-400 text-sm mt-3">No hay datos disponibles para el filtro seleccionado.</p>
                    </div>
                `;
                return;
            }

            // Según el modo de visualización:
            if (currentViewMode === 'carousel') {
                renderCarouselView(container, targetGrades, data);
            } else if (currentViewMode === 'bars') {
                renderBarsView(container, targetGrades, data);
            } else {
                renderGridView(container, targetGrades, data);
            }
        }

        /* ================= MODO 1: CARRUSEL HORIZONTAL ================= */
        function renderCarouselView(container, targetGrades, data) {
            let html = `
                <div class="relative">
                    <div class="flex flex-nowrap overflow-x-auto snap-x snap-mandatory gap-4 custom-scrollbar pb-6 pt-2">
            `;

            targetGrades.forEach(g => {
                const cardHtml = generateCardContent(g, data[g] || {}, true);
                html += `
                    <div class="min-w-[260px] max-w-[280px] snap-start shrink-0">
                        ${cardHtml}
                    </div>
                `;
            });

            html += `
                    </div>
                </div>
            `;
            container.innerHTML = html;
        }

        /* ================= MODO 2: MALLA VERTICAL TRADICIONAL ================= */
        function renderGridView(container, targetGrades, data) {
            let html = `
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
            `;

            targetGrades.forEach(g => {
                const cardHtml = generateCardContent(g, data[g] || {}, false);
                html += cardHtml;
            });

            html += `</div>`;
            container.innerHTML = html;
        }

        /* ================= MODO 3: BARRAS FLOTANTES COLAPSADAS ================= */
        function renderBarsView(container, targetGrades, data) {
            let html = `<div class="space-y-2.5">`;

            targetGrades.forEach(g => {
                const gradeDbas = data[g] || {};
                const dbaKeys = Object.keys(gradeDbas);
                const ciclo = CICLOS_INFO[g] || { ciclo: "Básica", icon: "📚" };

                let totalEvids = 0;
                dbaKeys.forEach(k => totalEvids += (gradeDbas[k].evidencias || []).length);

                html += `
                    <div class="glass-bar flex items-center justify-between p-3.5 rounded-2xl gap-3">
                        <div class="flex items-center gap-3 min-w-0">
                            <span class="text-2xl shrink-0">${ciclo.icon}</span>
                            <div class="truncate">
                                <div class="flex items-center gap-2">
                                    <h4 class="text-sm font-black text-white">Grado ${g}°</h4>
                                    <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                                        ${ciclo.ciclo}
                                    </span>
                                </div>
                                <p class="text-xs text-slate-400 mt-0.5">
                                    ${dbaKeys.length} DBAs registrados • ${totalEvids} evidencias de aprendizaje
                                </p>
                            </div>
                        </div>

                        <div class="flex items-center gap-2 shrink-0">
                            <button onclick="openDetailModal('${g}')" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-sky-500 hover:bg-sky-400 text-white transition-all shadow-sm flex items-center gap-1.5">
                                <span>Ver DBAs</span>
                                <span>➔</span>
                            </button>
                        </div>
                    </div>
                `;
            });

            html += `</div>`;
            container.innerHTML = html;
        }

        /* ================= GENERADOR DE TARJETA COMPACTA Y ESBELTA ================= */
        function generateCardContent(g, gradeDbas, isCarousel) {
            const ciclo = CICLOS_INFO[g] || { ciclo: "Básica", color: "from-sky-500/10 to-indigo-500/10", border: "border-sky-500/20", icon: "📚" };
            const dbaKeys = Object.keys(gradeDbas).sort((a, b) => parseInt(a) - parseInt(b));

            let totalEvids = 0;
            let filteredKeys = [];

            dbaKeys.forEach(k => {
                const item = gradeDbas[k];
                totalEvids += (item.evidencias || []).length;

                if (!searchQuery) {
                    filteredKeys.push(k);
                } else {
                    const textToSearch = (item.statement + ' ' + (item.evidencias || []).join(' ')).toLowerCase();
                    if (textToSearch.includes(searchQuery)) {
                        filteredKeys.push(k);
                    }
                }
            });

            // Si hay búsqueda y no coincide ningún DBA en este grado, ocultar la tarjeta
            if (searchQuery && filteredKeys.length === 0) {
                return '';
            }

            // Vista previa de los primeros 2 DBAs
            let previewHtml = '';
            const previewKeys = filteredKeys.slice(0, 2);

            previewKeys.forEach(k => {
                const item = gradeDbas[k];
                const cleanStatement = highlightText(item.statement, searchQuery);
                const evidCount = (item.evidencias || []).length;

                previewHtml += `
                    <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800/80 text-xs">
                        <div class="flex items-center justify-between mb-1">
                            <span class="font-extrabold text-[11px] text-sky-400">DBA #${k}</span>
                            <span class="text-[10px] text-slate-400 font-semibold">${evidCount} evids</span>
                        </div>
                        <p class="text-slate-300 leading-snug text-[11px] line-clamp-3">
                            ${cleanStatement}
                        </p>
                    </div>
                `;
            });

            const remaining = filteredKeys.length - previewKeys.length;

            return `
                <div class="glass-card flex flex-col justify-between p-4 rounded-2xl h-full border ${ciclo.border} bg-gradient-to-b ${ciclo.color}">
                    <!-- Cabecera de Tarjeta -->
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div class="flex items-center gap-2">
                                <span class="text-xl">${ciclo.icon}</span>
                                <div>
                                    <h3 class="text-sm font-black text-white leading-tight">Grado ${g}°</h3>
                                    <span class="text-[9px] font-bold text-slate-400 block">${ciclo.ciclo}</span>
                                </div>
                            </div>
                            <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-sky-500/20 text-sky-300 border border-sky-500/30">
                                ${dbaKeys.length} DBAs
                            </span>
                        </div>

                        <!-- Resumen y Previews -->
                        <div class="space-y-2 mt-3">
                            ${previewHtml}
                        </div>

                        ${remaining > 0 ? `
                            <p class="text-[10px] text-center font-bold text-slate-400 mt-2">
                                + ${remaining} DBAs adicionales
                            </p>
                        ` : ''}
                    </div>

                    <!-- Botón de Acción Directa -->
                    <div class="mt-4 pt-3 border-t border-slate-800/60">
                        <button onclick="openDetailModal('${g}')" class="w-full py-2 rounded-xl text-xs font-black bg-sky-500 hover:bg-sky-400 text-white transition-all shadow-md shadow-sky-500/20 flex items-center justify-center gap-1.5">
                            <span>Explorar DBAs</span>
                            <span>➔</span>
                        </button>
                    </div>
                </div>
            `;
        }

        /* ================= MODAL DETALLE PEDAGÓGICO ================= */
        let currentModalGrade = null;

        function openDetailModal(gradeKey) {
            currentModalGrade = gradeKey;
            const data = getActiveDataset();
            const gradeDbas = data[gradeKey] || {};
            const dbaKeys = Object.keys(gradeDbas).sort((a, b) => parseInt(a) - parseInt(b));
            const ciclo = CICLOS_INFO[gradeKey] || { ciclo: "Básica", icon: "📚" };

            document.getElementById('modal-grade-icon').textContent = ciclo.icon;
            document.getElementById('modal-title').textContent = `Grado ${gradeKey}° • ${AREA_TITLES[currentArea] || currentArea}`;
            document.getElementById('modal-version-tag').textContent = (currentArea === 'matematicas' || currentArea === 'lenguaje')
                ? `Versión ${currentVersion.toUpperCase()}`
                : 'Oficial MEN';
            document.getElementById('modal-subtitle').textContent = `${ciclo.ciclo} • Transcripción Literal 100% Sin Parafraseo`;
            document.getElementById('modal-counter-tag').textContent = `Total DBAs en Grado ${gradeKey}°: ${dbaKeys.length}`;

            // Renderizar todos los DBAs con sus evidencias
            const contentEl = document.getElementById('printable-modal-content');
            let html = '';

            dbaKeys.forEach(k => {
                const item = gradeDbas[k];
                const evidences = item.evidencias || [];

                html += `
                    <div class="p-4 sm:p-5 rounded-2xl bg-slate-950/70 border border-slate-800 text-left space-y-3">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-2.5 py-1 rounded-lg text-xs font-black bg-sky-500/20 text-sky-400 border border-sky-500/30">
                                DBA #${k}
                            </span>
                            <span class="text-[11px] font-semibold text-slate-400">
                                ${evidences.length} evidencias oficiales
                            </span>
                        </div>

                        <!-- Enunciado Literal -->
                        <div class="text-sm font-semibold text-slate-100 leading-relaxed">
                            ${highlightText(item.statement, searchQuery)}
                        </div>

                        <!-- Evidencias de Aprendizaje con Viñetas -->
                        ${evidences.length > 0 ? `
                            <div class="pt-2 border-t border-slate-800/80">
                                <h5 class="text-[11px] font-extrabold uppercase tracking-wider text-slate-400 mb-2">
                                    Evidencias de Aprendizaje:
                                </h5>
                                <ul class="space-y-1.5 text-xs text-slate-300">
                                    ${evidences.map(ev => `
                                        <li class="flex items-start gap-2">
                                            <span class="text-sky-400 font-bold shrink-0 leading-tight">•</span>
                                            <span class="leading-relaxed">${highlightText(ev, searchQuery)}</span>
                                        </li>
                                    `).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                `;
            });

            contentEl.innerHTML = html;

            // Abrir modal con microanimación
            const modal = document.getElementById('detail-modal');
            const box = document.getElementById('modal-box');
            modal.classList.remove('hidden');
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                box.classList.remove('scale-95');
                box.classList.add('scale-100');
            }, 10);
        }

        function closeModal() {
            const modal = document.getElementById('detail-modal');
            const box = document.getElementById('modal-box');
            modal.classList.add('opacity-0');
            box.classList.remove('scale-100');
            box.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 200);
        }

        /* ================= COPIAR E IMPRIMIR MODAL ================= */
        function copyModalContent() {
            if (!currentModalGrade) return;
            const data = getActiveDataset();
            const gradeDbas = data[currentModalGrade] || {};
            const dbaKeys = Object.keys(gradeDbas).sort((a, b) => parseInt(a) - parseInt(b));

            let text = `=========================================================\n`;
            text += `ASESORÍAS PEDAGÓGICAS S.A.S. - PORTAL CURRICULAR\n`;
            text += `Área: ${AREA_TITLES[currentArea] || currentArea} | Grado: ${currentModalGrade}°\n`;
            text += `=========================================================\n\n`;

            dbaKeys.forEach(k => {
                const item = gradeDbas[k];
                text += `DBA #${k}: ${item.statement}\n`;
                text += `Evidencias de aprendizaje:\n`;
                (item.evidencias || []).forEach(ev => {
                    text += `  • ${ev}\n`;
                });
                text += `\n`;
            });

            navigator.clipboard.writeText(text).then(() => {
                alert(`✓ Se han copiado al portapapeles todos los DBAs y evidencias del Grado ${currentModalGrade}°.`);
            }).catch(() => {
                alert('No se pudo copiar automáticamente. Por favor seleccione y copie el texto manualmente.');
            });
        }

        function printModalContent() {
            window.print();
        }

        /* ================= MODAL SABER CHECK PMA ================= */
        function openPmaModal() {
            const modal = document.getElementById('pma-modal');
            modal.classList.remove('hidden');
            setTimeout(() => {
                modal.classList.remove('opacity-0');
            }, 10);
            renderPmaCards('all');
        }

        function closePmaModal() {
            const modal = document.getElementById('pma-modal');
            modal.classList.add('opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 200);
        }

        function renderPmaCards(targetGrade) {
            document.querySelectorAll('.pma-filter-pill').forEach(btn => {
                btn.className = "pma-filter-pill px-2 py-1 rounded-lg text-xs font-semibold text-slate-300 hover:bg-slate-800 shrink-0";
            });
            const activeBtn = document.getElementById(`pma-filter-${targetGrade}`);
            if (activeBtn) {
                activeBtn.className = "pma-filter-pill px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-500 text-slate-950 shrink-0";
            }

            const container = document.getElementById('pma-cards-container');
            const pmaData = (window.CURRICULO_DATA && CURRICULO_DATA.pma) || {};
            let html = '';

            const grades = Object.keys(pmaData).sort((a, b) => parseInt(a) - parseInt(b));
            const filteredGrades = targetGrade === 'all' ? grades : grades.filter(g => g === targetGrade);

            filteredGrades.forEach(g => {
                const plans = pmaData[g] || [];
                plans.forEach(plan => {
                    html += `
                        <div class="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="text-xl">${plan.icon || '🔢'}</span>
                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                        Grado ${plan.grade}°
                                    </span>
                                </div>
                                <h4 class="text-xs font-black text-white leading-tight">
                                    ${plan.component_name}
                                </h4>
                                <p class="text-[11px] text-slate-400 mt-1 line-clamp-2">
                                    ${plan.standard || 'Estándar curricular articulado'}
                                </p>

                                ${plan.actividades && plan.actividades.length > 0 ? `
                                    <div class="mt-2.5 p-2 rounded-lg bg-slate-900/90 border border-slate-800/80">
                                        <span class="text-[10px] font-bold text-amber-400 block mb-1">Actividades Clave:</span>
                                        <p class="text-[10px] text-slate-300 leading-tight">
                                            ${plan.actividades.join(' • ')}
                                        </p>
                                    </div>
                                ` : ''}
                            </div>

                            <div class="mt-3.5 pt-2.5 border-t border-slate-800/80 flex items-center justify-between gap-2">
                                <a href="${plan.drive_view_url}" target="_blank" rel="noopener" class="flex-1 py-1.5 rounded-xl text-center text-[11px] font-bold bg-slate-800 hover:bg-slate-700 text-sky-400 border border-slate-700 transition-all">
                                    Ver en Drive ↗
                                </a>
                                <a href="${plan.drive_download_url}" target="_blank" rel="noopener" class="px-3 py-1.5 rounded-xl text-[11px] font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 transition-all">
                                    Descargar PDF
                                </a>
                            </div>
                        </div>
                    `;
                });
            });

            container.innerHTML = html;
        }

        /* ================= UTILIDAD HIGHLIGHT BÚSQUEDA ================= */
        function highlightText(text, query) {
            if (!query || !text) return text || '';
            const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
            return text.replace(regex, '<mark class="search-match">$1</mark>');
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("index.html successfully updated! Size:", len(html_code))
