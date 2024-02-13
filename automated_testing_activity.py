"""
A program that converts a roman to integer 

Given a string in a roman numeral format, the program needs to convert it to an integer.

I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Combine numerals to make numbers: II=2, VII=7, XVI=16.

Subtractive notation: I, II, III, IV=4, V, VI, VII, VIII, IX=9, X, …

"""

class RomanNumeral:
    def __init__(self):
        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, s):
        converted_number = 0
        for i in range(len(s)):
            current_number = self.map[s[i]]
            next_num = self.map[s[i + 1]] if i + 1 < len(s) else 0
            if current_number >= next_num:
                converted_number += current_number
            else:
                converted_number -= current_number
        return converted_number

# Example usage:
roman = RomanNumeral()
print(roman.roman_to_int("IV"))  # Output: 4
print(roman.roman_to_int("IX"))  # Output: 9
print(roman.roman_to_int("LVIII"))  # Output: 58
print(roman.roman_to_int("MCMXCIV"))  # Output: 1994
