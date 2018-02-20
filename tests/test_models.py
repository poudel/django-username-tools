from django.test import TestCase

from username_tools.models import UsernameBlacklist
from username_tools.blacklist import BLACKLIST


class TestModelAndManager(TestCase):

    def setUp(self):
        self.raw_list = list(sorted(set(BLACKLIST)))

    def test_is_blacklisted(self):
        UsernameBlacklist.objects.populate()

        self.assertTrue(
            UsernameBlacklist.objects.is_blacklisted("root"),
            "Should return True for blacklisted usernames"
        )

        self.assertTrue(
            UsernameBlacklist.objects.is_blacklisted("rOoT"),
            "Should return be case insensitive"
        )

        self.assertFalse(
            UsernameBlacklist.objects.is_blacklisted("oot"),
            "Should not be False for just containing the words"
        )

        self.assertFalse(
            UsernameBlacklist.objects.is_blacklisted("goodboyme22"),
            "Should return False for non-blacklisted usernames"
        )

    def test_blacklisted(self):
        UsernameBlacklist.objects.populate()

        self.assertEqual(
            UsernameBlacklist.objects.blacklisted().count(),
            len(self.raw_list),
            "It should return all blocked usernames"
        )

        first = UsernameBlacklist.objects.first()
        first.is_blocked = False
        first.save()

        self.assertEqual(
            UsernameBlacklist.objects.blacklisted().count(),
            len(self.raw_list) - 1,
            "It should only include blocked usernames"

        )

    def test__str__(self):
        instance = UsernameBlacklist(username="asdf")
        self.assertEqual(str(instance), "asdf", "It should return the username for str")

    def test_populate(self):
        created = UsernameBlacklist.objects.populate()

        self.assertEqual(created,
                         len(self.raw_list),
                         "Should be equal to the length of raw_list")

        first = UsernameBlacklist.objects.blacklisted().first()
        first.is_blocked = False
        first.save()

        second_total = UsernameBlacklist.objects.populate()

        self.assertEqual(second_total, 0, "Should not create any more objects")

        second = UsernameBlacklist.objects.get(id=first.id)
        self.assertEqual(
            second.is_blocked,
            False,
            "Should not reset the changes made in the database by user"
        )
