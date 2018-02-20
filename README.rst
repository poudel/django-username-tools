=============================
Django Username Tools
=============================

.. image:: https://travis-ci.org/poudel/dj-username-tools.svg?branch=master
    :target: https://travis-ci.org/poudel/dj-username-tools

.. image:: https://codecov.io/gh/poudel/dj-username-tools/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/poudel/dj-username-tools

Username validation et cetera

Documentation
-------------

The full documentation is at https://dj-username-tools.readthedocs.io.

Quickstart
----------

Install Django Username Tools::

    pip install dj-username-tools

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'username_tools.apps.UsernameToolsConfig',
        ...
    )

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
