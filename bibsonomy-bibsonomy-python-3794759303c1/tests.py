#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import bibsonomy

class TestRefParser(unittest.TestCase):
    """
    unit tests
    """

    def setUp(self):
        self.json = TestJsonSource()
        self.bib = bibsonomy.BibSonomy(self.json)

    def test_get_posts_for_user_bookmark(self):
        posts = self.bib.getPostsForUser("bookmark", "jaeschke", ["myown"], 0, 1)
        self.assertEqual(2, len(posts))
        # check first post
        self.assertEqual("jaeschke", posts[0].user.name)
        self.assertEqual("15th Discovery Challenge | organized in conjunction with ECML PKDD 2013", posts[0].resource.title)

    def test_get_posts_for_user_bibtex(self):
        posts = self.bib.getPostsForUser("bibtex", "jaeschke", ["myown"], 0, 1)
        self.assertEqual(1, len(posts))
        # check first post
        self.assertEqual("jaeschke", posts[0].user.name)
        self.assertEqual("Data", posts[0].resource.extraurls[0].title)

    def test_get_posts_for_tags(self):
        posts = self.bib.getPostsForTag("bookmark", ["web"], 0, 3)
        self.assertEqual(3, len(posts))
        # check first post
        self.assertEqual("c", posts[0].user.name)
        # only public posts are returned
        self.assertEqual("public", posts[0].groups[0])


