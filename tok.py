import requests

r = requests.post('https://getpocket.com/v3/oauth/request', data = {'consumer_key':'53840-105632a57614ddf6e5d7ff84',"redirect_uri":"http://www.google.com"})


print(r.text)
