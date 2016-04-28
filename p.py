from pymongo import MongoClient


def getReadability():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient.readability
    collection = db.bookmarks
    cursor = collection.find()
    arr=[]
    for bookmark in cursor:
        for item in bookmark["bookmarks"]:
            ob={}
            ob["titulo"]=item["article"]["title"]
            ob["url"]=item["article"]["url"]
            ob["abstract"]=item["article"]["excerpt"]
            arr.append(ob)

    return arr

x=getReadability()
print x
