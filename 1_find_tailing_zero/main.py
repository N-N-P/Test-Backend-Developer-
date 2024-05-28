"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        count = 0
        power_of_5 = 5
        
        while number >= power_of_5:
            count += number // power_of_5
            power_of_5 *= 5
        
        return count

if __name__ == "__main__":
    solution = Solution()

    test_cases = [7, -10, 25, 100, 0, 5, 50, 85, -33]
    for number in test_cases:
        print(f"Input: {number} -> Output: {solution.find_tailing_zeroes(number)}")

