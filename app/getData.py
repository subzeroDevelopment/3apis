from pymongo import MongoClient

mongoClient = MongoClient('localhost',27017)

def getPocket():
    db = mongoClient.pocket
    collection = db.bookmarks
    cursor = collection.find()
    arr=[]
    for bookmark in cursor:
        for b in bookmark["list"]:
            ob={}
            ob["titulo"]=bookmark["list"][b]["resolved_title"]
            ob["url"]=bookmark["list"][b]["resolved_url"]
            ob["abstract"]=bookmark["list"][b]["excerpt"]
            arr.append(ob)

    return arr

"""a=getPocket()
print len(a)"""

def getZotero():
    db = mongoClient.zotero
    collection = db.bookmarks
    cursor = collection.find()
    arr=[]
    for bookmark in cursor:
        ob={}
        ob["titulo"]=bookmark["data"]["title"]
        ob["url"]=bookmark["data"]["url"]
        ob["abstract"]=bookmark["data"]["abstractNote"]
        arr.append(ob)

    return arr

"""a=getZotero()
print len(a)"""
def getReadability():
    db = mongoClient.readability
    collection = db.bookmarks
    cursor = collection.find()
    arr=[]
    for bookmark in cursor:
        ob={}
        for item in bookmark["bookmarks"]:
            ob["titulo"]=item["article"]["title"]
            ob["url"]=item["article"]["url"]
            ob["abstract"]=item["article"]["excerpt"]
            arr.append(ob)

    return arr

#a=getReadability()
#print len(a)
