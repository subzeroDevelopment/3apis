"""from libZotero import zotero

#zlib=zotero.Library('group','3072464','<null>','zDIQE2HGasdIonUcrV8Dnsee')
zlib=zotero.Library('user','3072464','<null>','zDIQE2HGasdIonUcrV8Dnsee')
items = zlib.fetchItemsTop({'limit': 5, 'content': 'json,bib,coins'})

for item in items:
    print 'Item Type: %s | Key: %s | Title: %s' % (item.itemType,item.itemKey, item.title)
    #print item.url
    print item.bibContent
"""
from pyzotero import zotero
import pymongo

def actualizar():
    zot = zotero.Zotero("3072464","user","zDIQE2HGasdIonUcrV8Dnsee")
    items = zot.top()
    print len(items)
    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    """coneccion = pymongo.MongoClient("localhost")
    db = coneccion.zotero
    db.drop_collection("bookmarks")
    datos=db.bookmarks"""
    for item in items:
        print item["data"]["title"]
        #datos.insert(item)

actualizar()
#for key in map["list"]:
    #print map["list"][key]["resolved_title"]
