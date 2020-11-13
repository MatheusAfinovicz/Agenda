from django.test import TestCase
from .functions import check_request_method_is_post


class LoginTestCase(TestCase):
    def test_login_method_is_not_post(self):
        methods = ['GET', 'HEAD', 'PUT', 'DELETE']
        for method in methods:
            with self.subTest(method=method):
                TestCase.assertFalse(check_request_method_is_post(method), False)

    def test_login_method_is_post(self):
        self.assertTrue(check_request_method_is_post('POST'))
