import requests,pymongo
from requests.auth import HTTPBasicAuth


data = {"resourcetype":"bookmark","format":"json","user":"subzero"}
auth=HTTPBasicAuth("subzero","6124d682bb73da8bb5269fe475e85a2f")
r = requests.get('http://www.bibsonomy.org/api/posts',auth=auth,params=data)
print r.url
print r.status_code
if r.status_code==requests.codes.ok:
    map=r.json()
    #coneccion = pymongo.MongoClient("localhost")
    #db = coneccion.pocket
    #db.drop_collection("bookmarks")
    #datos=db.bookmarks
#for key in map["list"]:
    #print map["list"][key]["resolved_title"]

    #datos.insert(map)


#https://getpocket.com/auth/authorize?request_token=e626939d-8b33-c987-1bcf-9216de&redirect_uri=http://www.google.com
