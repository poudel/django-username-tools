from django.test import TestCase
from django.core.exceptions import ValidationError
from username_tools.fields import UsernameFormField, UsernameModelField
from username_tools.models import UsernameBlacklist
from username_tools.settings import BLACKLIST_VALIDATION_ERROR_MESSAGE, USERNAME_MIN_LENGTH


class TestUsernameFormField(TestCase):

    def setUp(self):
        UsernameBlacklist.objects.populate()
        self.field = UsernameFormField()

    def test_to_python(self):
        msg = BLACKLIST_VALIDATION_ERROR_MESSAGE.format()
        with self.assertRaisesRegex(ValidationError, msg):
            with self.settings(USERNAME_MIN_LENGTH=1):
                self.field.clean("root")

    def test_min_length(self):
        msg = "at least {} characters".format(USERNAME_MIN_LENGTH)
        with self.assertRaisesRegex(ValidationError, msg):
            self.field.clean("abcd")


class TestUsernameModelField(TestCase):

    def setUp(self):
        UsernameBlacklist.objects.populate()
        self.field = UsernameModelField()

    def test_formfield(self):
        field = self.field.formfield()
        self.assertTrue(isinstance(field, UsernameFormField))
