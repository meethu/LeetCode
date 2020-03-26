# from typing import List


# class Solution:

#     def search(self, nums: List[int], target: int) -> bool:
#         size = len(nums)
#         if size == 0:
#             return False

#         left = 0
#         right = size - 1

#         while left < right:
#             mid = (left + right) >> 1
#             if nums[mid] > nums[left]:
#                 if nums[left] <= target <= nums[mid]:
#                     # 落在前有序数组里
#                     right = mid
#                 else:
#                     left = mid + 1
#             elif nums[mid] < nums[left]:
#                 # 让分支和上面分支一样
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid
#             else:
#                 # 要排除掉左边界之前，先看一看左边界可以不可以排除
#                 if nums[left] == target:
#                     return True
#                 left = left + 1
#         # 后处理，夹逼以后，还要判断一下，是不是 target
#         return nums[left] == target


# 部分bug版本  258 / 275 个通过测试用例
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        if size == 0:
            return False
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            # mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                # 右半部分有序
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[right] == target:
                    return True
                right = right - 1
        # 后处理
        return nums[left] == target

# from typing import List

# # 中间元素和右边界比较

# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         size = len(nums)
#         if size == 0:
#             return False
#         left = 0
#         right = size - 1
#         while left < right:
#             # mid = left + (right - left + 1) // 2
#             mid = (left + right + 1) >> 1
#             if nums[mid] < nums[right]:
#                 # 后面是有序的
#                 # [2,3,4,5,5,6,6,7]
#                 if nums[mid] <= target <= nums[right]:
#                     left = mid
#                 else:
#                     right = mid - 1
#             elif nums[mid] > nums[right]:
#                 # [3,4,5,5,6,6,7,2]
#                 if nums[left] <= target <= nums[mid - 1]:
#                     right = mid - 1
#                 else:
#                     left = mid
#             else:
#                 assert nums[mid] == nums[right]
#                 if nums[right] == target:
#                     return True
#                 # 右边不是才删除
#                 right = right - 1
#         # 后处理
#         return nums[left] == target