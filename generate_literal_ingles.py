import json

ingles_dict = {str(i): {} for i in range(1, 12)}

# Grado 1 (doc1 p9)
ingles_dict["1"]["1"] = {
    "statement": "Comprende y responde a instrucciones sobre tareas escolares básicas, de manera verbal y no verbal.",
    "evidencias": [
        "Responde de manera no verbal a instrucciones sobre tareas escolares sencillas (e.g. 'Use red to color the circle').",
        "Sigue instrucciones orales simples dadas por el docente para el desarrollo de actividades en el aula."
    ]
}
ingles_dict["1"]["2"] = {
    "statement": "Organiza la secuencia de eventos principales en una historia corta y sencilla, sobre temas familiares, usando imágenes, después de haberla leído o escuchado.",
    "evidencias": [
        "Ordena secuencias lógicas de historias sencillas apoyándose en ilustraciones visuales.",
        "Identifica el inicio, desarrollo y final de relatos breves adaptados a su nivel."
    ]
}
ingles_dict["1"]["3"] = {
    "statement": "Responde preguntas sencillas sobre información personal básica, como su nombre, edad, familia y compañeros de clase.",
    "evidencias": [
        "Contesta a preguntas personales elementales estructuradas (e.g. 'How old are you? - I am 7 years old').",
        "Reconoce preguntas sobre su identidad formuladas por el docente o compañeros."
    ]
}
ingles_dict["1"]["4"] = {
    "statement": "Comprende y realiza declaraciones sencillas, usando expresiones ensayadas, sobre su entorno inmediato (casa y escuela).",
    "evidencias": [
        "Identifica objetos escolares y de su hogar al escuchar o ver su representación en inglés.",
        "Pronuncia frases cortas modeladas para referirse a cosas que observa a su alrededor."
    ]
}
ingles_dict["1"]["5"] = {
    "statement": "Menciona algunas cualidades físicas propias y de las personas que le rodean a través de palabras y frases previamente ensayadas.",
    "evidencias": [
        "Describe características físicas elementales (e.g. 'My mother has long, black hair').",
        "Asocia vocabulario de rasgos físicos con imágenes y modelos guiados."
    ]
}

# Grado 2 (doc1 p10)
ingles_dict["2"]["1"] = {
    "statement": "Expresa ideas sencillas sobre temas estudiados, usando palabras y frases cortas.",
    "evidencias": [
        "Comunica gustos, habilidades y preferencias básicas modeladas en el aula.",
        "Utiliza estructuras simples aprendidas para interactuar en juegos y actividades escolares."
    ]
}
ingles_dict["2"]["2"] = {
    "statement": "Intercambia información personal como su nombre, edad y procedencia con compañeros y profesores, usando frases sencillas, siguiendo modelos provistos por el docente.",
    "evidencias": [
        "Pregunta y responde sobre el origen geográfico (e.g. 'Where are you from? - I am from Duitama').",
        "Saluda, se presenta y formula preguntas guiadas a sus pares."
    ]
}
ingles_dict["2"]["3"] = {
    "statement": "Menciona aspectos culturales propios de su entorno, usando vocabulario y expresiones conocidas.",
    "evidencias": [
        "Nombra elementos representativos de su región o país usando términos en inglés trabajados en clase.",
        "Reconoce particularidades de su comunidad escolar y local a través de imágenes y expresiones guiadas."
    ]
}
ingles_dict["2"]["4"] = {
    "statement": "Comprende la secuencia de una historia corta y sencilla sobre temas familiares, y la cuenta nuevamente a partir de ilustraciones y palabras conocidas.",
    "evidencias": [
        "Relata eventos breves en orden cronológico apoyándose en tarjetas o diapositivas con dibujos.",
        "Identifica personajes centrales y acciones clave en historias infantiles."
    ]
}

