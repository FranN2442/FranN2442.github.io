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
        <link rel="stylesheet" href="PaginaCategorias.css" type="text/css"/>
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
                            <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaObrea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
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
                             <p class="PAR">NALINE</p>
                        </div>
                    </div>
                </a>
                <a href="PaginaCarretera.html">
                    <div class="carretera">
                        <div class="wrap">
                            <h2 class="header2">CARRETERA</h2>
                             <p class="PAR">DSDSD</p>
                        </div>
                    </div>
                </a>
                <a href="PaginaE-Bike.html">
                    <div class="e-bike">
                        <div class="wrap">
                            <h2 class="header2">E-BIKE</h2>
                             <p class="PAR">HELP</p>
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
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
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
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaAGINACannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
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
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaAGINACannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="KTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
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

        <html class="pag_ind">
        <head>
            <title>TODO supply a title</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="Individuales.css" type="text/css"/>
        </head>
        <nav>
            <ul id="lista">
                <li><a href="PaginaCategorias.html">HOME</a></li>
                <li><a href="PaginaContacto.html">CONTACT</a></li>
                <li><a href="PaginaMTB.html">MTB</a></li>
                <li><a href="PaginaCarretera.html">CARRETERA</a></li>
                <li><a href="PaginaE-Bike.html">E-BIKE</a></li>
                <li><a>MARCAS</a>
                    <ul>
                        <li><a href="PaginaBH.html">BH</a></li>
                        <li><a href="PaginaCannondale.html">Cannondale</a></li>
                        <li><a href="PaginaCanyon.html">Canyon</a></li>
                        <li><a href="PaginaKTM.html">KTM</a></li>
                        <li><a href="PaginaMondraker.html">Mondraker</a></li>
                        <li><a href="PaginaOrbea.html">Orbea</a></li>
                        <li><a href="PaginaSpecialized.html">Specialized</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
        <body>
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
                <div id="txt">"""
        if item.get("type") == "MTB":
            html_content +="""    
                     <p class="PAR">Esta es la mejor bicicleta para la montaña, con {model}<br> podras ir por las zonas mas atrevidas de las montañas.<br> Ven y pruebala ya por {price_day} € al dia o {price_hour} € / hora. </p>   
                </div>  
            </div>
        </body>
    </html>""".format(model = item.get("model"), price_day = item.get("price day"), price_hour = item.get("price hour"))
        elif item.get("type") == "Carretera":

            html_content +="""    
                     <p class="PAR">Esta es la mejor bicicleta para carretera, con {model}<br> podras ir de ruta por donde quieras.<br> Ven y pruebala ya por {price_day} € al dia o {price_hour} € / hora. </p>   
                </div>  
            </div>
        </body>
    </html>""".format(model = item.get("model"), price_day = item.get("price day"), price_hour = item.get("price hour"))

        elif item.get("type") == "E-Bike":
            html_content +="""    
                     <p class="PAR">Esta es la mejor bicicleta correr sin esfuerzo, con {model}<br> podras ir por cuestas o rutas, que no te vas a cansar.<br> Ven y pruebala ya por {price_day} € al dia o {price_hour} € / hora. </p>   
                </div>  
            </div>
        </body>
    </html>""".format(model = item.get("model"), price_day = item.get("price day"), price_hour = item.get("price hour"))

        escribirHTML(item.get('serial'), html_content)

def PaginaOrbea(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                                    <li><a href="PaginaCannondale.html">Cannondale</a></li>
                                    <li><a href="PaginaCanyon.html">Canyon</a></li>
                                    <li><a href="PaginaKTM.html">KTM</a></li>
                                    <li><a href="PaginaMondraker.html">Mondraker</a></li>
                                    <li><a href="PaginaOrbea.html">Orbea</a></li>
                                    <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'Orbea':

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

    return escribirHTML("PaginaOrbea", html_content)


def PaginaBH(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'BH':

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

    return escribirHTML("PaginaBH", html_content)



def PaginaKTM(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'KTM':

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

    return escribirHTML("PaginaKTM", html_content)
        
def PaginaSpecialized(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'Specialized':

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

    return escribirHTML("PaginaSpecialized", html_content)

def PaginaCanyon(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'Canyon':

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

    return escribirHTML("PaginaCanyon", html_content)

        
        
def PaginaMondraker(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'Mondraker':

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

    return escribirHTML("PaginaMondraker", html_content)

def PaginaCannondale(items):
    html_content = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Rent Bike Mallorca</title>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="carretera.css" type="text/css"/>
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
                    <div id="contenedor">
                    """

    for item in items:
        if item.get('brand') == 'Cannondale':

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

    return escribirHTML("PaginaCannondale", html_content)

