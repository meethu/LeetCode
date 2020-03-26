class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])  # row 列 ，clo 行
        for i in range(row):
            for j in range(col):
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i - 1][j]
                elif i != 0 and j != 0:
                    grid[i][j] = grid[i][j] + min(grid[i][j - 1], grid[i - 1][j])
                else:
                    grid[i][j] = grid[0][0]
        return grid[-1][-1]

# python 左上角开始
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         dp = [0 for _ in range(len(grid[0]))]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == 0 and j == 0:
#                     dp[j] = grid[i][j]
#                 elif i == 0 and j != 0:
#                     dp[j] = dp[j - 1] + grid[i][j]
#                 elif i != 0 and j == 0:
#                     dp[j] = dp[j] + grid[i][j]
#                 else:
#                     dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
#         return dp[-1]
