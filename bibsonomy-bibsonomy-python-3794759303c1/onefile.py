#!/usr/bin/python3

from __future__ import print_function
import argparse, os, bibsonomy, post_io, sys

"""
Download all your BibSonomy bookmarks or publications into one nice
HTML file. Inclusion of the previews or documents is possible.
"""

version = "0.1.0"

# TODO: 
# - support sorting of posts by posting date, publication year, author, title, etc.
# - improve support for XML and JSON output - currently only the first 1000 posts can be retrieved

# configure command line parsing
parser = argparse.ArgumentParser(description='Download posts from BibSonomy and store them in a file.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('user', type=str, help='BibSonomy user name')
parser.add_argument('apikey', type=str, help='corresponding API key (get it from http://www.bibsonomy.org/settings?selTab=1)')
parser.add_argument('-u', '--user', type=str, dest="user_name", metavar="USER", help='return posts for USER instead of user')
parser.add_argument('-t', '--tags', type=str, default=None, nargs='+', metavar="TAG", help='return posts with the given tags')
parser.add_argument( '-d', '--documents', action="store_true", help='download documents for publications')
parser.add_argument('--directory', type=str, default=os.curdir, metavar="DIR", help='target directory')
parser.add_argument('--bookmark-file', type=str, default='bookmarks', metavar="BFILE", help='bookmarks file name')
parser.add_argument('--publication-file', type=str, default='publications', metavar="BFILE", help='publications file name')
parser.add_argument('--css-file', type=str, default=None, metavar="CSSFILE", help='write CSS to file')
parser.add_argument('--no-bookmarks', action="store_true", help='do not write bookmarks')
parser.add_argument('--no-publications', action="store_true", help='do not write publications')
parser.add_argument('-f', '--format', type=str, default="html", choices=["html", "json", "xml"], metavar="FORMAT", help='output format')
parser.add_argument('-v', '--version', action="version", version="%(prog)s " + version)

args = parser.parse_args()

# initialize BibSonomy data source
if args.format == "html":
    rest_source = bibsonomy.REST(args.user, args.apikey, data_format="json")
    bib = bibsonomy.BibSonomy(rest_source)
else:
    bib = bibsonomy.REST(args.user, args.apikey, data_format=args.format)


# prepare the query arguments
if args.user_name:
    user_name = args.user_name
else:
    user_name = args.user

print("getting posts for " + user_name + " with tags " + str(args.tags))

docw = post_io.DocumentWriter(args.documents)

if args.css_file == None:
    css_file = None
else:
    css_file = os.path.join(args.directory, args.css_file)
pio = post_io.PostWriter(docw, css_file)


# get bookmarks
if not args.no_bookmarks:
    # get them
    posts = bib.getPostsForUser("book", user_name, args.tags)
    if posts != None:
        bookmark_file = os.path.join(args.directory, args.bookmark_file + "." + args.format);
        if args.format == "html":
            pio.write_bookmarks(bookmark_file, posts)
            print(str(len(posts)) + " bookmarks written to " + bookmark_file)
        else:
            with open(bookmark_file, 'w') as f:
                f.write(posts)
            print(str(len(posts)) + " characters written to " + bookmark_file)

# get publications
if not args.no_publications:
    # get them
    posts = bib.getPostsForUser("publ", user_name, args.tags)
    if posts != None:
        publication_file = os.path.join(args.directory, args.publication_file + "." + args.format)

        if args.format == "html":
            pio.write_publications(publication_file, posts)
            print(str(len(posts)) + " publications written to " + publication_file)
        else:
            with open(publication_file, 'w') as f:
                f.write(posts)
            print(str(len(posts)) + " characters written to " + publication_file)


        if args.documents:
            # count documents
            doc_ctr = 0
            for post in posts:
                if hasattr(post, "documents") and post.documents != None:
                    for doc in post.documents:
                        doc_ctr = doc_ctr + 1
            # write documents
            print("getting " + str(doc_ctr) + " documents")
            ctr = 0
            for post in posts:
                if hasattr(post, "documents") and post.documents != None:
                    for doc in post.documents:
                        ctr = ctr + 1

                        # write document
                        content,mime = bib.getDocument(doc)
                        # because of a bug
                        # (https://bitbucket.org/bibsonomy/bibsonomy/issue/1934/documents-with-a-in-the-filename-cause)
                        # files with a "+" in the file name can not be
                        # downloaded. Hence, we check again, if we
                        # really got the file.
                        if content != None:
                            # TODO: use normalized file name, handle duplicates (compare md5sum?)
                            f = open(os.path.join(args.directory, doc.file_name), "wb")
                            f.write(content)
                            f.close()

                            # write preview
                            content,mime = bib.getDocumentPreview(doc, "MEDIUM")
                            # TODO: use normalized file name, handle duplicates (compare md5sum?)
                            f = open(os.path.join(args.directory, doc.file_name + ".jpg"), "wb")
                            f.write(content)
                            f.close()
                        else:
                            # print error mark
                            print("X", end="")
                        # print progress
                        if ctr % 10 == 0:
                            print(str(ctr), end="")
                        else:
                            print(".", end="")
                            if ctr % 50 == 0 and ctr < doc_ctr:
                                print()
                        sys.stdout.flush()
            print()
            print(str(ctr) + " documents written to " + args.directory)
                                    
