class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curl, p1 = 0, 0, len(nums) - 1

        while curl <= p1:
            if nums[curl] == 0:
                nums[p0], nums[curl] = nums[curl], nums[p0]
                p0 += 1
                curl += 1
            elif nums[curl] == 2:
                nums[p1], nums[curl] = nums[curl], nums[p1]
                p1 -= 1
            else:
                curl += 1
        return nums  # leetcode 中不需要返回 nums


# 测试用例
# [2,0,2,1,1,0]
# [2,0,1]
# [1,2,0]

nums = [2, 0, 2, 1, 1, 0]
problems = Solution()
print(problems.sortColors(nums))
