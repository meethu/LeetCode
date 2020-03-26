# 定义一个函数f(n)，以第n个数为结束点的子数列的最大和，存在一个递推关系f(n) = max(f(n-1) + A[n], A[n]);
# 将这些最大和保存下来后，取最大的那个就是，最大子数组和。因为最大连续子数组 等价于 最大的以n个数为结束点的子数列和 附代码
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, tmp = nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp = max(tmp + nums[i], nums[i]) # 递推关系f(n) = max(f(n-1) + A[n], A[n]);
            max_sum = max(max_sum, tmp)
        return max_sum

# 思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#          """
#         for i in range(1, len(nums)):
#             nums[i]= nums[i] + max(nums[i-1], 0)
#         return max(nums)
