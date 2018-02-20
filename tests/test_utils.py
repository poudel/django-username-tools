from unittest import mock
from django.test import TestCase
from username_tools.utils import blacklist_model, is_blacklisted


class TestUtils(TestCase):

    def test_blacklist_model(self):
        BlacklistModel = blacklist_model()

        self.assertEqual(
            BlacklistModel._meta.model_name,
            "usernameblacklist",
            "It should return UsernameBlacklist model"
        )

    @mock.patch("username_tools.utils.blacklist_model")
    def test_is_blacklisted(self, blacklist_model_):
        is_blacklisted("root")
        blacklist_model_.assert_called()

    @mock.patch("username_tools.utils.blacklist_model")
    def test_is_blacklisted_without_INSTALLED_APPS(self, blacklist_model_):
        apps = {"remove": "username_tools"}
        with self.modify_settings(INSTALLED_APPS=apps):
            self.assertTrue(
                is_blacklisted("root"),
                "Should return true for check from file"
            )

            self.assertTrue(
                is_blacklisted("roOt"),
                "Should do a lowercase check"
            )

            blacklist_model_.assert_not_called()