# Grado 3 (doc1 p11)
ingles_dict["3"]["1"] = {
    "statement": "Comprende y describe algunos detalles en textos cortos y sencillos sobre temas familiares, a partir de imágenes y frases conocidas.",
    "evidencias": [
        "Extrae información específica de textos ilustrados elementales.",
        "Asocia frases descriptivas con las representaciones gráficas correspondientes."
    ]
}
ingles_dict["3"]["2"] = {
    "statement": "Responde, de manera oral o escrita, preguntas sencillas sobre textos descriptivos cortos y alusivos a temas conocidos y de clase.",
    "evidencias": [
        "Contesta cuestionarios breves de comprensión literal sobre lecturas guiadas.",
        "Formula respuestas orales concisas ante interrogantes planteados sobre lecturas."
    ]
}
ingles_dict["3"]["3"] = {
    "statement": "Intercambia ideas y opiniones sencillas con compañeros y profesores, siguiendo modelos o a través de imágenes.",
    "evidencias": [
        "Expresa acuerdos y desacuerdos simples ante temas de clase cotidianos.",
        "Participa en diálogos guiados compartiendo preferencias personales."
    ]
}
ingles_dict["3"]["4"] = {
    "statement": "Describe, de manera oral y escrita, objetos, lugares, personas y comunidades, usando oraciones simples.",
    "evidencias": [
        "Escribe oraciones cortas describiendo su vecindario, escuela o familia (e.g. 'This is my neighborhood. There is a park...').",
        "Presenta de forma oral descripciones básicas siguiendo una plantilla estructurada."
    ]
}

# Grado 4 (doc1 p12)
ingles_dict["4"]["1"] = {
    "statement": "Comprende la idea general y algunos detalles en un texto informativo corto y sencillo sobre temas conocidos y de interés.",
    "evidencias": [
        "Identifica el tema central y datos puntuales en tablas informativas y párrafos simples.",
        "Clasifica información relevante de textos sobre naturaleza, animales y vida cotidiana."
    ]
}
ingles_dict["4"]["2"] = {
    "statement": "Intercambia opiniones sencillas sobre un tema de interés, a través de oraciones simples y conocidas.",
    "evidencias": [
        "Emite opiniones breves sobre proyectos y actividades del colegio (e.g. 'It is great / It is important').",
        "Hace preguntas sencillas para conocer la postura de otros compañeros."
    ]
}
ingles_dict["4"]["3"] = {
    "statement": "Compara características básicas de personas, objetos y lugares de su escuela y comunidad, a través de oraciones simples.",
    "evidencias": [
        "Emplea adjetivos comparativos simples para contrastar tamaños, cualidades y lugares (e.g. 'This tree is taller than that one').",
        "Elabora cuadros comparativos orales y escritos guiados."
    ]
}
ingles_dict["4"]["4"] = {
    "statement": "Pregunta y responde, de forma oral o escrita, interrogantes relacionados con el 'quién, cuándo y dónde', después de leer o escuchar un texto corto y sencillo.",
    "evidencias": [
        "Formula preguntas tipo Wh- (Who, When, Where) sobre lecturas o audios trabajados.",
        "Responde con exactitud identificando personajes, tiempos y locaciones en textos."
    ]
}

# Grado 5 (doc1 p13)
ingles_dict["5"]["1"] = {
    "statement": "Comprende información general y específica en un texto narrativo corto sobre temas conocidos y de interés.",
    "evidencias": [
        "Reconoce la trama principal y eventos destacados en una narración breve.",
        "Responde a preguntas de detalle sobre lecturas de relatos culturales o fábulas adaptadas."
    ]
}
ingles_dict["5"]["2"] = {
    "statement": "Produce un texto narrativo oral y/o escrito, corto y sencillo, que responde al '¿qué?, ¿quién?, ¿cuándo? y ¿dónde?' de un evento o anécdota.",
    "evidencias": [
        "Escribe párrafos narrativos breves organizados cronológicamente sobre vivencias personales.",
        "Relata experiencias pasadas siguiendo pautas discursivas simples."
    ]
}
ingles_dict["5"]["3"] = {
    "statement": "Intercambia información sobre hábitos, gustos y preferencias acerca de temas conocidos, siguiendo modelos provistos por el docente.",
    "evidencias": [
        "Entrevista a compañeros acerca de sus rutinas y pasatiempos diarios.",
        "Presenta los resultados de diálogos sobre intereses grupales."
    ]
}
ingles_dict["5"]["4"] = {
    "statement": "Explica causas y consecuencias de una situación a través de oraciones simples de manera oral y escrita siguiendo un modelo establecido.",
    "evidencias": [
        "Utiliza conectores causales básicos como 'because' para justificar afirmaciones.",
        "Establece relaciones sencillas de causa-efecto sobre el cuidado ambiental y la salud."
    ]
}

