"""
思路：

首先创建一个字典，target 和 item 相减，如果目标 result 在字典中，直接返回 res[result],即 result 下标，以及此刻item下标
如果result没有在字典中，那么将此时进行的item（值），以及index(键)存入字典 res
"""


# Hash 表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for (idx, item) in enumerate(nums):
            tmp = target - item
            if tmp in res:
                return res[tmp], idx
            res[item] = idx
        return None

        

# 变形，输出所有可能的答案
class Solution():

    def twosum(self, nums, target):
        tmp = {}  # 创建字典
        res = []
        for index, item in enumerate(nums):
            result = target - item
            if result in tmp:  # 如果result好办在字典内，直接返回，否则将此时的item放入字典
                res.append([tmp[result], index])
            tmp[item] = index
        return res


nums = [2, 7, 11, 15, 3, 6]
target = 9

problems = Solution()
print(problems.twosum(nums, target))
