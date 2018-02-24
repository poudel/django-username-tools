from django.core.management import BaseCommand
from username_tools.models import UsernameBlacklist


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        queryset = UsernameBlacklist.objects.all()
        count = queryset.count()

        queryset.delete()

        self.stdout.write("Removed {} items from the database.".format(count))
