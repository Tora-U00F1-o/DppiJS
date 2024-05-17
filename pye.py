
def doForTodas():
    with open("dppi-todos.txt", "r", encoding="utf-8") as file:
        data = file.read()

    data = data.split("?: ")

    data.sort()

    elegidas = []
    i = 0
    for pregunta in data:
        if len(pregunta.strip()) == 0:
            continue
        datos = pregunta.split("\n")
        if(len(datos) < 2):
            continue

        print(datos[0])

        correcta = [dato for dato in datos if "$" in dato]
        i+=1
        print(i)

        elegidas.append((datos[0] , correcta[0]))

    print(elegidas)
    with open("dppi-resp.txt", "w", encoding="utf-8") as file:
        for elegida in elegidas:
            file.write(elegida[0]+ "\n\t - "+elegida[1])
            file.write("\n\n")

def getSolucionesTema(nTema):
    name = "dppi-tema"+str(nTema)+".txt"
    with open(name, "r", encoding="utf-8") as file:
        data = file.read()
    
    data = data.split("?: ")

    data.sort()

    elegidas = []
    i = 0
    for pregunta in data:
        if len(pregunta.strip()) == 0:
            continue
        datos = pregunta.split("\n")
        if(len(datos) < 2):
            continue


        correcta = [dato for dato in datos if "$" in dato]
        i+=1

        elegidas.append((datos[0] , correcta[0]))

    return elegidas

sols = []
for i in range(1, 10):
    sols.append(getSolucionesTema(i))

    # print("Tema "+str(i)+":")

    # for sol in sols[i-1]:
    #     print(sol[0])

    # print("\n\n")

from html import escape

# def generate_html(sols):
#     html_content = "<html><head><link rel='stylesheet' type='text/css' href='styles.css'></head><body>"
#     for i, tema in enumerate(sols, start=1):
#         nPreg = 1
#         html_content += f'<div class="tema tema{i}"><h2>Tema {i}</h2>'
#         html_content += "<div class='preguntas'>" # Apertura de preguntas
#         for pregunta, respuesta in tema:
#             html_content += f'<div class="pregunta"><p><b>{nPreg} Pr:</b> {escape(pregunta)}</p>'
#             html_content += f'<p class="respuesta"> Resp: {escape(respuesta)}</p></div>'
#             nPreg += 1
#         html_content += "</div>" # Cierre de preguntas
#         html_content += "</div>" # Cierre de tema
#     html_content += "</body></html>"
#     return html_content

def generate_html(sols):
    html_content = "<html><head><link rel='stylesheet' type='text/css' href='styles.css'></head><body>"
    html_content += "<nav><ul>"  # Apertura de navegación
    for i in range(1, len(sols) + 1):
        html_content += f'<li><a href="#tema{i}">Tema {i}</a></li>'
    html_content += "</ul></nav>"  # Cierre de navegación
    for i, tema in enumerate(sols, start=1):
        nPreg = 1
        html_content += f'<div class="tema tema{i}" id="tema{i}"><h2>Tema {i}</h2>'  # Agregado id al div del tema
        html_content += "<div class='preguntas'>"  # Apertura de preguntas
        for pregunta, respuesta in tema:
            html_content += f'<div class="pregunta"><p><b>{nPreg} Pr:</b> {escape(pregunta)}</p>'
            html_content += f'<p class="respuesta"> Resp: {escape(respuesta)}</p></div>'
            nPreg += 1
        html_content += "</div>"  # Cierre de preguntas
        html_content += "</div>"  # Cierre de tema
    html_content += "</body></html>"
    return html_content

def generate_css():
    css_content = """
    .tema {
        border-left: 10px solid;
        padding-left: 10px;
        margin-bottom: 20px;
    }
    .tema1 { border-color: red; }
    .tema2 { border-color: orange; }
    .tema3 { border-color: yellow; }
    .tema4 { border-color: green; }
    .tema5 { border-color: blue; }
    .tema6 { border-color: indigo; }
    .tema7 { border-color: violet; }
    .tema8 { border-color: brown; }
    .tema9 { border-color: black; }
    .pregunta {
        background-color: #f0f0f0;
        margin-bottom: 10px;
        padding: 10px;
    }
    .respuesta {
        font-weight: bold;
    }
    """
    return css_content

# Generar el HTML y escribirlo en un archivo
html_content = generate_html(sols)
with open('preguntas.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Generar el CSS y escribirlo en un archivo
css_content = generate_css()
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)