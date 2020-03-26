# 记录【今天之前买入的最小值】
# 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
# 比较【每天的最大获利】，取最大值即可
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minp, maxp = prices[0], 0
        for i in range(len(prices)):
            minp = min(minp, prices[i])  # 今天之前买入的最小值和今天价格比较
            maxp = max(maxp, prices[i] - minp)  # 今天之前卖出的最大值和今天卖出价格(今天价格 - 今天之前买入最低价格)比较
        return maxp
