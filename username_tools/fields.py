import unicodedata

from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from username_tools.utils import is_blacklisted
from username_tools.settings import (
    BLACKLIST_VALIDATION_ERROR_MESSAGE,
    USERNAME_MIN_LENGTH
)


class UsernameFormField(forms.CharField):
    """
    A `forms.CharField` subclass that comes with validation for blacklisted usernames.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('min_length', USERNAME_MIN_LENGTH)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        value = unicodedata.normalize('NFKC', super().to_python(value))
        if is_blacklisted(value):
            raise ValidationError(BLACKLIST_VALIDATION_ERROR_MESSAGE)
        return value


class UsernameModelField(models.CharField):
    """
    A `models.CharField` subclass that comes with validation for blacklisted usernames.
    """
    default_validators = [UnicodeUsernameValidator()]
    default_error_messages = {
        'unique': _("A user with that username already exists."),
    }

    def __init__(self, *args, **kwargs):
        # defaults are copied from django.contrib.auth's username field
        defaults = {
            'verbose_name': _('username'),
            'max_length': 150,
            'unique': True,
            'help_text': _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        }
        defaults.update(**kwargs)
        super().__init__(*args, **defaults)

    def formfield(self, **kwargs):
        defaults = {'form_class': UsernameFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
