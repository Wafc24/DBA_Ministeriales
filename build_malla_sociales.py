# -*- coding: utf-8 -*-
"""
Generador del Banco de Malla Temática Extendida por Periodos para Ciencias Sociales y Ciudadanas (1° a 11°).
Empresa: Asesorías Pedagógicas S.A.S.
"""
import json

EVIDENCIAS_OFICIALES = {
    1: {
        1: "Utiliza nociones espaciales como arriba, abajo, delante, detrás, izquierda, derecha para ubicarse en el espacio y representar recorridos.",
        2: "Emplea términos temporales como ayer, hoy, mañana, antes, después para secuenciar eventos y cambios en su vida cotidiana.",
        3: "Reconoce que existen diferentes conformaciones familiares y valora la importancia del respeto, el diálogo y el cumplimiento de normas de convivencia.",
        4: "Identifica elementos naturales y construidos de su entorno inmediato (barrio, vereda o corregimiento) y propone acciones para su cuidado."
    },
    2: {
        1: "Ubica el oriente a partir de la salida del sol y utiliza puntos de referencia y planos sencillos para orientarse en su municipio.",
        2: "Reconoce cómo han cambiado los medios de transporte, trabajos y costumbres a través del tiempo en su localidad.",
        3: "Identifica comunidades indígenas, afrodescendientes, raizales, palenqueras y campesinas, reconociendo la riqueza de la diversidad étnica y cultural.",
        4: "Reconoce las funciones del Alcalde y del Concejo Municipal, así como la importancia del personero y el gobierno escolar."
    },
    3: {
        1: "Ubica los límites territoriales y los municipios del departamento, describiendo sus principales formas de relieve y fuentes hidrográficas.",
        2: "Distingue actividades del sector primario, secundario y terciario presentes en la economía de su departamento y municipio.",
        3: "Describe técnicas agrícolas, orfebrería y alfarería de los pueblos indígenas prehispánicos que habitaron el territorio departamental.",
        4: "Diferencia monumentos, tradiciones orales y leyendas que conforman el patrimonio cultural material e inmaterial de su región."
    },
    4: {
        1: "Localiza en el mapa las seis regiones naturales de Colombia y explica sus características geográficas, climáticas y culturales.",
        2: "Relaciona los cultivos característicos con los pisos térmicos y analiza la oferta ambiental del territorio colombiano.",
        3: "Describe instituciones virreinales como la Real Audiencia, el Cabildo y el proceso de mestizaje durante el periodo colonial.",
        4: "Distingue las funciones de las Ramas Ejecutiva, Legislativa y Judicial del poder público en Colombia y la protección de los derechos de la niñez."
    },
    5: {
        1: "Explica causas externas e internas de la Independencia de Colombia y las vicisitudes del proyecto de la Gran Colombia.",
        2: "Analiza pirámides poblacionales, factores de migración interna y el fenómeno del desplazamiento forzado en el territorio nacional.",
        3: "Contrasta los idearios del Partido Liberal y Conservador en el siglo XIX y el impacto de las guerras civiles en la consolidación del Estado.",
        4: "Identifica la Acción de Tutela y el Derecho de Petición como mecanismos constitucionales para la exigibilidad y protección de derechos fundamentales."
    },
    6: {
        1: "Explica la teoría del Big Bang, el modelo heliocéntrico y las principales eras geológicas que dieron origen a la Tierra.",
        2: "Compara el modo de vida nómada de los homínidos primitivos con el sedentarismo agrícola durante la Revolución Neolítica.",
        3: "Analiza la importancia de los ríos Nilo, Tigris y Éufrates en el desarrollo agrícola, social y político de Egipto y Mesopotamia.",
        4: "Examina el origen de la democracia directa en Atenas y la organización republicana del Senado en la Roma clásica."
    },
    7: {
        1: "Describe relaciones de vasallaje, estamentos feudales y la economía agraria en Europa medieval frente a la expansión islámica.",
        2: "Contrasta el teocentrismo medieval con el antropocentrismo renacentista y los adelantos técnicos que impulsaron las exploraciones atlánticas.",
        3: "Examina la catástrofe demográfica indígena provocada por la conquista y las instituciones coloniales de servidumbre en América.",
        4: "Analiza problemáticas ambientales globales como la deforestación, la pérdida de biodiversidad y la sobreexplotación de biomas."
    },
    8: {
        1: "Explica mecanización, éxodo rural, surgimiento del proletariado industrial y la caída del Antiguo Régimen con la Revolución Francesa.",
        2: "Analiza factores desencadenantes de las independencias hispanoamericanas y la construcción de repúblicas criollas.",
        3: "Analiza el Reparto de África en la Conferencia de Berlín y los tratados desiguales de dominación colonial en Asia.",
        4: "Distingue los Derechos Civiles y Políticos (primera generación) frente a las luchas sociales obreras del siglo XIX."
    },
    9: {
        1: "Explica la crisis del Tratado de Versalles, la Gran Depresión de 1929, el ascenso de los totalitarismos y el Holocausto en la Segunda Guerra Mundial.",
        2: "Analiza la confrontación bipolar entre el bloque capitalista y comunista, la carrera armamentista y los procesos de descolonización en el Tercer Mundo.",
        3: "Explica el magnicidio de Jorge Eliécer Gaitán, la época de La Violencia bipartidista, el pacto del Frente Nacional y el surgimiento de guerrillas.",
        4: "Analiza la Doctrina de la Seguridad Nacional, las dictaduras cívico-militares en el Cono Sur y los procesos de Memoria Histórica y DDHH."
    },
    10: {
        1: "Contrasta el Estado de Bienestar keynesiano con el Consenso de Washington y evalúa el impacto de la desigualdad económica global.",
        2: "Analiza el papel del FMI, Banco Mundial y OMC en la apertura económica, así como disputas geopolíticas por recursos hidrocarburíferos y agua.",
        3: "Explica la irrupción de carteles del narcotráfico, la expansión paramilitar, el despojo violento de tierras y el impacto en las víctimas en Colombia.",
        4: "Explica la supremacía constitucional del Estado Social de Derecho, los Derechos Económicos, Sociales y Culturales (DESC) y la jurisprudencia de tutela."
    },
    11: {
        1: "Analiza tensiones geopolíticas entre potencias emergentes, la crisis global de refugiados, migraciones forzadas y el cambio climático.",
        2: "Examina el Sistema Integral para la Paz (JEP, Comisión de la Verdad, UBPD), garantías de no repetición y reconciliación nacional en Colombia.",
        3: "Evalúa alternativas de decisión pública analizando dilemas morales, multiperspectivismo y colisión entre derechos fundamentales.",
        4: "Diseña veedurías ciudadanas, mecanismos de participación democrática y promueve una cultura de paz y ciudadanía activa global."
    }
}

