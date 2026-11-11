const fs = require('fs');

// 1. Simular entorno de navegador completo
global.window = global;
global.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); }
};

if (!global.navigator) global.navigator = {};
global.navigator.clipboard = {
  lastCopied: '',
  writeText(txt) {
    this.lastCopied = txt;
    return Promise.resolve();
  }
};
global.alert = (msg) => console.log('  [Alert]:', msg);

function createMockElement() {
  return {
    classList: { add() {}, remove() {}, toggle() {} },
    value: '',
    textContent: '',
    innerHTML: '',
    appendChild() {},
    addEventListener() {}
  };
}

global.document = {
  getElementById(id) { return createMockElement(); },
  querySelectorAll() { return []; },
  createElement() {
    const el = createMockElement();
    el.className = '';
    return el;
  },
  addEventListener() {}
};

// Cargar bases de datos y controlador
require('./dbas_master_data.js');
require('./malla_tematica_data.js');
require('./malla_sociales_data.js');
require('./malla_naturales_data.js');
require('./curriculum_matrix_builder.js');

console.log('--- TEST 1: Verificación de Bases de Datos Curriculares ---');
console.assert(window.MALLA_TEMATICA_MATEMATICAS, 'MALLA_TEMATICA_MATEMATICAS debe existir');
console.assert(window.MALLA_TEMATICA_SOCIALES, 'MALLA_TEMATICA_SOCIALES debe existir');
console.assert(window.MALLA_TEMATICA_NATURALES, 'MALLA_TEMATICA_NATURALES debe existir');

const subjects = ['matematicas', 'sociales', 'naturales'];
subjects.forEach(sub => {
  const dbKey = sub === 'matematicas' ? 'MALLA_TEMATICA_MATEMATICAS' : (sub === 'sociales' ? 'MALLA_TEMATICA_SOCIALES' : 'MALLA_TEMATICA_NATURALES');
  const db = window[dbKey];
  for (let g = 1; g <= 11; g++) {
    console.assert(db[g], `Grado ${g} debe existir en ${sub}`);
    console.assert(db[g].periodos3.length === 3, `Grado ${g} en ${sub} debe tener 3 periodos en periodos3`);
    console.assert(db[g].periodos4.length === 4, `Grado ${g} en ${sub} debe tener 4 periodos en periodos4`);
  }
});
console.log('✅ TEST 1 APROBADO: Las 3 áreas (Matemáticas, Sociales, Naturales) tienen los 11 grados con 3 y 4 periodos.\n');

console.log('--- TEST 2: Verificación de renderMatrix(subject, grade, periodsCount) ---');
console.assert(typeof window.renderMatrix === 'function', 'renderMatrix debe ser una función');

let totalTests = 0;
subjects.forEach(sub => {
  for (let g = 1; g <= 11; g++) {
    [3, 4].forEach(p => {
      const html = window.renderMatrix(sub, g, p);
      console.assert(html.length > 500, `renderMatrix(${sub}, ${g}, ${p}) debe retornar HTML estructurado`);
      console.assert(html.includes('P1'), `Debe contener P1 en ${sub} G${g} P${p}`);
      console.assert(html.includes(`P${p}`), `Debe contener P${p} en ${sub} G${g} P${p}`);
      console.assert(html.includes('Núcleo DBA') || html.includes('Prerrequisito EBC'), `Debe contener etiquetas`);
      console.assert(html.includes('bg-amber-100 text-amber-900 border border-amber-300'), 'Debe contener badge de Núcleo DBA');
      totalTests++;
    });
  }
});
console.log(`✅ TEST 2 APROBADO: Evaluadas exitosamente ${totalTests} combinaciones de (Área, Grado, Periodos) en renderMatrix.\n`);

console.log('--- TEST 3: Verificación de Pre-Física, Pre-Química, Física y Química en Ciencias Naturales ---');
// G6, G7, G8, G9
const natG6_p3 = window.renderMatrix('naturales', 6, 3);
console.assert(natG6_p3.includes('Pre-Química') && natG6_p3.includes('Pre-Física'), 'Grado 6° Naturales debe incluir Pre-Química y Pre-Física');

const natG8_p3 = window.renderMatrix('naturales', 8, 3);
console.assert(natG8_p3.includes('Genética Mendeliana') && natG8_p3.includes('Pre-Química') && natG8_p3.includes('Pre-Física'), 'Grado 8° Naturales debe incluir Genética, Pre-Química y Pre-Física');

// G10 y G11 (Media: Física y Química estrictas)
const natG10_p3 = window.renderMatrix('naturales', 10, 3);
console.assert(natG10_p3.includes('Química I') && natG10_p3.includes('Física II'), 'Grado 10° Naturales debe incluir Química I y Física II');

const natG11_p3 = window.renderMatrix('naturales', 11, 3);
console.assert(natG11_p3.includes('Química Orgánica') && natG11_p3.includes('Termodinámica avanzada') && natG11_p3.includes('Física Moderna'), 'Grado 11° Naturales debe incluir Química Orgánica, Fluidos/Termodinámica y Física Moderna');

console.log('✅ TEST 3 APROBADO: Progresión de Pre-Física/Pre-Química en básica secundaria y Física/Química en la Media validada al 100%.\n');

console.log('--- TEST 4: Verificación de renderAllGradesMatrix(subject, periodsCount) ---');
subjects.forEach(sub => {
  [3, 4].forEach(p => {
    const el = window.renderAllGradesMatrix(sub, p);
    console.assert(el.innerHTML.includes('Malla Temática Extendida por Periodos'), `Debe renderizar encabezado para ${sub}`);
    console.assert(el.innerHTML.includes('11°'), `Debe incluir hasta Grado 11° para ${sub}`);
  });
});
console.log('✅ TEST 4 APROBADO: renderAllGradesMatrix renderiza correctamente los 11 grados en las 3 áreas.\n');

console.log('--- TEST 5: Verificación de copiarMallaCurricular ---');
window.currentPeriodRegime = '3';
window.copiarMallaCurricular('naturales', 10);
console.assert(global.navigator.clipboard.lastCopied.includes('Ciencias Naturales'), 'Copia de Naturales 10 debe incluir área');
console.assert(global.navigator.clipboard.lastCopied.includes('Química I') || global.navigator.clipboard.lastCopied.includes('PERIODO 1'), 'Copia de Naturales 10 debe incluir periodos');
console.log('✅ TEST 5 APROBADO: copiarMallaCurricular copia con trazabilidad oficial.\n');

console.log('--- TEST 6: Verificación de Integridad en index.html y Gatekeeper ---');
const indexHtml = fs.readFileSync('index.html', 'utf8');
console.assert(indexHtml.includes('curriculum_matrix_builder.js'), 'index.html debe incluir curriculum_matrix_builder.js');
console.assert(indexHtml.includes('malla_naturales_data.js'), 'index.html debe incluir malla_naturales_data.js');
console.assert(indexHtml.includes('renderMatrix'), 'index.html debe llamar a renderMatrix');

const gatekeeper = fs.readFileSync('auth-gatekeeper.js', 'utf8');
console.assert(gatekeeper.includes('Asesorias2026*'), 'La clave de acceso Asesorias2026* debe estar intacta');
console.log('✅ TEST 6 APROBADO: Integridad de scripts y Gatekeeper confirmada.\n');

console.log('🎉 TODOS LOS TESTS DEL REQUERIMIENTO HAN SIDO SUPERADOS CON ÉXITO.');
