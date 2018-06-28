.. image:: https://travis-ci.org/buriy/python-readability.svg?branch=master
    :target: https://travis-ci.org/buriy/python-readability


python-readability
==================

Given a html document, it pulls out the main body text and cleans it up.

This is a python port of a ruby port of `arc90's readability
project <http://lab.arc90.com/experiments/readability/>`__.

Installation
------------

It's easy using ``pip``, just run:

::

    $ pip install readability-lxml

Usage
-----

::

    >> import requests
    >> from readability import Document
    >>
    >> response = requests.get('http://example.com')
    >> doc = Document(response.text)
    >> doc.title()
    >> 'Example Domain'

Change Log
----------

-  0.7 Improved HTML5 tags handling. Heuristics were changed for a lot of sites: Fixed an important
bug with stripping unwanted HTML nodes (only first matching node was removed before).
-  0.6 Finally a release which supports Python versions 2.6, 2.7, 3.3
   and 3.4
-  0.5 Preparing a release to support Python versions 2.6, 2.7, 3.3 and
   3.4
-  0.4 Added Videos loading and allowed more images per paragraph
-  0.3 Added Document.encoding, positive\_keywords and
   negative\_keywords

Licensing
=========

This code is under `the Apache License
2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__ license.

Thanks to
---------

-  Latest
   `readability.js <https://github.com/MHordecki/readability-redux/blob/master/readability/readability.js>`__
-  Ruby port by starrhorne and iterationlabs
-  `Python port <https://github.com/gfxmonk/python-readability>`__ by
   gfxmonk
-  `Decruft
   effort <http://www.minvolai.com/blog/decruft-arc90s-readability-in-python/>`__
   to move to lxml
-  "BR to P" fix from readability.js which improves quality for smaller
   texts
-  Github users contributions.


