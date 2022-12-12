import requests
import json

def ApiMongoDB():
  url = "https://data.mongodb-api.com/app/data-qnzsx/endpoint/data/v1/action/find"
  payload = json.dumps({
    "collection": "AllBikesCollection",
    "database": "BikesRentalDB",
    "dataSource": "BikeCluster",
    "filter": {
        
    }
  })
  headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ldV69gv9eH4MIthyClLbY958QB6MFBJNClLGihKWAkUyqOKvDGnyfX3YKpc6I8I0",
  'Accept': 'application/ejson' 
  }
  try:
    bicisCarretera = requests.post(url, headers=headers, data=payload)
    bicisCarretera = bicisCarretera.text
    bicisCarretera = json.loads(bicisCarretera)
  except requests.exceptions.ConnectTimeout:
    print ("Timeout Error")
    SystemExit()
  else:
    print ("Conexion realizada con exito!")
    return bicisCarretera

  