# Grado 6 (doc2 p15-16)
ingles_dict["6"]["1"] = {
    "statement": "Participa en una conversación corta para decir su nombre, edad y datos básicos a profesores, amigos y familiares.",
    "evidencias": [
        "Brinda información personal básica con pronunciación clara y vocabulario pertinente.",
        "Interactúa con compañeros en situaciones cotidianas de presentación mutua."
    ]
}
ingles_dict["6"]["2"] = {
    "statement": "Solicita y brinda aclaraciones sobre cómo se escriben nombres y palabras desconocidas en una conversación corta.",
    "evidencias": [
        "Deletrea nombres propios y palabras desconocidas en inglés utilizando el alfabeto.",
        "Pide aclaraciones a su interlocutor cuando no comprende una palabra pronunciada."
    ]
}
ingles_dict["6"]["3"] = {
    "statement": "Comprende instrucciones relacionadas con las actividades y tareas de la clase, la escuela y su comunidad y expresa de manera escrita y oral lo que entiende de estas.",
    "evidencias": [
        "Interpreta normas, indicaciones escolares y señales comunitarias formuladas en inglés.",
        "Reformula instrucciones breves para comprobar su adecuada comprensión."
    ]
}
ingles_dict["6"]["4"] = {
    "statement": "Comprende y utiliza palabras familiares y frases cortas sobre rutinas, actividades cotidianas y gustos.",
    "evidencias": [
        "Describe sus actividades diarias y ocupaciones habituales con oraciones simples estructuradas.",
        "Identifica horarios y hábitos en textos orales y escritos sencillos."
    ]
}
ingles_dict["6"]["5"] = {
    "statement": "Describe las características básicas de personas, cosas y lugares de su escuela, ciudad y comunidad, a través de frases y oraciones sencillas.",
    "evidencias": [
        "Elabora descripciones elementales de lugares emblemáticos de su municipio o región.",
        "Nombra atributos físicos, ocupaciones y rasgos de personas de su entorno."
    ]
}
ingles_dict["6"]["6"] = {
    "statement": "Escribe información personal básica en formatos preestablecidos que solicitan datos como nombre, edad, fecha de nacimiento, género, nacionalidad, dirección, teléfono, etc.",
    "evidencias": [
        "Diligencia carnets, fichas de registro y formularios de identificación escolar.",
        "Revisa la ortografía y puntuación correcta de sus datos biográficos."
    ]
}
ingles_dict["6"]["7"] = {
    "statement": "Responde a preguntas relacionadas con el 'qué, quién y cuándo' después de leer o escuchar un texto corto y sencillo, siempre y cuando el tema esté relacionado con eventos que le son familiares.",
    "evidencias": [
        "Localiza datos clave de tiempo, sujetos y eventos en relatos breves y diálogos escolares.",
        "Formula respuestas coherentes a interrogantes sobre textos informativos leídos."
    ]
}
ingles_dict["6"]["8"] = {
    "statement": "Comprende el tema e información general de un texto corto y sencillo, valiéndose de ayudas tales como imágenes, títulos y palabras clave.",
    "evidencias": [
        "Infiere el sentido global de una lectura asociando elementos paratextuales.",
        "Comenta la idea principal de lecturas temáticas con sus pares."
    ]
}

