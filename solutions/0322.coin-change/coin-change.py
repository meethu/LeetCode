class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        ret = [0] * (amount + 1)

        for i in range(1, amount + 1):
            cost = float('inf')

            for c in coins:
                if i - c >= 0:
                    cost = min(cost, ret[i - c] + 1)
            ret[i] = cost

        return ret[amount] if ret[amount] != float('inf') else -1