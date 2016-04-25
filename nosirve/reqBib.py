import bibsonomy


user="subzero"
# get your API key at http://www.bibsonomy.org/settings?selTab=1
json_source = bibsonomy.RestSource(user,'6124d682bb73da8bb5269fe475e85a2f')
bib = bibsonomy.BibSonomy(json_source)

posts = bib.getPostsForUser("bookmark",user, None, 0, 10);

for post in posts:
    bookmark = post.resource
    print(bookmark.title)
