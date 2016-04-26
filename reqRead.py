from readability import ReaderClient
import pymongo

token="eXefzayksuGLSqP6ea"
secret="UPUM4ZddsKBrNe58e9Jb46tdg4CHdrZt"

# If no client credentials are passed to ReaderClient's constructor, they
# will be looked for in your environment variables
coneccion = pymongo.MongoClient("localhost")
db = coneccion.readability
db.drop_collection("bookmarks")
datos=db.bookmarks

client = ReaderClient(token_key=token,token_secret=secret)
bookmarks_response = client.get_bookmarks()

datos.insert(bookmarks_response.json())
