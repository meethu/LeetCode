class Solution:
    def maxSlidingWindow(self, nums, k):
        if nums is None:
            return []
        windows, res = [], []
        for i, x in enumerate(nums):
            if i >= k and windows[0] <= i - k:  # i >k 并且滑动窗口最左侧元素下标小于i-k，在窗口以外
                windows.pop(0)
            while windows and nums[windows[-1]] <= x:  # 保持最右侧元素最大，（左侧元素比右侧小）当窗口元素不为空，并
                windows.pop()
            windows.append(i)
            if i >= k - 1:  # k = 3, i >= 2 恰好满足最小滑动窗口大小
                res.append(nums[windows[0]])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
problems = Solution()
print(problems.maxSlidingWindow(nums, k))
