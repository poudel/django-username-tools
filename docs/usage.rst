=====
Usage
=====

You can either use the `UsernameFormField` or `UsernameModelField`.


Username form field
-------------------

If you are using the default `User` model from `django.contrib.auth` then you should
use the `UsernameFormField`.


.. code-block:: python

    from django import forms
    from username_tools.fields import UsernameFormField


    class MyUserRegistrationForm(forms.Form):
        username = UsernameFormField()

	# other form fields



Custom user models
------------------

If you have defined a custom user model in your project, you can use `UsernameModelField`
as your username field.


.. code-block:: python

    from django.db import models
    from username_tools.fields import UsernameModelField


    class MyCustomUser(models.Model):
        username = UsernameModelField()

	# other model fields



Populate default blocked usernames
----------------------------------

Use `populate_blacklist` management command to populate from
the command line interface::

    python manage.py populate_blacklist
    

Or, you can use the `populate` manager method to populate from your
code or the python shell.


.. code-block:: python

    from username_blacklist.models import UsernameBlacklist
    UsernameBlacklist.objects.populate()

