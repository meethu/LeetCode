# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # nums1copy = []
#         nums1copy = nums1[:m]
#         nums1[:] = []
#         p1, p2 = 0, 0
#         while p1 < m and p2 < n:
#             if nums1copy[p1] < nums2[p2]:
#                 nums1.append(nums1copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
#              # if there are still elements to add  因为m n 数组大小不一样
#         if p1 < m:
#             nums1[p1 + p2:] = nums1copy[p1:]
#         if p2 < n:
#             nums1[p1 + p2:] = nums2[p2:]
#         return nums1   # leetcode 中不需要


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1

            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # if there are still elements to add  因为m n 数组大小不一样
        # 如果 p1 大于0 ，直接不做任何操作，因为本身就在nums1数组中
        if p2 > 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1


nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
m, n = 3, 3
problems = Solution()
print(problems.merge(nums1, m, nums2, n))
