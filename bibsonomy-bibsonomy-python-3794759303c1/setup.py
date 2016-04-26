from distutils.core import setup


setup(
    name = "bibsonomy",
    version = "0.2.1",
    py_modules = ["bibsonomy"],
    description = "BibSonomy REST client",
    author = "Robert Jäschke",
    author_email = "jaeschke@l3s.de",
    url = "https://bitbucket.org/bibsonomy/bibsonomy-python",
    download_url = "https://pypi.python.org/pypi/bibsonomy",
    keywords = ["bibsonomy", "rest", "web"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        ],
    long_description = """\
BibSonomy REST client
---------------------

This library provides a Python abstraction to BibSonomy's REST
library. In particular, it can
- retrieve posts for users and/or tags
- download documents (incl. preview images) for publication posts
- retrieve information about users

Its functionality can and will be extended to other queries currently
supported by the REST API
(cf. https://bitbucket.org/bibsonomy/bibsonomy/wiki/documentation/api/REST%20API).

"""
)
