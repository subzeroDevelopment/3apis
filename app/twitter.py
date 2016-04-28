import tweepy

def getTweets(tag):
    cons_key="riGxHsH7FmnEuj5EzuxcRhF34"
    cons_secret="HOrz0GsyDysZbhPyph9P3N7SMxkHbqhl6yFZ1YmF1WETO6sO7p"
    acc_token="2269290260-JinauwfnXKLFuLRiBa27JKaeeEEjYl2121U1XH1"
    acc_token_secret="3H0wZiWAZtBPWFhbcOhqlSrCFjxkK1JftVEoPk65uHZSs"
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_token_secret)
    arre=[]
    api = tweepy.API(auth)
    search=api.search(tag,show_user=True)
    for tweet in search:
        obj={}
        obj["text"]=tweet.text
        obj["user"]=tweet.user.screen_name
        obj["img"]=tweet.user.profile_image_url
        arre.append(obj)
    return arre

t=getTweets("Crystal")
print t
