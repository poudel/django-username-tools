from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from username_tools.blacklist import BLACKLIST


UserModel = get_user_model()


class UsernameBlacklistManager(models.Manager):

    def is_blacklisted(self, username):
        lookup = "{}__iexact".format(UserModel.USERNAME_FIELD)
        fil = {lookup: username, 'is_blocked': True}
        return self.filter(**fil).exists()

    def blacklisted(self, *args, **kwargs):
        return self.filter(*args, is_blocked=True, **kwargs)

    def populate(self):
        """
        Populate database from file.

        Set `reset` to True if you want to update those
        that you have modified.
        """
        blacklist = set(BLACKLIST)

        saved = self.values_list('username', flat=True)
        if saved:
            blacklist = blacklist.difference(saved)

        objs = [self.model(username=u) for u in blacklist]
        self.bulk_create(objs)
        return len(objs)


class UsernameBlacklist(models.Model):
    username = models.CharField(
        _("username"),
        help_text=_("Username to black list"),
        max_length=250,
        unique=True
    )
    is_blocked = models.BooleanField(
        _("is blocked"),
        default=True,
        help_text=_(
            "Set this to False if you need to whitelist this username but don't "
            "want to delete it. This also ensures that a whitelisted username "
            "will stay whitelisted when re-populating using the `populate` "
            "manager method."
        )
    )

    objects = UsernameBlacklistManager()

    def __str__(self):
        return self.username
