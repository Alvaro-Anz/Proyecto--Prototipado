class UniversidadDelValle:
    def __init__(self):
        self.facultades = {
            "Facultad de Ingeniería": {
                "decano": "M.Sc. Víctor Hugo Ayerdi Bardales",
                "carreras": {
                    1: {"nombre": "Ingeniería Biomédica", "director": "M.Sc. Carlos Esquit"},
                    2: {"nombre": "Ingeniería en Biotecnología Industrial", "director": "M.Sc. Gamaliel Zambrano"},
                    3: {"nombre": "Ingeniería en Ciencias de los Alimentos", "director": "M.Sc. Ana Silvia Colmenares de Ruiz"},
                    4: {"nombre": "Ingeniería en Ciencia de la Administración", "director": "MBA Raúl Fernando Dacaret Román"},
                    5: {"nombre": "Ingeniería Civil", "director": "M.Sc. Otoniel Alejandro Echeverría Castellanos"},
                    6: {"nombre": "Ingeniería Civil Arquitectónica", "director": "M.Sc. Otoniel Alejandro Echeverría Castellanos"},
                    7: {"nombre": "Ingeniería en Computación y Tecnologías de la Información", "director": "M.Sc. Douglas Barrios"},
                    8: {"nombre": "Ingeniería Electrónica", "director": "M.Sc. Carlos Esquit"},
                    9: {"nombre": "Ingeniería Industrial", "director": "Ing. Ingrid Lorena de León Vilaseca"},
                    10: {"nombre": "Ingeniería Mecánica", "director": "M.Sc. Gustavo Barrera"},
                    11: {"nombre": "Ingeniería Mecánica Industrial", "director": "M.Sc. Gustavo Barrera"},
                    12: {"nombre": "Ingeniería Mecatrónica", "director": "M.Sc. Carlos Esquit"},
                    13: {"nombre": "Ingeniería Química", "director": "M.Sc. Gamaliel Zambrano"},
                    14: {"nombre": "Ingeniería Química Industrial", "director": "M.Sc. Gamaliel Zambrano"}
                }
            },
            "Facultad de Bridge Business School": {
                "decano": "Mgtr. Ofelia Fernandez de la Torre",
                "carreras": {
                    1: {"nombre": "Ingeniería en Ciencia de la Administración", "director": "MBA Raúl Fernando Dacaret Román"},
                    2: {"nombre": "Administración de Empresas", "director": "MBA Raúl Fernando Dacaret Román"},
                    3: {"nombre": "International Marketing and Business Analytics", "director": "MBA José Carlos Cárcamo"},
                    4: {"nombre": "Comunicación Estratégica", "director": "M.A. Luna Mishaan"}
                }
            },
            "Facultad de Educación": {
                "decano": "MPA Carolina Roca",
                "carreras": {
                    1: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Ciencias Biológicas y Químicas", "director": "M.A. Ester Cristina Ruiz Cruz"},
                    2: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Ciencias Sociales", "director": "Lda. Ester Cristina Ruiz Cruz"},
                    3: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Comunicación y Lenguaje", "director": "M.A. Ester Cristina Ruiz Cruz"},
                    4: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Educación Inclusiva", "director": "Lda. Leslie Staackmann"},
                    5: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Educación Musical", "director": "Lic. Mayra Araceli Carrera Alvarado"},
                    6: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Educación Primaria", "director": "Lda. Ester Cristina Ruiz Cruz"},
                    7: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en English Language Teaching", "director": "M.A. Karin Rossbach Lemus"},
                    8: {"nombre": "Profesorado y Licenciatura en Educación con Especialidad en Matemática y Ciencias Físicas", "director": "M.A. Ester Cristina Ruiz Cruz"},
                    9: {"nombre": "Profesorado Especializado en Problemas del Aprendizaje", "director": "Lda. Leslie Carolina Staackmann"}
                }
            },
            "Facultad de Ciencias y Humanidades": {
                "decano": "Dra. Pamela Pennington",
                "carreras": {
                    1: {"nombre": "Licenciatura en Biología", "director": "MSc. Gabriela Alfaro Marroquin"},
                    2: {"nombre": "Licenciatura en Bioquímica y Microbiología", "director": "Dra. Patrizia Lupo"},
                    3: {"nombre": "Licenciatura en Biotecnología Molecular", "director": "Dra. Patrizia Lupo"},
                    4: {"nombre": "Licenciatura en Comunicación Estratégica", "director": "Lda. Luna Mishaan"},
                    5: {"nombre": "Licenciatura en Física", "director": "MSc. Eduardo Alvarez Massis"},
                    6: {"nombre": "Licenciatura en Matemática Aplicada", "director": "MA. Nancy Anely Zurita Villagrán"},
                    7: {"nombre": "Licenciatura en Nutrición", "director": "MA. Ana Isabel Rosal"},
                    8: {"nombre": "Licenciatura en Química", "director": "Lda. Irma Patricia Orellana Catalan"},
                    9: {"nombre": "Licenciatura en Química Farmacéutica", "director": "MA. Elfego Rolando López"}
                }
            },
            "Facultad de Ciencias Sociales": {
                "decano": "Dra. Linda Asturias de Barrios",
                "carreras": {
                    1: {"nombre": "Licenciatura en Antropología y Sociología", "director": "M.A. Isolda Annette Fortín"},
                    2: {"nombre": "Licenciatura en Arqueología", "director": "Lic. Tomás Barrientos Quezada"},
                    3: {"nombre": "Licenciatura en Psicología", "director": "Dra. Dina María Elías Rodas"},
                    4: {"nombre": "Licenciatura en Relaciones Internacionales", "director": "Mgtr. Luis Andrés Padilla"}
                }
            },
            "Design Innovation and Arts School": {
                "decano": "MA. María Cecilia de León",
                "carreras": {
                    1: {"nombre": "Licenciatura en Composición y Producción Musical", "director": "MA. Diego Raúl Guzmán"},
                    2: {"nombre": "Licenciatura en Diseño de Productos e Innovación", "director": "MA. María Cecilia de León"}
                }
            },
            "Colegio Universitario": {
                "decano": "Lda. Maricruz Alvarez Mury",
                "carreras": {
                    1: {"nombre": "Baccalaureatus en Artibus (B.A.)", "director": "Lda. Maricruz Alvarez Mury"},
                    2: {"nombre": "Baccalaureatus en Scientiis (B.S.)", "director": "Lda. Maricruz Alvarez Mury"}
                }
            },
            "Escuela de Arquitectura": {
                "decano": "Lic. Eduardo Francisco Escobar Monzón",
                "carreras": {
                    1: {"nombre": "Licenciatura en Arquitectura", "director": "Lic. Eduardo Francisco Escobar Monzón"}
                }
            }
        }
        
        self.cursos = {
            "Primer Semestre": {
                "Ciudadanía Global": ["María Isabel Carrascosa"],
                "Coaching para la Excelencia": ["Rony Herrarte", "Isis López"],
                "Dibujo Mecánico": ["Ing. Laura Roldán", "MSc. Héctor Gómez", "Ing. Eileen Nancy Del Carmen Meda Albizures"],
                "Introducción a la Ingeniería Mecánica": ["MSc. Gustavo Barrera gabarrera@uvg.edu.gt", "Ing. Samuel Reyes, sareyes@uvg.edu.gt", "Ing. Luis Diego Castañeda ldcastaneda@uvg.edu.gt"],
                "Manufactura Digital": ["José Antonio Bagur Nájera"],
                "Pensamiento Cuantitativo": ["Amalia Ruballos (Coordinadora) aeruballos@uvg.edu.gt", "Ronald Curtiss rcurtiss@uvg.edu.gt", "Eugenio Aristondo eaaristondo@uvg.edu.gt", "José Pablo Ortega jportega@uvg.edu.gt", "Luis Alvarado Ifalvaradoa@uvg.edu.gt", "Zayda Pérez zrperez@uvg.edu.gt", "Ma.Eugenia de Nieves mecp@uvg.edu.gt", "Nancy Zurita nazurita@uvg.edu.gt", "Christian Ramírez csramírez@uvg.edu.gt", "Rodrigo Leonardo Iriconardo@uvg.edu.gt", "Ranferi Gutiérrez mygutierrcz@uvg.edu.gt", "Arturo Castellanos arcastellanos@uvg.edu.gt", "Daniel Romero jdromero@uvg.edu.gt"],
                "Química General": ["Inga. María Romero", "Ing. Hugo Oliveros", "Lic. Julio Guzmán", "Lic. Hugo Escobar", "Lic. Saúl Loaiza"]
            },
            "Segundo Semestre": {
                "Algoritmos y Programación Básica": ["Erick Marroquin (coordinador) efmarroquin@uvg.edu.gt", "Leonel Guillén Iguillen@uvg.edu.gt", "Kimberly Barrera kmbarrera@uvg.edu.gt", "Luis Esturbán icesturban@uvg.edu.gt", "Pablo Koch pabarreno@uvg.edu.gt", "Diego Contreras djcontreras@uvg.edu.gt"],
                "Cálculo 1": ["M.A. Ronald Curtiss Quifiónez rcurtiss@uvg.edu.gt (Coordinador)", "M.A. Amalia Esmeralda Ruballos Juárez de Mancio aeruballos@uvg.edu.gt", "M.A. Magda Violeta Mendizábal Lara de Schwendener schwende@uvg.edu.gt", "M.A. Luis Fernando Alvarado Arroyo Ifalvaradoa@uvg.edu.gt", "MBA. Arturo René Castellanos Pineda arcastellanos@uvg.edu.gt", "Ing. Luis Edgar Arana Sincal learana@uvg.edu.gt", "Ing. Julio David Guzmán Benitez jdguzman@uvg.edu.gt", "MSc. Danilo Antonio Rodríguez Cerón darodriguez@uvg.edu.gt", "Dr. Ranferi Gutiérrez Morales mygutierrcz@uvg.edu.gt", "Dr. José Ernesto Ramírez Calderón jeramirez@uvg.edu.gt", "MSc. José Daniel Romero jdromero@uvg.edu.gt", "M.A. Ingrid Susanne Zufliga Kaufmann de Alvarado szuniga@uvg.edu.gt", "M.A. Nancy Anely Zurita Villagrán de Calgua nazurita@uvg.edu.gt"],
                "Comunicación Efectiva": ["M.A. María Isabel Prado Cobos de Bolafios miprado@uvg.edu.gt"],
                "Estadística 1": ["M.A. Amalia Ruballos (Coordinadora) aeruballos@uvg.edu.gt", "M.A. Luis Alvarado Ifalvaradoa@uvg.edu.gt", "M.A. Denise Pennueller dmpemueller@uvg.edu.gt", "PhD. Zayda Pérez zrperez@uvg.edu.gt", "M.A. Aníbal Vargas alvargas@uvg.edu.gt", "M.A. Eugenio Aristondo eaaristondo@uvg.edu.gt", "Ing. Arturo Castellanos arcastellanos@uvg.edu.gt", "Ing. Danilo Rodríguez darodriguez@uvg.edu.gt", "PhD. José Ramírez jeramirez@uvg.edu.gt", "M.Sc José Daniel Romero jdromero@uvg.edu.gt", "M.A. Irina Reyes iareyes@uvg.edu.gt"],
                "Física 1": ["Lic. Zaida Urrutia", "M.A. María Elisa Duarte", "M.A. Elí Saul De Paz", "M.A. Magda Moscoso (coordinadora)", "Lic. Gonzalo Morán", "MSc Irene Aguilar", "MSc Antonio Mendez"],
                "Máquinas Herramienta": ["Ing. Gustavo Pineda, gwpineda@uvg.edu.g (teoria)", "Edgar Castillo, ercastillo@uvg.edu.gt (práctica)"]
            }
        }
        
        self.cursos_selectivos = {
            1: {"codigo": "CU192", "nombre": "Desarrollo de competencias para el éxito profesional", "descripcion": "Esta iniciativa surge del interés de proporcionar al estudiante herramientas prácticas y concretas para prepararlo para el entorno laboral. Estas herramientas serán complementadas por la visita de expertos que laboran en empresas y que tienen conocimiento actualizado de los requerimientos de los empleadores."},
            2: {"codigo": "CU1100", "nombre": "English Practice for Business", "descripcion": "This course is designed to help students build upon their fundamental English language communication skills by using professional and formal business tools in structured business environments."},
            3: {"codigo": "CU193", "nombre": "Confianza creativa", "descripcion": "Esta iniciativa académica se enfoca en que el estudiante desarrolle conceptos creativos cuya aplicación resuelva retos y necesidades del mundo actual, de manera disruptiva, para salir de la zona de confort."},
            4: {"codigo": "CU194", "nombre": "Neurodiseño y psicología del consumidor", "descripcion": "El consumo es una actividad humana que evoluciona de la mano de la sociedad. El comportamiento de los consumidores cambia a medida que van surgiendo nuevos hábitos y se generan nuevas necesidades en los individuos."},
            5: {"codigo": "EU199", "nombre": "Locución y expresión pública", "descripcion": "Esta iniciativa académica desarrolla en los estudiantes de todas las carreras, las capacidades de expresarse con propiedad y confianza frente al público, sin importar el contexto, ni el medio de comunicación."},
            6: {"codigo": "CP1001", "nombre": "Psicología, música y expresión", "descripcion": "Esta iniciativa describe la relación que existe entre la música, la expresión y el comportamiento humano. Estudia el sistema nervioso, auditivo, la percepción y cómo el sonido afecta física y emocionalmente al individuo y a la sociedad."},
            7: {"codigo": "CP3033", "nombre": "Lenguaje musical para todos", "descripcion": "El lenguaje musical es un componente esencial de la cultura humana. Comprenderlo permite desarrollar sensibilidad auditiva, pensamiento analítico y creatividad."},
            8: {"codigo": "HL1004", "nombre": "Storytelling", "descripcion": "En este curso se estudiará la importancia de narrar y comprender historias en nuestra comunicación diaria. Se presentarán y analizarán ejemplos de personas que transmiten su historia de una manera efectiva a través de diversos medios de comunicación."},
            9: {"codigo": "HL3045", "nombre": "Comunicación en los negocios", "descripcion": "El mercado laboral demanda profesionales, con la habilidad de transmitir y recibir información correcta en el momento adecuado. Profesionales capaces de comunicar efectivamente para guiar la gestión empresarial de forma exitosa."},
            10: {"codigo": "HL3042", "nombre": "Escritura creativa", "descripcion": "Este curso introductorio aborda elementos de la escritura creativa, el desarrollo y el pensamiento inventivo."},
            11: {"codigo": "HL1005", "nombre": "Comunicación para la ciencia y la tecnología", "descripcion": "Se fundamenta en la importancia que tiene la divulgación científica o comunicación pública de la ciencia, como parte del proceso de formación académica para los estudiantes de UVG."},
            12: {"codigo": "HL1006", "nombre": "Construye tu marca personal", "descripcion": "El marketing pasó de un enfoque funcional a otro emocional, que cambia la unidireccionalidad por la relación. En este contexto, todo profesional debe preguntarse: ¿Puedo yo ser una marca?"},
            13: {"codigo": "EN3072", "nombre": "Cultivando una relación sana con la comida y contigo mismo", "descripcion": "¿Alguna vez te has sentido frustrado/a con la manera en que comes? ¿Y te preguntas, qué es una alimentación sana, y cómo logro sentirme mejor? No estás solo."},
            14: {"codigo": "PP198", "nombre": "Mindfulness y liderazgo positivo", "descripcion": "Mindfulness y Liderazgo Positivo aborda sobre los beneficios que ofrece el Mindfulness o Atención Plena, con la finalidad de ejercer un liderazgo positivo en el ámbito de vida personal, académico y profesional."},
            15: {"codigo": "CU195", "nombre": "Desafíos de la Equidad de Género", "descripcion": "La temática y las actividades propuestas permitirán a los estudiantes desarrollar una visión general acerca del tema de género, que conlleva, qué lo influye y el desarrollo humano y su relación con el género."},
            16: {"codigo": "EI148", "nombre": "A Writing Journey through Fantastic Worlds", "descripcion": "This course relates to the creation of writing that goes outside the bounds of regular professional, journalistic, academic or technical forms of literature."},
            17: {"codigo": "II3045", "nombre": "Toma de decisiones efectivas y resolución de problemas", "descripcion": "Este curso le permite al estudiante proponer soluciones utilizando herramientas del proceso de toma de decisiones para obtener resultados innovadores y creativos a distintas problemáticas."},
            18: {"codigo": "II101", "nombre": "Administración de Finanzas Personales", "descripcion": "El curso aborda los principios y prácticas de la administración financiera personal, cubriendo temas como planificación financiera, presupuesto, ahorro, inversión y gestión del riesgo."},
            19: {"codigo": "II3047", "nombre": "Análisis cognitivo para la inmersión en la realidad virtual", "descripcion": "El curso de Análisis Cognitivo para la Inmersión en Realidad propone un valor sin comparación para el perfil de egreso de la Universidad del Valle de Guatemala."},
            20: {"codigo": "IM3041", "nombre": "Diseño e innovación para el desarrollo", "descripcion": "Este curso se basa en el curso D-Lab: Development, del Massachusetts Institute of Technology (MIT). Está orientado para que el estudiante conozca el proceso de diseño y pueda aplicarlo para crear tecnologías de bajo costo."},
            21: {"codigo": "IA2012", "nombre": "Design Thinking", "descripcion": "En este curso el estudiante propone proyectos de innovación centrada en las personas a través de la metodología del Design Thinking como proceso creativo."},
            22: {"codigo": "IA3035", "nombre": "Liderazgo y Comportamiento Organizacional", "descripcion": "Este es un curso que desarrolla las competencias de liderazgo para que los estudiantes logren al máximo su propio desempeño y de las personas o equipos que están o estarán a su cargo."},
            23: {"codigo": "IA3036", "nombre": "Negociación, Resolución de Conflictos e Implementación de Acuerdos", "descripcion": "El curso introduce a los estudiantes a la teoría y la práctica de la negociación. Se orienta al desarrollo de habilidades analíticas, emocionales y comunicacionales que son necesarias para una buena negociación."},
            24: {"codigo": "IA3041", "nombre": "Entrepreneurial Finance", "descripcion": "El curso de Entrepreneurial finance, está enfocado para alumnos de cualquier nivel de conocimiento. En el curso se empieza estudiando lo esencial de economía, para lograr entender el contexto social."},
            25: {"codigo": "TD2020", "nombre": "The Science of Happiness", "descripcion": "Este curso repasa lo que dice la ciencia psicológica sobre la felicidad el bienestar. El propósito del curso es aprender lo que dice la investigación psicológica sobre lo que nos hace felices."},
            26: {"codigo": "TD3005", "nombre": "Coaching and Teams", "descripcion": "Este curso está dirigido a todos ustedes estudiantes que desean comprender y poner en práctica las competencias del Coaching de Excelencia."},
            27: {"codigo": "IA1003", "nombre": "Pensamiento clásico y mitología", "descripcion": "El curso propone que las ideas clásicas son responsables por el desarrollo de la cultura occidental del mundo moderno y que este mismo es el heredero intelectual de los antiguos griegos y romanos."},
            28: {"codigo": "L11001", "nombre": "Consumer Behaviour for Entrepreneurs", "descripcion": "Entender al consumidor es clave para saber cómo reaccionan ante un nuevo producto o servicio, con el fin de desarrollar estímulos y estrategias que se utilizan para atraerlos y retenerlos."},
            29: {"codigo": "L11002", "nombre": "Strategy Toolkit for Entrepreneurs", "descripcion": "El curso tiene como principal objetivo introducir al estudiante en la dinámica empresarial para que el mismo pueda encontrar aplicaciones reales al conocimiento adquirido."},
            30: {"codigo": "CC178", "nombre": "Diseño e innovación con Inteligencia Artificial y LLM", "descripcion": "La inteligencia artificial generativa está siendo usada para innovar y crear modelos de negocio en áreas tan diversas como mercadeo, educación, salud, banca, ciencia e investigación."},
            31: {"codigo": "QA3054", "nombre": "Estrategias de Diseño participativo para la Innovación", "descripcion": "Este curso es una serie de conceptos y estrategias basados en el trabajo del MIT D-Lab* en diseño participativo e innovación inclusiva."},
            32: {"codigo": "ID1001", "nombre": "Computación científica para Ciencia e Ingeniería", "descripcion": "El curso propuesto busca presentar a los estudiantes las herramientas existentes para la solución de problemas de ciencia e ingeniería que requieren la aplicación de métodos matemáticos y estadísticos."}
        }
    
    def mostrar_menu_principal(self):
        print("\n" + "="*80)
        print("Bienvenidos a este programa.")
        print("Este programa tiene como objetivo que tu conozcas a la Universidad Del Valle de Guatemala")
        print("y todo lo que tiene que ofrecer.")
        print("A continuación, puedes escoger temas en los que puedes expandir tu conocimiento,")
        print("o resolver dudas sobre lo presentado.")
        print("1) Información sobre las diferentes Facultades y sus respectivas carreras")
        print("2) Información sobre cursos y sus respectivos docentes")
        print("3) Información sobre cursos selectivos")
        print("4) Salir")
        print("="*80)
    
    def mostrar_facultades(self):
        print("\n" + "="*80)
        print("FACULTADES DE LA UNIVERSIDAD DEL VALLE DE GUATEMALA")
        print("="*80)
        
        facultades = list(self.facultades.keys())
        for i, facultad in enumerate(facultades, 1):
            print(f"{i}) {facultad}")
        
        try:
            opcion = int(input("\nSeleccione el número de la facultad que desea explorar: "))
            if 1 <= opcion <= len(facultades):
                facultad_seleccionada = facultades[opcion-1]
                self.mostrar_carreras(facultad_seleccionada)
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    def mostrar_carreras(self, facultad):
        print("\n" + "="*80)
        print(f"FACULTAD: {facultad}")
        print(f"Decano: {self.facultades[facultad]['decano']}")
        print("CARRERAS:")
        print("="*80)
        
        carreras = self.facultades[facultad]["carreras"]
        for num, info in carreras.items():
            print(f"{num}) {info['nombre']}")
        
        try:
            opcion = int(input("\nSeleccione el número de la carrera que desea conocer: "))
            if opcion in carreras:
                carrera = carreras[opcion]
                print("\n" + "="*80)
                print(f"INFORMACIÓN DE LA CARRERA")
                print("="*80)
                print(f"Facultad: {facultad}")
                print(f"Carrera: {carrera['nombre']}")
                print(f"Director de Carrera: {carrera['director']}")
                print(f"Decano de la Facultad: {self.facultades[facultad]['decano']}")
                print("="*80)
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    def mostrar_cursos(self):
        print("\n" + "="*80)
        print("CURSOS POR SEMESTRE")
        print("="*80)
        
        semestres = list(self.cursos.keys())
        for i, semestre in enumerate(semestres, 1):
            print(f"{i}) {semestre}")
        
        try:
            opcion_semestre = int(input("\nSeleccione el número del semestre que desea explorar: "))
            if 1 <= opcion_semestre <= len(semestres):
                semestre_seleccionado = semestres[opcion_semestre-1]
                cursos_semestre = self.cursos[semestre_seleccionado]
                
                print("\n" + "="*80)
                print(f"CURSOS DEL {semestre_seleccionado.upper()}")
                print("="*80)
                
                cursos_lista = list(cursos_semestre.keys())
                for i, curso in enumerate(cursos_lista, 1):
                    print(f"{i}) {curso}")
                
                try:
                    opcion_curso = int(input("\nSeleccione el número del curso que desea conocer: "))
                    if 1 <= opcion_curso <= len(cursos_lista):
                        curso_seleccionado = cursos_lista[opcion_curso-1]
                        docentes = cursos_semestre[curso_seleccionado]
                        
                        print("\n" + "="*80)
                        print(f"INFORMACIÓN DEL CURSO")
                        print("="*80)
                        print(f"Semestre: {semestre_seleccionado}")
                        print(f"Curso: {curso_seleccionado}")
                        print("\nDOCENTES:")
                        for docente in docentes:
                            print(f"- {docente}")
                        print("="*80)
                    else:
                        print("Opción no válida. Por favor, seleccione un número de la lista.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    def mostrar_cursos_selectivos(self):
        print("\n" + "="*80)
        print("CURSOS SELECTIVOS DISPONIBLES")
        print("="*80)
        
        for num, curso in self.cursos_selectivos.items():
            print(f"{num}) {curso['codigo']} - {curso['nombre']}")
        
        try:
            opcion = int(input("\nSeleccione el número del curso selectivo que desea conocer: "))
            if opcion in self.cursos_selectivos:
                curso = self.cursos_selectivos[opcion]
                print("\n" + "="*80)
                print(f"INFORMACIÓN DEL CURSO SELECTIVO")
                print("="*80)
                print(f"Código: {curso['codigo']}")
                print(f"Nombre: {curso['nombre']}")
                print(f"\nDescripción:\n{curso['descripcion']}")
                print("="*80)
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            
            try:
                opcion = int(input("\nPor favor, seleccione una opción (1-4): "))
                
                if opcion == 1:
                    self.mostrar_facultades()
                elif opcion == 2:
                    self.mostrar_cursos()
                elif opcion == 3:
                    self.mostrar_cursos_selectivos()
                elif opcion == 4:
                    print("\n" + "="*80)
                    print("¡Gracias por utilizar nuestro programa!")
                    print("Esperamos que esta información te haya sido útil.")
                    print("¡Éxito en tu camino académico en la Universidad del Valle de Guatemala!")
                    print("="*80)
                    break
                else:
                    print("Opción no válida. Por favor, seleccione un número entre 1 y 4.")
            
            except ValueError:
                print("Por favor, ingrese un número válido.")

# Ejecutar el programa
if __name__ == "__main__":
    programa = UniversidadDelValle()
    programa.ejecutar()
