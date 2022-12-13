import pymongo
from src.DB.ApiMongoDB import ApiMongoDB
from src.appJsonToHTML import PaginasIndividuales, cargarDatos,PaginaBH,PaginaOrbea,PaginaPrincipalCarretera,PaginaPrincipalEbike,PaginaPrincipalMTB 

items = cargarDatos()

myclient = pymongo.MongoClient("mongodb+srv://Fran:20Fran04.@bikecluster.fvhjzpv.mongodb.net/test")
mydb = myclient["BikesRentalDB"]
mycol = mydb["AllBikesCollection"]


def funciones():
    print ("""

Que deseas realizar?
    -Editar
    -Eliminar
    -Insertar   
---------------------
    """)
    funcion = input()

    if funcion == "Editar":

        editBikes()
    elif funcion == "Eliminar":
            deleteBikes()
    elif funcion == "Insertar":
            insertBikes()

        
    
def deleteBikes():
    valor = input("ID de la bicicleta?")

    myquery = {  "_id" : valor }
    
    mycol.delete_one(myquery)


    PaginasIndividuales(items),PaginaBH(items)
    PaginaOrbea(items),PaginaPrincipalCarretera(items)
    PaginaPrincipalEbike(items),ApiMongoDB()
    PaginaPrincipalMTB(items)

def insertBikes():

    max_id = mycol.find_one(sort=[("_id", pymongo.DESCENDING)])
    _id = int(max_id.get("_id")) + 1
    _id = str(_id).zfill(4)
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

    PaginasIndividuales(items),PaginaBH(items)
    PaginaOrbea(items),PaginaPrincipalCarretera(items)
    PaginaPrincipalEbike(items),ApiMongoDB()
    PaginaPrincipalMTB(items)

    

def editBikes():

    numero = input("Introduzca el numero de serie de la bici que desea editar: ")

    filterBySerial = {"serial" : numero}

    print (mycol.find_one(filterBySerial))

    valor = input("Que caracteristica desea editar? ")

    cambio = input("Introduzca el cambio: ")

    conf = input("Estas seguro del cambio? (S/N)")

    if conf == "S":
    
        newvalues = {"$set" :{valor : cambio}}
    
        mycol.update_one(filterBySerial, newvalues)

        print ("El cambio ha sido realizado correctamente!")

    else:

        print ("Volviendo ha editar...")
        return editBikes()

    


if __name__ == '__main__':

   funciones()



