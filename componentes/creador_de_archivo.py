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
    </body>
    </html>
    """

    # Contenido del archivo CSS
    contenido_css = """
    /* Estilos CSS aquí */body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  
  header {
    padding: 10px 20px;
    color: #fff;
}

header h4 {
    color: #000; /* Cambia el color del texto a negro */
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#menu_bx {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

#menu_bx li {
    display: inline-block;
    margin-right: 20px;
}

#menu_bx li:last-child {
    margin-right: 0;
}

#menu_bx li a {
    text-decoration: none;
    color: #ffffff;
    font-weight: bold;
}

#menu_bx li a:hover {
    color: #ffcc00;
}
header {
    padding: 10px 20px;
    color: #fff;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#menu_bx {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

#menu_bx li {
    display: inline-block;
    margin-right: 20px;
}

#menu_bx li:last-child {
    margin-right: 0;
}

#menu_bx li a {
    text-decoration: none;
    color: #030303;
    font-weight: bold;
}

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
