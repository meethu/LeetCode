# 每个站点加的油总量必须不小于到达此站点消耗的总油量。如果每个站点加的油总量和小于消耗的总油量，则肯定环绕不了一周
# 对于加油站 i ，如果 gas[i] - cost[i] < 0 ，则不可能从这个加油站出发，因为在前往 i + 1 的过程中，汽油就不够了。
# 下一步我们把这个加油站当做新的起点，并将 curr_tank 重置为 0 ，因为重新出发，油箱中的油为 0 。
# （从上一次重置的加油站到当前加油站的任意一个加油站出发，到达当前加油站之前， curr_tank 也一定会比 0 小）

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank, start_station = 0, 0, 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0
        return start_station if total_tank >= 0 else -1;
