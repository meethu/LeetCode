class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = [-1, -1]
        n = len(nums)
        left, right, res = 0, n - 1, [-1, -1]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        res[0] = left if left < n and nums[left] == target else -1
        if res[0] == -1:
            return res
        while right < n - 1 and nums[right] == nums[right + 1]:
            right += 1
        res[1] = right
        return res

# 利用二分思想先找其左边界，再找其右边界即可，注意找左边界的时候，由右侧逼近；找右边界的时候，由左侧逼近，即可。

# # 利用库函数
# class Solution:
#     def searchRange(self, nums: [int], target: int) -> [int]:
#         if nums and target in nums: #if target in nums:
#             index = nums.index(target)
#             return [index, nums.count(target)+index-1]
#         else:
#             return [-1, -1]


# O(n) 算法

# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         res = []
#         for index, value in enumerate(nums):
#             if value == target:
#                 res.append(index)
#         if res:
#             return [res[0],res[-1]]
#         else:
#             return [-1,-1]
