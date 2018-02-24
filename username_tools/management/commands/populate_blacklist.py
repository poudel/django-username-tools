from django.core.management import BaseCommand
from username_tools.models import UsernameBlacklist


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        created = UsernameBlacklist.objects.populate()

        self.stdout.write("Added {} blocked items to the database.".format(created))
