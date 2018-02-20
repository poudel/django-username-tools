from django.apps import apps
from username_tools.blacklist import BLACKLIST

# to cache the model class after the first import
UsernameBlacklist = None


def blacklist_model():
    global UsernameBlacklist

    if UsernameBlacklist is None:
        from username_tools.models import UsernameBlacklist
    return UsernameBlacklist


def is_blacklisted(value):
    if apps.is_installed("username_tools"):
        return blacklist_model().objects.is_blacklisted(value)
    return value.lower() in BLACKLIST
