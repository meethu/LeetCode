class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ret = []
        nums.sort()
        visited = [False] *  len(nums)

        def backtrack(nums, tmp):

            if len(tmp) == len(nums):
                ret.append(tmp[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and visited[i-1]:
                    break
                tmp.append(nums[i])
                visited[i] = True
                backtrack(nums, tmp)
                tmp.pop()
                visited[i] = False

        backtrack(nums, [])

        return ret


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
