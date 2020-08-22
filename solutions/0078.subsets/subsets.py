class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(nums, idx, tmp):
            # if idx > len(nums):
            #     return
            ret.append(tmp[:])
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, i + 1, tmp)
                tmp.pop()

        backtrack(nums, 0, [])
        return ret


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
