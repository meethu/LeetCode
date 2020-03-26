class Solution:
    def permute(self, nums):
        result, temp = [], []
        return self.backtrack(nums, temp, result)

    def backtrack(self, nums, temp, result):
        if not nums:  # nums 里面没有元素，代表已经被用完，直接将temp返回
            result.append(temp)

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], temp + [nums[i]], result)
        return result


# from typing import List
#
#
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#         backtrack(nums, [])
#         return res


nums = [1, 2, 3]
problems = Solution()
print(problems.permute(nums))
