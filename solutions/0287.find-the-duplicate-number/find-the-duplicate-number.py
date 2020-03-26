# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         left = 1
#         right = len(nums)
#         while left < right:
#             mid = left + (right - left) // 2
#             cnt = 0
#             for num in nums:
#                 if num <= mid:  # 如果这些数字小于中位数，那么 +1 计数
#                     cnt += 1
#             if cnt <= mid:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1

            counter = 0
            for num in nums:
                if num < mid:
                    counter += 1

            if counter >= mid:
                # 如果小于 4 的个数等于 4 或者更多
                # 那么重复的数一定位于 1、2、3
                right = mid - 1
            else:
                left = mid

        return left

    # class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:

#         ''' 1、暴力不符合题意
#         for i in nums:
#             count = 0
#             for num in nums:
#                 if num == i:
#                     count += 1
#             if count > 1:
#                 return i
#         return -1
#         '''

#         '''2、小于O(n^2) 二分查找
#         我们不要考虑数组,只需要考虑 数字都在 1 到 n 之间
#         示例 1:
#         arr = [1,3,4,2,2] 此时数字在 1 — 5 之间

#         mid = (1 + 5) / 2 = 3 arr小于等于的3有4个(1,2,2,3)，1到3中肯定有重复的值
#         mid = (1 + 3) / 2 = 2 arr小于等于的2有3个(1,2,2)，1到2中肯定有重复的值
#         mid = (1 + 2) / 2 = 1 arr小于等于的1有1个(1)，2到2中肯定有重复的值
#         所以重复的数是 2
#         '''
#         left = 1
#         right = len(nums)
#         while left < right:
#             mid = left + (right - left)//2
#             cnt = 0
#             for num in nums:
#                 if num <= mid:  # 如果这些数字小于中位数，那么 +1 计数
#                     cnt += 1
#             if cnt <= mid:
#                 left = mid + 1
#             else:
#                 right = mid
#         return right


# class Solution {
#     public int findDuplicate(int[] nums) {
#         /**
#         快慢指针思想, fast 和 slow 是指针, nums[slow] 表示取指针对应的元素
#         注意 nums 数组中的数字都是在 1 到 n 之间的(在数组中进行游走不会越界),
#         因为有重复数字的出现, 所以这个游走必然是成环的, 环的入口就是重复的元素,
#         即按照寻找链表环入口的思路来做
#         **/
#         int fast = 0, slow = 0;
#         while(true) {
#             fast = nums[nums[fast]];
#             slow = nums[slow];
#             if(slow == fast) {
#                 fast = 0;
#                 while(nums[slow] != nums[fast]) {
#                     fast = nums[fast];
#                     slow = nums[slow];
#                 }
#                 return nums[slow];
#             }
#         }
#     }
# }
