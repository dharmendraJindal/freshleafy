from django.test import TestCase


class AdditionTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