class TestJsonSource:
    """
    Returns constant JSON strings for testing purposes.
    """
    
    def get_max_posts_per_request(self):
        return 3

    def getPostsForTag(self, resource_type, tags, start, end):
        if "bookmark" == resource_type:
            return """
{
   "posts" : {
      "end" : 3,
      "post" : [
         {
            "user" : {
               "href" : "http://www.bibsonomy.org/api/users/c",
               "name" : "c"
            },
            "description" : "material",
            "postingdate" : "2014-11-11T14:55:44.000+01:00",
            "tag" : [
               {
                  "href" : "http://www.bibsonomy.org/api/tags/button",
                  "name" : "button"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/free",
                  "name" : "free"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/icon",
                  "name" : "icon"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/vector",
                  "name" : "vector"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/web",
                  "name" : "web"
               }
            ],
            "changedate" : "2014-11-11T14:55:44.000+01:00",
            "bookmark" : {
               "href" : "http://www.bibsonomy.org/api/users/c/posts/f3aa90a88a166f0a4e6a8afef78cddcb",
               "url" : "http://www.example.org/2014/",
               "interhash" : "f3aa90a88a166f0a4e6a8afef78cddcb",
               "title" : "Icon",
               "intrahash" : "f3aa90a88a166f0a4e6a8afef78cddcb"
            }
         },
         {
            "description" : "File",
            "postingdate" : "2014-11-11T14:55:39.000+01:00",
            "tag" : [
               {
                  "name" : "button",
                  "href" : "http://www.bibsonomy.org/api/tags/button"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/free",
                  "name" : "free"
               },
               {
                  "name" : "icon",
                  "href" : "http://www.bibsonomy.org/api/tags/icon"
               },
               {
                  "href" : "http://www.bibsonomy.org/api/tags/vector",
                  "name" : "vector"
               },
               {
                  "name" : "web",
                  "href" : "http://www.bibsonomy.org/api/tags/web"
               }
            ],
            "user" : {
               "name" : "clementchiew",
               "href" : "http://www.bibsonomy.org/api/users/c"
            },
            "bookmark" : {
               "href" : "http://www.bibsonomy.org/api/users/c/posts/f19c472f4d883c24ea1392c1285e700d",
               "url" : "http://www.example.org/download/",
               "interhash" : "f19c472f4d883c24ea1392c1285e700d",
               "intrahash" : "f19c472f4d883c24ea1392c1285e700d",
               "title" : "Web"
            },
            "changedate" : "2014-11-11T14:55:39.000+01:00"
         },
         {
            "tag" : [
               {
                  "name" : "Development",
                  "href" : "http://www.bibsonomy.org/api/tags/Development"
               },
               {
                  "name" : "Web",
                  "href" : "http://www.bibsonomy.org/api/tags/Web"
               }
            ],
            "postingdate" : "2014-11-07T07:11:49.000+01:00",
            "description" : "applications",
            "user" : {
               "href" : "http://www.bibsonomy.org/api/users/g",
               "name" : "g"
            },
            "bookmark" : {
               "url" : "http://www.example.com/",
               "href" : "http://www.bibsonomy.org/api/users/g/posts/0913c9a1307272bf2287a1b72b8247e3",
               "title" : "stay connected",
               "intrahash" : "0913c9a1307272bf2287a1b72b8247e3",
               "interhash" : "0913c9a1307272bf2287a1b72b8247e3"
            },
            "changedate" : "2014-11-07T07:11:49.000+01:00"
         }
      ],
      "next" : "http://www.bibsonomy.org/api/posts?start=3&end=6&resourcetype=bookmark&tags=web",
      "start" : 0
   },
   "stat" : "ok"
}
"""
        if "bibtex" == resource_type:
            return """
"""

    def getPostsForUser(self, resource_type, user_name, tags, start, end):
        if "bookmark" == resource_type:
            return """
{
  "posts":{
    "post":[
      {
        "user":{
          "name":"jaeschke",
          "href":"http://www.bibsonomy.org/api/users/jaeschke"},
        "group":[{
          "name":"public",
          "href":"http://www.bibsonomy.org/api/groups/public"}],
        "tag":[
          {"name":"2013","href":"http://www.bibsonomy.org/api/tags/2013"},
          {"name":"challenge","href":"http://www.bibsonomy.org/api/tags/challenge"},
          {"name":"dc13","href":"http://www.bibsonomy.org/api/tags/dc13"},
          {"name":"discovery","href":"http://www.bibsonomy.org/api/tags/discovery"},
          {"name":"ecmlpkdd","href":"http://www.bibsonomy.org/api/tags/ecmlpkdd"},
          {"name":"myown","href":"http://www.bibsonomy.org/api/tags/myown"},
          {"name":"recommender","href":"http://www.bibsonomy.org/api/tags/recommender"}
        ],
        "bookmark":{
          "title":"15th Discovery Challenge | organized in conjunction with ECML PKDD 2013",
          "url":"http://www.kde.cs.uni-kassel.de/ws/dc13/",
          "interhash":"1bea279aaa24fd28808e03c151894c69",
          "intrahash":"1bea279aaa24fd28808e03c151894c69",
          "href":"http://www.bibsonomy.org/api/users/jaeschke/posts/1bea279aaa24fd28808e03c151894c69"
        },
        "postingdate":"2013-02-27T19:29:12.000+01:00",
        "changedate":"2013-02-27T19:29:12.000+01:00"
      },
      {
        "user":{"name":"jaeschke","href":"http://www.bibsonomy.org/api/users/jaeschke"},
        "group":[{"name":"public","href":"http://www.bibsonomy.org/api/groups/public"}],
        "tag":[
          {"name":"challenge","href":"http://www.bibsonomy.org/api/tags/challenge"},
          {"name":"dc09","href":"http://www.bibsonomy.org/api/tags/dc09"},
          {"name":"discovery","href":"http://www.bibsonomy.org/api/tags/discovery"},
          {"name":"ecmlpkdd","href":"http://www.bibsonomy.org/api/tags/ecmlpkdd"},
          {"name":"myown","href":"http://www.bibsonomy.org/api/tags/myown"},
          {"name":"recommender","href":"http://www.bibsonomy.org/api/tags/recommender"}
        ],
        "bookmark":{
          "title":"11th Discovery Challenge",
          "url":"http://www.kde.cs.uni-kassel.de/ws/dc09/",
          "interhash":"1bea279aaa24fd28808e03c151894c69",
          "intrahash":"1bea279aaa24fd28808e03c151894c69",
          "href":"http://www.bibsonomy.org/api/users/jaeschke/posts/1bea279aaa24fd28808e03c151894c69"
        },
        "postingdate":"2009-02-27T19:29:12.000+01:00",
        "changedate":"2009-02-27T19:29:12.000+01:00"
      }
    ],
    "start":0,
    "end":1,
    "next":"http://www.bibsonomy.org/api/users/jaeschke/posts?start=1&end=2&tags=myown&resourcetype=bookmark"
  },
  "stat":"ok"
}
"""
        if "bibtex" == resource_type:
            return """
{
  "posts":{
    "post":[
      {
        "user":{"name":"jaeschke","href":"http://www.bibsonomy.org/api/users/jaeschke"},
        "group":[{"name":"public","href":"http://www.bibsonomy.org/api/groups/public"}],
        "tag":[
          {"name":"2014","href":"http://www.bibsonomy.org/api/tags/2014"},
          {"name":"booksprint","href":"http://www.bibsonomy.org/api/tags/booksprint"},
          {"name":"buch","href":"http://www.bibsonomy.org/api/tags/buch"},
          {"name":"coscience","href":"http://www.bibsonomy.org/api/tags/coscience"},
          {"name":"literatur","href":"http://www.bibsonomy.org/api/tags/literatur"},
          {"name":"myown","href":"http://www.bibsonomy.org/api/tags/myown"},
          {"name":"recherche","href":"http://www.bibsonomy.org/api/tags/recherche"},
          {"name":"tib","href":"http://www.bibsonomy.org/api/tags/tib"},
          {"name":"verwaltung","href":"http://www.bibsonomy.org/api/tags/verwaltung"}
        ],
        "bibtex":{
          "title":"Literatur recherchieren und verwalten",
          "bibtexKey":"bluemel2014literatur",
          "misc":"  doi = {10.2314/coscv1.1}",
          "bibtexAbstract":"Zusammenfassung",
          "entrytype":"incollection",
          "address":"Hannover",
          "author":"Blümel, Ina and Hauschke, Christian and Jäschke, Robert",
          "booktitle":"CoScience - Gemeinsam forschen und publizieren mit dem Netz",
          "chapter":"1",
          "pages":"12--20",
          "publisher":"Technische Informationsbibliothek",
          "year":"2014",
          "url":"http://handbuch.io/w/index.php?title=Handbuch_CoScience/Literatur_recherchieren_und_verwalten",
          "intrahash":"9d87348e2ce9f970dfac29446b04729b",
          "interhash":"6afb1ffe49a76d68d11457c980a56542",
          "href":"http://www.bibsonomy.org/api/users/jaeschke/posts/9d87348e2ce9f970dfac29446b04729b",
          "extraurls":{"url":[{"title":"Data", "href":"http://github.com/L3S", "date":"2011-04-28T10:15:14.000+02:00"}]}
        },
        "postingdate":"2014-06-10T08:20:50.000+02:00",
        "changedate":"2014-07-28T15:57:31.000+02:00"
      }
    ],
    "start":0,
    "end":1,
    "next":"http://www.bibsonomy.org/api/users/jaeschke/posts?start=1&end=2&tags=myown&resourcetype=publication"
  },
  "stat":"ok"
}
"""

    def getPost(self, user_name, intra_hash):
       return '{"posts":{"post":[{"user":{"name":"jaeschke","href":"http://www.bibsonomy.org/api/users/jaeschke"},"group":[{"name":"public","href":"http://www.bibsonomy.org/api/groups/public"}],"tag":[{"name":"2013","href":"http://www.bibsonomy.org/api/tags/2013"},{"name":"challenge","href":"http://www.bibsonomy.org/api/tags/challenge"},{"name":"dc13","href":"http://www.bibsonomy.org/api/tags/dc13"},{"name":"discovery","href":"http://www.bibsonomy.org/api/tags/discovery"},{"name":"ecmlpkdd","href":"http://www.bibsonomy.org/api/tags/ecmlpkdd"},{"name":"myown","href":"http://www.bibsonomy.org/api/tags/myown"},{"name":"recommender","href":"http://www.bibsonomy.org/api/tags/recommender"}],"bookmark":{"title":"15th Discovery Challenge | organized in conjunction with ECML PKDD 2013","url":"http://www.kde.cs.uni-kassel.de/ws/dc13/","interhash":"1bea279aaa24fd28808e03c151894c69","intrahash":"1bea279aaa24fd28808e03c151894c69","href":"http://www.bibsonomy.org/api/users/jaeschke/posts/1bea279aaa24fd28808e03c151894c69"},"postingdate":"2013-02-27T19:29:12.000+01:00","changedate":"2013-02-27T19:29:12.000+01:00"}],"start":0,"end":1,"next":"http://www.bibsonomy.org/api/users/jaeschke/posts?start=1&end=2&tags=myown&resourcetype=bookmark"},"stat":"ok"}' 


    def getUser(self, user_name):
        return """
{
  "stat":"ok",
  "user":{
    "href":"http://www.bibsonomy.org/api/users/foo",
    "name":"foo",
    "realname":"John Doe",
    "groups":{
      "group":[
        {"name":"kde","href":"http://www.bibsonomy.org/api/groups/kde"}
      ],
      "end":0,
      "start":1
    }
  }
}
"""


if __name__ == '__main__':
    unittest.main()

