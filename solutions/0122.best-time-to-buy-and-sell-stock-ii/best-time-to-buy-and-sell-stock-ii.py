# 算法可以直接简化为只要今天比昨天大，就卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                ans += prices[i + 1] - prices[i]
        return ans
