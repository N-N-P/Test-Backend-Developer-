"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number can not more than 10,000,000"

        thai_numerals = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
        units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        
        if number == 0:
            return "ศูนย์"
        
        result = ""
        digits = list(map(int, str(number)))
        
        for i in range(len(digits)):
            digit = digits[i]
            position = len(digits) - i - 1
            
            if digit == 0:
                continue
            
            if position == 0 and digit == 1 and i != 0:
                result += "เอ็ด"
            elif position == 1 and digit == 2:
                result += "ยี่สิบ"
            elif position == 1 and digit == 1:
                result += "สิบ"
            else:
                result += thai_numerals[digit]
                result += units[position]
        
        return result

solution = Solution()

print(solution.number_to_thai(101))   # Output: หนึ่งร้อยเอ็ด
print(solution.number_to_thai(-1))    # Output: number can not less than 0
print(solution.number_to_thai(21))    # Output: ยี่สิบเอ็ด
print(solution.number_to_thai(10000001)) # Output: number can not more than 10,000,000
print(solution.number_to_thai(1000200))  # Output: หนึ่งล้านสองร้อย

