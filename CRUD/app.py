import pymongo
import os
from src.appJsonToHTML import cargarDatos
from src.DB.ApiMongoDB import ApiMongoDB
from src.appJsonToHTML import PaginaCanyon as CanyonHTML, PaginaBH as BhHTML, PaginaCategorias, PaginaKTM as KTMHtml, PaginaMondraker as MondrakerHTML , PaginaOrbea as ObreaHTML, PaginaPrincipalCarretera as CarreteraHTML , PaginaPrincipalEbike as EBikeHTML , PaginaPrincipalMTB as MTBhtml , PaginasIndividuales as IndiviHTML , PaginaSpecialized as SpezHTML , PaginaCannondale, PaginaContactar

myclient = pymongo.MongoClient("mongodb+srv://Fran:20Fran04.@bikecluster.fvhjzpv.mongodb.net/test")
mydb = myclient["BikesRentalDB"]
mycol = mydb["AllBikesCollection"]


def funciones():

    ApiMongoDB()

    items = cargarDatos()

    print ("""
  <............................>
    Que deseas realizar?     |
        -Editar              |
        -Eliminar            |
        -Insertar            |
        -Ejecutar Programa   |
  <---------------------------->
    """)
    funcion = input()

    if funcion == "Editar":

        editBikes()
    elif funcion == "Eliminar":
            deleteBikes()
    elif funcion == "Insertar":
            insertBikes()
    elif funcion == "Ejecutar Programa":

            try:    
                BhHTML(items),CanyonHTML(items),
                PaginaCategorias(items),SpezHTML(items),
                MondrakerHTML(items),ObreaHTML(items),
                EBikeHTML(items),IndiviHTML(items),
                MTBhtml(items),CarreteraHTML(items),PaginaCannondale(items),
                KTMHtml(items),PaginaContactar()

            except:
                print ("Algo a sucedido en el programa!")

                return exit



def deleteBikes():

    valor = input("Que bicicleta quieres eliminar?")

    myquery = {  "_id" : valor }

    mycol.delete_one(myquery)

    ApiMongoDB()

def insertBikes():

    _id = input("Introduzaca el ID: ")
    material = input("Material de la bicicleta: ")
    marca = input("Cual es la marca? ")
    grupo_piñon = input("Grupo del piñon? ")
    modelo = input("Modelo de la bicicleta?")
    talla = input("Que talla tiene? ")
    transmision = input("Tipo de transmisión: ")
    peso = input("Que pesa la bicicleta? ¡Introduzca solo el numero!")
    p_dia = input("Que cuesta la bicicleta por dia? ")
    p_hora = input("Que custa por hora? ")
    loc = input("En que localidad esta disponible? ")
    disp = input("Esta disponible? ")
    serial = input("Introduzca el numero de serie: ")
    tipo = input("""
        Que tipo de bicicleta es? 
            - Carretera
            - MTB
            - E-Bike
        Introduzca el resultado: """)

    myquery = { 

                "_id" : _id,
                "material" : material, 
                "brand" : marca, 
                "group_sproket" : grupo_piñon,
                "modelo" : modelo,
                "size" : talla,
                "transmission" : transmision,
                "weight" : peso,
                "price_day" : p_dia,
                "price_hour" : p_hora,
                "location" : loc,
                "avaiable" : disp,
                "serial" : serial,
                "type" : tipo

                }

    mycol.insert_one(myquery)

    ApiMongoDB()

def editBikes():

    numero = input("Introduzca el numero de serie de la bici que desea editar: ")

    filtro = {"serial" : numero}

    print (mycol.find_one(filtro))

    valor = input("Que caracteristica desea editar? ")

    cambio = input("Introduzca el cambio: ")

    conf = input("Estas seguro del cambio? (S/N)")

    if conf == "S":

        newvalues = {"$set" :{valor : cambio}}

        mycol.update_one(filtro, newvalues)

        print ("El cambio ha sido realizado correctamente!")

        ApiMongoDB()

    else:

        print ("Volviendo ha editar...")
        return editBikes()




if __name__ == '__main__':

   funciones()
