from django.conf import settings
from django.utils.translation import gettext_lazy as _


BLACKLIST_VALIDATION_ERROR_MESSAGE = getattr(
    settings,
    "BLACKLIST_VALIDATION_ERROR_MESSAGE",
    _("Username not available.")
)


EMAIL_IS_USERNAME = getattr(
    settings,
    "EMAIL_IS_USERNAME",
    False
)


USERNAME_MIN_LENGTH = getattr(
    settings,
    "USERNAME_MIN_LENGTH",
    6
)
