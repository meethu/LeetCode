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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        visited = [False] * len(nums)

        def backtrack(nums, tmp):

            if len(tmp) == len(nums):
                ret.append(tmp[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                tmp.append(nums[i])
                visited[i] = True
                backtrack(nums, tmp)
                visited[i] = False
                tmp.pop()

        backtrack(nums, [])

        return ret


# https://leetcode-cn.com/problems/permutations/solution/xiong-mao-shua-ti-python3-di-gui-qiu-jie-8xing-by-/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []

        def backtrack(nums, tmp):

            if len(tmp) == len(nums):
                ret.append(tmp[:])
                return

            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                backtrack(nums, tmp)
                tmp.pop()

        backtrack(nums, [])

        return ret


nums = [1, 2, 3]
problems = Solution()
print(problems.permute(nums))
