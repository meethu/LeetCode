# # 分治
# class Solution:
#     def mypow(self, x, n):
#         if n == 0: # if not n: return 1
#             return 1
#         if n < 0:
#             return 1 / self.mypow(x, -n)
#         if n % 2:
#             return x * self.mypow(x, n-1)
#         return self.mypow(x*x, n/2)

# 位运算

class Solution:
    def mypow(self, x, n):
        if n < 0:
            n = -n
            x = 1 / x
        pow = 1

        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

problems = Solution()
print(problems.mypow(2.0000, 10))