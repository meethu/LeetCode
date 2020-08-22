# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         ret = 0
#         visited = [False] * 10

#         def dfs(idx, tmp):
#             nonlocal ret
#             ret += 1
#             if idx == n:
#                 return
#             for i in range(10):
#                 if visited[i]:
#                     continue
#                 if idx == 0 and i == 0:
#                     continue
#                 tmp.append(i)
#                 visited[i] = True
#                 dfs(idx+1, tmp)
#                 tmp.pop()
#                 visited[i] = False
#         dfs(0, [])

#         return ret


#  * 排列组合：n位有效数字 = 每一位都从 0~9 中选择，且不能以 0 开头
#  * 1位数字：0~9                      10
#  * 2位数字：C10-2，且第一位不能是0      9 * 9
#  * 3位数字：C10-3，且第一位不能是0      9 * 9 * 8
#  * 4位数字：C10-4，且第一位不能是0      9 * 9 * 8 * 7
#  * ... ...
#  * 最后，总数 = 所有 小于 n 的位数个数相加


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n == 0: return 1

        first = 10
        second = 9 * 9

        for i in range(2, n + 1):
            first += second
            second *= 10 - i

        return first

# class Solution {
#     /**

#      */
#     public int countNumbersWithUniqueDigits(int n) {
#         if (n == 0) return 1;
#         int first = 10, second = 9 * 9;
#         int size = Math.min(n, 10);
#         for (int i = 2; i <= size; i++) {
#             first += second;
#             second *= 10 - i;
#         }
#         return first;
#     }
# }

# 作者：rainlight
# 链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits/solution/javaduo-jie-fa-hui-su-dong-tai-gui-hua-mei-ju-by-r/
