/**
 * CONTROLADOR UNIFICADO DE MALLA TEMÁTICA EXTENDIDA POR PERIODOS
 * Asesorías Pedagógicas S.A.S.
 * Soporte Multi-Periodo (3 y 4 Periodos) y Trazabilidad 1:1 DBA-Evidencia Oficial
 * Áreas: Matemáticas, Ciencias Sociales y Ciencias Naturales (1° a 11°)
 */

(function(window) {
  'use strict';

  // Configuración y Metadatos por Asignatura
  const MATRIX_SUBJECT_CONFIG = {
    matematicas: {
      name: "Matemáticas",
      badgeTitle: "Matemáticas • MEN V.2 (2016)",
      icon: "📐",
      dbKey: "MALLA_TEMATICA_MATEMATICAS",
      themeColor: "sky",
      btnClass: "bg-sky-600 hover:bg-sky-700 text-white",
      activeTabClass: "bg-sky-600 text-white shadow-xs",
      borderAccent: "border-sky-300",
      bgGradient: "from-sky-500/10 via-indigo-500/10 to-teal-500/10",
      hoverBorder: "hover:border-sky-400"
    },
    sociales: {
      name: "Ciencias Sociales y Ciudadanas",
      badgeTitle: "Ciencias Sociales • MEN Vigente",
      icon: "🏛️",
      dbKey: "MALLA_TEMATICA_SOCIALES",
      themeColor: "amber",
      btnClass: "bg-amber-600 hover:bg-amber-700 text-white",
      activeTabClass: "bg-amber-600 text-white shadow-xs",
      borderAccent: "border-amber-300",
      bgGradient: "from-amber-500/10 via-orange-500/10 to-indigo-500/10",
      hoverBorder: "hover:border-amber-400"
    },
    naturales: {
      name: "Ciencias Naturales y Educación Ambiental",
      badgeTitle: "Ciencias Naturales • MEN Vigente (Física / Química)",
      icon: "🔬",
      dbKey: "MALLA_TEMATICA_NATURALES",
      themeColor: "emerald",
      btnClass: "bg-emerald-600 hover:bg-emerald-700 text-white",
      activeTabClass: "bg-emerald-600 text-white shadow-xs",
      borderAccent: "border-emerald-300",
      bgGradient: "from-emerald-500/10 via-teal-500/10 to-cyan-500/10",
      hoverBorder: "hover:border-emerald-400"
    }
  };

  function getSubjectDb(subject) {
    const cfg = MATRIX_SUBJECT_CONFIG[subject];
    if (!cfg) return null;
    return (typeof window !== 'undefined' && window[cfg.dbKey]) ? window[cfg.dbKey] : null;
  }

  // =========================================================================
  // FUNCIÓN COPIAR MALLA CURRICULAR AL PORTAPAPELES
  // =========================================================================
  window.copiarMallaCurricular = function(subject, grade) {
    const cfg = MATRIX_SUBJECT_CONFIG[subject] || MATRIX_SUBJECT_CONFIG.matematicas;
    const db = getSubjectDb(subject) || {};
    const gradeNum = parseInt(grade);
    const data = db[gradeNum];
    if (!data) return;

    const regime = (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : '3');
    const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';
    const periodos = data[regimeKey] || [];
    const regimeLabel = regime === '4' ? 'Malla de 4 Periodos Académicos' : 'Malla de 3 Periodos Académicos';

    let text = `=========================================================\\n` +
               `ASESORÍAS PEDAGÓGICAS S.A.S. - MALLA TEMÁTICA POR PERIODOS\\n` +
               `Área: ${cfg.name} | ${data.title} (${data.cycle})\\n` +
               `Régimen: ${regimeLabel}\\n` +
               `=========================================================\\n\\n`;

    periodos.forEach(p => {
      text += `📅 ${p.titulo.toUpperCase()}\\n`;
      p.items.forEach((it, idx) => {
        if (it.tipo === 'nucleo') {
          text += `  ${idx + 1}. [Núcleo DBA]: ${it.tema}\\n` +
                  `     ↳ DBA ${it.dba} - Evidencia: "${it.evidencia}"\\n` +
                  `     ↳ ID Oficial: ${it.dba_id}\\n`;
        } else {
          text += `  ${idx + 1}. [Prerrequisito EBC]: ${it.tema}\\n` +
                  `     ↳ Fundamento previo según Estándares Básicos de Competencias (EBC).\\n`;
        }
      });
      text += `\\n`;
    });

    if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        alert(`¡Malla Temática de ${data.title} en ${cfg.name} (${regimeLabel}) copiada con éxito al portapapeles!`);
      }).catch(() => {
        alert('Por favor copie el texto manualmente.');
      });
    }
  };

  // =========================================================================
  // 1. RENDERIZADO DE MATRIZ DE UN GRADO: renderMatrix(subject, grade, periodsCount)
  // =========================================================================
  window.renderMatrix = function(subject, grade, periodsCount) {
    const cfg = MATRIX_SUBJECT_CONFIG[subject] || MATRIX_SUBJECT_CONFIG.matematicas;
    const gradeNum = parseInt(grade);
    const db = getSubjectDb(subject) || {};
    const data = db[gradeNum];

    if (!data) {
      return `<div class="p-8 text-center text-slate-400 bg-white rounded-3xl border border-dashed border-slate-300">
        No hay datos de Malla Temática disponibles para este grado en ${cfg.name}.
      </div>`;
    }

    const regime = String(periodsCount || (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : '3'));
    const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';
    const periodos = data[regimeKey] || [];

    const totalNucleos = periodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'nucleo').length, 0);
    const totalPrereqs = periodos.reduce((acc, p) => acc + p.items.filter(x => x.tipo === 'prerrequisito').length, 0);

    return `
      <div class="space-y-6">
        <!-- Banner Informativo Institucional y Selector de Régimen Académico -->
        <div class="bg-gradient-to-r ${cfg.bgGradient} border ${cfg.borderAccent} rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div class="flex items-start sm:items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl ${cfg.btnClass.split(' ')[0]} text-white flex items-center justify-center font-black text-2xl shadow-md shrink-0">
              ${cfg.icon}
            </div>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h3 class="text-base sm:text-lg font-black text-slate-900">Malla Temática por Periodos • ${data.title}</h3>
                <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-white text-slate-800 border border-slate-200 shadow-2xs">
                  ${cfg.badgeTitle}
                </span>
              </div>
              <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
                Organización curricular cronológica por periodos con trazabilidad 1:1 a Núcleos DBA, Evidencias Oficiales y Prerrequisitos EBC.
              </p>
            </div>
          </div>

          <!-- Selector de Régimen Académico (Tabs 3 vs 4 Periodos) y Acciones -->
          <div class="flex flex-wrap items-center gap-2.5 shrink-0">
            <div class="flex items-center bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs">
              <button onclick="setPeriodRegime('3')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${regime === '3' ? cfg.activeTabClass : 'text-slate-600 hover:text-slate-900'}">
                <span>📅</span> <span>3 Periodos</span>
              </button>
              <button onclick="setPeriodRegime('4')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${regime === '4' ? cfg.activeTabClass : 'text-slate-600 hover:text-slate-900'}">
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

            <button onclick="copiarMallaCurricular('${subject}', ${gradeNum})" class="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1.5">
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
              <details open class="group bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden transition-all duration-200 ${cfg.hoverBorder}">
                <summary class="p-4 sm:p-4.5 bg-gradient-to-r from-slate-50 via-slate-50/80 to-white border-b border-slate-100 flex items-center justify-between cursor-pointer select-none">
                  <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-xl ${cfg.btnClass.split(' ')[0]} text-white font-black text-xs sm:text-sm flex items-center justify-center shadow-xs shrink-0">
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

                <!-- Listado Compacto y Subordinado (ul, li con viñetas anidadas) -->
                <div class="p-3 sm:p-4 bg-white">
                  <ul class="divide-y divide-slate-100">
                    ${p.items.map(it => {
                      if (it.tipo === 'nucleo') {
                        return `
                          <li class="py-1.5">
                            <details class="group/item rounded-xl border border-transparent hover:border-slate-200 hover:bg-slate-50/70 p-2 sm:p-2.5 transition">
                              <summary class="flex items-center justify-between gap-3 cursor-pointer select-none list-none">
                                <div class="flex items-center gap-2.5 flex-wrap flex-1">
                                  <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded-lg bg-amber-100 text-amber-900 border border-amber-300 shrink-0 flex items-center gap-1 shadow-2xs">
                                    <span>🎯</span> Núcleo DBA
                                  </span>
                                  <span class="px-2 py-0.5 text-[10px] font-black rounded-lg bg-indigo-100 text-indigo-900 border border-indigo-200 shrink-0">
                                    DBA ${it.dba}
                                  </span>
                                  <span class="text-xs sm:text-sm font-bold text-slate-800 group-hover/item:text-slate-950 transition leading-snug">
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

                              <!-- Despliegue Subordinado con Sangría y Evidencia Exacta -->
                              <div class="mt-2.5 pt-2.5 border-t border-slate-200/60 pl-3 pr-1 space-y-2">
                                <div class="p-3 rounded-xl bg-slate-50/90 border border-slate-200/80 text-xs space-y-1.5 leading-relaxed">
                                  <div class="flex items-start gap-1.5 text-slate-800">
                                    <span class="text-amber-600 font-black not-italic shrink-0">↳</span>
                                    <div>
                                      <strong class="text-slate-900">Alineación Oficial MEN:</strong>
                                      <span class="text-indigo-700 font-bold ml-1">DBA ${it.dba}</span>
                                    </div>
                                  </div>
                                  <div class="flex items-start gap-1.5 text-slate-600 pl-4 italic">
                                    <span>Evidencia de Aprendizaje: "${it.evidencia}"</span>
                                  </div>
                                </div>
                                <div class="flex items-center justify-between gap-2 pt-1">
                                  <span class="text-[10px] font-bold text-slate-400">${cfg.name} • MEN Colombia</span>
                                  <button onclick="openDbaModal('${it.dba_id}')" class="px-3 py-1.5 bg-slate-900 hover:bg-indigo-600 text-white font-black text-xs rounded-xl shadow-xs transition flex items-center gap-1.5 cursor-pointer">
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
                              <div class="mt-2.5 pt-2.5 border-t border-emerald-200/60 pl-3 pr-1 space-y-1">
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
  };

  // =========================================================================
  // 2. RENDERIZADO DE MATRIZ DE TODOS LOS GRADOS: renderAllGradesMatrix(subject, periodsCount)
  // =========================================================================
  window.renderAllGradesMatrix = function(subject, periodsCount) {
    const cfg = MATRIX_SUBJECT_CONFIG[subject] || MATRIX_SUBJECT_CONFIG.matematicas;
    const db = getSubjectDb(subject) || {};
    const wrapper = document.createElement('div');
    wrapper.className = "space-y-6";

    const regime = String(periodsCount || (typeof window !== 'undefined' && window.currentPeriodRegime ? window.currentPeriodRegime : '3'));
    const regimeKey = regime === '4' ? 'periodos4' : 'periodos3';
    let filterTerm = (typeof window !== 'undefined' && window.currentSearch) ? window.currentSearch.toLowerCase() : '';

    const gradesMeta = (typeof window !== 'undefined' && window.GRADES_METADATA) ? window.GRADES_METADATA : [
      { grade: 1, title: "Grado 1°", cycle: "Ciclo I", bgGradient: "from-emerald-600 via-teal-700 to-emerald-950" },
      { grade: 2, title: "Grado 2°", cycle: "Ciclo I", bgGradient: "from-indigo-600 via-sky-700 to-indigo-950" },
      { grade: 3, title: "Grado 3°", cycle: "Ciclo I", bgGradient: "from-sky-600 via-cyan-700 to-blue-950" },
      { grade: 4, title: "Grado 4°", cycle: "Ciclo II", bgGradient: "from-purple-600 via-violet-700 to-indigo-950" },
      { grade: 5, title: "Grado 5°", cycle: "Ciclo II", bgGradient: "from-amber-600 via-orange-600 to-amber-950" },
      { grade: 6, title: "Grado 6°", cycle: "Ciclo III", bgGradient: "from-blue-600 via-indigo-800 to-slate-950" },
      { grade: 7, title: "Grado 7°", cycle: "Ciclo III", bgGradient: "from-teal-600 via-emerald-800 to-teal-950" },
      { grade: 8, title: "Grado 8°", cycle: "Ciclo IV", bgGradient: "from-purple-700 via-fuchsia-800 to-slate-950" },
      { grade: 9, title: "Grado 9°", cycle: "Ciclo IV", bgGradient: "from-blue-700 via-sky-800 to-indigo-950" },
      { grade: 10, title: "Grado 10°", cycle: "Ciclo V", bgGradient: "from-emerald-700 via-teal-800 to-slate-950" },
      { grade: 11, title: "Grado 11°", cycle: "Ciclo V", bgGradient: "from-indigo-900 via-purple-950 to-slate-950" }
    ];

    wrapper.innerHTML = `
      <div class="bg-gradient-to-r ${cfg.bgGradient} border ${cfg.borderAccent} rounded-3xl p-5 sm:p-6 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="flex items-start sm:items-center gap-3.5">
          <div class="w-12 h-12 rounded-2xl ${cfg.btnClass.split(' ')[0]} text-white flex items-center justify-center font-black text-2xl shadow-md shrink-0">
            ${cfg.icon}
          </div>
          <div>
            <div class="flex items-center gap-2 flex-wrap">
              <h2 class="text-lg sm:text-xl font-black text-slate-900">Malla Temática Extendida por Periodos • ${cfg.name} (1° a 11°)</h2>
              <span class="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-white text-slate-800 border border-slate-200 shadow-2xs">
                ${cfg.badgeTitle}
              </span>
            </div>
            <p class="text-xs text-slate-600 mt-1 leading-relaxed max-w-2xl">
              Matriz curricular organizada cronológicamente por periodos académicos con trazabilidad 1:1 a Núcleos DBA, Evidencias Oficiales y Prerrequisitos EBC.
            </p>
          </div>
        </div>
        <div class="flex flex-wrap items-center gap-2 shrink-0">
          <div class="flex items-center bg-white p-1 rounded-2xl border border-slate-200 shadow-2xs">
            <button onclick="setPeriodRegime('3')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${regime === '3' ? cfg.activeTabClass : 'text-slate-600 hover:text-slate-900'}">
              <span>📅</span> <span>3 Periodos</span>
            </button>
            <button onclick="setPeriodRegime('4')" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition cursor-pointer flex items-center gap-1.5 ${regime === '4' ? cfg.activeTabClass : 'text-slate-600 hover:text-slate-900'}">
              <span>📅</span> <span>4 Periodos</span>
            </button>
          </div>
          <button onclick="setCurricularModule('dbas')" class="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-black text-xs transition cursor-pointer flex items-center gap-1.5 shadow-2xs">
            <span>📋</span> <span>Ver Catálogo DBAs</span>
          </button>
        </div>
      </div>

      <!-- Selector rápido de grados para la Malla -->
      <div class="flex items-center gap-2 overflow-x-auto pb-2 custom-scrollbar">
        <span class="text-xs font-bold text-slate-500 whitespace-nowrap">Ir al Grado:</span>
        ${gradesMeta.map(g => `
          <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3 py-1.5 rounded-xl bg-white hover:${cfg.btnClass.split(' ')[0]} hover:text-white border border-slate-200 text-slate-700 font-black text-xs transition cursor-pointer shadow-2xs whitespace-nowrap">
            ${g.grade}°
          </button>
        `).join('')}
      </div>

      <!-- Lista de los 11 Grados con Acordeón por Periodo -->
      <div class="space-y-6">
        ${gradesMeta.map(g => {
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
              return Object.assign({}, p, { items: fItems });
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
                      <h3 class="text-base font-black text-slate-900">${g.title} • ${cfg.name}</h3>
                      <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">${g.cycle}</span>
                    </div>
                    <p class="text-xs text-slate-500 font-medium">${totalNucleos} Núcleos DBA • ${totalPrereqs} Prerrequisitos EBC (${regime} Periodos)</p>
                  </div>
                </div>
                <div class="flex items-center gap-2">
                  <button onclick="copiarMallaCurricular('${subject}', ${g.grade})" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition cursor-pointer flex items-center gap-1 shadow-2xs">
                    <span>📋</span> <span>Copiar</span>
                  </button>
                  <button onclick="seleccionarGradoMallaTematica(${g.grade})" class="px-3.5 py-1.5 rounded-xl ${cfg.btnClass} font-black text-xs transition cursor-pointer shadow-xs flex items-center gap-1">
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
                        <span class="w-7 h-7 rounded-lg ${cfg.btnClass.split(' ')[0]} text-white font-black text-xs flex items-center justify-center shadow-2xs">
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
                              <div class="mt-2 pt-2 border-t border-slate-100 text-xs text-slate-600 pl-3 space-y-1">
                                ${it.tipo === 'nucleo' ? `
                                  <p class="italic text-slate-500">↳ <strong>DBA ${it.dba} - Evidencia:</strong> "${it.evidencia}"</p>
                                  <div class="pt-1">
                                    <button onclick="openDbaModal('${it.dba_id}')" class="text-[11px] font-bold text-indigo-600 hover:text-indigo-800 cursor-pointer">Consultar DBA ${it.dba} en Modal →</button>
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

    return wrapper;
  };

})(typeof window !== 'undefined' ? window : global);
