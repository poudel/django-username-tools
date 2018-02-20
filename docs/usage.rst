=====
Usage
=====

To use Django Username Tools in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'username_tools.apps.UsernameToolsConfig',
        ...
    )

Add Django Username Tools's URL patterns:

.. code-block:: python

    from username_tools import urls as username_tools_urls


    urlpatterns = [
        ...
        url(r'^', include(username_tools_urls)),
        ...
    ]
