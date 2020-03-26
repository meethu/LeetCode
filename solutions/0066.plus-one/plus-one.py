class Solution:
    def plusOne(self, digits):
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


digits = [9, 9, 9]
problems = Solution()
print(problems.plusOne(digits))
