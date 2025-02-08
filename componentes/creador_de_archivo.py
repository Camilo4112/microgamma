import os

# Lista de departamentos de Colombia en orden alfabético
departamentos = [
    "Amazonas", "Antioquia", "Arauca", "Atlántico", "Bolívar", "Boyacá", "Caldas", 
    "Caquetá", "Casanare", "Cauca", "Cesar", "Chocó", "Córdoba", "Cundinamarca", 
    "Guainía", "Guaviare", "Huila", "La Guajira", "Magdalena", "Meta", "Nariño", 
    "Norte de Santander", "Putumayo", "Quindío", "Risaralda", "San Andrés y Providencia", 
    "Santander", "Sucre", "Tolima", "Valle del Cauca", "Vaupés", "Vichada"
]

# Ruta de la carpeta de componentes
ruta_carpeta = "C:\\Users\\JUAN CAMILO\\Desktop\\Proyectos\\page the travel\\componentes"


# Crear un archivo HTML y CSS para cada departamento
for departamento in departamentos:
    # Nombre de los archivos
    nombre_html = departamento.lower() + ".html"
    nombre_css = departamento.lower() + ".css"

    # Contenido del archivo HTML
    contenido_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{departamento}</title>
        <link rel="stylesheet" href="{nombre_css}">
    </head>
    <body>
        <header>
            <nav>
                <h4>Magic Routes</h4>
                <ul id="menu_bx">
                    <li><a href="/index.html">Descubrir</a></li>
                    <li><a href="/Community.html">Coummunity</a></li>
                    <li><a href="#">Special Deals</a></li>
                    <li><a href="#">About US</a></li>
                    <li><a href="/form.html">Register</a></li>
                </ul>
            </nav>
        </header>

        <div class="container">
            <h1>Bienvenidos Al Departamento de {departamento}</h1>
            <div class="item">
                <img src="../img/Portada_{departamento.lower()}.jpg" alt="Parque Nacional Natural Los Katíos">
                <div class="text">   
                    <h2>{departamento}</h2>
                    <p>{departamento} es un departamento de Colombia, conocido por su rica cultura, historia y belleza natural. Cuenta con 125 municipios, cada uno con su propio encanto. Algunos de los aspectos destacados de {departamento} incluyen:
                    Cultura y Gastronomía: {departamento} es famosa por su cultura vibrante y su deliciosa gastronomía.
                    Riqueza Natural: El paisaje de {departamento} es diverso, con montañas, selvas y mar.
                    Arquitectura e Historia: Puedes encontrar arquitectura colonial en lugares como Santa Fe de {departamento}.
                    Aventura: Hay muchas oportunidades para actividades de aventura y ecoturismo.
                    Además, Medellín, la capital de {departamento}, es conocida como la ciudad de la eterna primavera y ofrece una variedad de atractivos culturales y eventos</p>
                </div>
            </div>

            <h1>Lugares Turísticos</h1>
            <div class="item">
                <img src="../img/Park_katios.jpg" alt="Parque Nacional Natural Los Katíos">
                <div class="text">
                    <h2>Parque Nacional Natural Los Katíos</h2>
                    <p>Parque Nacional Natural Los Katíos: Situado en la región del Urabá antioqueño, este parque es reconocido por su biodiversidad y belleza paisajística.</p>
                </div>
            </div>

            <div class="item">
                <img src="../img/Guatape.jpg" alt="Guatapé">
                <div class="text">
                    <h2>Guatapé</h2>
                    <p>Guatapé es un pintoresco pueblo conocido por su espectacular piedra de El Peñol y sus coloridas fachadas decoradas con zócalos. Ofrece una experiencia única con paisajes naturales impresionantes y actividades como escalada en roca, paseos en bote y más.</p>
                </div>
            </div>

            <!-- Puedes agregar más lugares turísticos aquí siguiendo la misma estructura -->

            <h1>Festivales y Fiestas</h1>
            <div class="item">
                <img src="../img/feria de las flores.jpg" alt="Feria de las Flores">
                <div class="text">
                    <h2>Feria de las Flores</h2>
                    <p>Este festival, que se celebra en Medellín en agosto, es uno de los eventos más importantes de {departamento}, con desfiles de flores, conciertos, exposiciones de arte y más.</p>
                </div>
            </div>

            <h1>Deportistas</h1>
            <div class="item">
                <img src="../img/Rigoberto uruan.jpg" alt="Rigoberto Uran">
                <p>Rigoberto Uran: Conocido mundialmente como uno de los mejores ciclistas colombianos, Rigoberto Uran ha ganado varias etapas en el Tour de Francia y la Vuelta a España.</p>
            </div>

            <h1>Artistas</h1>
            <div class="item">
                <img src="../img/Fernando Botero.jpg" alt="Fernando Botero">
                <p>Fernando Botero: Uno de los artistas más reconocidos de Colombia, Botero es famoso por sus pinturas y esculturas que representan figuras exageradamente voluminosas.</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Contenido del archivo CSS
    contenido_css = f"""
/* Estilos generales */
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
}}

.container {{
    width: 80%;
    margin: 20px auto;
}}

h1 {{
    color: #333;
    margin-top: 20px;
}}

.item {{
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    display: flex; /* Utilizamos flexbox para colocar la imagen y el texto en línea */
}}

.item img {{
    max-width: 300px; /* Tamaño deseado para todas las imágenes */
    margin-right: 20px; /* Espacio entre la imagen y el texto */
}}

.item .text {{
    flex: 1; /* El texto ocupará todo el espacio restante */
}}

.item h2 {{
    margin-bottom: 10px; /* Espacio entre el título y el párrafo */
}}

.item p {{
    color: #000000;
}}

/* Estilos de encabezado y menú */
header {{
    padding: 10px 20px;
    color: #fff;
}}

header h4 {{
    color: #000; /* Cambia el color del texto a negro */
}}

nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease; /* Transición gradual para cambios en el menú */
}}

#menu_bx {{
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
}}

#menu_bx li {{
    display: inline-block;
    margin-right: 20px;
}}

#menu_bx li:last-child {{
    margin-right: 0;
}}

#menu_bx li a {{
    text-decoration: none;
    color: #030303;
    font-weight: bold;
}}

#menu_bx li a:hover {{
    color: #ffcc00;
}}

/* Estilos para dispositivos más pequeños */
@media screen and (max-width: 768px) {{
    .item {{
        flex-direction: column;
        align-items: center;
    }}

    .item img {{
        margin-right: 0;
        margin-bottom: 20px;
    }}

    .item .text {{
        text-align: center;
    }}

    nav {{
        flex-direction: column;
        align-items: center; /* Centrar el menú verticalmente */
        justify-content: center; /* Centrar el menú horizontalmente */
        height: auto; /* Ajustar automáticamente la altura del menú */
        overflow: hidden; /* Ocultar el menú desbordado */
        max-height: none; /* Eliminar la altura máxima para que el menú pueda crecer verticalmente */
    }}

    #menu_bx {{
        flex-direction: column;
        align-items: center; /* Centrar los elementos del menú verticalmente */
    }}

    #menu_bx li {{
        display: block;
        margin: 10px 0;
    }}

    /* Mostrar el menú cuando se activa */
    nav.active {{
        max-height: none; /* Eliminar la altura máxima para que el menú pueda crecer verticalmente */
    }}
}}
"""

    # Rutas completas de los archivos
    ruta_html = os.path.join(ruta_carpeta, nombre_html)
    ruta_css = os.path.join(ruta_carpeta, nombre_css)

    # Escribir contenido en los archivos
    with open(ruta_html, "w") as archivo_html:
        archivo_html.write(contenido_html)

    with open(ruta_css, "w") as archivo_css:
        archivo_css.write(contenido_css)

print("Archivos creados exitosamente.")
