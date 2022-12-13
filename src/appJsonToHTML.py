import json
import os


def escribirHTML(nombre, contenido):

    with open("docs/" + nombre + ".html", "w+") as html_file:
        html_file.write(contenido)
        print("HTML file created successfully")



def cargarDatos(ruta='DataBase/bicisCarretera.json'):
    with open(ruta) as contenido:
        jsondoc = json.load(contenido)
        mainkey = jsondoc.get('documents')
        return mainkey


def CheckWrite():
    os.path.exists("../index.html")



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
                    <li><a href="index.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            <header class="Presentacion">
                <div id="presentacion">
                    <h1>Bienvenidos a<br>Bike Rental</h1>
                </div>
            </header>
            <div id="contenedor">
                <a href="PaginaMTB.html">
                    <div class="mtb">
                        <div class="wrap">
                            <h2 class="header2">MOUNTAIN BIKE</h2>
                             <p class="PAR"NALINE</p>
                        </div>
                    </div>
                </a>
                <a href="PaginaCarretera.html">
                    <div class="carretera">
                        <div class="wrap">
                            <h2 class="header2">CARRETERA</h2>
                             <p class="PAR"</p>
                        </div>
                    </div>
                </a>
                <a href="PaginaE-Bike.html">
                    <div class="e-bike">
                        <div class="wrap">
                            <h2 class="header2">E-BIKE</h2>
                             <p class="PAR"HELP</p>
                        </div>
                    </div>
                </a>
            </div>
        </section>
    </body>
</html>"""

    return escribirHTML("index", html_content)


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
                            <li><a href="index.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                        </ul>
                    </nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'MTB':

            html_content += """
                <a id="link" href="{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                         <p class="PAR">{brand}: {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
    html_content += """
                </body>
            </html>"""

    return escribirHTML("PaginaMTB", html_content)


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
                            <li><a href="index.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                            <li><a>MARCAS</a>
                                <ul>
                                    <li><a href="BH.html">BH</a></li>
                                    <li><a href="Cannondale.html">Cannondale</a></li>
                                    <li><a href="Canyon.html">Canyon</a></li>
                                    <li><a href="KTM.html">KTM</a></li>
                                    <li><a href="Mondraker.html">Mondraker</a></li>
                                    <li><a href="ORBEA.html">Orbea</a></li>
                                    <li><a href="specialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'CARRETERA':

            html_content += """
                <a id="link" href="{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                         <p class="PAR">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
        else:
            pass
    html_content += """
                </div>
            </body>
        </html>"""

    return escribirHTML("PaginaCarretera", html_content)


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
                            <li><a href="index.html">HOME</a></li>
                            <li><a href="PaginaContacto.html">CONTACT</a></li>
                            <li><a href="PaginaMTB.html">MTB</a></li>
                            <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                            <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                            <li><a>MARCAS</a>
                                <ul>
                                    <li><a href="BH.html">BH</a></li>
                                    <li><a href="Cannondale.html">Cannondale</a></li>
                                    <li><a href="Canyon.html">Canyon</a></li>
                                    <li><a href="KTM.html">KTM</a></li>
                                    <li><a href="Mondraker.html">Mondraker</a></li>
                                    <li><a href="ORBEA.html">Orbea</a></li>
                                    <li><a href="specialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('type') == 'E-Bike':

            html_content += """
                <a id="link" href="{serial}.html">
                    <div class="box">
                        <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0">
                         <p class="PAR">{brand} : {model}</p>
                    </div>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
        else:
            pass
    html_content += """
                </div>
            </body>
        </html>"""

    return escribirHTML("PaginaE-Bike", html_content)


def PaginasIndividuales(items):
    for item in items:
        html_content = f"""
        <!DOCTYPE html>

        <html>
        <head>
            <title>TODO supply a title</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="../css/Individuales.css" type="text/css"/>
        </head>
        <body>
            <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            <h1 class="title"> {item.get('brand')}:{item.get('model')}</h1>
            <div id="contenedor">
                <div id="imagen">
                    <img src="{item.get('imagen')}" alt="Descripcion de la imagen">
                </div>
                <div id="tabla">
                    <table>
                            <colgroup>
                                <col span="1" style="background-color: #79b8db">
                            </colgroup>
                        <thead>  
                            <tr>
                            
                                <th>Caracteristicas</th>
                                
                            </tr>
                        </thead>
                        <tbody>"""
                        
        for k, v in item.items():
            html_content += """
                        <tr>
                            <td><b>%s</b></td>
                            <td>%s</td>
                        </tr>
                        """ % (k, v)
        html_content += """
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="contenedor2">
                
                <div>
                    
                    <h1>UN POCO MAS SOBRE LA BICICLETA</h1>        
                </div>
                <div id="txt">
                    
                     <p class="PAR"fffffffffffffffffffff</p>   
                </div>  
            </div>
        </body>
    </html>"""
        escribirHTML(item.get('serial'), html_content)

def PaginaOrbea(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'Orbea':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
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
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'BH':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
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
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'KTM':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
            brand = item.get('brand')
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
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'specialized':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
            brand = item.get('brand')
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
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'Canyon':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
            brand = item.get('brand')
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
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'Mondraker':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>
                </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
            brand = item.get('brand')
            escribirHTML(brand, html_content)
        else:
            pass

def PaginaCannondale(items):
    html_content = """
        <!DOCTYPE html>

        <html>
            <head>
                <title>TODO supply a title</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="estilos.css" type="text/css"/>
            </head>
            <body>
                <nav>
                <ul id="lista">
                    <li><a href="PaginaCategorias.html">HOME</a></li>
                    <li><a href="PaginaContacto.html">CONTACT</a></li>
                    <li><a href="PaginaMTB.html">MTB</a></li>
                    <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                    <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                    <li><a>MARCAS</a>
                        <ul>
                            <li><a href="BH.html">BH</a></li>
                            <li><a href="Cannondale.html">Cannondale</a></li>
                            <li><a href="Canyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="Mondraker.html">Mondraker</a></li>
                            <li><a href="ORBEA.html">Orbea</a></li>
                            <li><a href="specialized.html">Specialized</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
                <div class="contenedorMarca">"""
    for item in items:
        if item.get('brand') == 'Cannondale':
            html_content += """
                    <a id="link" href="{serial}.html">
                        <div class="box">
                            <img class="img" src="https://contents.mediadecathlon.com/p2091636/k$cc0790528e1a07724f38362c6dc52705/sq/bicicleta-de-montaa-29-aluminio-ntt-sport-60-rojo.jpg?format=auto&f=800x0%22%3E">
                             <p class="PAR">{brand} : {model}</p>
                        </div>
                    </a>""".format(model=item.get('model'), brand=item.get('brand'), serial=item.get('serial'))
            html_content += """
                    </div>
                </body>
            </html>"""
            brand = item.get('brand')
            escribirHTML(brand, html_content)
        else:
            pass
