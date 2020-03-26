# 二分法存在问题
class Solution(object):
    def mysqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0  # 考虑0
        right = x // 2 + 1  # 考虑1

        while left < right:
            mid = (left + right + 1) / 2
            square = mid ** 2

            if square > x:
                right = mid - 1
            else:
                left = mid
        return int(left)


x = 6
problems = Solution()
print(problems.mysqrt(x))
