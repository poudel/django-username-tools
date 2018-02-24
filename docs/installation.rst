============
Installation
============

At the command line::

    $ pip install django-username-tools

Now  add `username_tools` to your `INSTALLED_APPS`.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'username_tools',
        ...
    )

It is necessary to populate the database with usernames to blacklist. Go to your project directory and run this command::

    python manage.py populate_blacklist