# Grado 7 (doc2 p18-19)
ingles_dict["7"]["1"] = {
    "statement": "Participa en conversaciones cortas en las que brinda información sobre sí mismo, sobre personas, lugares y eventos que le son familiares.",
    "evidencias": [
        "Utiliza frases y oraciones memorizadas para relatar vivencias familiares y locales.",
        "Mantiene el flujo de una conversación breve respondiendo oportunamente a preguntas."
    ]
}
ingles_dict["7"]["2"] = {
    "statement": "Escribe textos cortos y sencillos sobre acciones, experiencias y planes que le son familiares.",
    "evidencias": [
        "Organiza oraciones en párrafos breves con adecuada coherencia temporal.",
        "Emplea vocabulario sobre pasatiempos, planes futuros inmediatos y anécdotas."
    ]
}
ingles_dict["7"]["3"] = {
    "statement": "Describe, de manera oral, personas, actividades, eventos y experiencias personales estructurando estas descripciones con oraciones conectadas.",
    "evidencias": [
        "Presenta monólogos descriptivos cortos sobre su rutina o actividades de tiempo libre.",
        "Articula descripciones usando conectores básicos de secuencia y adición."
    ]
}
ingles_dict["7"]["4"] = {
    "statement": "Reconoce información específica relacionada con objetos, personas y acciones cuando le son conocidos y le hablan de manera clara.",
    "evidencias": [
        "Identifica instrucciones detalladas y recomendaciones orales de fuentes auditivas.",
        "Selecciona información clave en conversaciones cotidianas grabadas o del aula."
    ]
}
ingles_dict["7"]["5"] = {
    "statement": "Describe acciones relacionadas con un tema de su entorno familiar o escolar usando oraciones sencillas y apoyándose en imágenes.",
    "evidencias": [
        "Explica procesos secuenciales paso a paso (recetas sencillas, instrucciones de juegos).",
        "Sintetiza la información visual en textos explicativos breves."
    ]
}

# Grado 8 (doc2 p21-22)
ingles_dict["8"]["1"] = {
    "statement": "Solicita y brinda información sobre experiencias y planes de manera clara y breve.",
    "evidencias": [
        "Intercambia información sobre metas a corto plazo y recuerdos personales significativos.",
        "Formula preguntas pertinentes para obtener detalles sobre planes de otros."
    ]
}
ingles_dict["8"]["2"] = {
    "statement": "Reconoce información específica en textos cortos orales y escritos sobre temas de interés general.",
    "evidencias": [
        "Aplica técnicas de lectura rápida (skimming y scanning) para extraer fechas, lugares y hechos.",
        "Distingue ideas principales de secundarias en notas de interés general."
    ]
}
ingles_dict["8"]["3"] = {
    "statement": "Explica por escrito, de forma coherente y sencilla, situaciones y hechos que le son familiares.",
    "evidencias": [
        "Redacta párrafos estructurados estableciendo relaciones causales básicas.",
        "Usa signos de puntuación y vocabulario variado para describir hechos reales o ficticios."
    ]
}
ingles_dict["8"]["4"] = {
    "statement": "Intercambia información sobre temas académicos del entorno escolar y de interés general, a través de conversaciones sencillas.",
    "evidencias": [
        "Participa activamente en debates dirigidos y discusiones en grupo sobre materias escolares.",
        "Sustenta su opinión de forma respetuosa con argumentos breves."
    ]
}
ingles_dict["8"]["5"] = {
    "statement": "Expresa sus emociones y sentimientos sobre una situación o tema específico de su entorno familiar o escolar.",
    "evidencias": [
        "Manifiesta estados de ánimo y reacciones personales frente a acontecimientos comunes.",
        "Empatiza con las emociones de sus compañeros usando expresiones de apoyo en inglés."
    ]
}
ingles_dict["8"]["6"] = {
    "statement": "Narra brevemente hechos actuales, situaciones cotidianas o sus experiencias propias, en forma oral o escrita.",
    "evidencias": [
        "Construye relatos cronológicos integrando inicio, nudo y desenlace.",
        "Utiliza tiempos verbales en pasado para reportar anécdotas vividas."
    ]
}

