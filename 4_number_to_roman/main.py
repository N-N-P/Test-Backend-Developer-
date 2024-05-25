"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number <= 0:
            return "number can not be less than 0"
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_text = ""
        i = 0
        
        while number > 0:
            for _ in range(number // val[i]):
                roman_text += syms[i]
                number -= val[i]
            i += 1
        
        return roman_text

solution = Solution()

print(solution.number_to_roman(101))   # Output: CI
print(solution.number_to_roman(-1))    # Output: number can not be less than 0
print(solution.number_to_roman(3999))  # Output: MMMCMXCIX
print(solution.number_to_roman(0))     # Output: number can not be less than 0
print(solution.number_to_roman(44))    # Output: XLIV
print(solution.number_to_roman(57))    # Output: LVII
print(solution.number_to_roman(309))   # Output: CCCIX