from django.db import models
from username_tools.fields import UsernameModelField


class HypotheticalUserModel(models.Model):
    username = UsernameModelField()

    def __str__(self):
        return self.username
