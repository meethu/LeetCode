# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:

#         left, right = 0, len(nums) - 1

#         while left < right:
#             mid = left + (right - left) // 2

#             if nums[mid] < nums[mid+1]:
#                 left = mid + 1
#             else:
#                 right = mid

#         return left


# 由于题目假设nums[-1]=nums[n]=-∞。所以，我们从0开始往后遍历元素，如果某个元素大于其后面的元素，则该元素就是峰值元素。（但是它时O(n)，不符合题意）
# O(logN)一般考虑二分搜索。有如下规律：
# 规律一：如果nums[i] > nums[i+1]，则在i之前一定存在峰值元素
# 规律二：如果nums[i] < nums[i+1]，则在i+1之后一定存在峰值元素


# 为什么二分查找大的那一半一定会有峰值呢？
# （即nums[mid]<nums[mid+1]时，mid+1~N一定存在峰值）
# 首先已知 nums[mid+1]>nums[mid]，那么mid+2只有两种可能，一个是大于mid+1，一个是小于mid+1，
# 小于mid+1的情况，那么mid+1就是峰值，大于mid+1的情况，继续向右推，如果一直到数组的末尾都是大于的，
# 那么可以肯定最后一个元素是峰值，因为nums[nums.length] = 负无穷

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        return left if nums[left] > nums[right] else right
