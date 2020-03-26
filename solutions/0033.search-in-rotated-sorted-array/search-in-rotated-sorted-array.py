# 将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
# 此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。

class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            # mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                # 右半部分有序
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        # 后处理
        return left if nums[left] == target else -1
