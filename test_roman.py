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

    def test_roman_to_int_repetition(self):
        self.assertEqual(self.roman_numeral.roman_to_int('II'), 2)
        self.assertEqual(self.roman_numeral.roman_to_int('VII'), 7)
        self.assertEqual(self.roman_numeral.roman_to_int('XX'), 20)

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
            self.roman_numeral.roman_to_int('VV')
            self.roman_numeral.roman_to_int('Z')

    def test_roman_to_int_null_input(self):
        with self.assertRaises(TypeError):
            self.roman_numeral.roman_to_int(None)

    def test_roman_to_int_subtractive_notation(self):
        self.assertEqual(self.roman_numeral.roman_to_int('IV'), 4)
        self.assertEqual(self.roman_numeral.roman_to_int('IX'), 9)
        self.assertEqual(self.roman_numeral.roman_to_int('XL'), 40)
        self.assertEqual(self.roman_numeral.roman_to_int('XC'), 90)
        self.assertEqual(self.roman_numeral.roman_to_int('CD'), 400)
        self.assertEqual(self.roman_numeral.roman_to_int('CM'), 900)


if __name__ == '__main__':
    unittest.main()