# Grado 9 (doc2 p24-25)
ingles_dict["9"]["1"] = {
    "statement": "Explica el por qué de planes y acciones relacionadas con su entorno personal, escolar y comunitario.",
    "evidencias": [
        "Estructura explicaciones orales y escritas fundamentando decisiones individuales y colectivas.",
        "Emplea marcadores discursivos de causa, efecto y finalidad con fluidez."
    ]
}
ingles_dict["9"]["2"] = {
    "statement": "Reconoce relaciones de causa y efecto en lecturas cortas sobre temas académicos.",
    "evidencias": [
        "Identifica conectores lógicos de causa-efecto en textos de divulgación científica y social.",
        "Sintetiza la cadena de acontecimientos en diagramas de flujo o mapas conceptuales."
    ]
}
ingles_dict["9"]["3"] = {
    "statement": "Expresa su opinión sobre un tema discutido en clase y relacionado con su entorno académico citando lo que han dicho otros.",
    "evidencias": [
        "Alude a puntos de vista de sus compañeros o autores para respaldar o refutar ideas.",
        "Participa en foros de clase manteniendo una postura argumentada y respetuosa."
    ]
}
ingles_dict["9"]["4"] = {
    "statement": "Intercambia información sobre temas del entorno escolar y de interés general en una conversación formal o informal.",
    "evidencias": [
        "Ajusta su registro comunicativo de acuerdo con la formalidad del contexto y el interlocutor.",
        "Propone temas de discusión y sostiene el intercambio conversacional."
    ]
}
ingles_dict["9"]["5"] = {
    "statement": "Redacta textos de mediana longitud en los cuales realiza recomendaciones o sugerencias sobre situaciones de interés personal, escolar o social.",
    "evidencias": [
        "Escribe guías, correos o cartas con recomendaciones prácticas para mejorar la convivencia o el aprendizaje.",
        "Emplea verbos modales de sugerencia y consejo de forma adecuada (should, could, must)."
    ]
}
ingles_dict["9"]["6"] = {
    "statement": "Identifica el propósito, las partes y tipo de textos en una lectura o audio cortos y los comparte con sus compañeros.",
    "evidencias": [
        "Distingue textos narrativos, descriptivos, instructivos y argumentativos.",
        "Señala la intención comunicativa del autor y la estructura compositiva del documento."
    ]
}

# Grado 10 (doc2 p27-28)
ingles_dict["10"]["1"] = {
    "statement": "Redacta textos narrativos, descriptivos y expositivos relacionados con temas de su interés o que le resultan familiares.",
    "evidencias": [
        "Aplica procesos de planificación, redacción, revisión y edición en sus producciones escritas.",
        "Utiliza variedad léxica, coherencia temática y corrección gramatical en textos extensos."
    ]
}
ingles_dict["10"]["2"] = {
    "statement": "Explica las ideas de un texto oral o escrito acerca de temas de su interés o que le son familiares a partir de su conocimiento previo.",
    "evidencias": [
        "Parafrasea y sintetiza conferencias breves, podcasts o artículos de interés juvenil.",
        "Conecta los planteamientos del texto con realidades de su entorno o aprendizajes de otras asignaturas."
    ]
}
ingles_dict["10"]["3"] = {
    "statement": "Produce mensajes escritos, tales como cartas y correos electrónicos, claros y bien estructurados teniendo en cuenta el contexto.",
    "evidencias": [
        "Adapta las fórmulas de cortesía, saludo y despedida acordes con la relación institucional o personal.",
        "Transmite solicitudes, agradecimientos o quejas formales con precisión y claridad."
    ]
}
ingles_dict["10"]["4"] = {
    "statement": "Sostiene conversaciones espontáneas y sencillas acerca de temas que son de su conocimiento, interés personal o académico.",
    "evidencias": [
        "Selecciona expresiones idiomáticas apropiadas para iniciar, mantener y cerrar una conversación.",
        "Negocia significados y aclara malentendidos de manera ágil durante la interacción."
    ]
}
ingles_dict["10"]["5"] = {
    "statement": "Intercambia opiniones sobre situaciones de interés personal, escolar o social presentando sus opiniones de manera natural y coherente.",
    "evidencias": [
        "Participa activamente en mesas redondas, paneles y debates escolares.",
        "Usa recursos retóricos básicos para persuadir y evidenciar solidez en su punto de vista."
    ]
}
ingles_dict["10"]["6"] = {
    "statement": "Responde preguntas e inquietudes después de hacer una exposición oral sobre temas generales o académicos de interés.",
    "evidencias": [
        "Prepara exposiciones orales con apoyos visuales y responde dudas formuladas por el público.",
        "Profundiza en aspectos técnicos o conceptuales de la exposición de forma articulada."
    ]
}

