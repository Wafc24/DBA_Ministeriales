import os

html_template = """<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Plataforma Curricular DBA (MEN Colombia) • Asesorías Pedagógicas S.A.S.</title>

  <!-- Control de Acceso y Seguridad Gatekeeper Institucional -->
  <script src="auth-gatekeeper.js"></script>

  <!-- Banco Maestro de Datos Curriculares Unificado 100% Literal MEN -->
  <script src="dbas_master_data.js"></script>

  <!-- Banco de Malla Temática Extendida con Trazabilidad DBA-Evidencia Oficial -->
  <script src="malla_tematica_data.js"></script>
  <script src="malla_sociales_data.js"></script>
  <script src="malla_naturales_data.js"></script>

  <!-- Controlador Unificado de Matriz Curricular Multi-Periodo (renderMatrix) -->
  <script src="curriculum_matrix_builder.js"></script>
  
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
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          }
        }
      }
    }
  </script>

  <style>
    /* ================= TEMA BASE (LIGHT / EDITORIAL) ================= */
    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      transition: background-color 0.25s ease, color 0.25s ease;
    }
    .glass-card {
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    .portal-tab-btn {
      color: #475569;
      background-color: transparent;
      border: 1px solid transparent;
      transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .portal-tab-btn:hover {
      color: #0f172a;
      background-color: #f1f5f9;
      border-color: #e2e8f0;
    }
    .portal-tab-btn.active {
      background: linear-gradient(135deg, #0f172a, #1e293b) !important;
      color: #ffffff !important;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.25);
      border-color: #334155 !important;
    }
    .view-mode-btn {
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .view-mode-btn.active {
      background: #0f172a !important;
      color: #ffffff !important;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.25);
    }
    
    /* Modo 1: Carrusel Horizontal Estilizado (~260px) */
    .horizontal-carousel-rail {
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scroll-behavior: smooth;
      gap: 1rem;
      padding: 0.5rem 0.25rem 1.25rem 0.25rem;
      -webkit-overflow-scrolling: touch;
    }
    .horizontal-carousel-rail::-webkit-scrollbar {
      height: 7px;
    }
    .horizontal-carousel-rail::-webkit-scrollbar-track {
      background: #e2e8f0;
      border-radius: 9999px;
    }
    .horizontal-carousel-rail::-webkit-scrollbar-thumb {
      background: #6366f1;
      border-radius: 9999px;
    }
    .grade-card-carousel {
      flex: 0 0 260px;
      width: 260px;
      scroll-snap-align: start;
    }

    /* Modo 3: Barras Horizontales Flotantes (Acordeón con Chevrons) */
    .grade-bar-body {
      transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s ease;
      overflow: hidden;
    }
    .grade-bar-body.collapsed {
      max-height: 0 !important;
      opacity: 0 !important;
      padding-top: 0 !important;
      padding-bottom: 0 !important;
      margin-top: 0 !important;
      border-top-width: 0 !important;
      pointer-events: none;
    }
    .grade-bar-body:not(.collapsed) {
      max-height: 3000px !important;
      opacity: 1 !important;
    }
    .bar-chevron {
      transition: transform 0.28s ease;
    }
    .bar-chevron.rotated {
      transform: rotate(180deg);
    }

    /* Tarjetas Compactas DBA con Micro-Animaciones */
    .sim-editorial-card {
      transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s ease;
    }
    .sim-editorial-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 28px -6px rgba(15, 23, 42, 0.12), 0 6px 12px -3px rgba(15, 23, 42, 0.05);
      border-color: #818cf8;
    }

    /* ================= TEMA OSCURO (DARK MODE) ================= */
    body.dark-theme {
      background-color: #070D18 !important;
      color: #F8FAFC !important;
    }
    body.dark-theme .glass-card {
      background: rgba(15, 23, 42, 0.88) !important;
      border-color: rgba(255, 255, 255, 0.08) !important;
    }
    body.dark-theme .bg-white {
      background-color: #0F172A !important;
      color: #F8FAFC !important;
    }
    body.dark-theme .text-slate-900 {
      color: #F8FAFC !important;
    }
    body.dark-theme .text-slate-800 {
      color: #F1F5F9 !important;
    }
    body.dark-theme .text-slate-600 {
      color: #94A3B8 !important;
    }
    body.dark-theme .bg-slate-50 {
      background-color: #0B1120 !important;
    }
    body.dark-theme .bg-slate-100 {
      background-color: #1E293B !important;
    }
    body.dark-theme .border-slate-200 {
      border-color: #334155 !important;
    }
    body.dark-theme .border-slate-100 {
      border-color: #1E293B !important;
    }
    body.dark-theme .sim-editorial-card {
      background-color: #0F172A !important;
      border-color: #334155 !important;
    }
    body.dark-theme .sim-editorial-card:hover {
      border-color: #38BDF8 !important;
      box-shadow: 0 14px 28px -6px rgba(0, 0, 0, 0.6), 0 0 20px rgba(56, 189, 248, 0.15) !important;
    }
    body.dark-theme .horizontal-carousel-rail::-webkit-scrollbar-track {
      background: #0F172A;
    }
    body.dark-theme .horizontal-carousel-rail::-webkit-scrollbar-thumb {
      background: #38BDF8;
    }
    body.dark-theme .portal-tab-btn {
      color: #94A3B8;
    }
    body.dark-theme .portal-tab-btn:hover {
      color: #FFFFFF;
      background-color: #1E293B;
    }
    body.dark-theme .portal-tab-btn.active {
      background: linear-gradient(135deg, #0284C7, #4F46E5) !important;
      color: #FFFFFF !important;
    }
    body.dark-theme .from-emerald-50 {
      --tw-gradient-from: #042f2e !important;
      --tw-gradient-to: #0f172a !important;
      --tw-gradient-stops: var(--tw-gradient-from), #064e3b, var(--tw-gradient-to) !important;
      border-color: #059669 !important;
    }
    body.dark-theme .bg-amber-50\\/40,
    body.dark-theme .bg-amber-50\\/30 {
      background-color: rgba(120, 53, 15, 0.2) !important;
      border-color: #b45309 !important;
    }

    /* Print styles */
    @media print {
      body * { visibility: hidden; }
      #dbaModal, #dbaModal * { visibility: visible; }
      #dbaModal {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        background: white !important;
        color: black !important;
      }
      .no-print { display: none !important; }
    }
  </style>
</head>
<body class="bg-gradient-to-br from-slate-50 via-sky-50/30 to-indigo-50/20 text-slate-800 min-h-screen antialiased flex flex-col selection:bg-indigo-500 selection:text-white">

  <!-- ================= ENCABEZADO INSTITUCIONAL ================= -->
  <header class="glass-card border-b border-slate-200/90 bg-white/95 sticky top-0 z-40 backdrop-blur-md shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap items-center justify-between gap-3">
      
      <!-- Identidad Corporativa -->
      <div class="flex items-center gap-3">
        <div id="brandLogo" class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-sky-500 via-indigo-600 to-indigo-900 flex items-center justify-center text-white font-black text-lg shadow-md shadow-indigo-500/20 ring-2 ring-white shrink-0">
          📐
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs sm:text-sm font-black uppercase tracking-wider text-slate-900">
              Asesorías Pedagógicas S.A.S.
            </span>
            <span id="brandBadge" class="text-[10px] font-black uppercase tracking-wider text-sky-800 bg-sky-100/90 px-2.5 py-0.5 rounded-md">
              MEN Colombia • V.2
            </span>
          </div>
          <h1 class="text-xs sm:text-sm font-bold text-slate-600 tracking-tight leading-snug mt-0.5">
            Plataforma Curricular Unificada de Derechos Básicos de Aprendizaje (1° a 11°)
          </h1>
        </div>
      </div>

      <!-- Controles Superiores: Versión y Tema -->
      <div class="flex items-center flex-wrap gap-2.5">
        
        <!-- Switcher de Versiones (V1 2015 ⇄ V2 2016) para Matemáticas y Lenguaje -->
        <div id="versionSwitchGroup" class="flex items-center bg-slate-100 p-0.5 rounded-xl border border-slate-200 text-xs shadow-2xs">
          <button id="btnVerV1" onclick="switchVersion('v1')" class="px-2.5 py-1 rounded-lg font-bold text-slate-500 hover:text-slate-900 transition cursor-pointer">
            V.1 (2015)
          </button>
          <button id="btnVerV2" onclick="switchVersion('v2')" class="px-2.5 py-1 rounded-lg font-bold bg-indigo-600 text-white shadow-xs transition cursor-pointer">
            V.2 (2016)
          </button>
        </div>
        <div id="versionBadgeSingle" class="hidden px-2.5 py-1 rounded-xl bg-slate-100 border border-slate-200 text-[11px] font-bold text-slate-700">
          Vigente MEN
        </div>

        <!-- Conmutador Tema Claro / Oscuro -->
        <button id="themeToggleBtn" onclick="toggleTheme()" class="p-1.5 px-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-700 transition cursor-pointer flex items-center justify-center gap-1.5 text-xs font-bold shadow-2xs" title="Alternar Modo Claro / Oscuro">
          <span id="themeToggleIcon">☀️</span>
          <span class="hidden sm:inline" id="themeToggleText">Modo</span>
        </button>

      </div>

    </div>

    <!-- ================= BARRA DE PESTAÑAS POR ASIGNATURA ================= -->
    <nav class="portal-tab-nav border-t border-slate-200/80 bg-slate-50/80 px-4 sm:px-6 lg:px-8 py-2 overflow-x-auto no-print">
      <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
        <div class="flex items-center gap-2 sm:gap-3 shrink-0">
          <button onclick="switchSubject('matematicas')" id="tab-matematicas" class="portal-tab-btn active px-3.5 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 cursor-pointer shadow-xs">
            <span>📐</span> <span>Matemáticas</span>
          </button>
          <button onclick="switchSubject('lenguaje')" id="tab-lenguaje" class="portal-tab-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 cursor-pointer">
            <span>📚</span> <span>Lenguaje</span>
          </button>
          <button onclick="switchSubject('sociales')" id="tab-sociales" class="portal-tab-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 cursor-pointer">
            <span>🗺️</span> <span>Ciencias Sociales</span>
          </button>
          <button onclick="switchSubject('naturales')" id="tab-naturales" class="portal-tab-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 cursor-pointer">
            <span>🔬</span> <span>Ciencias Naturales</span>
          </button>
          <button onclick="switchSubject('ingles')" id="tab-ingles" class="portal-tab-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 cursor-pointer">
            <span>🇬🇧</span> <span>Inglés</span>
          </button>
        </div>
      </div>
    </nav>
  </header>

  <!-- ================= CONTENEDOR PRINCIPAL ================= -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full space-y-6">
    
    <!-- BARRA DE FILTROS Y CONTROLES -->
    <section class="glass-card border border-white/90 rounded-3xl p-4 sm:p-5 shadow-sm space-y-3">
      <div class="flex flex-col lg:flex-row items-center justify-between gap-3.5">
        
        <!-- Buscador Inteligente -->
        <div class="w-full lg:flex-1 relative">
          <input type="text" id="searchInput" placeholder="Buscar por palabra clave, enunciado o evidencia..." class="w-full pl-10 pr-9 py-2.5 text-xs sm:text-sm bg-white border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-all shadow-xs placeholder:text-slate-400 font-medium">
          <svg class="w-4 h-4 text-indigo-500 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          <button id="clearSearch" onclick="clearSearchInput()" class="hidden absolute right-3 top-3 text-slate-400 hover:text-slate-600 text-xs">✕</button>
        </div>

        <!-- Selects de Grado y Vistas -->
        <div class="flex flex-wrap sm:flex-nowrap items-center gap-3 w-full lg:w-auto">
          
          <div class="relative min-w-[190px] flex-1 sm:flex-initial">
            <select id="select-grado" onchange="onSelectGradoChange(this.value)" class="w-full pl-9 pr-9 py-2.5 text-xs sm:text-sm bg-white border border-slate-200 rounded-2xl focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-xs font-bold text-slate-800 cursor-pointer appearance-none">
              <option value="all">Todos los Grados (1° a 11°)</option>
              <option value="1">1° Grado</option><option value="2">2° Grado</option><option value="3">3° Grado</option>
              <option value="4">4° Grado</option><option value="5">5° Grado</option><option value="6">6° Grado</option>
              <option value="7">7° Grado</option><option value="8">8° Grado</option><option value="9">9° Grado</option>
              <option value="10">10° Grado</option><option value="11">11° Grado</option>
            </select>
            <span class="absolute left-3 top-2.5 text-slate-500 pointer-events-none text-sm">🏫</span>
            <span class="absolute right-3.5 top-3.5 text-slate-400 pointer-events-none text-[10px]">▼</span>
          </div>

          <!-- Selector de Módulo Curricular: Catálogo DBA vs Malla Temática Extendida -->
          <div id="moduleNavGroup" class="flex items-center bg-slate-100 p-1 rounded-2xl border border-slate-200 shrink-0 shadow-2xs">
            <button onclick="setCurricularModule('dbas')" id="module-btn-dbas" title="Catálogo de DBAs Oficiales" class="view-mode-btn active px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer">
              <span>📋</span> <span class="hidden sm:inline">DBAs</span>
            </button>
            <button onclick="setCurricularModule('malla')" id="module-btn-malla" title="Malla Temática Extendida con Trazabilidad Exacta" class="view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 cursor-pointer">
              <span>🗺️</span> <span class="hidden sm:inline">Malla Temática</span>
            </button>
          </div>

          <!-- Modos de Vista -->
          <div id="catalogViewModesGroup" class="flex items-center bg-slate-100 p-1 rounded-2xl border border-slate-200 shrink-0 shadow-2xs">
            <button onclick="setViewDisplayMode('carousel')" id="view-mode-carousel" title="Carrusel (↔️)" class="view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 cursor-pointer">
              <span>↔️</span> <span class="hidden sm:inline">Carrusel</span>
            </button>
            <button onclick="setViewDisplayMode('grid')" id="view-mode-grid" title="Malla (⊞)" class="view-mode-btn active px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 cursor-pointer">
              <span>⊞</span> <span class="hidden sm:inline">Malla</span>
            </button>
            <button onclick="setViewDisplayMode('bars')" id="view-mode-bars" title="Barras (☰)" class="view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 cursor-pointer">
              <span>☰</span> <span class="hidden sm:inline">Barras</span>
            </button>
          </div>

          <div class="text-xs text-slate-600 font-semibold whitespace-nowrap flex items-center gap-1.5 px-3 py-2 bg-slate-50 rounded-2xl border border-slate-200 shrink-0">
            <span>DBAs:</span>
            <span id="visibleCount" class="bg-indigo-600 text-white font-black text-xs px-2.5 py-0.5 rounded-full shadow-xs">0</span>
          </div>

        </div>
      </div>
    </section>

    <!-- CONTENEDOR DINÁMICO DE TARJETAS DBA -->
    <div id="contentContainer" class="space-y-6"></div>

  </main>

  <!-- ================= MODAL DE CONSULTA DE EVIDENCIAS 100% LITERAL ================= -->
  <div id="dbaModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-md z-50 hidden flex items-center justify-center p-2 sm:p-4 transition-all">
    <div class="bg-white border border-slate-200 rounded-3xl w-full max-w-3xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden ring-1 ring-black/5">
      
      <!-- Encabezado Modal -->
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-gradient-to-r from-indigo-50 to-white shrink-0">
        <div class="flex items-center gap-3">
          <span id="modalDbaBadge" class="px-3 py-1 rounded-full bg-indigo-600 text-white text-xs font-black">DBA 1</span>
          <span id="modalIdTag" class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-slate-200 text-slate-700">MAT_G1_DBA1</span>
          <h3 id="modalGradeTitle" class="text-base font-black text-slate-900">Grado 1°</h3>
        </div>
        <button onclick="closeModal()" class="p-2 text-slate-400 hover:text-slate-700 rounded-xl transition cursor-pointer">✕</button>
      </div>

      <!-- Contenido Scrolleable con Evidencias Completas -->
      <div class="p-6 overflow-y-auto space-y-4 text-xs sm:text-sm">
        <div>
          <span class="text-[11px] font-black uppercase tracking-wider text-indigo-600 block mb-1">Enunciado Oficial MEN:</span>
          <p id="modalEnunciado" class="font-bold text-slate-900 leading-relaxed bg-indigo-50/50 p-4 rounded-xl border border-indigo-100 text-sm"></p>
        </div>

        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-black uppercase tracking-wider text-slate-500">Evidencias de Aprendizaje Oficiales:</span>
            <span id="modalEvidenciasCount" class="text-[10px] font-bold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-100">0 Evidencias</span>
          </div>
          <ul id="modalEvidenciasList" class="space-y-2.5"></ul>
        </div>

        <div id="modalEjemploBox" class="hidden pt-3 border-t border-slate-200">
          <span class="text-[11px] font-black uppercase tracking-wider text-slate-500 block mb-1">Contexto / Ejemplo Oficial MEN:</span>
          <p id="modalEjemploText" class="text-slate-700 italic bg-slate-50 p-3.5 rounded-xl border border-slate-200 leading-relaxed"></p>
        </div>
      </div>

      <!-- Pie de Modal -->
      <div class="px-6 py-3 bg-slate-50 border-t border-slate-200 flex flex-wrap justify-between items-center gap-2 text-xs text-slate-500 shrink-0">
        <span class="font-semibold">Asesorías Pedagógicas S.A.S. • Integración Curricular MEN</span>
        <div class="flex items-center gap-2">
          <button onclick="printCurrentDba()" class="px-3 py-1.5 bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold rounded-xl transition cursor-pointer">
            🖨️ Imprimir
          </button>
          <button onclick="copyDbaData()" class="px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl transition shadow-xs cursor-pointer">
            📋 Copiar para Planeación
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= PIE DE PÁGINA ================= -->
  <footer class="glass-card border-t border-slate-200 py-6 mt-12">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-slate-500">
      <p class="font-bold text-slate-700">© 2026 Asesorías Pedagógicas S.A.S. • Todos los derechos reservados.</p>
      <p class="text-slate-500">Alineación Ministerial MEN Colombia • EBC • DBA V.2 • ICFES</p>
    </div>
  </footer>

  <!-- ================= LÓGICA DE APLICACIÓN Y RENDERIZADO ================= -->
  <script>
    // ================= ESTADO GLOBAL =================
    let currentSubject = 'matematicas';
    let currentVersion = 'v2'; // 'v1' o 'v2'
    let catalogDisplayMode = localStorage.getItem('ap_dba_display_mode') || 'grid'; // 'carousel', 'grid', 'bars'
    let currentGrade = 'all';
    let currentSearch = '';
    let isDarkMode = false;
    let currentModule = 'dbas'; // 'dbas' o 'malla'
    let currentPeriodRegime = localStorage.getItem('ap_period_regime') || '3'; // '3' o '4'

    const SUBJECT_META = {
      matematicas: { name: "Matemáticas", icon: "📐", badgeBg: "bg-sky-100 text-sky-800", prefix: "MAT" },
      lenguaje: { name: "Lenguaje", icon: "📚", badgeBg: "bg-rose-100 text-rose-800", prefix: "LEN" },
      sociales: { name: "Ciencias Sociales", icon: "🗺️", badgeBg: "bg-amber-100 text-amber-800", prefix: "SOC" },
      naturales: { name: "Ciencias Naturales", icon: "🔬", badgeBg: "bg-emerald-100 text-emerald-800", prefix: "NAT" },
      ingles: { name: "Inglés", icon: "🇬🇧", badgeBg: "bg-blue-100 text-blue-800", prefix: "ING" }
    };

    const GRADES_METADATA = [
      { grade: 1, title: "Grado 1°", cycle: "Ciclo I", ageRange: "6 - 7 años", icon: "🔢", bgGradient: "from-emerald-600 via-teal-700 to-emerald-950" },
      { grade: 2, title: "Grado 2°", cycle: "Ciclo I", ageRange: "7 - 8 años", icon: "➕➖", bgGradient: "from-indigo-600 via-sky-700 to-indigo-950" },
      { grade: 3, title: "Grado 3°", cycle: "Ciclo I", ageRange: "8 - 9 años", icon: "📏", bgGradient: "from-sky-600 via-cyan-700 to-blue-950" },
      { grade: 4, title: "Grado 4°", cycle: "Ciclo II", ageRange: "9 - 10 años", icon: "📐", bgGradient: "from-purple-600 via-violet-700 to-indigo-950" },
      { grade: 5, title: "Grado 5°", cycle: "Ciclo II", ageRange: "10 - 11 años", icon: "⚖️", bgGradient: "from-amber-600 via-orange-600 to-amber-950" },
      { grade: 6, title: "Grado 6°", cycle: "Ciclo III", ageRange: "11 - 12 años", icon: "📊", bgGradient: "from-blue-600 via-indigo-800 to-slate-950" },
      { grade: 7, title: "Grado 7°", cycle: "Ciclo III", ageRange: "12 - 13 años", icon: "📉", bgGradient: "from-teal-600 via-emerald-800 to-teal-950" },
      { grade: 8, title: "Grado 8°", cycle: "Ciclo IV", ageRange: "13 - 14 años", icon: "⚡", bgGradient: "from-purple-700 via-fuchsia-800 to-slate-950" },
      { grade: 9, title: "Grado 9°", cycle: "Ciclo IV", ageRange: "14 - 15 años", icon: "📈", bgGradient: "from-blue-700 via-sky-800 to-indigo-950" },
      { grade: 10, title: "Grado 10°", cycle: "Ciclo V", ageRange: "15 - 16 años", icon: "🔬", bgGradient: "from-emerald-700 via-teal-800 to-slate-950" },
      { grade: 11, title: "Grado 11°", cycle: "Ciclo V", ageRange: "16 - 17 años", icon: "🎓", bgGradient: "from-indigo-900 via-purple-950 to-slate-950" }
    ];

    // ================= ACCESO ROBUSTO AL BANCO DE DATOS =================
    function getActiveDbaList() {
      const db = (typeof MASTER_DBA_DATABASE !== 'undefined' ? MASTER_DBA_DATABASE : (typeof window !== 'undefined' ? window.MASTER_DBA_DATABASE : null)) || {};
      let key = currentSubject;
      if (currentVersion === 'v1') {
        if (currentSubject === 'matematicas') key = 'matematicas_v1';
        if (currentSubject === 'lenguaje') key = 'lenguaje_v1';
      }
      return db[key] || [];
    }

    // ================= FUNCIONES DE CONTROL Y NAVEGACIÓN =================
    window.switchSubject = function(subjectKey) {
      currentSubject = subjectKey;
      document.querySelectorAll('.portal-tab-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('tab-' + subjectKey);
      if (activeBtn) activeBtn.classList.add('active');

      const meta = SUBJECT_META[subjectKey];
      document.getElementById('brandLogo').textContent = meta.icon;
      if (!['matematicas', 'sociales', 'naturales'].includes(subjectKey) && currentModule === 'malla') {
        currentModule = 'dbas';
      }

      // Actualizar visibilidad de versión
      const switchGrp = document.getElementById('versionSwitchGroup');
      const badgeSingle = document.getElementById('versionBadgeSingle');
      if (subjectKey === 'matematicas' || subjectKey === 'lenguaje') {
        switchGrp.classList.remove('hidden');
        badgeSingle.classList.add('hidden');
        document.getElementById('brandBadge').textContent = `MEN Colombia • ${meta.name} ${currentVersion.toUpperCase()}`;
      } else {
        switchGrp.classList.add('hidden');
        badgeSingle.classList.remove('hidden');
        document.getElementById('brandBadge').textContent = `MEN Colombia • ${meta.name} Vigente`;
      }

      render();
    };

    window.switchVersion = function(ver) {
      currentVersion = ver;
      const b1 = document.getElementById('btnVerV1');
      const b2 = document.getElementById('btnVerV2');
      if (ver === 'v1') {
        b1.className = "px-2.5 py-1 rounded-lg font-bold bg-indigo-600 text-white shadow-xs transition cursor-pointer";
        b2.className = "px-2.5 py-1 rounded-lg font-bold text-slate-500 hover:text-slate-900 transition cursor-pointer";
      } else {
        b2.className = "px-2.5 py-1 rounded-lg font-bold bg-indigo-600 text-white shadow-xs transition cursor-pointer";
        b1.className = "px-2.5 py-1 rounded-lg font-bold text-slate-500 hover:text-slate-900 transition cursor-pointer";
      }
      const meta = SUBJECT_META[currentSubject];
      document.getElementById('brandBadge').textContent = `MEN Colombia • ${meta.name} ${ver.toUpperCase()}`;
      render();
    };

    window.toggleTheme = function() {
      isDarkMode = !isDarkMode;
      const icon = document.getElementById('themeToggleIcon');
      if (isDarkMode) {
        document.body.classList.add('dark-theme');
        icon.textContent = '🌙';
        localStorage.setItem('theme_preference', 'dark');
      } else {
        document.body.classList.remove('dark-theme');
        icon.textContent = '☀️';
        localStorage.setItem('theme_preference', 'light');
      }
    };

    window.onSelectGradoChange = function(val) {
      currentGrade = val;
      render();
    };

    window.clearSearchInput = function() {
      document.getElementById('searchInput').value = '';
      currentSearch = '';
      document.getElementById('clearSearch').classList.add('hidden');
      render();
    };

    document.getElementById('searchInput').addEventListener('input', (e) => {
      currentSearch = e.target.value.trim();
      document.getElementById('clearSearch').classList.toggle('hidden', currentSearch.length === 0);
      render();
    });

    window.setCurricularModule = function(mode) {
      currentModule = mode;
      updateModuleButtons();
      render();
    };

    function updateModuleButtons() {
      const btnDba = document.getElementById('module-btn-dbas');
      const btnMalla = document.getElementById('module-btn-malla');
      if (btnDba) {
        btnDba.className = currentModule === 'dbas'
          ? "view-mode-btn active px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer"
          : "view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 hover:text-slate-900 cursor-pointer";
      }
      if (btnMalla) {
        btnMalla.className = currentModule === 'malla'
          ? "view-mode-btn active px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer"
          : "view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 hover:text-slate-900 cursor-pointer";
      }

      const gradeBtnDba = document.getElementById('grade-module-dbas');
      const gradeBtnMalla = document.getElementById('grade-module-malla');
      if (gradeBtnDba) {
        gradeBtnDba.className = currentModule === 'dbas'
          ? "view-mode-btn active px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer"
          : "view-mode-btn px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 hover:text-slate-900 cursor-pointer";
      }
      if (gradeBtnMalla) {
        gradeBtnMalla.className = currentModule === 'malla'
          ? "view-mode-btn active px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer"
          : "view-mode-btn px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 hover:text-slate-900 cursor-pointer";
      }

      const catalogGroup = document.getElementById('catalogViewModesGroup');
      if (catalogGroup) {
        if (currentModule === 'malla' && currentGrade === 'all') {
          catalogGroup.classList.add('hidden');
        } else {
          catalogGroup.classList.remove('hidden');
        }
      }
    }

    window.seleccionarGradoMallaTematica = function(gradeNum) {
      currentGrade = String(gradeNum);
      currentModule = 'malla';
      document.getElementById('select-grado').value = currentGrade;
      updateModuleButtons();
      render();
      window.scrollTo({ top: 120, behavior: 'smooth' });
    };

    window.setPeriodRegime = function(regime) {
      currentPeriodRegime = String(regime);
      window.currentPeriodRegime = currentPeriodRegime;
      localStorage.setItem('ap_period_regime', currentPeriodRegime);
      render();
    };

    window.copiarMallaSociales = function(gradeNum) {
      const db = (typeof MALLA_TEMATICA_SOCIALES !== 'undefined' ? MALLA_TEMATICA_SOCIALES : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_SOCIALES : null)) || {};
      const data = db[gradeNum];
      if (!data) return;

      const regime = (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : (typeof currentPeriodRegime !== 'undefined' ? currentPeriodRegime : '3'));
      const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';
      const periodos = data[regimeKey] || [];
      const regimeLabel = regime === '4' ? 'Malla de 4 Periodos Académicos' : 'Malla de 3 Periodos Académicos';

      let text = `=========================================================\n` +
                 `ASESORÍAS PEDAGÓGICAS S.A.S. - MALLA TEMÁTICA EXTENDIDA POR PERIODOS\n` +
                 `Área: Ciencias Sociales y Ciudadanas | ${data.title} (${data.cycle})\n` +
                 `Régimen: ${regimeLabel}\n` +
                 `=========================================================\n\n`;

      periodos.forEach(p => {
        text += `📅 ${p.titulo.toUpperCase()}\n`;
        p.items.forEach((it, idx) => {
          if (it.tipo === 'nucleo') {
            text += `  ${idx + 1}. [Núcleo DBA]: ${it.tema}\n` +
                    `     ↳ DBA ${it.dba} | Evidencia: "${it.evidencia}"\n` +
                    `     ↳ ID Oficial: ${it.dba_id}\n`;
          } else {
            text += `  ${idx + 1}. [Prerrequisito EBC]: ${it.tema}\n` +
                    `     ↳ Fundamento previo según Estándares Básicos de Competencias (EBC).\n`;
          }
        });
        text += `\n`;
      });

      navigator.clipboard.writeText(text).then(() => {
        alert(`¡Malla Temática de ${data.title} (${regimeLabel}) copiada con éxito al portapapeles para su planeación pedagógica!`);
      }).catch(() => {
        alert('Por favor copie el texto manualmente.');
      });
    };

    window.renderGradeMallaTematica = renderGradeMallaTematica;
    window.renderAllGradesMallaTematica = renderAllGradesMallaTematica;
    window.renderGradeSocialesMallaTematica = renderGradeSocialesMallaTematica;
    window.renderAllGradesSocialesMallaTematica = renderAllGradesSocialesMallaTematica;

    window.copiarMallaTematica = function(gradeNum) {
      const db = (typeof MALLA_TEMATICA_MATEMATICAS !== 'undefined' ? MALLA_TEMATICA_MATEMATICAS : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_MATEMATICAS : null)) || {};
      const data = db[gradeNum];
      if (!data) return;

      let text = `=========================================================\\n` +
                 `ASESORÍAS PEDAGÓGICAS S.A.S. - MALLA TEMÁTICA EXTENDIDA\\n` +
                 `Área: Matemáticas (MEN V.2 2016) | ${data.title} (${data.cycle})\\n` +
                 `=========================================================\\n\\n` +
                 `🎯 NÚCLEOS TEMÁTICOS CON TRAZABILIDAD EXACTA A DBA Y EVIDENCIA:\\n`;

      const nucleos = data.items.filter(x => x.type === 'nucleo');
      nucleos.forEach((it, idx) => {
        text += `\\n${idx + 1}. [Núcleo DBA]: ${it.tema}\\n` +
                `   ↳ ${it.alineacion}\\n` +
                `   ↳ Identificador oficial: ${it.dba_id}\\n`;
      });

      const prereqs = data.items.filter(x => x.type === 'prerrequisito');
      if (prereqs.length > 0) {
        text += `\\n📌 PRERREQUISITOS DE LOS ESTÁNDARES BÁSICOS DE COMPETENCIAS (EBC):\\n`;
        prereqs.forEach((it, idx) => {
          text += `\\n${idx + 1}. [Prerrequisito EBC]: ${it.tema}\\n`;
        });
      }

      navigator.clipboard.writeText(text).then(() => {
        alert(`¡Malla Temática de ${data.title} copiada con éxito al portapapeles para su planeación pedagógica!`);
      }).catch(() => {
        alert('Por favor copie el texto manualmente.');
      });
    };

    window.setViewDisplayMode = function(mode) {
      catalogDisplayMode = mode;
      localStorage.setItem('ap_dba_display_mode', mode);
      updateViewModeButtons();
      render();
    };

    function updateViewModeButtons() {
      ['carousel', 'grid', 'bars'].forEach(m => {
        const btn = document.getElementById('view-mode-' + m);
        if (btn) {
          btn.className = m === catalogDisplayMode 
            ? "view-mode-btn active px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer"
            : "view-mode-btn px-2.5 py-1.5 rounded-xl text-xs font-black flex items-center gap-1.5 text-slate-600 hover:text-slate-900 cursor-pointer";
        }
        const gradeBtn = document.getElementById('grade-view-mode-' + m);
        if (gradeBtn) {
          gradeBtn.className = m === catalogDisplayMode 
            ? "view-mode-btn active px-2.5 py-1 rounded-xl text-xs font-black flex items-center gap-1 cursor-pointer"
            : "view-mode-btn px-2.5 py-1 rounded-xl text-xs font-black flex items-center gap-1 text-slate-600 hover:text-slate-900 cursor-pointer";
        }
      });
    }

    window.scrollCarousel = function(delta) {
      const rail = document.getElementById('gradesCarouselRail');
      if (rail) rail.scrollBy({ left: delta, behavior: 'smooth' });
    };

    window.scrollDbaCarousel = function(delta) {
      const rail = document.getElementById('dbaCarouselRail');
      if (rail) rail.scrollBy({ left: delta, behavior: 'smooth' });
    };

    window.toggleGradeBar = function(gradeNum) {
      const body = document.getElementById('grade-bar-body-' + gradeNum);
      const chevron = document.getElementById('bar-chevron-' + gradeNum);
      if (body) {
        const isCollapsed = body.classList.contains('collapsed');
        body.classList.toggle('collapsed', !isCollapsed);
        if (chevron) chevron.classList.toggle('rotated', !isCollapsed);
      }
    };

    window.toggleDbaBar = function(dbaId) {
      const body = document.getElementById('dba-bar-body-' + dbaId);
      const chevron = document.getElementById('dba-bar-chevron-' + dbaId);
      if (body) {
        const isCollapsed = body.classList.contains('collapsed');
        body.classList.toggle('collapsed', !isCollapsed);
        if (chevron) chevron.classList.toggle('rotated', !isCollapsed);
      }
    };

    window.seleccionarGradoDesdeTarjeta = function(gradeNum) {
      currentGrade = String(gradeNum);
      currentModule = 'dbas';
      document.getElementById('select-grado').value = currentGrade;
      updateModuleButtons();
      render();
      window.scrollTo({ top: 120, behavior: 'smooth' });
    };

    window.volverATodosLosGrados = function() {
      currentGrade = 'all';
      document.getElementById('select-grado').value = 'all';
      updateModuleButtons();
      render();
      window.scrollTo({ top: 80, behavior: 'smooth' });
    };

    // ================= MOTOR DE RENDERIZADO PRINCIPAL =================
    function render() {
      const container = document.getElementById('contentContainer');
      container.innerHTML = '';

      updateModuleButtons();
      updateViewModeButtons();

      const modGroup = document.getElementById('moduleNavGroup');
      if (modGroup) {
        if (['matematicas', 'sociales', 'naturales'].includes(currentSubject)) {
          modGroup.classList.remove('hidden');
        } else {
          modGroup.classList.add('hidden');
          currentModule = 'dbas';
        }
      }

      if (currentModule === 'malla' && ['matematicas', 'sociales', 'naturales'].includes(currentSubject)) {
        if (currentGrade === 'all') {
          const wrapper = renderAllGradesMatrix(currentSubject, currentPeriodRegime);
          document.getElementById('contentContainer').appendChild(wrapper);
        } else {
          renderGradeDetailsView(parseInt(currentGrade), getActiveDbaList());
        }
        return;
      }

      const rawData = getActiveDbaList();
      const filtered = rawData.filter(item => {
        if (currentGrade !== 'all' && String(item.grade) !== String(currentGrade)) return false;
        if (currentSearch) {
          const s = currentSearch.toLowerCase();
          const matchTitle = item.title && item.title.toLowerCase().includes(s);
          const matchDba = item.dba && item.dba.toLowerCase().includes(s);
          const matchDesc = item.enunciado && item.enunciado.toLowerCase().includes(s);
          const matchEv = item.evidencias && item.evidencias.some(ev => ev.toLowerCase().includes(s));
          if (!matchTitle && !matchDba && !matchDesc && !matchEv) return false;
        }
        return true;
      });

      document.getElementById('visibleCount').textContent = filtered.length;

      if (currentSearch) {
        renderSearchResults(filtered);
        return;
      }

      if (currentGrade === 'all') {
        if (catalogDisplayMode === 'carousel') renderCarouselView(filtered);
        else if (catalogDisplayMode === 'bars') renderBarsView(filtered);
        else renderGridView(filtered);
      } else {
        renderGradeDetailsView(parseInt(currentGrade), filtered);
      }
    }

    // ================= MODO 1: CARRUSEL HORIZONTAL (~260px) =================
    function renderCarouselView(filtered) {
      const subjectMeta = SUBJECT_META[currentSubject];
      const wrapper = document.createElement('div');
      wrapper.className = "space-y-4";
      wrapper.innerHTML = `
        <div class="flex items-center justify-between gap-3 pb-2 border-b border-slate-200/80">
          <div>
            <h2 class="text-base sm:text-lg font-black text-slate-900 tracking-tight flex items-center gap-2">
              <span>↔️</span> Carrusel de Grados • ${subjectMeta.icon} ${subjectMeta.name}
            </h2>
            <p class="text-xs text-slate-500 font-medium">Desplazamiento horizontal fluido entre los grados escolares con tarjetas compactas (~260px).</p>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="scrollCarousel(-280)" class="w-8 h-8 rounded-xl bg-white hover:bg-slate-100 border border-slate-200 flex items-center justify-center font-black cursor-pointer shadow-xs">←</button>
            <button onclick="scrollCarousel(280)" class="w-8 h-8 rounded-xl bg-white hover:bg-slate-100 border border-slate-200 flex items-center justify-center font-black cursor-pointer shadow-xs">→</button>
          </div>
        </div>
      `;

      const rail = document.createElement('div');
      rail.id = 'gradesCarouselRail';
      rail.className = 'horizontal-carousel-rail';

      GRADES_METADATA.forEach(g => {
        const gradeItems = filtered.filter(x => x.grade === g.grade);
        const count = gradeItems.length;
        const totalEvids = gradeItems.reduce((acc, it) => acc + (it.evidencias || []).length, 0);

        const card = document.createElement('div');
        card.className = `grade-card-carousel group relative flex flex-col justify-between overflow-hidden rounded-3xl bg-gradient-to-b ${g.bgGradient} text-white shadow-lg p-4 sm:p-4.5 min-h-[300px] hover:shadow-2xl transition`;
        card.innerHTML = `
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-[9px] font-black uppercase px-2 py-0.5 rounded-full bg-white/20">${g.cycle}</span>
              <span class="text-[9px] font-bold text-white/80 bg-black/30 px-2 py-0.5 rounded-full">${g.ageRange}</span>
            </div>
            <div>
              <div class="flex items-baseline justify-between mt-1">
                <span class="text-3xl font-black">${g.grade}°</span>
                <span class="text-2xl p-2 rounded-2xl bg-white/10">${subjectMeta.icon}</span>
              </div>
              <h3 class="text-base font-black mt-1 leading-snug">${g.title}</h3>
            </div>
          </div>
          <div class="space-y-2.5 pt-3 border-t border-white/15">
            <div class="flex items-center justify-between text-xs font-bold">
              <span>📋 DBAs Oficiales:</span>
              <span class="px-2 py-0.5 bg-black/30 rounded text-amber-300">${count}</span>
            </div>
            <div class="flex items-center justify-between text-[11px] text-white/80 font-medium">
              <span>Evidencias MEN:</span>
              <span class="font-bold text-white">${totalEvids}</span>
            </div>
            ${['matematicas', 'sociales', 'naturales'].includes(currentSubject) ? `
              <div class="grid grid-cols-2 gap-1.5">
                <button onclick="seleccionarGradoDesdeTarjeta(${g.grade})" class="w-full py-2 px-1 rounded-xl bg-white hover:bg-amber-400 text-slate-900 font-black text-[11px] uppercase transition cursor-pointer shadow-xs text-center truncate">
                  Ver DBAs
                </button>
                <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="w-full py-2 px-1 rounded-xl ${currentSubject === 'naturales' ? 'bg-emerald-600 hover:bg-emerald-500' : (currentSubject === 'sociales' ? 'bg-amber-600 hover:bg-amber-500' : 'bg-sky-600 hover:bg-sky-500')} text-white font-black text-[11px] uppercase transition cursor-pointer shadow-xs text-center truncate" title="Ver Malla Temática">
                  🗺️ Malla
                </button>
              </div>
            ` : `
              <button onclick="seleccionarGradoDesdeTarjeta(${g.grade})" class="w-full py-2 px-3 rounded-xl bg-white hover:bg-amber-400 text-slate-900 font-black text-xs uppercase transition cursor-pointer shadow-xs">
                Ver Grado →
              </button>
            `}
          </div>
        `;
        rail.appendChild(card);
      });
      wrapper.appendChild(rail);
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= MODO 2: MALLA VERTICAL TRADICIONAL =================
    function renderGridView(filtered) {
      const subjectMeta = SUBJECT_META[currentSubject];
      const wrapper = document.createElement('div');
      wrapper.className = "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4";

      GRADES_METADATA.forEach(g => {
        const gradeItems = filtered.filter(x => x.grade === g.grade);
        const count = gradeItems.length;
        const totalEvids = gradeItems.reduce((acc, it) => acc + (it.evidencias || []).length, 0);

        const card = document.createElement('div');
        card.className = `group relative flex flex-col justify-between overflow-hidden rounded-3xl bg-gradient-to-b ${g.bgGradient} text-white shadow-md p-4 sm:p-4.5 min-h-[310px] hover:-translate-y-1 hover:shadow-xl transition`;
        card.innerHTML = `
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-[9px] font-black uppercase px-2 py-0.5 rounded-full bg-white/20">${g.cycle}</span>
              <span class="text-[9px] font-bold text-white/80 bg-black/20 px-2 py-0.5 rounded-full">${g.ageRange}</span>
            </div>
            <div class="pt-1">
              <div class="flex items-baseline justify-between">
                <span class="text-3xl sm:text-4xl font-black">${g.grade}°</span>
                <span class="text-2xl sm:text-3xl p-2 rounded-2xl bg-white/10">${subjectMeta.icon}</span>
              </div>
              <h3 class="text-base sm:text-lg font-black mt-1 leading-snug">${g.title}</h3>
            </div>
          </div>
          <div class="space-y-2.5 pt-3 border-t border-white/15">
            <div class="flex items-center justify-between text-xs">
              <span class="text-white/80 font-medium">DBAs MEN:</span>
              <span class="px-2 py-0.5 rounded bg-black/30 text-amber-300 font-bold">${count}</span>
            </div>
            <div class="flex items-center justify-between text-[11px] text-white/80">
              <span>Evidencias:</span>
              <span class="font-bold text-white">${totalEvids}</span>
            </div>
            ${['matematicas', 'sociales', 'naturales'].includes(currentSubject) ? `
              <div class="grid grid-cols-2 gap-2">
                <button onclick="seleccionarGradoDesdeTarjeta(${g.grade})" class="w-full py-2 px-1.5 rounded-xl bg-white hover:bg-amber-400 text-slate-900 font-black text-xs uppercase transition cursor-pointer shadow-xs text-center truncate">
                  Ver DBAs
                </button>
                <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="w-full py-2 px-1.5 rounded-xl ${currentSubject === 'naturales' ? 'bg-emerald-600 hover:bg-emerald-500' : (currentSubject === 'sociales' ? 'bg-amber-600 hover:bg-amber-500' : 'bg-sky-600 hover:bg-sky-500')} text-white font-black text-xs uppercase transition cursor-pointer shadow-xs text-center truncate" title="Ver Malla Temática">
                  🗺️ Malla
                </button>
              </div>
            ` : `
              <button onclick="seleccionarGradoDesdeTarjeta(${g.grade})" class="w-full py-2.5 px-3 rounded-xl bg-white hover:bg-amber-400 text-slate-900 font-black text-xs uppercase transition cursor-pointer shadow-xs">
                Explorar Grado →
              </button>
            `}
          </div>
        `;
        wrapper.appendChild(card);
      });
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= MODO 3: BARRAS HORIZONTALES FLOTANTES (ACORDEÓN CON CHEVRONS) =================
    function renderBarsView(filtered) {
      const wrapper = document.createElement('div');
      wrapper.className = "space-y-3";

      GRADES_METADATA.forEach(g => {
        const gradeDbas = filtered.filter(x => x.grade === g.grade);
        const totalEvids = gradeDbas.reduce((acc, it) => acc + (it.evidencias || []).length, 0);

        const barCard = document.createElement('div');
        barCard.className = "bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden transition";
        barCard.innerHTML = `
          <div class="p-3.5 sm:p-4 flex items-center justify-between cursor-pointer bg-slate-50/50 hover:bg-slate-50 transition" onclick="toggleGradeBar(${g.grade})">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-gradient-to-tr ${g.bgGradient} text-white flex items-center justify-center font-black text-base shadow-xs">${g.grade}°</div>
              <div>
                <div class="flex items-center gap-2">
                  <h3 class="text-sm font-black text-slate-900">${g.title}</h3>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">${g.cycle}</span>
                </div>
                <span class="text-xs text-slate-500 font-medium">${gradeDbas.length} DBAs registrados • ${totalEvids} evidencias</span>
              </div>
            </div>
            <div class="flex items-center gap-2">
              ${['matematicas', 'sociales', 'naturales'].includes(currentSubject) ? `
                <button onclick="event.stopPropagation(); seleccionarGradoMallaTematica(${g.grade})" class="px-2.5 py-1.5 ${currentSubject === 'naturales' ? 'bg-emerald-600 hover:bg-emerald-700' : (currentSubject === 'sociales' ? 'bg-amber-600 hover:bg-amber-700' : 'bg-sky-600 hover:bg-sky-700')} text-white font-bold text-xs rounded-xl shadow-xs transition cursor-pointer" title="Ver Malla Temática">
                  🗺️ Malla
                </button>
              ` : ''}
              <button onclick="event.stopPropagation(); seleccionarGradoDesdeTarjeta(${g.grade})" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-xs transition cursor-pointer">
                Ver DBAs
              </button>
              <span id="bar-chevron-${g.grade}" class="bar-chevron text-slate-400 font-black text-sm">▼</span>
            </div>
          </div>
          <div id="grade-bar-body-${g.grade}" class="grade-bar-body collapsed p-4 border-t border-slate-100 bg-slate-50/60 space-y-2.5 text-xs">
            ${gradeDbas.map(d => `
              <div class="p-3 bg-white rounded-xl border border-slate-200/90 shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-1">
                    <span class="px-2 py-0.5 bg-indigo-600 text-white font-black text-[10px] rounded-md">${d.dba}</span>
                    <span class="text-[10px] font-mono font-bold text-slate-400">${d.id}</span>
                    <span class="text-xs font-black text-slate-900">${d.title}</span>
                  </div>
                  <p class="text-slate-600 line-clamp-2 leading-relaxed text-[11px]">${d.enunciado}</p>
                </div>
                <div class="flex items-center gap-2 shrink-0">
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-500">${d.evidencias.length} Evids</span>
                  <button onclick="openDbaModal('${d.id}')" class="px-2.5 py-1 bg-slate-900 hover:bg-indigo-600 text-white font-bold text-[11px] rounded-lg transition">
                    Evidencias →
                  </button>
                </div>
              </div>
            `).join('')}
            ${gradeDbas.length === 0 ? '<p class="text-slate-400 text-center py-2">Sin DBAs registrados bajo este filtro.</p>' : ''}
          </div>
        `;
        wrapper.appendChild(barCard);
      });
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= SUB-VISTAS DINÁMICAS DE DBAS (MALLA, CARRUSEL, BARRAS) =================
    function renderDbaGridView(items) {
      return `
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5">
          ${items.map(item => createDbaCardHtml(item)).join('')}
        </div>
      `;
    }

    function renderDbaCarouselView(items) {
      return `
        <div class="space-y-3">
          <div class="flex items-center justify-between gap-3 pb-1">
            <p class="text-xs text-slate-500 font-medium flex items-center gap-1.5">
              <span>↔️</span> Desplazamiento horizontal fluido de tarjetas DBA fijas (~300px).
            </p>
            <div class="flex items-center gap-2 shrink-0">
              <button onclick="scrollDbaCarousel(-320)" class="w-8 h-8 rounded-xl bg-white hover:bg-slate-100 border border-slate-200 flex items-center justify-center font-black cursor-pointer shadow-xs" title="Anterior">←</button>
              <button onclick="scrollDbaCarousel(320)" class="w-8 h-8 rounded-xl bg-white hover:bg-slate-100 border border-slate-200 flex items-center justify-center font-black cursor-pointer shadow-xs" title="Siguiente">→</button>
            </div>
          </div>
          <div id="dbaCarouselRail" class="horizontal-carousel-rail flex overflow-x-auto gap-4 py-2">
            ${items.map(item => `
              <div class="flex-shrink-0 w-[300px] min-w-[300px] max-w-[300px] snap-start">
                ${createDbaCardHtml(item)}
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    function renderDbaBarsView(items) {
      return `
        <div class="space-y-3">
          ${items.map(item => `
            <div class="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden transition">
              <div class="p-3.5 sm:p-4 flex items-center justify-between cursor-pointer bg-slate-50/50 hover:bg-slate-50 transition" onclick="toggleDbaBar('${item.id}')">
                <div class="flex items-center gap-3 flex-1 min-w-0 pr-2">
                  <span class="px-2.5 py-1 rounded-xl text-xs sm:text-sm font-black bg-indigo-600 text-white shadow-xs shrink-0">
                    ${item.dba}
                  </span>
                  <div class="min-w-0 flex-1">
                    <div class="flex items-center gap-2 flex-wrap">
                      <span class="text-[10px] font-mono font-bold text-slate-400">${item.id}</span>
                      <span class="text-xs sm:text-sm font-black text-slate-900 truncate">${item.title}</span>
                    </div>
                    <p class="text-xs text-slate-600 line-clamp-1 leading-snug mt-0.5">${item.enunciado}</p>
                  </div>
                </div>
                <div class="flex items-center gap-2.5 shrink-0">
                  <span class="text-[11px] font-bold px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 border border-indigo-100 hidden sm:inline-block">
                    ${item.evidencias.length} Evidencias
                  </span>
                  <button onclick="event.stopPropagation(); openDbaModal('${item.id}')" class="px-3 py-1.5 bg-slate-900 hover:bg-indigo-600 text-white font-bold text-xs rounded-xl shadow-xs transition flex items-center gap-1 cursor-pointer">
                    <span class="hidden md:inline">Consultar Evidencias en Modal</span>
                    <span class="md:hidden">Modal</span>
                    <span>→</span>
                  </button>
                  <span id="dba-bar-chevron-${item.id}" class="bar-chevron text-slate-400 font-black text-sm">▼</span>
                </div>
              </div>
              
              <!-- Acordeón Desplegable Directo de Evidencias Oficiales -->
              <div id="dba-bar-body-${item.id}" class="grade-bar-body collapsed p-4 border-t border-slate-100 bg-slate-50/60 space-y-3 text-xs">
                <div>
                  <span class="text-[10px] font-black uppercase tracking-wider text-indigo-700 block mb-1">Enunciado Oficial MEN:</span>
                  <p class="font-bold text-slate-800 leading-relaxed bg-white p-3 rounded-xl border border-slate-200 text-xs sm:text-sm">${item.enunciado}</p>
                </div>
                <div>
                  <div class="flex items-center justify-between mb-2">
                    <span class="text-[10px] font-black uppercase tracking-wider text-slate-500">Evidencias de Aprendizaje Oficiales (${item.evidencias.length}):</span>
                    <button onclick="openDbaModal('${item.id}')" class="text-[11px] font-bold text-indigo-600 hover:text-indigo-800 underline cursor-pointer">Abrir Modal Completo →</button>
                  </div>
                  <ul class="space-y-2">
                    ${item.evidencias.map((ev, idx) => `
                      <li class="flex items-start gap-2.5 bg-white p-2.5 rounded-xl border border-slate-200/80 shadow-2xs">
                        <span class="px-2 py-0.5 rounded bg-indigo-100 text-indigo-900 font-mono text-[10px] font-black shrink-0 mt-0.5">
                          ${item.dba} • Ev. ${idx + 1}
                        </span>
                        <span class="text-slate-800 font-medium leading-relaxed text-xs">
                          ${ev}
                        </span>
                      </li>
                    `).join('')}
                  </ul>
                </div>
                ${item.ejemplo ? `
                  <div class="pt-2 border-t border-slate-200/80">
                    <span class="text-[10px] font-black uppercase tracking-wider text-slate-500 block mb-1">Contexto / Ejemplo Oficial MEN:</span>
                    <p class="text-slate-700 italic bg-amber-50/50 p-2.5 rounded-xl border border-amber-200/60 text-xs">${item.ejemplo}</p>
                  </div>
                ` : ''}
              </div>
            </div>
          `).join('')}
        </div>
      `;
    }

    // ================= VISTA DETALLADA POR GRADO =================
    function renderGradeDetailsView(gradeNum, filtered) {
      const meta = GRADES_METADATA.find(x => x.grade === gradeNum) || { title: `Grado ${gradeNum}°`, cycle: "Ciclo" };
      const items = filtered.filter(x => x.grade === gradeNum);
      const subjectMeta = SUBJECT_META[currentSubject];
      const totalEvids = items.reduce((acc, it) => acc + (it.evidencias || []).length, 0);

      const wrapper = document.createElement('div');
      wrapper.className = "space-y-6";
      wrapper.innerHTML = `
        <div class="bg-white rounded-3xl border border-slate-200 p-4 sm:p-5 shadow-sm flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <button onclick="volverATodosLosGrados()" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-black text-xs transition cursor-pointer flex items-center gap-1.5 shadow-2xs shrink-0">
              <span>←</span> <span>Volver a Todos</span>
            </button>
            <div class="flex items-center gap-3">
              <span class="text-3xl">${subjectMeta.icon}</span>
              <div>
                <div class="flex items-center gap-2">
                  <h2 class="text-lg sm:text-xl font-black text-slate-900">${meta.title} • ${subjectMeta.name}</h2>
                  <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-800">${currentVersion.toUpperCase()}</span>
                </div>
                <p class="text-xs text-slate-500 font-medium">${meta.cycle} • ${items.length} DBAs Oficiales • ${totalEvids} Evidencias Registradas</p>
              </div>
            </div>
          </div>
          
          <div class="flex flex-wrap items-center gap-2.5">
            <!-- Selector de Módulo en Grado (DBAs vs Malla Temática) -->
            ${['matematicas', 'sociales', 'naturales'].includes(currentSubject) ? `
              <div class="flex items-center bg-slate-100 p-1 rounded-2xl border border-slate-200 shadow-2xs">
                <button onclick="setCurricularModule('dbas')" id="grade-module-dbas" class="view-mode-btn ${currentModule === 'dbas' ? 'active' : ''} px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer">
                  <span>📋</span> <span>DBAs</span>
                </button>
                <button onclick="setCurricularModule('malla')" id="grade-module-malla" class="view-mode-btn ${currentModule === 'malla' ? 'active' : ''} px-3 py-1 rounded-xl text-xs font-black flex items-center gap-1.5 cursor-pointer">
                  <span>🗺️</span> <span>Malla Temática</span>
                </button>
              </div>
            ` : ''}

            <!-- Selector de Modos de Vista cuando se ven DBAs -->
            <div id="gradeDbaViewModes" class="flex items-center bg-slate-100 p-1 rounded-2xl border border-slate-200 shadow-2xs ${currentModule === 'malla' ? 'hidden' : ''}">
              <button onclick="setViewDisplayMode('carousel')" id="grade-view-mode-carousel" title="Carrusel (↔️)" class="view-mode-btn ${catalogDisplayMode === 'carousel' ? 'active' : ''} px-2.5 py-1 rounded-xl text-xs font-black flex items-center gap-1 cursor-pointer">
                <span>↔️</span> <span class="hidden md:inline">Carrusel</span>
              </button>
              <button onclick="setViewDisplayMode('grid')" id="grade-view-mode-grid" title="Malla (⊞)" class="view-mode-btn ${catalogDisplayMode === 'grid' ? 'active' : ''} px-2.5 py-1 rounded-xl text-xs font-black flex items-center gap-1 cursor-pointer">
                <span>⊞</span> <span class="hidden md:inline">Malla</span>
              </button>
              <button onclick="setViewDisplayMode('bars')" id="grade-view-mode-bars" title="Barras (☰)" class="view-mode-btn ${catalogDisplayMode === 'bars' ? 'active' : ''} px-2.5 py-1 rounded-xl text-xs font-black flex items-center gap-1 cursor-pointer">
                <span>☰</span> <span class="hidden md:inline">Barras</span>
              </button>
            </div>
          </div>
        </div>

        <div id="gradeMainContentContainer">
          ${currentModule === 'malla' && ['matematicas', 'sociales', 'naturales'].includes(currentSubject)
            ? renderMatrix(currentSubject, gradeNum, currentPeriodRegime)
            : (items.length === 0 
                ? '<div class="py-12 text-center text-slate-400 bg-white rounded-3xl border border-dashed border-slate-300">No hay DBAs registrados para esta selección.</div>' 
                : (catalogDisplayMode === 'carousel' ? renderDbaCarouselView(items) : (catalogDisplayMode === 'bars' ? renderDbaBarsView(items) : renderDbaGridView(items))))
          }
        </div>
      `;
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= MÓDULO MALLA TEMÁTICA EXTENDIDA (UN GRADO) =================
    function renderGradeMallaTematica(gradeNum) {
      const meta = GRADES_METADATA.find(x => x.grade === gradeNum) || { title: `Grado ${gradeNum}°`, cycle: "Ciclo" };
      const db = (typeof MALLA_TEMATICA_MATEMATICAS !== 'undefined' ? MALLA_TEMATICA_MATEMATICAS : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_MATEMATICAS : null)) || {};
      const data = db[gradeNum];

      if (!data) {
        return `<div class="p-8 text-center text-slate-400 bg-white rounded-3xl border border-dashed border-slate-300">No hay datos de Malla Temática disponibles para este grado.</div>`;
      }

      const nucleos = data.items.filter(x => x.type === 'nucleo');
      const prereqs = data.items.filter(x => x.type === 'prerrequisito');

      return `
        <div class="space-y-6">
          <!-- Banner Informativo Institucional -->
          <div class="bg-gradient-to-r from-emerald-50 via-teal-50 to-indigo-50 border border-emerald-200/90 rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start sm:items-center gap-3.5">
              <div class="w-12 h-12 rounded-2xl bg-emerald-600 text-white flex items-center justify-center font-black text-xl shadow-md shrink-0">
                🗺️
              </div>
              <div>
                <div class="flex items-center gap-2 flex-wrap">
                  <h3 class="text-base sm:text-lg font-black text-slate-900">Malla Temática Extendida • ${meta.title}</h3>
                  <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
                    Matemáticas MEN V.2 (2016)
                  </span>
                </div>
                <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
                  Trazabilidad curricular exacta: Mapeo directo entre temáticas estructurantes, Núcleos DBA, Evidencias Oficiales y Prerrequisitos de los Estándares Básicos de Competencias (EBC).
                </p>
              </div>
            </div>
            <div class="flex flex-wrap items-center gap-2 shrink-0">
              <div class="px-3 py-1.5 rounded-xl bg-white/95 border border-emerald-200 text-xs font-bold text-slate-700 shadow-2xs">
                <span class="text-emerald-700 font-black">${nucleos.length}</span> Núcleos DBA
              </div>
              <div class="px-3 py-1.5 rounded-xl bg-white/95 border border-amber-200 text-xs font-bold text-slate-700 shadow-2xs">
                <span class="text-amber-700 font-black">${prereqs.length}</span> Prerrequisitos EBC
              </div>
              <button onclick="copiarMallaTematica(${gradeNum})" class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-emerald-700 text-white font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1.5">
                <span>📋</span> <span>Copiar Malla</span>
              </button>
            </div>
          </div>

          <!-- 1. Núcleos DBA con Trazabilidad Exacta -->
          <div class="space-y-3">
            <div class="flex items-center justify-between pb-1 border-b border-slate-200/80">
              <h4 class="text-xs sm:text-sm font-black text-slate-900 uppercase tracking-wider flex items-center gap-2">
                <span>🎯</span> Núcleos Temáticos Prioritarios (Alineación DBA y Evidencias)
              </h4>
              <span class="text-[11px] font-bold text-slate-500">${nucleos.length} Temáticas Oficiales</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              ${nucleos.map(item => `
                <div class="p-4 sm:p-4.5 rounded-2xl bg-white border border-slate-200/90 shadow-xs hover:border-emerald-500 hover:shadow-md transition flex flex-col justify-between space-y-3.5">
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between flex-wrap gap-2">
                      <div class="flex items-center gap-2">
                        <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-200 shrink-0 flex items-center gap-1">
                          <span>✅</span> Núcleo DBA
                        </span>
                        <span class="px-2 py-0.5 text-[10px] font-black rounded-lg bg-indigo-100 text-indigo-900 border border-indigo-200 shrink-0">
                          DBA ${item.dba}
                        </span>
                      </div>
                      <span class="text-[10px] font-mono text-slate-400 font-bold bg-slate-100 px-2 py-0.5 rounded border border-slate-200">
                        ${item.dba_id}
                      </span>
                    </div>

                    <h5 class="text-xs sm:text-sm font-black text-slate-900 leading-snug">
                      ${item.tema}
                    </h5>

                    <!-- Trazabilidad exacta requerida -->
                    <div class="bg-slate-50/90 p-3 rounded-xl border border-slate-200/80 leading-relaxed space-y-1">
                      <div class="flex items-start gap-1.5 text-xs text-slate-500 italic">
                        <span class="text-emerald-600 font-black not-italic shrink-0">↳</span>
                        <span class="text-slate-600">
                          Alineación: <strong class="text-slate-800 not-italic">DBA ${item.dba}</strong> | Evidencia: "${item.evidencia}"
                        </span>
                      </div>
                    </div>
                  </div>

                  <div class="pt-2 border-t border-slate-100 flex items-center justify-between gap-2">
                    <span class="text-[10px] font-bold text-slate-400">MEN Colombia • V.2</span>
                    <button onclick="openDbaModal('${item.dba_id}')" class="px-3 py-1.5 bg-slate-900 hover:bg-indigo-600 text-white font-bold text-xs rounded-xl shadow-xs transition flex items-center gap-1.5 cursor-pointer">
                      <span>Consultar DBA ${item.dba}</span>
                      <span>→</span>
                    </button>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- 2. Prerrequisitos de los Estándares Básicos (EBC) -->
          ${prereqs.length > 0 ? `
            <div class="space-y-3 pt-2">
              <div class="flex items-center justify-between pb-1 border-b border-slate-200/80">
                <h4 class="text-xs sm:text-sm font-black text-slate-900 uppercase tracking-wider flex items-center gap-2">
                  <span>📌</span> Prerrequisitos Curriculares (Estándares Básicos de Competencias EBC)
                </h4>
                <span class="text-[11px] font-bold text-slate-500">${prereqs.length} Prerrequisitos</span>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                ${prereqs.map(item => `
                  <div class="p-4 rounded-2xl bg-amber-50/40 border border-dashed border-amber-300 shadow-2xs space-y-2">
                    <div class="flex items-center gap-2">
                      <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded-lg bg-amber-100 text-amber-900 border border-amber-200 flex items-center gap-1 shrink-0">
                        <span>📌</span> Prerrequisito EBC
                      </span>
                      <span class="text-[10px] font-bold text-amber-800 bg-amber-100/70 px-2 py-0.5 rounded">
                        Fundamento Previo
                      </span>
                    </div>
                    <h5 class="text-xs sm:text-sm font-bold text-slate-900 leading-snug">
                      ${item.tema}
                    </h5>
                    <p class="text-xs text-slate-500 italic">
                      ↳ Fundamento curricular y competencia previa requerida en la progresión curricular según los Estándares Básicos (EBC).
                    </p>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      `;
    }

    // ================= MÓDULO MALLA TEMÁTICA EXTENDIDA (TODOS LOS GRADOS) =================
    function renderAllGradesMallaTematica() {
      const db = (typeof MALLA_TEMATICA_MATEMATICAS !== 'undefined' ? MALLA_TEMATICA_MATEMATICAS : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_MATEMATICAS : null)) || {};
      const wrapper = document.createElement('div');
      wrapper.className = "space-y-6";

      let filterTerm = currentSearch ? currentSearch.toLowerCase() : '';

      wrapper.innerHTML = `
        <div class="bg-gradient-to-r from-emerald-50 via-teal-50 to-indigo-50 border border-emerald-200 rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex items-start sm:items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl bg-emerald-600 text-white flex items-center justify-center font-black text-2xl shadow-md shrink-0">
              🗺️
            </div>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h2 class="text-lg sm:text-xl font-black text-slate-900">Malla Temática Extendida • Matemáticas 1° a 11°</h2>
                <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
                  MEN V.2 (2016)
                </span>
              </div>
              <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
                Matriz curricular completa de los 11 grados escolares con trazabilidad directa entre Temáticas, Núcleos DBA, Evidencias Oficiales y Prerrequisitos EBC.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button onclick="setCurricularModule('dbas')" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-black text-xs transition cursor-pointer flex items-center gap-1.5 shadow-2xs">
              <span>📋</span> <span>Ver Catálogo DBAs</span>
            </button>
          </div>
        </div>

        <!-- Selector rápido de grados para Malla Temática -->
        <div class="flex items-center gap-2 overflow-x-auto pb-2 custom-scrollbar">
          <span class="text-xs font-bold text-slate-500 whitespace-nowrap">Ir al Grado:</span>
          ${GRADES_METADATA.map(g => `
            <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3 py-1.5 rounded-xl bg-white hover:bg-emerald-600 hover:text-white border border-slate-200 text-slate-700 font-black text-xs transition cursor-pointer shadow-2xs whitespace-nowrap">
              ${g.grade}°
            </button>
          `).join('')}
        </div>

        <!-- Lista de Grados con su Malla Temática -->
        <div class="space-y-6">
          ${GRADES_METADATA.map(g => {
            const gradeData = db[g.grade];
            if (!gradeData) return '';
            
            let items = gradeData.items;
            if (filterTerm) {
              items = items.filter(it => 
                (it.tema && it.tema.toLowerCase().includes(filterTerm)) ||
                (it.evidencia && it.evidencia.toLowerCase().includes(filterTerm)) ||
                (it.dba_id && it.dba_id.toLowerCase().includes(filterTerm))
              );
              if (items.length === 0) return '';
            }

            const nucleos = items.filter(x => x.type === 'nucleo');
            const prereqs = items.filter(x => x.type === 'prerrequisito');

            return `
              <div class="bg-white rounded-3xl border border-slate-200/90 shadow-sm p-5 sm:p-6 space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-3 pb-3 border-b border-slate-200/80">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr ${g.bgGradient} text-white flex items-center justify-center font-black text-base shadow-xs">
                      ${g.grade}°
                    </div>
                    <div>
                      <div class="flex items-center gap-2">
                        <h3 class="text-base font-black text-slate-900">${g.title} • Matemáticas</h3>
                        <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">${g.cycle}</span>
                      </div>
                      <p class="text-xs text-slate-500 font-medium">${nucleos.length} Núcleos DBA • ${prereqs.length} Prerrequisitos EBC</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <button onclick="copiarMallaTematica(${g.grade})" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition cursor-pointer flex items-center gap-1 shadow-2xs">
                      <span>📋</span> <span>Copiar</span>
                    </button>
                    <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1">
                      <span>Ver Grado</span> <span>→</span>
                    </button>
                  </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                  ${nucleos.map(item => `
                    <div class="p-3.5 rounded-2xl bg-slate-50/80 border border-slate-200/80 flex flex-col justify-between space-y-2">
                      <div class="space-y-1.5">
                        <div class="flex items-center justify-between gap-2">
                          <span class="px-2 py-0.5 text-[9px] font-black uppercase rounded bg-emerald-100 text-emerald-800">
                            ✅ Núcleo DBA ${item.dba}
                          </span>
                          <span class="text-[9px] font-mono text-slate-400 font-bold">${item.dba_id}</span>
                        </div>
                        <h4 class="text-xs font-black text-slate-900 leading-snug">${item.tema}</h4>
                        <div class="text-[11px] text-slate-500 italic leading-snug">
                          ↳ Alineación: DBA ${item.dba} - "${item.evidencia}"
                        </div>
                      </div>
                      <div class="pt-1.5 flex justify-end">
                        <button onclick="openDbaModal('${item.dba_id}')" class="text-[11px] font-bold text-indigo-600 hover:text-indigo-800 cursor-pointer">
                          Consultar DBA ${item.dba} →
                        </button>
                      </div>
                    </div>
                  `).join('')}

                  ${prereqs.map(item => `
                    <div class="p-3.5 rounded-2xl bg-amber-50/30 border border-dashed border-amber-300/80 space-y-1.5">
                      <span class="px-2 py-0.5 text-[9px] font-black uppercase rounded bg-amber-100 text-amber-900 inline-block">
                        📌 Prerrequisito EBC
                      </span>
                      <h4 class="text-xs font-bold text-slate-800 leading-snug">${item.tema}</h4>
                      <p class="text-[11px] text-slate-500 italic">↳ Fundamento previo según Estándares Básicos (EBC).</p>
                    </div>
                  `).join('')}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= RESULTADOS DE BÚSQUEDA =================
    // ================= MÓDULO MALLA TEMÁTICA CIENCIAS SOCIALES (UN GRADO POR PERIODOS) =================
    function renderGradeSocialesMallaTematica(gradeNum) {
      const meta = GRADES_METADATA.find(x => x.grade === gradeNum) || { title: `Grado ${gradeNum}°`, cycle: "Ciclo" };
      const db = (typeof MALLA_TEMATICA_SOCIALES !== 'undefined' ? MALLA_TEMATICA_SOCIALES : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_SOCIALES : null)) || {};
      const data = db[gradeNum];

      if (!data) {
        return `<div class="p-8 text-center text-slate-400 bg-white rounded-3xl border border-dashed border-slate-300">No hay datos de Malla Temática disponibles para este grado en Ciencias Sociales.</div>`;
      }

      const regime = (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : (typeof currentPeriodRegime !== 'undefined' ? currentPeriodRegime : '3'));
      const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';
      const periodos = data[regimeKey] || [];
      const totalNucleos = periodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'nucleo').length, 0);
      const totalPrereqs = periodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'prerrequisito').length, 0);

      return `
        <div class="space-y-6">
          <!-- Banner Informativo Institucional y Selector de Régimen Académico -->
          <div class="bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-indigo-500/10 border border-amber-300/80 rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col lg:flex-row lg:items-center justify-between gap-4">
            <div class="flex items-start sm:items-center gap-3.5">
              <div class="w-12 h-12 rounded-2xl bg-amber-600 text-white flex items-center justify-center font-black text-2xl shadow-md shrink-0">
                🏛️
              </div>
              <div>
                <div class="flex items-center gap-2 flex-wrap">
                  <h3 class="text-base sm:text-lg font-black text-slate-900">Malla Temática por Periodos • ${meta.title}</h3>
                  <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300">
                    Ciencias Sociales y Ciudadanas • MEN
                  </span>
                </div>
                <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
                  Organización curricular cronológica por periodos académicos con trazabilidad exacta a Núcleos DBA, Evidencias Oficiales y Prerrequisitos EBC.
                </p>
              </div>
            </div>

            <!-- Selector de Régimen Académico (Tabs 3 vs 4 Periodos) y Acciones -->
            <div class="flex flex-wrap items-center gap-2.5 shrink-0">
              <div class="flex items-center bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs">
                <button onclick="setPeriodRegime('3')" class="px-3 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${currentPeriodRegime === '3' ? 'bg-amber-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}">
                  <span>📅</span> <span>3 Periodos</span>
                </button>
                <button onclick="setPeriodRegime('4')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${currentPeriodRegime === '4' ? 'bg-amber-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}">
                  <span>📅</span> <span>4 Periodos</span>
                </button>
              </div>

              <div class="px-3 py-1.5 rounded-xl bg-white border border-amber-200 text-xs font-bold text-slate-700 shadow-2xs">
                <span class="text-amber-700 font-black">${totalNucleos}</span> Núcleos DBA
              </div>
              ${totalPrereqs > 0 ? `
                <div class="px-3 py-1.5 rounded-xl bg-white border border-emerald-200 text-xs font-bold text-slate-700 shadow-2xs">
                  <span class="text-emerald-700 font-black">${totalPrereqs}</span> EBC
                </div>
              ` : ''}

              <button onclick="copiarMallaSociales(${gradeNum})" class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-amber-600 text-white font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1.5">
                <span>📋</span> <span>Copiar Malla</span>
              </button>
            </div>
          </div>

          <!-- Estructura de Acordeones por Periodo Académico -->
          <div class="space-y-4">
            ${periodos.map(p => {
              const pNucleos = p.items.filter(x => x.tipo === 'nucleo');
              const pPrereqs = p.items.filter(x => x.tipo === 'prerrequisito');

              return `
                <details open class="group bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden transition-all duration-200 hover:border-amber-400">
                  <summary class="p-4 sm:p-4.5 bg-gradient-to-r from-slate-50 via-amber-50/30 to-slate-50 border-b border-slate-100 flex items-center justify-between cursor-pointer select-none">
                    <div class="flex items-center gap-3">
                      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 to-orange-500 text-white font-black text-xs sm:text-sm flex items-center justify-center shadow-xs shrink-0">
                        P${p.periodo}
                      </div>
                      <div>
                        <h4 class="text-xs sm:text-sm font-black text-slate-900">${p.titulo}</h4>
                        <p class="text-[11px] text-slate-500 font-medium">${p.items.length} Temáticas estructurantes para este periodo</p>
                      </div>
                    </div>
                    <div class="flex items-center gap-2">
                      <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-white text-slate-700 border border-slate-200 shadow-2xs">
                        ${pNucleos.length} Núcleos DBA ${pPrereqs.length > 0 ? `• ${pPrereqs.length} EBC` : ''}
                      </span>
                      <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200 text-xs font-bold px-1">
                        ▼
                      </span>
                    </div>
                  </summary>

                  <!-- Listado Compacto y Expandible (ul, li) -->
                  <div class="p-3 sm:p-4 bg-white">
                    <ul class="divide-y divide-slate-100">
                      ${p.items.map(it => {
                        if (it.tipo === 'nucleo') {
                          return `
                            <li class="py-1.5">
                              <details class="group/item rounded-xl border border-transparent hover:border-amber-200 hover:bg-amber-50/20 p-2 sm:p-2.5 transition">
                                <summary class="flex items-center justify-between gap-3 cursor-pointer select-none list-none">
                                  <div class="flex items-center gap-2.5 flex-wrap flex-1">
                                    <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded-lg bg-amber-100 text-amber-900 border border-amber-300 shrink-0 flex items-center gap-1 shadow-2xs">
                                      <span>🎯</span> Núcleo DBA
                                    </span>
                                    <span class="px-2 py-0.5 text-[10px] font-black rounded-lg bg-indigo-100 text-indigo-900 border border-indigo-200 shrink-0">
                                      DBA ${it.dba}
                                    </span>
                                    <span class="text-xs sm:text-sm font-bold text-slate-800 group-hover/item:text-amber-900 transition leading-snug">
                                      ${it.tema}
                                    </span>
                                  </div>
                                  <div class="flex items-center gap-2 shrink-0">
                                    <span class="text-[10px] font-mono text-slate-400 font-bold bg-slate-100 px-2 py-0.5 rounded border border-slate-200">
                                      ${it.dba_id}
                                    </span>
                                    <span class="text-xs text-slate-400 group-open/item:rotate-180 transition-transform duration-200 font-black">
                                      ▾
                                    </span>
                                  </div>
                                </summary>

                                <!-- Despliegue Suave de Trazabilidad Exacta -->
                                <div class="mt-2.5 pt-2.5 border-t border-amber-200/60 pl-2 pr-1 space-y-2">
                                  <div class="p-3 rounded-xl bg-amber-50/70 border border-amber-200/80 text-xs space-y-1.5 leading-relaxed">
                                    <div class="flex items-start gap-1.5 text-slate-700">
                                      <span class="text-amber-700 font-black not-italic shrink-0">↳</span>
                                      <div>
                                        <strong class="text-amber-950">Alineación Oficial MEN:</strong>
                                        <span class="text-slate-800 font-bold ml-1">DBA ${it.dba}</span>
                                      </div>
                                    </div>
                                    <div class="flex items-start gap-1.5 text-slate-600 pl-4 italic">
                                      <span>Evidencia: "${it.evidencia}"</span>
                                    </div>
                                  </div>
                                  <div class="flex items-center justify-between gap-2 pt-1">
                                    <span class="text-[10px] font-bold text-slate-400">Ciencias Sociales y Ciudadanas • MEN Colombia</span>
                                    <button onclick="openDbaModal('${it.dba_id}')" class="px-3 py-1.5 bg-slate-900 hover:bg-amber-600 text-white font-black text-xs rounded-xl shadow-xs transition flex items-center gap-1.5 cursor-pointer">
                                      <span>Consultar DBA ${it.dba} en Modal</span>
                                      <span>→</span>
                                    </button>
                                  </div>
                                </div>
                              </details>
                            </li>
                          `;
                        } else {
                          return `
                            <li class="py-1.5">
                              <details class="group/item rounded-xl border border-transparent hover:border-emerald-200 hover:bg-emerald-50/20 p-2 sm:p-2.5 transition">
                                <summary class="flex items-center justify-between gap-3 cursor-pointer select-none list-none">
                                  <div class="flex items-center gap-2.5 flex-wrap flex-1">
                                    <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded-lg bg-emerald-100 text-emerald-900 border border-emerald-300 shrink-0 flex items-center gap-1 shadow-2xs">
                                      <span>📌</span> Prerrequisito EBC
                                    </span>
                                    <span class="text-xs sm:text-sm font-semibold text-slate-700 group-hover/item:text-emerald-900 transition leading-snug">
                                      ${it.tema}
                                    </span>
                                  </div>
                                  <div class="flex items-center gap-2 shrink-0">
                                    <span class="text-[10px] font-bold text-emerald-700 bg-emerald-100/70 px-2 py-0.5 rounded border border-emerald-200">
                                      Fundamento Previo
                                    </span>
                                    <span class="text-xs text-slate-400 group-open/item:rotate-180 transition-transform duration-200 font-black">
                                      ▾
                                    </span>
                                  </div>
                                </summary>
                                <div class="mt-2.5 pt-2.5 border-t border-emerald-200/60 pl-2 pr-1 space-y-1">
                                  <p class="text-xs text-emerald-950/90 italic bg-emerald-50/70 p-2.5 rounded-xl border border-emerald-200/80">
                                    ↳ Fundamento curricular y competencia previa requerida en la progresión según los Estándares Básicos de Competencias (EBC). No posee DBA numérico asignado directamente.
                                  </p>
                                </div>
                              </details>
                            </li>
                          `;
                        }
                      }).join('')}
                    </ul>
                  </div>
                </details>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }

    // ================= MÓDULO MALLA TEMÁTICA CIENCIAS SOCIALES (TODOS LOS GRADOS POR PERIODOS) =================
    function renderAllGradesSocialesMallaTematica() {
      const db = (typeof MALLA_TEMATICA_SOCIALES !== 'undefined' ? MALLA_TEMATICA_SOCIALES : (typeof window !== 'undefined' ? window.MALLA_TEMATICA_SOCIALES : null)) || {};
      const wrapper = document.createElement('div');
      wrapper.className = "space-y-6";

      let filterTerm = currentSearch ? currentSearch.toLowerCase() : '';
      const regime = (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : (typeof currentPeriodRegime !== 'undefined' ? currentPeriodRegime : '3'));
      const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';

      wrapper.innerHTML = `
        <div class="bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-indigo-500/10 border border-amber-300 rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex items-start sm:items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl bg-amber-600 text-white flex items-center justify-center font-black text-2xl shadow-md shrink-0">
              🏛️
            </div>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h2 class="text-lg sm:text-xl font-black text-slate-900">Malla Temática Extendida por Periodos • Ciencias Sociales 1° a 11°</h2>
                <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300">
                  MEN Vigente
                </span>
              </div>
              <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
                Matriz curricular organizada cronológicamente por periodos académicos con trazabilidad exacta a Núcleos DBA, Evidencias Oficiales y Prerrequisitos EBC.
              </p>
            </div>
          </div>
          <div class="flex flex-wrap items-center gap-2 shrink-0">
            <!-- Tabs 3 vs 4 Periodos Global -->
            <div class="flex items-center bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs">
              <button onclick="setPeriodRegime('3')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${currentPeriodRegime === '3' ? 'bg-amber-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}">
                <span>📅</span> <span>3 Periodos</span>
              </button>
              <button onclick="setPeriodRegime('4')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${currentPeriodRegime === '4' ? 'bg-amber-600 text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'}">
                <span>📅</span> <span>4 Periodos</span>
              </button>
            </div>
            <button onclick="setCurricularModule('dbas')" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-black text-xs transition cursor-pointer flex items-center gap-1.5 shadow-2xs">
              <span>📋</span> <span>Ver Catálogo DBAs</span>
            </button>
          </div>
        </div>

        <!-- Selector rápido de grados para Malla de Sociales -->
        <div class="flex items-center gap-2 overflow-x-auto pb-2 custom-scrollbar">
          <span class="text-xs font-bold text-slate-500 whitespace-nowrap">Ir al Grado:</span>
          ${GRADES_METADATA.map(g => `
            <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3 py-1.5 rounded-xl bg-white hover:bg-amber-600 hover:text-white border border-slate-200 text-slate-700 font-black text-xs transition cursor-pointer shadow-2xs whitespace-nowrap">
              ${g.grade}°
            </button>
          `).join('')}
        </div>

        <!-- Lista de los 11 Grados con Acordeón por Periodo -->
        <div class="space-y-6">
          ${GRADES_METADATA.map(g => {
            const gradeData = db[g.grade];
            if (!gradeData) return '';

            const periodos = gradeData[regimeKey] || [];
            let filteredPeriodos = periodos;

            if (filterTerm) {
              filteredPeriodos = periodos.map(p => {
                const fItems = p.items.filter(it => 
                  (it.tema && it.tema.toLowerCase().includes(filterTerm)) ||
                  (it.evidencia && it.evidencia.toLowerCase().includes(filterTerm)) ||
                  (it.dba_id && it.dba_id.toLowerCase().includes(filterTerm))
                );
                return { ...p, items: fItems };
              }).filter(p => p.items.length > 0);

              if (filteredPeriodos.length === 0) return '';
            }

            const totalNucleos = filteredPeriodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'nucleo').length, 0);
            const totalPrereqs = filteredPeriodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'prerrequisito').length, 0);

            return `
              <div class="bg-white rounded-3xl border border-slate-200/90 shadow-sm p-5 sm:p-6 space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-3 pb-3 border-b border-slate-200/80">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr ${g.bgGradient} text-white flex items-center justify-center font-black text-base shadow-xs">
                      ${g.grade}°
                    </div>
                    <div>
                      <div class="flex items-center gap-2">
                        <h3 class="text-base font-black text-slate-900">${g.title} • Ciencias Sociales</h3>
                        <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">${g.cycle}</span>
                      </div>
                      <p class="text-xs text-slate-500 font-medium">${totalNucleos} Núcleos DBA • ${totalPrereqs} Prerrequisitos EBC (${currentPeriodRegime} Periodos)</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-2">
                    <button onclick="copiarMallaSociales(${g.grade})" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition cursor-pointer flex items-center gap-1 shadow-2xs">
                      <span>📋</span> <span>Copiar</span>
                    </button>
                    <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3.5 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1">
                      <span>Ver Grado</span> <span>→</span>
                    </button>
                  </div>
                </div>

                <!-- Acordeones de Periodo para este Grado -->
                <div class="space-y-3">
                  ${filteredPeriodos.map(p => `
                    <details open class="group bg-slate-50/60 rounded-2xl border border-slate-200/80 overflow-hidden">
                      <summary class="p-3 bg-white border-b border-slate-100 flex items-center justify-between cursor-pointer select-none">
                        <div class="flex items-center gap-2.5">
                          <span class="w-7 h-7 rounded-lg bg-amber-500 text-white font-black text-xs flex items-center justify-center shadow-2xs">
                            P${p.periodo}
                          </span>
                          <span class="text-xs sm:text-sm font-black text-slate-800">${p.titulo}</span>
                        </div>
                        <div class="flex items-center gap-2">
                          <span class="text-[10px] text-slate-500 font-bold">${p.items.length} temas</span>
                          <span class="text-slate-400 group-open:rotate-180 transition-transform duration-200 text-xs font-bold">▼</span>
                        </div>
                      </summary>
                      <div class="p-3 bg-white">
                        <ul class="divide-y divide-slate-100">
                          ${p.items.map(it => `
                            <li class="py-1">
                              <details class="group/subitem p-1.5 rounded-lg hover:bg-slate-50">
                                <summary class="flex items-center justify-between gap-2 cursor-pointer list-none">
                                  <div class="flex items-center gap-2 flex-wrap flex-1">
                                    ${it.tipo === 'nucleo' 
                                      ? `<span class="px-2 py-0.5 text-[9px] font-black uppercase rounded bg-amber-100 text-amber-900 border border-amber-300">🎯 Núcleo DBA ${it.dba}</span>`
                                      : `<span class="px-2 py-0.5 text-[9px] font-black uppercase rounded bg-emerald-100 text-emerald-900 border border-emerald-300">📌 Prerrequisito EBC</span>`
                                    }
                                    <span class="text-xs font-bold text-slate-800">${it.tema}</span>
                                  </div>
                                  <span class="text-xs text-slate-400 group-open/subitem:rotate-180 transition-transform font-black">▾</span>
                                </summary>
                                <div class="mt-2 pt-2 border-t border-slate-100 text-xs text-slate-600 pl-2 space-y-1">
                                  ${it.tipo === 'nucleo' ? `
                                    <p class="italic text-slate-500">↳ Alineación: <strong>DBA ${it.dba}</strong> | Evidencia: "${it.evidencia}"</p>
                                    <div class="pt-1">
                                      <button onclick="openDbaModal('${it.dba_id}')" class="text-[11px] font-bold text-amber-700 hover:text-amber-900 cursor-pointer">Consultar DBA ${it.dba} en Modal →</button>
                                    </div>
                                  ` : `
                                    <p class="italic text-slate-500">↳ Fundamento previo según Estándares Básicos de Competencias (EBC).</p>
                                  `}
                                </div>
                              </details>
                            </li>
                          `).join('')}
                        </ul>
                      </div>
                    </details>
                  `).join('')}
                </div>
              </div>
            `;
          }).join('')}
        </div>
      `;
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    function renderSearchResults(filtered) {
      const subjectMeta = SUBJECT_META[currentSubject];
      const wrapper = document.createElement('div');
      wrapper.className = "space-y-4";
      wrapper.innerHTML = `
        <div class="flex items-center justify-between pb-2 border-b border-slate-200">
          <div class="text-sm font-black text-slate-800">
            Resultados para: <span class="text-indigo-600">"${currentSearch}"</span> en ${subjectMeta.icon} ${subjectMeta.name} (${filtered.length} encontrados)
          </div>
          <button onclick="clearSearchInput()" class="text-xs font-bold text-slate-500 hover:text-slate-800 cursor-pointer">✕ Quitar Búsqueda</button>
        </div>
        <div>
          ${filtered.length === 0 
            ? '<div class="py-12 text-center text-slate-400 bg-white rounded-3xl border border-dashed border-slate-300">No se encontraron DBAs con este término.</div>' 
            : (catalogDisplayMode === 'carousel' ? renderDbaCarouselView(filtered) : (catalogDisplayMode === 'bars' ? renderDbaBarsView(filtered) : renderDbaGridView(filtered)))}
        </div>
      `;
      document.getElementById('contentContainer').appendChild(wrapper);
    }

    // ================= GENERADOR DE TARJETA DETALLADA DE DBA (COMPACTA Y ESBELTA) =================
    function createDbaCardHtml(item) {
      const subjectMeta = SUBJECT_META[currentSubject];
      return `
        <div class="sim-editorial-card bg-white rounded-2xl border border-slate-200/90 shadow-xs p-4 sm:p-4.5 flex flex-col justify-between space-y-3.5 h-full min-h-[310px]">
          <div class="space-y-2.5">
            <!-- Bloque Superior: Número del DBA en Grande, ID de Simulador y Conteo de Evidencias -->
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-1 rounded-xl text-sm font-black bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-100 shrink-0">
                  ${item.dba}
                </span>
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-slate-100 text-slate-500 font-bold border border-slate-200" title="Identificador para Simulador">
                  ${item.id}
                </span>
                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full ${subjectMeta.badgeBg}">
                  Grado ${item.grade}°
                </span>
              </div>
              <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md border border-slate-200">
                ${item.evidencias.length} Evidencias
              </span>
            </div>

            <!-- Título y Enunciado Truncado -->
            <div>
              <h4 class="font-black text-xs sm:text-sm text-slate-900 leading-snug line-clamp-1">
                ${item.title}
              </h4>
              <p class="text-xs text-slate-600 line-clamp-2 sm:line-clamp-3 leading-relaxed mt-1">
                ${item.enunciado}
              </p>
            </div>

            <!-- Vista previa de Evidencias Oficiales -->
            <div class="bg-slate-50/80 rounded-xl p-2.5 border border-slate-100 space-y-1.5 text-[11px]">
              <div class="text-[9px] font-black uppercase tracking-wider text-slate-400 flex items-center justify-between">
                <span>Evidencias Oficiales:</span>
                <span class="text-indigo-600 font-bold">${item.evidencias.length} total</span>
              </div>
              ${(item.evidencias || []).slice(0, 2).map((ev, i) => `
                <div class="flex items-start gap-1.5 text-slate-700 leading-snug">
                  <span class="text-indigo-500 font-bold shrink-0">•</span>
                  <span class="line-clamp-1 text-[10.5px]">${ev}</span>
                </div>
              `).join('')}
              ${(item.evidencias || []).length > 2 ? `<div class="text-[9.5px] text-slate-400 font-medium italic">+ ${(item.evidencias.length - 2)} evidencias más en el modal...</div>` : ''}
            </div>
          </div>

          <!-- Botón de Consulta de Evidencias en Modal -->
          <div class="pt-2 border-t border-slate-100">
            <button onclick="openDbaModal('${item.id}')" class="w-full py-2.5 bg-slate-900 hover:bg-indigo-600 text-white font-black text-xs rounded-xl transition cursor-pointer flex items-center justify-center gap-1.5 shadow-xs">
              <span>Consultar Evidencias en Modal</span>
              <span>→</span>
            </button>
          </div>
        </div>
      `;
    }

    // ================= MODAL DE EVIDENCIAS 100% LITERAL =================
    let currentDbaModalData = null;

    window.openDbaModal = function(id) {
      const allItems = getActiveDbaList();
      const item = allItems.find(x => x.id === id);
      if (!item) return;
      currentDbaModalData = item;
      const subjectMeta = SUBJECT_META[currentSubject];

      document.getElementById('modalDbaBadge').textContent = item.dba;
      document.getElementById('modalIdTag').textContent = item.id;
      document.getElementById('modalGradeTitle').textContent = `Grado ${item.grade}° • ${subjectMeta.icon} ${subjectMeta.name}`;
      document.getElementById('modalEnunciado').textContent = item.enunciado;
      document.getElementById('modalEvidenciasCount').textContent = `${item.evidencias.length} Evidencias Oficiales`;

      const list = document.getElementById('modalEvidenciasList');
      list.innerHTML = item.evidencias.map((ev, idx) => `
        <li class="flex items-start gap-2.5 bg-slate-50 p-3 rounded-xl border border-slate-200">
          <span class="px-2 py-0.5 rounded bg-indigo-100 text-indigo-900 font-mono text-[10px] font-black shrink-0 mt-0.5">
            ${item.dba} • Ev. ${idx + 1}
          </span>
          <span class="text-slate-800 font-medium leading-relaxed text-xs sm:text-sm">
            ${ev}
          </span>
        </li>
      `).join('');

      const ejemploBox = document.getElementById('modalEjemploBox');
      if (item.ejemplo) {
        ejemploBox.classList.remove('hidden');
        document.getElementById('modalEjemploText').textContent = item.ejemplo;
      } else {
        ejemploBox.classList.add('hidden');
      }

      document.getElementById('dbaModal').classList.remove('hidden');
    };

    window.closeModal = function() {
      document.getElementById('dbaModal').classList.add('hidden');
    };

    window.copyDbaData = function() {
      if (!currentDbaModalData) return;
      const subjectMeta = SUBJECT_META[currentSubject];
      const text = `=========================================================\\n` +
                   `ASESORÍAS PEDAGÓGICAS S.A.S. - BANCO CURRICULAR MEN\\n` +
                   `Área: ${subjectMeta.name} | Grado: ${currentDbaModalData.grade}° | ID: ${currentDbaModalData.id}\\n` +
                   `=========================================================\\n\\n` +
                   `${currentDbaModalData.dba}: ${currentDbaModalData.enunciado}\\n\\n` +
                   `EVIDENCIAS DE APRENDIZAJE:\\n` +
                   currentDbaModalData.evidencias.map((ev, i) => `  • Evidencia ${i+1}: ${ev}`).join('\\n') +
                   (currentDbaModalData.ejemplo ? `\\n\\nEJEMPLO / CONTEXTO OFICIAL:\\n${currentDbaModalData.ejemplo}` : '');
      
      navigator.clipboard.writeText(text).then(() => {
        alert('¡Contenido del DBA y sus evidencias copiado al portapapeles con éxito para su planeación pedagógica!');
      }).catch(() => {
        alert('Por favor copie el texto manualmente.');
      });
    };

    window.printCurrentDba = function() {
      window.print();
    };

    // ================= INICIALIZACIÓN =================
    document.addEventListener('DOMContentLoaded', () => {
      if (localStorage.getItem('theme_preference') === 'dark') {
        toggleTheme();
      }
      render();
    });
  </script>
</body>
</html>
"""

with open(r"d:\WILMER_FERRER\JSON\DBA_Antigravity\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"index.html successfully updated! Size: {len(html_template):,} bytes")
