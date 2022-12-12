import json
import os


def escribirHTML(nombre, contenido):

    with open("html/" + nombre + ".html", "w+") as html_file:
        html_file.write(contenido)
        print("HTML file created successfully")


def cargarDatos(ruta='DataBase/bicisCarretera.json'):
    with open(ruta) as contenido:
        jsondoc = json.load(contenido)
        mainkey = jsondoc.get('documents')
        return mainkey


def CheckWrite():
    os.path.exists("../html/PaginaCategorias.html")


print("Existe")


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
        <section>
            <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                </ul>
            </nav>
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
        </section>
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
                    <nav>
                        <ul id="lista">
                            <li><a href="PaginaCategorias.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                        </ul>
                    </nav>
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
                    <nav>
                        <ul id="lista">
                            <li><a href="PaginaCategorias.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'CARRETERA':

            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
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


def PaginaPrincipalEbike(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="../css/ebike.css" type="text/css"/>
                </head>

                <body>
                    <nav>
                        <ul id="lista">
                            <li><a href="PaginaCategorias.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'E-Bike':

            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
        else:
            pass
    html_content += """
                </div>
            </body>
        </html>"""

    escribirHTML("PaginaE-Bike", html_content)


def PaginasIndividuales(items):
    for item in items:
        html_content = f"""
     <!DOCTYPE html>

    <html>
        <head>
            <title>TODO supply a title</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
        </head>
        <body>
            <nav>
                <ul id="lista">
                    <li><a href="../PaginaCategorias.html">HOME</a></li>
                    <li><a href="../PaginaContacto.html">CONTACT</a></li>
                    <li><a href="../PaginaMTB.html">MTB</a></li>
                    <li><a href="../PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="../PaginaE-Bike.html">E-BIKE</a></li>
                </ul>
            </nav>
            <h1>{item.get('brand')}:{item.get('model')}</h1>

            <div id="contenedor">
                <div id="imagen">
                    <img src="https://labicicleta.net/media/catalog/product/cache/1/small_image/295x/602f0fa2c1f0d1ba5e241f914e856ff9/t/r/trek_marlin_8_2022_rojo_.png" alt="Descripción de la imagen">
                </div>
            </div>"""
        for k, v in item.items():
            html_content += """
                <div id="tabla">
                    <table class="default">
                            <colgroup>
                                <col span="1" style="background-color: #79b8db">
                            </colgroup>"""
        for k, v in item.items():
            html_content += """
                        <tr>
                            <td><b>%s</b></td>
                            <td>%s</td>
                        </tr>
                        """ % (k, v)
        html_content += """
                    </table>
                </div>
            </div>
        </body>
    </html>"""
        escribirHTML("PaginasIndividuales/" + item.get('serial'), html_content)


def PaginaOrbea(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'ORBEA':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand = item.get('brand')
            escribirHTML(brand, html_content)
        else:
            pass


def PaginaBH(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'BH':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand = item.get('brand')
            escribirHTML(brand, html_content)
        else:
            pass


def PaginaKTM(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'KTM':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand=item.get('brand')
            escribirHTML(brand, html_content)                
        else:
            pass

def PaginaSpecialized(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'specialized':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand=item.get('brand')
            escribirHTML(brand, html_content)                
        else:
            pass

def PaginaCanyon(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'Canyon':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand=item.get('brand')
            escribirHTML(brand, html_content)                
        else:
            pass

def PaginaMondraker(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="css\Individuales.css" type="text/css"/>
            </head>
            <body>
                <nav>
                    <ul id="lista">
                        <li><a href="PaginaCategorias.html">HOME</a></li>
                        <li><a href="PaginaContacto.html">CONTACT</a></li>
                        <li><a href="PaginaMTB.html">MTB</a></li>
                        <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                        <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    </ul>
                </nav>"""
    for item in items:
        if item.get('brand') == 'Mondraker':
            html_content += """
                <a id="link" href="PaginasIndividuales/{serial}.html">
                    <div class="box"> 
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                        <p id="divText">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            brand=item.get('brand')
            escribirHTML(brand, html_content)                
        else:
            pass
    


if __name__ == "__main__":

    items = cargarDatos()

    PaginaCategorias(items)

    PaginaPrincipalMTB(items)

    PaginaPrincipalCarretera(items)

    PaginaPrincipalEbike(items)

    PaginasIndividuales(items)

    PaginaOrbea(items)
    
    PaginaBH(items)
    
    PaginaKTM(items)
    
    PaginaSpecialized(items)
    
    PaginaCanyon(items)
    
    PaginaMondraker(items)