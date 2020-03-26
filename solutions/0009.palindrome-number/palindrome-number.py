# # 切片
# x = '123'
# y = x[::-1]  # 321
#
# # reverse函数
# y = list(x)
# y.reverse()  # 注意：作用于y，而不是返回值


# 将字符串逆序
class Solution:
    def ispalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        else:
            return str(x) == str(x)[::-1]


class Solution:
    def ispalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x != 0 and x % 10 == 0: return False
        result, pre = 0, x  # 需要保留原来的 x 数值
        while x > 0:
            result = result * 10 + x % 10
            x //= 10  # 取整除赋值运算符

        return result == pre


x = 121
problems = Solution()
print(problems.ispalindrome(x))
