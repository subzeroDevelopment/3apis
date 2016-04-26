from flask import Flask,render_template,jsonify
from readability import ReaderClient
from readability import auth

#import getData,reqRead,request,reqZotero
from pymongo import MongoClient
import requests
from pyzotero import zotero
mongoClient = MongoClient('localhost',27017)

consumer_key='OribeAbadSilva'
consumer_secret='UX8XRzJMgkmsqaaFTDX9yJFPA9bWrkp2'
parser_token='5a180fbd6d5c1338a44fa937320f9700f1a38475'
username='subcero000@gmail.com '
password='edward.1'
#(u'eXefzayksuGLSqP6ea', u'UPUM4ZddsKBrNe58e9Jb46tdg4CHdrZt')

def getAuth():
    s=auth.xauth(consumer_key=consumer_key,consumer_secret=consumer_secret,username=username,password=password);
    return s

def actualizarReadability():
    cred=getAuth()

# If no client credentials are passed to ReaderClient's constructor, they
# will be looked for in your environment variables
    coneccion = mongoClient
    db = coneccion.readability
    db.drop_collection("bookmarks")
    datos=db.bookmarks
    client = ReaderClient(token_key=cred[0],token_secret=cred[1],consumer_key=consumer_key,consumer_secret=consumer_secret)

    print client
    bookmarks_response = client.get_bookmarks()
    print bookmarks_response.content

    datos.insert(bookmarks_response.json())


def actualizarZotero():
    zot = zotero.Zotero("3072464","user","zDIQE2HGasdIonUcrV8Dnsee")
    items = zot.top()
    print len(items)
    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    coneccion = mongoClient
    db = coneccion.zotero
    db.drop_collection("bookmarks")
    datos=db.bookmarks
    for item in items:
        print item["data"]["url"]
        datos.insert(item)


def actualizarPocket():
    r = requests.post('https://getpocket.com/v3/get', data = {'consumer_key':'53840-105632a57614ddf6e5d7ff84',"access_token":"f8e1b9ce-3b39-9004-1e25-a56ba7"})
    if r.status_code==requests.codes.ok:
        map=r.json()
        coneccion = mongoClient
        db = coneccion.pocket
        db.drop_collection("bookmarks")
        datos=db.bookmarks
#for key in map["list"]:
    #print map["list"][key]["resolved_title"]

        datos.insert(map)

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





app = Flask(__name__)

@app.route('/intro')
def index():
    datos=getPocket()
    datos.extend(getZotero())
    datos.extend(getReadability())
    return render_template('index2.html',data=datos)

@app.route('/actualizar')
def update():
    actualizarPocket()
    actualizarZotero()
    actualizarReadability()
    return jsonify({"status":"ok"})



if __name__ == '__main__':
    app.run(debug=True)
