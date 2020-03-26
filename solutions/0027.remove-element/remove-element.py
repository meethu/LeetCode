# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag = 0
        for num in nums:
            if num != val:
                nums[flag] = num
                flag += 1
        return flag
            


# 既然问题要求我们就地删除给定值的所有元素，我们就必须用O(1) 的额外空间来处理它。如何解决？我们可以保留两个指针 i 和 j，其中 i 是慢指针，jj是快指针。


# 当 nums[j]  与给定的值相等时，递增 j 以跳过该元素。只要 nums[j] != val，
# 我们就复制 nums[j] 到 nums[i] 并同时递增两个索引。重复这一过程，直到 j 到达数组的末尾，该数组的新长度为 i。

# 链接：https://leetcode-cn.com/problems/remove-element/solution/yi-chu-yuan-su-by-leetcode/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

# 双指针做法
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         j = 0
#         for i in range(len(nums)):
#             if(nums[i] == val):
#                 continue
#             else:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
