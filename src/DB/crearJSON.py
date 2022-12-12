import json

def crearJSON(bicisCarretera):


    apiToJson = open("DataBase/bicisCarretera.json", "w+", encoding="UTF-8")
    
    apiToJson.write(bicisCarretera)

    print ( "El documento ha sido creado correctamente" )