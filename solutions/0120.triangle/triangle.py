# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         length = len(triangle)
#         if not triangle:
#             return 0
#         for i in range(1,length):
#             for j in range(i+1):
#                 if j == 0:
#                     triangle[i][j] = triangle[i-1][j] + triangle[i][j]
#                 elif j == i:
#                      triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
#                 else:
#                     triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
#         return min(triangle[-1])

# 自底下往上，没有开辟其他空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        for i in range(row - 2, -1, -1):  # 状态转移是从倒数第二行开始的（也就是递推的顺序）
            for j in range(i + 1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]
