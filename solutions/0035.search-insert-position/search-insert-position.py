class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1


from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判 1
        if size == 0:
            return 0
        # 特判 2：如果比最后一个数字还要大，直接接在它后面就可以了
        if target > nums[-1]:
            return size

        left = 0
        right = size - 1
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                right = mid
        return left
