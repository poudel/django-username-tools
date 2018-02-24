from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class TestCommands(TestCase):

    def test_populate_blacklist(self):
        out = StringIO()
        call_command('populate_blacklist', stdout=out)

        value = out.getvalue()
        self.assertIn('Added ', value)
        self.assertIn('items to the database.', value)

    def test_clear_blacklist(self):
        out = StringIO()
        call_command('clear_blacklist', stdout=out)

        value = out.getvalue()
        self.assertIn('Removed ', value)
        self.assertIn('items from the database.', value)
