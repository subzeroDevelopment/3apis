# -*- coding: utf-8 -*-
import re, os
from urllib.parse import quote

# TODO: proper HTML escaping
class PostWriter:

    def __init__(self, document_writer, css_file):
        self.document_writer = document_writer
        self.css_file = css_file

    def write_bookmarks(self, file_name, posts):
        # print them into a file
        f = open(file_name, "w", encoding="utf-8")

        # print the header
        self.write_html_header(f)

        # print the bookmarks
        f.write("<ul class='posts'>\n")
        for post in posts:
            f.write("<li class='bookmark'>")
            f.write("<a href='" + post.resource.url + "'>" + post.resource.title + "</a>")
            # tags
            self.write_tags(f, post)
            f.write("</li>\n")
        f.write("</ul>\n")
        f.write("</body></html>\n")
        f.close()

    def write_publications(self, file_name, posts):
        # print them into a file
        f = open(file_name, "w", encoding="utf-8")

        # print the header
        self.write_html_header(f)

        # print the bookmarks
        f.write("<ul class='posts'>\n")
        for post in posts:
            # TODO: BibTeX-Key as ID
            f.write("<li class='publication' id='" + post.resource.intra_hash + "'>\n")
            f.write("  <a class='title' href='http://www.bibsonomy.org/publication/" + post.resource.intra_hash + "/" + quote(post.user.name, '') + "'>" + self.remove_latex(post.resource.title) + "</a>")
            # author / editor
            if hasattr(post.resource, "author"):
                f.write("  <div class='author'>" + self.format_persons(post.resource.author) + "</div>")
            elif hasattr(post.resource, "editor"):
                f.write("  <div class='author'>" + self.format_persons(post.resource.editor) + " (Eds.)</div>")
            # metadata
            f.write("  <div class='meta'>")
            self.write_meta(f, post.resource)
            # documents
            if hasattr(post, "documents") and len(post.documents) > 0:
                f.write(" [" + ", ".join([self.get_document_link(post, doc) for doc in post.documents]) + "]");
            f.write("  </div>")
            # preview image for first document
            if hasattr(post, "documents") and len(post.documents) > 0:
                path = self.document_writer.get_document_link(post.documents[0], post)
                preview_path = self.document_writer.get_document_preview_link(post.documents[0], post)
                f.write("  <a href='" + path + "'><img src='" + preview_path + "'/></a>")
            # abstracts
            if hasattr(post.resource, "abstract"):
                f.write("  <div class='abstract'>" + post.resource.abstract + "</div>");
            f.write("  ")
            # tags
            self.write_tags(f, post)
            f.write("</li>\n")
        f.write("</ul>\n")
        f.write("</body></html>\n")
        f.close()


    def write_tags(self, f, post):
        f.write("<ul class='tags'>\n")
        for tag in post.tags:
            f.write("<li><a href='http://www.bibsonomy.org/user/" + quote(post.user.name, '') + "/" + quote(tag, '') + "'>" + tag + "</a></li>")
        f.write("</ul>\n")
            

    def write_html_header(self, f):
        f.write("<!DOCTYPE html>\n")
        f.write("<html><head>\n")
        f.write("<meta charset='utf-8'>\n");
        f.write("<title>BibSonomy posts</title>\n");
        f.write("<meta name='generator' content='onefile.py'/>\n");
        if (self.css_file == None):
            f.write("<style type='text/css'>")
            self.write_css(f)
            f.write("</style>")
        else:
            f.write("<link rel='stylesheet' href='style.css' type='text/css'/>")
            if (os.path.isfile(self.css_file)): 
                print("CSS file " + self.css_file + " already exists, not writing it")
            else:
                css = open(self.css_file, "w", encoding="utf-8")
                self.write_css(css)
                css.close()
        f.write("</head><body>\n");

    """
    format publications
    TODO: - complete metadata
    """
    def write_meta(self, f, publication):
        closing_tag = "</a>"
        if hasattr(publication, "url"):
            f.write("<a class='source' href='" + publication.url + "'>")
        elif hasattr(publication, "doi"):
            f.write("<a class='source' href='http://dx.doi.org/" + publication.doi + "'>")
        else:
            f.write("<span class='source'>")
            closing_tag = "</span>"
        if publication.entry_type == "article":
            if hasattr(publication, "journal"):
                f.write(" " + self.remove_latex(publication.journal) + " ")
            if hasattr(publication, "volume"):
                f.write(" <strong>" + self.remove_latex(publication.volume) + "</strong> ")
            if hasattr(publication, "number"):
                f.write(" (" + self.remove_latex(publication.number) + ") ")
            if hasattr(publication, "pages"):
                f.write(" " + self.format_pages(publication.pages) + " ")
        elif publication.entry_type in ("inproceedings", "incollection", "inbook"):
            if hasattr(publication, "booktitle"):
                f.write(self.remove_latex(publication.booktitle))
                if hasattr(publication, "pages"):
                    f.write(", " + self.format_pages(publication.pages))
            if hasattr(publication, "publisher"):
                if hasattr(publication, "booktitle"):
                    f.write(", ")
                f.write(self.remove_latex(publication.publisher))
                if hasattr(publication, "address"):
                    f.write(", " + self.remove_latex(publication.address))
            elif hasattr(publication, "organization"):
                if hasattr(publication, "booktitle"):
                    f.write(", ")
                f.write(self.remove_latex(publication.organization))
                if hasattr(publication, "address"):
                    f.write(", " + self.remove_latex(publication.address))
        elif publication.entry_type in ("book", "booklet", "proceedings"):
            if hasattr(publication, "publisher"):
                f.write(self.remove_latex(publication.publisher))
        elif publication.entry_type in ("mastersthesis", "phdthesis"):
            if hasattr(publication, "school"):
                f.write(self.remove_latex(publication.school))
                if hasattr(publication, "address"):
                    f.write(", " + self.remove_latex(publication.address))
        elif publication.entry_type == "techreport":
            if hasattr(publication, "type"):
                f.write(self.remove_latex(publication.type))
            else:
                f.write("Technical Report")
            if hasattr(publication, "number"):
                f.write(" " + self.remove_latex(publication.number))
            if hasattr(publication, "institution"):
                f.write(", " + self.remove_latex(publication.institution))
        elif publication.entry_type == "manual":
            if hasattr(publication, "organization"):
                f.write(self.remove_latex(publication.organization))
            if hasattr(publication, "address"):
                if hasattr(publication, "organization"):
                    f.write(", ")
                f.write(self.remove_latex(publication.address))
        f.write(" (" + self.remove_latex(publication.year) + ") ")
        f.write(closing_tag + " ")


    """ 
    pretty-print pages
    """
    def format_pages(self, s):
        return re.sub("\s*--\s*", "-", s)

    def remove_latex(self, s):
        return re.sub("--", "&#8211;", re.sub("[{}]", "", s)).strip()

    def format_person(self, s):
        return " ".join(list(reversed(s.split(", "))))
    
    def rreplace(self, s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

    def format_persons(self, s):
        return self.rreplace(", ".join(map(self.format_person, s.split(" and "))), ", ", " and ", 1)

    def get_document_link(self, post, doc):
        return "<a class='pdf' href='" + self.document_writer.get_document_link(doc, post) + "'>" + doc.file_name + "</a>"

    # write CSS to f
    def write_css(self, f):
        f.write("""
ul.posts {
  padding-left: 0;
  font-family: sans-serif;
  font-size: 10pt;
  max-width: 800px;
}
ul.posts a {
  text-decoration: none;
  color: #006699;
}
ul.posts a:active, ul.posts a:hover {
  text-decoration: underline;
}
.publication {
  list-style: none;
  margin-bottom: 1em;
  border: 1px solid #ddd;
  padding: 10px;
  clear: both;
}
.publication a.title {
  display: block;
  text-align: center;
  font-weight: bold;
  font-size: 16px;
}
.publication a.source, .publication a.pdf {
  font-weight: normal;
}
.publication .author, .publication .meta {
  color: #888;
  text-align: center;
}
.publication img {
  float: left;
  margin: 0 10px 10px 0;
}
.publication .abstract {
  line-height: 150%;
  color: #666;
}
ul.publicationlist li {
  list-style-type: none;
}
ul.publicationlist a {
  font-weight: normal;
}
ul.publicationlist .year {
  color: #303F5A;
}
ul.publicationlist .author {
  color: #666;
}
ul.tags {
  padding-left: 0em;
}
ul.tags li {
  margin-right: .5em;
  display: inline;
}
""")



class DocumentWriter:
    
    # to create nicer file names
    clean_string_map = str.maketrans({'ä':"ae", 'ö':"oe", 'ü':"ue", 'Ä':"Ae", 'Ö':"Oe", 'Ü':"Ue", 'ß':"ss"})

    def __init__(self, local_documents):
        self.local_documents = local_documents

    # lastnameYEARtitleword
    def get_filename(self, doc, post):
        # get first author's last name
        if hasattr(post.resource, "author"):
            person = post.resource.author
        else:
            person = post.resource.editor
        commapos = person.find(",")
        if commapos > 1:
            lastname = person[0:commapos]
        else:
            lastname = person
        return self.clean_string(lastname + post.resource.year + self.get_first_long_word(post.resource.title))

    def get_first_long_word(self, s):
        for word in map(self.clean_string, s.split()):
            if len(word) >= 5:
                return word
        return s

    def clean_string(self, s):
        return re.sub("[^a-zA-Z0-9]+", "", s.translate(self.clean_string_map)).lower()

    def get_document_preview_link(self, doc, post):
        path = self.get_document_link(doc, post)
        if self.local_documents:
            return path + ".jpg"
        else:
            return path + "?preview=MEDIUM"

    def get_document_link(self, doc, post):
        # print(self.get_filename(doc, post))
        if self.local_documents:
            return doc.file_name
        else:
            return "http://www.bibsonomy.org/documents/" + post.resource.intra_hash + "/" + post.user.name + "/" + doc.file_name
