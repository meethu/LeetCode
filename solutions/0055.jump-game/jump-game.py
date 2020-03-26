class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx, n = 0, len(nums)
        
        for i in range(n):
            if maxidx >= n -1:  # 如果到某个位置，maxidx可以直接到最后一个元素，那么直接返回true
                return True
            if i > maxidx:   # i 这个位置，从前面开始到不了 i 这个位置，更不用说到最后
                return False
            maxidx = max(maxidx, i + nums[i])
            
        return False