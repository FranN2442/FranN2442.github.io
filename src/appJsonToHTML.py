import json

def escribirHTML(nombre, contenido):

    with open("html/" + nombre + ".html", "w+") as html_file:
        html_file.write(contenido)
        print("HTML file created successfully")

def cargarDatos(ruta='DataBase/bicisCarretera.json'):
    with open(ruta) as contenido:
        jsondoc = json.load(contenido)
        mainkey = jsondoc.get('documents')
        return mainkey

def PaginaCategorias(items):

    html_content = f"""
     <!DOCTYPE html>
    <html>
    <head>
        <title>Rent Bike Mallorca</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../css/PaginaCategorias.css" type="text/css"/>
    </head>
    <body>
        <header>
            <div id="presentacion">
                <h1>Bienvenidos a<br>Bike Rental</h1>
            </div>
        </header>
        <div id="contenedor">
            <a href="PaginaMTB.html">
                <div class="mtb">
                    <div class="wrap">
                        <h2>MOUNTAIN BIKE</h2>
                        <p>LOVE TO ADRENALINE</p>
                    </div>
                </div>
            </a>
            <a href="PaginaCarretera.html">    
                <div class="carretera">
                    <div class="wrap">
                        <h2>CARRETERA</h2>
                        <p>LOVE TO RIDE</p>
                    </div>
                </div>
            </a>
            <a href="PaginaE-Bike.html">
                <div class="e-bike">
                    <div class="wrap">
                        <h2>E-BIKE</h2>
                        <p>RIDE WITH E-HELP</p>
                    </div>
                </div>
            </a>
        </div>
    </body>
</html>"""

    escribirHTML("PaginaCategorias",html_content)
    
if __name__ == "__main__":
    
    items = cargarDatos()

    PaginaCategorias(items)
