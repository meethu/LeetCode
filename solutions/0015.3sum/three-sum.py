class Solution():

    def threesum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(res)

    # # # 双指针
    # def threesum(self, nums):
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     res = []
    #     for i in range(len(nums) - 2):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         left, right = i + 1, len(nums) - 1
    #         while left < right:
    #             sum = nums[i] + nums[left] + nums[right]
    #             if sum < 0:
    #                 left += 1
    #             elif sum > 0:
    #                 right -= 1
    #             else:
    #                 res.append((nums[i], nums[left], nums[right]))
    #                 while left < right and nums[left] == nums[left+1]:  # 跳过相同数字
    #                     left += 1
    #                 while left < right and nums[right] == nums[right-1]:
    #                     right -= 1
    #                 left += 1
    #                 right -= 1
    #     return res




nums = [-1, 0, 1, 2, -1, -4]

problems = Solution()
print(problems.threesum(nums))