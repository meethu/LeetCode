# 除 K 取余数
# class Solution(object):
#     def hammingweight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         result = 0
#         while(n):
#             result += n % 2
#             n = n >> 1
#         return result

# 位运算
class Solution(object):
    def hammingweight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n):
            n = n & (n - 1)   # 清除最低位的1，如果有1存在，n大于0
            count += 1
        return count
n = 3
problems = Solution()
print(problems.hammingweight(n))