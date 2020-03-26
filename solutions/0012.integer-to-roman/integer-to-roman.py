# rome = {
#     1: 'I',
#     4: 'IV',
#     5: 'V',
#     9: 'IX',
#     10: 'X',
#     40: 'XL',
#     50: 'L',
#     90: 'XC',
#     100: 'C',
#     400: 'CD',
#     500: 'D',
#     900: 'CM',
#     1000: 'M',
# }

class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index, result = 0, ""

        for index in range(len(nums)):
            while num >= nums[index]:
                result += romans[index]
                num -= nums[index]
            index += 1
        return result