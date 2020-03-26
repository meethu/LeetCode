class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums):
        return self.helper(nums, 0, [])

    def helper(self, nums, index, temp):
        if index == len(nums):
            self.result.append(temp)
            return
        self.result.append(temp)
        for i in range(index, len(nums)):
            self.helper(nums, i + 1, temp + [nums[i]])
        return self.result


# 思路一：库函数
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for i in range(len(nums)+1):
#             for tmp in itertools.combinations(nums, i):
#                 res.append(tmp)
#         return res
# 思路二:迭代

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in nums:
#             res = res + [[i] + num for num in res]
#         return res

# https://leetcode-cn.com/problems/subsets/solution/liang-chong-fang-fa-qiu-jie-zi-ji-by-tangzixia/
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/

nums = [1, 2, 3]
problems = Solution()
print(problems.subsets(nums))