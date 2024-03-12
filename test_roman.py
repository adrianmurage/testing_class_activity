import unittest
from automated_testing_activity import RomanNumeral

class TestRomanNumeral(unittest.TestCase):
    def setUp(self):
        self.roman_numeral = RomanNumeral()

    def test_roman_to_int(self):
        self.assertEqual(self.roman_numeral.roman_to_int('I'), 1)
        self.assertEqual(self.roman_numeral.roman_to_int('IV'), 4)
        self.assertEqual(self.roman_numeral.roman_to_int('IX'), 9)
        self.assertEqual(self.roman_numeral.roman_to_int('LVIII'), 58)
        self.assertEqual(self.roman_numeral.roman_to_int('MCMXCIV'), 1994)

    # test wrong assertions
    def test_roman_to_int_wrong_assertions(self):
        # catch the assertion error
        with self.assertRaises(AssertionError):
            self.assertEqual(self.roman_numeral.roman_to_int('I'), 2)
            self.assertEqual(self.roman_numeral.roman_to_int('VI'), 100)
            self.assertEqual(self.roman_numeral.roman_to_int('XV'), 100)


    def test_roman_to_int_empty_string(self):
        self.assertEqual(self.roman_numeral.roman_to_int(''), 0)

    def test_roman_to_int_invalid_input(self):
        with self.assertRaises(KeyError):
            self.roman_numeral.roman_to_int('XIZ')

if __name__ == '__main__':
    unittest.main()