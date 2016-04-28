import requests,pymongo

def actualizar():
    r = requests.post('https://getpocket.com/v3/get', data = {'consumer_key':'53840-105632a57614ddf6e5d7ff84',"access_token":"f8e1b9ce-3b39-9004-1e25-a56ba7"})
    if r.status_code==requests.codes.ok:
        mapa=r.json()
        for key in mapa["list"]:
            for q in mapa["list"][key]:
                print mapa["list"][key]["resolved_title"]
        """coneccion = pymongo.MongoClient("localhost")
        db = coneccion.pocket
        db.drop_collection("bookmarks")
        datos=db.bookmarks
#for key in map["list"]:
    #print map["list"][key]["resolved_title"]

        datos.insert(map)"""

actualizar()


#https://getpocket.com/auth/authorize?request_token=e626939d-8b33-c987-1bcf-9216de&redirect_uri=http://www.google.com
