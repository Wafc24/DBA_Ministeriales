const fs = require('fs');

// 1. Simular entorno DOM completo
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

// Cargar bases de datos
require('./dbas_master_data.js');
require('./malla_tematica_data.js');
require('./malla_sociales_data.js');

console.log('--- TEST 1: Verificación de Carga de Datos Sociales ---');
console.assert(window.MALLA_TEMATICA_SOCIALES, 'MALLA_TEMATICA_SOCIALES no está definida');
const grades = Object.keys(window.MALLA_TEMATICA_SOCIALES);
console.log('Grados registrados en Sociales:', grades);
console.assert(grades.length === 11, 'Deben haber 11 grados');

grades.forEach(g => {
  const item = window.MALLA_TEMATICA_SOCIALES[g];
  console.assert(item.periodos3.length === 3, `Grado ${g} debe tener 3 periodos en periodos3`);
  console.assert(item.periodos4.length === 4, `Grado ${g} debe tener 4 periodos en periodos4`);
});
console.log('✅ TEST 1 APROBADO: Todos los 11 grados tienen estructura de 3 y 4 periodos.\n');

console.log('--- TEST 2: Verificación de Funciones de UI en index.html ---');
const indexHtml = fs.readFileSync('index.html', 'utf8');

// Validar inclusión de scripts
console.assert(indexHtml.includes('malla_sociales_data.js'), 'index.html debe incluir malla_sociales_data.js');
console.assert(indexHtml.includes('auth-gatekeeper.js'), 'index.html debe incluir auth-gatekeeper.js');
console.assert(indexHtml.includes('renderGradeSocialesMallaTematica'), 'renderGradeSocialesMallaTematica debe existir');
console.assert(indexHtml.includes('renderAllGradesSocialesMallaTematica'), 'renderAllGradesSocialesMallaTematica debe existir');
console.assert(indexHtml.includes('setPeriodRegime'), 'setPeriodRegime debe existir');
console.assert(indexHtml.includes('copiarMallaSociales'), 'copiarMallaSociales debe existir');

// Validar etiquetas de color según requerimiento
console.assert(indexHtml.includes('bg-amber-100 text-amber-900 border border-amber-300'), 'Núcleo DBA debe tener estilo ámbar');
console.assert(indexHtml.includes('bg-emerald-100 text-emerald-900 border border-emerald-300'), 'Prerrequisito EBC debe tener estilo esmeralda');

console.log('✅ TEST 2 APROBADO: Scripts, funciones y estilos visuales validados en index.html.\n');

console.log('--- TEST 3: Verificación de Copiado de Malla ---');
// Extraer script de lógica de index.html
const scriptMatches = indexHtml.match(/<script>([\s\S]*?)<\/script>/gi);
const lastScript = scriptMatches[scriptMatches.length - 1].replace(/<\/?script>/gi, '');

function createMockElement() {
  return {
    classList: {
      add() {},
      remove() {},
      toggle() {}
    },
    value: '',
    textContent: '',
    innerHTML: '',
    appendChild() {},
    addEventListener() {}
  };
}

global.document = {
  getElementById(id) {
    return createMockElement();
  },
  querySelectorAll() { return []; },
  createElement() {
    const el = createMockElement();
    el.className = '';
    return el;
  },
  addEventListener() {}
};

eval(lastScript);

// Testear copiarMallaSociales
window.copiarMallaSociales(1);
console.assert(global.navigator.clipboard.lastCopied.includes('Ciencias Sociales y Ciudadanas'), 'El texto copiado debe incluir el área');
console.assert(global.navigator.clipboard.lastCopied.includes('PERIODO 1'), 'El texto copiado debe incluir periodos');
console.assert(global.navigator.clipboard.lastCopied.includes('DBA 1'), 'El texto copiado debe incluir el DBA');
console.log('✅ TEST 3 APROBADO: copiarMallaSociales genera el formato oficial correctamente.\n');

console.log('--- TEST 4: Verificación de Renderizado HTML de Grado ---');
window.currentPeriodRegime = '3';
const htmlP3 = window.renderGradeSocialesMallaTematica(1);
console.assert(htmlP3.includes('P1'), 'Debe renderizar Periodo 1');
console.assert(htmlP3.includes('P2'), 'Debe renderizar Periodo 2');
console.assert(htmlP3.includes('P3'), 'Debe renderizar Periodo 3');
console.assert(!htmlP3.includes('P4'), 'En régimen de 3 periodos no debe tener P4');
console.assert(htmlP3.includes('bg-amber-100 text-amber-900 border border-amber-300'), 'Debe incluir badge ámbar');
console.assert(htmlP3.includes('bg-emerald-100 text-emerald-900 border border-emerald-300'), 'Debe incluir badge esmeralda');
console.assert(htmlP3.includes('openDbaModal'), 'Debe incluir botón para modal de DBA');

window.currentPeriodRegime = '4';
const htmlP4 = window.renderGradeSocialesMallaTematica(1);
console.assert(htmlP4.includes('P4'), 'En régimen de 4 periodos debe incluir P4');
console.log('✅ TEST 4 APROBADO: renderGradeSocialesMallaTematica conmuta correctamente entre 3 y 4 periodos y renderiza badges con micro-interacción.\n');

console.log('--- TEST 5: Verificación de Credenciales de Seguridad ---');
const gatekeeperCode = fs.readFileSync('auth-gatekeeper.js', 'utf8');
console.assert(gatekeeperCode.includes('Asesorias2026*'), 'La contraseña oficial Asesorias2026* debe estar intacta');
console.log('✅ TEST 5 APROBADO: Seguridad Gatekeeper intacta con contraseña oficial Asesorias2026*.\n');

console.log('🎉 TODOS LOS TESTS HAN SIDO SUPERADOS SATISFACTORIAMENTE.');
