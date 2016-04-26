Python code for BibSonomy
=========================

This project hosts Python code to interact with BibSonomy via its `REST
API <https://bitbucket.org/bibsonomy/bibsonomy/wiki/documentation/api/REST%20API>`__.
The file
`bibsonomy.py <https://bitbucket.org/bibsonomy/bibsonomy-python/src/tip/bibsonomy.py>`__
contains the ``BibSonomy`` class which implements the REST calls. The
`status
page <https://bitbucket.org/bibsonomy/bibsonomy-python/wiki/Status>`__
describes the current state of the implementation.
The library is also available in the `Python Package Index <https://pypi.python.org/pypi/bibsonomy>`__.

License
-------

Copyright 2014 Robert Jäschke. The code is distributed under the terms
of the GNU Lesser General Public License 3, see the file
`LICENSE.txt <https://bitbucket.org/bibsonomy/bibsonomy-python/src/tip/LICENSE.txt>`__.

Requirements
------------

-  Python3
-  urllib
-  `requests <http://docs.python-requests.org/en/latest/>`__

On Debian/Ubuntu, you can install the required packages with
``sudo apt-get install python3 python3-urllib3 python3-requests``.

History
-------

See the file `HISTORY.txt <https://bitbucket.org/bibsonomy/bibsonomy-python/src/tip/HISTORY.txt>`__.

Usage
-----

.. code:: python

    import bibsonomy

    # get your API key at http://www.bibsonomy.org/settings?selTab=1
    json_source = bibsonomy.RestSource("yourUserName", "yourApiKey")
    bib = bibsonomy.BibSonomy(json_source)

    posts = bib.getPostsForUser("bookmark", "jaeschke", None, 0, 10);

    for post in posts:
        bookmark = post.resource
        print(bookmark.title)

Tools
-----

The script
`onefile.py <https://bitbucket.org/bibsonomy/bibsonomy-python/src/tip/onefile.py>`__
allows you to download posts from BibSonomy and store them in a file.

Requirements
~~~~~~~~~~~~

-  Python3
-  requests
-  argparse

On Debian/Ubuntu, you can install the required packages with
``sudo apt-get install python3 python3-httplib2 python-argparse python3-requests``.

Usage
~~~~~

Call the script with the ``--help`` option to get some help:

::

    usage: onefile.py [-h] [-u USER] [-t TAG [TAG ...]] [-d] [--directory DIR]
                      [--bookmark-file BFILE] [--publication-file BFILE]
                      [--css-file CSSFILE] [--no-bookmarks] [--no-publications]
                      [--test]
                      user apikey

    Download posts from BibSonomy and store them in a file.

    positional arguments:
      user                  BibSonomy user name
      apikey                corresponding API key (get it from
                            http://www.bibsonomy.org/settings?selTab=1)

    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  return posts for USER instead of user (default: None)
      -t TAG [TAG ...], --tags TAG [TAG ...]
                            return posts with the given tags (default: None)
      -d, --documents       download documents for publications (default: False)
      --directory DIR       target directory (default: .)
      --bookmark-file BFILE
                            bookmarks file name (default: bookmarks.html)
      --publication-file BFILE
                            publications file name (default: publications.html)
      --css-file CSSFILE    write CSS to file (default: None)
      --no-bookmarks        do not write bookmarks (default: False)
      --no-publications     do not write publications (default: False)
      --test                use test data (default: False)

