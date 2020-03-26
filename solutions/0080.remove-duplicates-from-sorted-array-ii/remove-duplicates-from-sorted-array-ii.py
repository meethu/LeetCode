class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i

# class Solution(object):

#     # 模板写法

#     def removeDuplicates(self, nums, k):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         size = len(nums)
#         if size <= 2:
#             return size
#         # counter 表示下一个要覆盖的索引
#         counter = k
#         # 索引为 0 和 1 的数一定会被保留，因此遍历从索引 2 开始
#         for i in range(k, size):
#             if nums[i] != nums[counter - k]:
#                 nums[counter] = nums[i]
#                 counter += 1
#         return counter
# Python3: 从第三个元素开始遍历，看其是否与第一个元素相等，相等就删掉，否则向后一位；

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 2
#         while i < len(nums):
#             if nums[i]==nums[i-2]:
#                 nums[:] = nums[:i]+nums[i+1:]
#             else:
#                 i += 1

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         flag, count = 0, 0
#         for num in nums:
#
#             if nums[flag] != num:
#                 if count < 3:
#                     flag += count
#                     count = 0
#                 else:
#                     while count > 2:
#                         nums[flag+2] = num
#                         flag += 1
#                         count -= 1
#                     count = 0
#             count += 1