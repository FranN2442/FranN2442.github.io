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

    escribirHTML("PaginaCategorias", html_content)


def PaginaPrincipalMTB(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="../css/mtb.css" type="text/css"/>
                </head>

                <body>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'MTB':

            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand}: {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
    html_content += """
                </body>
            </html>"""

    escribirHTML("PaginaMTB", html_content)


def PaginaPrincipalCarretera(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="../css/carretera.css" type="text/css"/>
                </head>

                <body>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'CARRETERA':

            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E"
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
        else:
            pass
    html_content += """
                </div>
            </body>
        </html>"""

    escribirHTML("PaginaCarretera", html_content)


if __name__ == "__main__":

    items = cargarDatos()

    PaginaCategorias(items)

    PaginaPrincipalMTB(items)
    
    PaginaPrincipalCarretera(items)
