class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.dfs(nums, [], results)
        return results

    def dfs(self, nums, temp, results):
        if len(nums) == 0:
            results.append(temp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], temp+[nums[i]], results)

nums = [3, 2, 3, 3]
problems = Solution()
print(problems.permuteUnique(nums))
