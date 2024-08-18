import unittest
from check_valid_order.solution import verify_order, contains_order_number


class TestVerifyOrder(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(contains_order_number('The order number is 123.4567.A'), 1)

    def test_string_with_only_letters(self):
        self.assertEqual(contains_order_number('The order number is 1234567A'), 1)

    def test_string_with_only_digits(self):
        self.assertEqual(contains_order_number("Oh, I don't have an order number"), 0)

    def test_string_with_letters_followed_by_digits(self):
        self.assertEqual(contains_order_number('RYZ.1187.C'), 0)

    def test_string_with_digits_followed_by_letters(self):
        self.assertEqual(contains_order_number('123abc'), 0)

    def test_string_with_mixed_characters(self):
        self.assertEqual(contains_order_number('a1b2c3'), 1)


if __name__ == '__main__':
    unittest.main()
