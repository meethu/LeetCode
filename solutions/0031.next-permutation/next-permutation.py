class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length, firstidx = len(nums), -1
        i = length - 1
        while i >= 1:
            if nums[i - 1] < nums[i]:
                firstidx = i - 1
                break
            i -= 1

        if firstidx == -1:
            nums[:] = nums[::-1]
            return
        for j in range(length - 1, firstidx + 1, -1):
            if nums[j] > nums[firstidx]:
                nums[j], nums[firstidx] = nums[firstidx], nums[j]
                break
        nums[firstidx + 1:] = reversed(nums[firstidx + 1:])

        return nums


nums = [1, 3, 2]
problems = Solution()
print(problems.nextPermutation(nums))
