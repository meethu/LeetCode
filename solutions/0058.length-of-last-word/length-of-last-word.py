# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip(' ')
#         count = 0
#         for i in list(s)[::-1]:
#             if i is " ":
#                 break
#             count += 1
#         return count

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        if not s:
            return 0
        else:
            L = s.split(' ')
            return len(L[-1])