# Grado 11 (doc2 p30-32)
ingles_dict["11"]["1"] = {
    "statement": "Identifica el propósito de textos orales y escritos de mediana longitud relacionados con temas de interés general y académico y la comparte con otros.",
    "evidencias": [
        "Analiza discursos, reportajes y artículos reconociendo el registro y el objetivo persuasivo o informativo.",
        "Expone resúmenes analíticos contrastando fuentes documentales diversas."
    ]
}
ingles_dict["11"]["2"] = {
    "statement": "Explica tanto en forma oral como escrita las causas y los efectos, así como el problema y la solución de una situación.",
    "evidencias": [
        "Desarrolla ensayos breves de causa-efecto y propuesta de soluciones a problemáticas globales o locales.",
        "Emplea conectores avanzados de transición lógica y subordinación discursiva."
    ]
}
ingles_dict["11"]["3"] = {
    "statement": "Reconoce la opinión del autor(a) en textos orales y escritos de mediana longitud que se relacionan con su contexto escolar y académico.",
    "evidencias": [
        "Distingue hechos objetivos de juicios de valor o posturas subjetivas del autor.",
        "Comenta críticamente la validez de los argumentos presentados en el texto."
    ]
}
ingles_dict["11"]["4"] = {
    "statement": "Expresa de manera oral y escrita su posición acerca de un tema conocido teniendo en cuenta a quién está dirigido el texto.",
    "evidencias": [
        "Modula el tono comunicativo (formal, académico, informal) según el destinatario y la audiencia.",
        "Produce cartas de motivación o columnas de opinión estudiantiles bien fundamentadas."
    ]
}
ingles_dict["11"]["5"] = {
    "statement": "Redacta textos argumentativos con una estructura clara y sencilla sobre temas académicos siguiendo un proceso de planeación, escritura y edición.",
    "evidencias": [
        "Formula tesis claras respaldadas por argumentos sólidos, evidencias y conclusiones coherentes.",
        "Aplica técnicas de brainstorming, esquematización previa y corrección de estilo."
    ]
}
ingles_dict["11"]["6"] = {
    "statement": "Expresa de manera oral su punto de vista acerca de un tema controversial previamente estudiado a partir de notas y fuentes confiables.",
    "evidencias": [
        "Interviene en debates formales y modelos de asamblea (e.g. Model UN o foros ciudadanos).",
        "Refuta argumentos contrarios respetando las normas de discusión y el turno de la palabra."
    ]
}
ingles_dict["11"]["7"] = {
    "statement": "Narra de manera oral o escrita experiencias personales o historias conocidas brindando detalles de situaciones, lugares, personas y acciones.",
    "evidencias": [
        "Produce narrativas expresivas ricas en descripción sensorial, tiempo y ambiente.",
        "Transmite reflexiones éticas, aprendizajes personales o lecciones de vida a su audiencia."
    ]
}

with open("literal_ingles.json", "w", encoding="utf-8") as f:
    json.dump(ingles_dict, f, ensure_ascii=False, indent=2)

print("literal_ingles.json saved successfully!")
