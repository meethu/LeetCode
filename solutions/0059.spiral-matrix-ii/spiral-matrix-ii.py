class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while c <= n * n:
            # 从左向右
            for i in range(j, n - j):
                array[j][i] = c
                c += 1
            # 从上往下走
            for i in range(j + 1, n - j):
                array[i][n - j - 1] = c
                c += 1
            # 从右往左走
            for i in range(n - j - 2, j - 1, -1):
                array[n - j - 1][i] = c
                c += 1
            # 从下往上走
            for i in range(n - j - 2, j, -1):
                array[i][j] = c
                c += 1
            j += 1
        return array

# class Solution:
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         res = [[0] * n for _ in range(n)]
#         i, j, dx, dy = 0, 0, 0, 1
#         for num in range(1, n*n+1):
#             res[i][j] = num
#             if res[(i+dx)%n][(j+dy)%n] > 0:
#                 dx, dy = dy, -dx
#             i += dx
#             j += dy
#         return res
