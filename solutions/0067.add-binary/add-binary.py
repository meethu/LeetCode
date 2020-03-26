# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a, b = int('0b' + a, 2), int('0b' + b, 2)
#         return bin(a + b)[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         ans, extra = '',0
#         i,j=len(a)-1,len(b)-1
#         while i>=0 or j>=0:
#             if i >= 0:
#                 extra += ord(a[i]) - ord('0')
#             if j >= 0:
#                 extra += ord(b[j]) - ord('0')
#             ans += str(extra % 2)
#             extra //= 2
#             i,j = i-1,j-1
#         if extra == 1:
#             ans += '1'
#         return ans[::-1]


# https://leetcode-cn.com/problems/add-binary/solution/hua-jie-suan-fa-67-er-jin-zhi-qiu-he-by-guanpengch/