MALLA_SOCIALES = {
    1: {
        "grade": 1,
        "title": "Grado 1°",
        "cycle": "Ciclo I",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Espacio y Entorno)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Orientación espacial y trayectorias.",
                        "dba": 1,
                        "dba_id": "SOC_G1_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[1][1]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Nociones de geografía física (mi casa, mi colegio).",
                        "origen": "EBC"
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Tiempo e Historia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Noción de tiempo (pasado, presente, futuro).",
                        "dba": 2,
                        "dba_id": "SOC_G1_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[1][2]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Mi entorno inmediato (barrio/vereda).",
                        "dba": 4,
                        "dba_id": "SOC_G1_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[1][4]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica y Convivencia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Tipos de familias y normas.",
                        "dba": 3,
                        "dba_id": "SOC_G1_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[1][3]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Orientación Espacial)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Orientación espacial.",
                        "dba": 1,
                        "dba_id": "SOC_G1_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[1][1]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Geografía de mi colegio.",
                        "origen": "EBC"
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Noción Temporal)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Noción de tiempo.",
                        "dba": 2,
                        "dba_id": "SOC_G1_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[1][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Familia y Convivencia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Tipos de familias y normas.",
                        "dba": 3,
                        "dba_id": "SOC_G1_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[1][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Entorno Comunitario)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Mi entorno inmediato.",
                        "dba": 4,
                        "dba_id": "SOC_G1_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[1][4]
                    }
                ]
            }
        ]
    },
    2: {
        "grade": 2,
        "title": "Grado 2°",
        "cycle": "Ciclo I",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Espacio)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Puntos cardinales y mapas.",
                        "dba": 1,
                        "dba_id": "SOC_G2_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[2][1]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Formas de relieve básico.",
                        "origen": "EBC"
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia/Cultura)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Cambios en el tiempo (transporte, trabajo).",
                        "dba": 2,
                        "dba_id": "SOC_G2_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[2][2]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Diversidad étnica comunitaria.",
                        "dba": 3,
                        "dba_id": "SOC_G2_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[2][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Autoridades y gobierno escolar.",
                        "dba": 4,
                        "dba_id": "SOC_G2_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[2][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Espacio y Orientación)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Puntos cardinales y mapas.",
                        "dba": 1,
                        "dba_id": "SOC_G2_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[2][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Evolución y Cambios)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Cambios en el tiempo.",
                        "dba": 2,
                        "dba_id": "SOC_G2_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[2][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Identidad y Etnicidad)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Diversidad étnica comunitaria.",
                        "dba": 3,
                        "dba_id": "SOC_G2_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[2][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Cívica e Institucionalidad)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Autoridades y gobierno escolar.",
                        "dba": 4,
                        "dba_id": "SOC_G2_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[2][4]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Símbolos patrios.",
                        "origen": "EBC"
                    }
                ]
            }
        ]
    },
    3: {
        "grade": 3,
        "title": "Grado 3°",
        "cycle": "Ciclo II",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geografía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Relieve, hidrografía y límites del departamento.",
                        "dba": 1,
                        "dba_id": "SOC_G3_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[3][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Sectores de la economía departamental.",
                        "dba": 2,
                        "dba_id": "SOC_G3_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[3][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Legado indígena prehispánico.",
                        "dba": 3,
                        "dba_id": "SOC_G3_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[3][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Funciones de autoridades y patrimonio cultural.",
                        "dba": 4,
                        "dba_id": "SOC_G3_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[3][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geografía Departamental)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Relieve e hidrografía departamental.",
                        "dba": 1,
                        "dba_id": "SOC_G3_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[3][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Economía Regional)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Sectores de la economía.",
                        "dba": 2,
                        "dba_id": "SOC_G3_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[3][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Historia Ancestral)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Legado indígena prehispánico.",
                        "dba": 3,
                        "dba_id": "SOC_G3_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[3][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Cívica y Ciudadanía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Autoridades y patrimonio.",
                        "dba": 4,
                        "dba_id": "SOC_G3_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[3][4]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Derechos y deberes infantiles.",
                        "origen": "EBC"
                    }
                ]
            }
        ]
    },
    4: {
        "grade": 4,
        "title": "Grado 4°",
        "cycle": "Ciclo II",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geografía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Regiones naturales de Colombia.",
                        "dba": 1,
                        "dba_id": "SOC_G4_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[4][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Pisos térmicos y producción agrícola.",
                        "dba": 2,
                        "dba_id": "SOC_G4_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[4][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Instituciones coloniales y mestizaje.",
                        "dba": 3,
                        "dba_id": "SOC_G4_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[4][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Ramas del Poder Público y niñez.",
                        "dba": 4,
                        "dba_id": "SOC_G4_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[4][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Regiones de Colombia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Regiones naturales de Colombia.",
                        "dba": 1,
                        "dba_id": "SOC_G4_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[4][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Geografía y Economía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Pisos térmicos.",
                        "dba": 2,
                        "dba_id": "SOC_G4_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[4][2]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Sectores económicos nacionales.",
                        "origen": "EBC"
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Historia Colonial)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Época Colonial y mestizaje.",
                        "dba": 3,
                        "dba_id": "SOC_G4_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[4][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Estado Colombiano)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Ramas del Poder Público.",
                        "dba": 4,
                        "dba_id": "SOC_G4_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[4][4]
                    }
                ]
            }
        ]
    },
    5: {
        "grade": 5,
        "title": "Grado 5°",
        "cycle": "Ciclo II",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Historia S.XIX)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Independencia y Gran Colombia.",
                        "dba": 1,
                        "dba_id": "SOC_G5_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[5][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Bipartidismo y guerras civiles.",
                        "dba": 3,
                        "dba_id": "SOC_G5_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[5][3]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Geografía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Demografía, migraciones y desplazamiento.",
                        "dba": 2,
                        "dba_id": "SOC_G5_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[5][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Constitución de 1991 y mecanismos de protección.",
                        "dba": 4,
                        "dba_id": "SOC_G5_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[5][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Independencia y República)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Independencia y Gran Colombia.",
                        "dba": 1,
                        "dba_id": "SOC_G5_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[5][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Siglo XIX y Partidos Políticos)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Bipartidismo y guerras del siglo XIX.",
                        "dba": 3,
                        "dba_id": "SOC_G5_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[5][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Geografía Humana)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Demografía y desplazamiento.",
                        "dba": 2,
                        "dba_id": "SOC_G5_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[5][2]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Constitución y Derechos)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Constitución 1991.",
                        "dba": 4,
                        "dba_id": "SOC_G5_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[5][4]
                    },
                    {
                        "tipo": "prerrequisito",
                        "tema": "Ramas de control (Procuraduría, Contraloría).",
                        "origen": "EBC"
                    }
                ]
            }
        ]
    },
    6: {
        "grade": 6,
        "title": "Grado 6°",
        "cycle": "Ciclo III",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geografía/Origen)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Origen del universo y eras geológicas.",
                        "dba": 1,
                        "dba_id": "SOC_G6_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[6][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Proceso de hominización y Neolítico.",
                        "dba": 2,
                        "dba_id": "SOC_G6_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[6][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia Antigua)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Civilizaciones fluviales (Egipto, Mesopotamia).",
                        "dba": 3,
                        "dba_id": "SOC_G6_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[6][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Clásicos y Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Grecia, Roma y legado político.",
                        "dba": 4,
                        "dba_id": "SOC_G6_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[6][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Cosmología y Geología)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Universo, Tierra y eras geológicas.",
                        "dba": 1,
                        "dba_id": "SOC_G6_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[6][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Hominización y Prehistoria)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Hominización y Neolítico.",
                        "dba": 2,
                        "dba_id": "SOC_G6_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[6][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Primeras Civilizaciones)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Civilizaciones fluviales de Asia y África.",
                        "dba": 3,
                        "dba_id": "SOC_G6_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[6][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Mundo Clásico Greco-Romano)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Grecia y Roma clásica.",
                        "dba": 4,
                        "dba_id": "SOC_G6_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[6][4]
                    }
                ]
            }
        ]
    },
    7: {
        "grade": 7,
        "title": "Grado 7°",
        "cycle": "Ciclo III",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Historia Medieval)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Feudalismo e Imperio Islámico.",
                        "dba": 1,
                        "dba_id": "SOC_G7_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[7][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Renacimiento y exploraciones.",
                        "dba": 2,
                        "dba_id": "SOC_G7_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[7][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia Americana)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Conquista y colonia de América.",
                        "dba": 3,
                        "dba_id": "SOC_G7_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[7][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Geografía y Ambiente)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Biomas y recursos naturales.",
                        "dba": 4,
                        "dba_id": "SOC_G7_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[7][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Medioevo y Mundo Islámico)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Edad Media y Mundo Islámico.",
                        "dba": 1,
                        "dba_id": "SOC_G7_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[7][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Renacimiento y Ultramar)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Renacimiento y expansiones europeas.",
                        "dba": 2,
                        "dba_id": "SOC_G7_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[7][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Invasión y Virreinatos)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Invasión y Conquista de América.",
                        "dba": 3,
                        "dba_id": "SOC_G7_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[7][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Ecología y Biomas)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Biomas mundiales y explotación.",
                        "dba": 4,
                        "dba_id": "SOC_G7_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[7][4]
                    }
                ]
            }
        ]
    },
    8: {
        "grade": 8,
        "title": "Grado 8°",
        "cycle": "Ciclo IV",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Revoluciones)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Revoluciones Industriales y Francesa.",
                        "dba": 1,
                        "dba_id": "SOC_G8_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[8][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia de América)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Independencia latinoamericana y Estados Nacionales.",
                        "dba": 2,
                        "dba_id": "SOC_G8_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[8][2]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Imperialismo y colonialismo en África/Asia.",
                        "dba": 3,
                        "dba_id": "SOC_G8_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[8][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Evolución de los Derechos Humanos.",
                        "dba": 4,
                        "dba_id": "SOC_G8_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[8][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (La Era de las Revoluciones)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Revolución Industrial y Francesa.",
                        "dba": 1,
                        "dba_id": "SOC_G8_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[8][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Independencias en América)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Independencias de América Latina.",
                        "dba": 2,
                        "dba_id": "SOC_G8_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[8][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Imperialismo Global)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Imperialismo europeo en el mundo.",
                        "dba": 3,
                        "dba_id": "SOC_G8_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[8][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Derechos Humanos y Ciudadanía)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Historia de los Derechos Humanos.",
                        "dba": 4,
                        "dba_id": "SOC_G8_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[8][4]
                    }
                ]
            }
        ]
    },
    9: {
        "grade": 9,
        "title": "Grado 9°",
        "cycle": "Ciclo IV",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Guerras Mundiales)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "I y II Guerra Mundial, Totalitarismos.",
                        "dba": 1,
                        "dba_id": "SOC_G9_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[9][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Guerra Fría y descolonización.",
                        "dba": 2,
                        "dba_id": "SOC_G9_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[9][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Historia de Colombia S.XX)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "La Violencia, Frente Nacional y guerrillas.",
                        "dba": 3,
                        "dba_id": "SOC_G9_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[9][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica Cono Sur)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Dictaduras en el Cono Sur y Memoria Histórica.",
                        "dba": 4,
                        "dba_id": "SOC_G9_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[9][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Conflictos Bélicos Mundiales)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Guerras Mundiales y Totalitarismos.",
                        "dba": 1,
                        "dba_id": "SOC_G9_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[9][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Mundo Bipolar)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Guerra Fría y Descolonización.",
                        "dba": 2,
                        "dba_id": "SOC_G9_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[9][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Colombia en el Siglo XX)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Historia de Colombia S.XX.",
                        "dba": 3,
                        "dba_id": "SOC_G9_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[9][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Autoritarismos y Memoria)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Dictaduras latinoamericanas y DDHH.",
                        "dba": 4,
                        "dba_id": "SOC_G9_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[9][4]
                    }
                ]
            }
        ]
    },
    10: {
        "grade": 10,
        "title": "Grado 10°",
        "cycle": "Ciclo V (Media)",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Economía y Globalización)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Modelos macroeconómicos y desigualdad.",
                        "dba": 1,
                        "dba_id": "SOC_G10_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[10][1]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Globalización y recursos estratégicos.",
                        "dba": 2,
                        "dba_id": "SOC_G10_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[10][2]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Conflicto en Colombia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Narcotráfico, paramilitarismo y víctimas.",
                        "dba": 3,
                        "dba_id": "SOC_G10_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[10][3]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Cívica y Estado)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Estado Social de Derecho y DESC.",
                        "dba": 4,
                        "dba_id": "SOC_G10_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[10][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Sistemas Macroeconómicos)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Modelos macroeconómicos.",
                        "dba": 1,
                        "dba_id": "SOC_G10_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[10][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Geopolítica de Recursos)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Geopolítica y Globalización.",
                        "dba": 2,
                        "dba_id": "SOC_G10_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[10][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Conflicto y Realidad Social)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Conflicto Armado Colombiano reciente.",
                        "dba": 3,
                        "dba_id": "SOC_G10_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[10][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Constitución y Justicia)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Estado Social de Derecho y Tutela.",
                        "dba": 4,
                        "dba_id": "SOC_G10_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[10][4]
                    }
                ]
            }
        ]
    },
    11: {
        "grade": 11,
        "title": "Grado 11°",
        "cycle": "Ciclo V (Media)",
        "periodos3": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geopolítica)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Multipolaridad, clima y migración.",
                        "dba": 1,
                        "dba_id": "SOC_G11_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[11][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Paz y Transición)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Acuerdos de Paz y Justicia Transicional (JEP).",
                        "dba": 2,
                        "dba_id": "SOC_G11_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[11][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Saber 11 Ciudadanas)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Pensamiento sistémico y dilemas sociales.",
                        "dba": 3,
                        "dba_id": "SOC_G11_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[11][3]
                    },
                    {
                        "tipo": "nucleo",
                        "tema": "Control social y ciudadanía global.",
                        "dba": 4,
                        "dba_id": "SOC_G11_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[11][4]
                    }
                ]
            }
        ],
        "periodos4": [
            {
                "periodo": 1,
                "titulo": "Periodo 1 (Geopolítica Contemporánea)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Geopolítica mundial contemporánea.",
                        "dba": 1,
                        "dba_id": "SOC_G11_DBA1",
                        "evidencia": EVIDENCIAS_OFICIALES[11][1]
                    }
                ]
            },
            {
                "periodo": 2,
                "titulo": "Periodo 2 (Paz y Justicia Transicional)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Acuerdos de Paz y JEP en Colombia.",
                        "dba": 2,
                        "dba_id": "SOC_G11_DBA2",
                        "evidencia": EVIDENCIAS_OFICIALES[11][2]
                    }
                ]
            },
            {
                "periodo": 3,
                "titulo": "Periodo 3 (Multiperspectivismo y Saber 11)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Pensamiento sistémico y multiperspectivismo.",
                        "dba": 3,
                        "dba_id": "SOC_G11_DBA3",
                        "evidencia": EVIDENCIAS_OFICIALES[11][3]
                    }
                ]
            },
            {
                "periodo": 4,
                "titulo": "Periodo 4 (Participación Democrática)",
                "items": [
                    {
                        "tipo": "nucleo",
                        "tema": "Control social y mecanismos democráticos.",
                        "dba": 4,
                        "dba_id": "SOC_G11_DBA4",
                        "evidencia": EVIDENCIAS_OFICIALES[11][4]
                    }
                ]
            }
        ]
    }
}

js_content = "/**\n * BANCO DE MALLA TEMÁTICA EXTENDIDA POR PERIODOS - CIENCIAS SOCIALES Y CIUDADANAS 1° A 11°\n * Asesorías Pedagógicas S.A.S.\n * Trazabilidad curricular exacta: Mapeo de Periodos Académicos (3 y 4 periodos), Núcleos DBA y Prerrequisitos EBC.\n */\n"
js_content += "window.MALLA_TEMATICA_SOCIALES = " + json.dumps(MALLA_SOCIALES, ensure_ascii=False, indent=2) + ";\n"

with open("malla_sociales_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("malla_sociales_data.js generado con éxito!")
