import pymongo
from readability import ReaderClient
from readability import auth

consumer_key='OribeAbadSilva'
consumer_secret='UX8XRzJMgkmsqaaFTDX9yJFPA9bWrkp2'
parser_token='5a180fbd6d5c1338a44fa937320f9700f1a38475'
username='subcero000@gmail.com '
password='edward.1'
#(u'eXefzayksuGLSqP6ea', u'UPUM4ZddsKBrNe58e9Jb46tdg4CHdrZt')

def getAuth():
    s=auth.xauth(consumer_key=consumer_key,consumer_secret=consumer_secret,username=username,password=password);
    return s


cred=getAuth()

# If no client credentials are passed to ReaderClient's constructor, they
# will be looked for in your environment variables


coneccion = pymongo.MongoClient("localhost")
db = coneccion.readability
db.drop_collection("bookmarks")
datos=db.bookmarks
client = ReaderClient(token_key=cred[0],token_secret=cred[1],consumer_key=consumer_key,consumer_secret=consumer_secret)

print client
bookmarks_response = client.get_bookmarks()
print bookmarks_response.content

datos.insert(bookmarks_response.json())
