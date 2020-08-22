# 翻译过来：

# 先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
# 再找出另一个最大索引 l 满足 nums[l] > nums[k]；
# 交换 nums[l] 和 nums[k]；
# 最后翻转 nums[k+1:]
# 举个例子：

# 比如 nums = [1,2,7,4,3,1]，下一个排列是什么？
# 我们找到第一个最大索引是 nums[1] = 2
# 再找到第二个最大索引是 nums[5] = 3
# 交换，nums = [1,3,7,4,2,1];
# 翻转，nums = [1,3,1,2,4,7]
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-powcai/


# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         length, firstidx = len(nums), -1
#         i = length - 1
#         while i >= 1:
#             if nums[i-1] < nums[i]:
#                 firstidx = i - 1
#                 break
#             i -= 1
#         if firstidx == -1:
#             nums[:] = nums[::-1]
#             return
#         for j in range(length -1, firstidx, -1):
#             if nums[j] > nums[firstidx]:
#                 nums[j], nums[firstidx] = nums[firstidx], nums[j]
#                 break
#         nums[firstidx+1:] = reversed(nums[firstidx+1:])

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        elif n == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        i, j = n - 2, n - 1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])

    #     class Solution:


#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """

#         l=len(nums)
#         for i in range(l-2,-1,-1):
#             for j in range(l-1,i,-1):
#                 if nums[j]>nums[i]:
#                     nums[j],nums[i]=nums[i],nums[j]
#                     nums[i+1:l]=sorted(nums[i+1:l])
#                     return

#         nums.sort()

# 应该先把nums[i+1:]排序，再从nums[i+1:]中遍历出第一个比nums[i]大的值并交换位置
# 判断按照字典序有木有下一个，如果完全降序就没有下一个
# 如何判断有木有下一个呢？只要存在a[i-1] < a[i]的升序结构，就有，而且我们应该从右往左找，一旦找到，因为这样才是真正下一个
# 当发现a[i-1] < a[i]的结构时，从在[i, ∞]中找到最接近a[i-1]并且又大于a[i-1]的数字，由于降序，从右往左遍历即可得到k
# 然后交换a[i-1]与a[k]，然后对[i, ∞]排序即可，排序只需要首尾不停交换即可，因为已经是降序 上面说的很抽象，还是需要拿一些例子思考才行，比如[0,5,4,3,2,1]，下一个是[1,0,2,3,4,5]

nums = [1, 3, 2]
problems = Solution()
print(problems.nextPermutation(nums))