def PaginaContactar():

    html_content = """

    <!DOCTYPE html>
<html>

<head>
    <title>Rent Bike Mallorca</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="PaginaContacto.css" type="text/css" />
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
                                    <li><a href="PaginaBH.html">BH</a></li>
                            <li><a href="PaginaCannondale.html">Cannondale</a></li>
                            <li><a href="PaginaCanyon.html">Canyon</a></li>
                            <li><a href="PaginaKTM.html">KTM</a></li>
                            <li><a href="PaginaMondraker.html">Mondraker</a></li>
                            <li><a href="PaginaOrbea.html">Orbea</a></li>
                            <li><a href="PaginaSpecialized.html">Specialized</a></li>
                                </ul>
                            </li>
                        </ul>
                    </nav>
    <div id="contenedor">
        <div id="mapa">
            <h2>Dónde estamos?</h2>
            <p id="adress">Passeig Es Traves, 12, 07108 Port de Sóller, Illes Balears</p>
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d766.4025320709195!2d2.696090632855315!3d39.79330395954447!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1297e8be30444a15%3A0x1634a0ae00aa275f!2sTramuntana%20Tours!5e0!3m2!1ses!2ses!4v1670758715326!5m2!1ses!2ses"
                width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <div id="contacto" class="formulario">
            <h2>Contacto</h2>
            <form action="https://jkorpela.fi/cgi-bin/echo.cgi" method="post">
                <p>
                    <label for="nombre" class="colocar_nombre">Nombre
                        <span class="obligatorio">*</span>
                    </label>
                    <input type="text" name="introducir_nombre" id="nombre" required="obligatorio"
                        placeholder="Escribe tu nombre">
                </p>

                <p>
                    <label for="email" class="colocar_email">Email
                        <span class="obligatorio">*</span>
                    </label>
                    <input type="email" name="introducir_email" id="email" required="obligatorio"
                        placeholder="Escribe tu Email">
                </p>

                <p>
                    <label for="telefone" class="colocar_telefono">Teléfono
                    </label>
                    <input type="tel" name="introducir_telefono" id="telefono" placeholder="Escribe tu teléfono">
                </p>

                <p>
                    <label for="website" class="colocar_website">Sitio web
                    </label>
                    <input type="url" name="introducir_website" id="website" placeholder="Escribe la URL de tu web">
                </p>

                <p>
                    <label for="asunto" class="colocar_asunto">Asunto
                        <span class="obligatorio">*</span>
                    </label>
                    <input type="text" name="introducir_asunto" id="assunto" required="obligatorio"
                        placeholder="Escribe un asunto">
                </p>

                <p>
                    <label for="mensaje" class="colocar_mensaje">Mensaje
                        <span class="obligatorio">*</span>
                    </label>
                    <textarea name="introducir_mensaje" class="texto_mensaje" id="mensaje" required="obligatorio"
                        placeholder="Deja aquí tu comentario..."></textarea>
                </p>

                <button type="submit" name="enviar_formulario" id="enviar">
                    <p>Enviar</p>
                </button>

                <p class="aviso">
                    <span class="obligatorio"> * </span>los campos son obligatorios.
                </p>
            </form>
        </div>
    </div>
</body>
    
    """
    return escribirHTML("PaginaContacto", html_content)