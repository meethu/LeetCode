class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return matrix
        n = len(matrix[0])
        flag = False
        if 0 in matrix[0]:  # 如果第一行有 0 ，flag 置 true
            flag = True
        for i in range(1, m):  # 1 - m 行
            for j in range(n):  # 0- j 列
                if matrix[i][j] == 0:  # 如果 matrix[i][j] 为 0
                    matrix[i][0] = 0  # 这一行首元素设置为0
                    matrix[0][j] = 0  # 这一列首元素设置为0
        for i in range(1, m):  # 1 - m 列，如果首元素为0，那么这一列全部置0
            if matrix[i][0] == 0:
                matrix[i] = [0] * n  # n个0
        for i in range(n):
            if matrix[0][i] == 0:  # 如果首行元素中有元素为 0 ，那么 遍历对应的 1-m列，全部置 0
                for j in range(1, m):
                    matrix[j][i] = 0
        if flag:
            matrix[0] = [0] * n  # 如果首行有 0 ，全部置0

# class Solution:
#     def setZeroes(self, matrix):
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         r = []
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     r.append([i,j])
#        # print(r)
#         for i in r:
#             matrix[i[0]] = [0 for _ in range(n)]
#         for i in r:
#             for j in range(m):
#                 matrix[j][i[1]] = 0

#         return matrix


# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         R = len(matrix)
#         C = len(matrix[0])
#         rows, cols = set(), set()

#         # Essentially, we mark the rows and columns that are to be made zero
#         for i in range(R):
#             for j in range(C):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)

#         # Iterate over the array once again and using the rows and cols sets, update the elements
#         for i in range(R):
#             for j in range(C):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/set-matrix-zeroes/solution/ju-zhen-zhi-ling-by-leetcode/


# class Solution:
#     def setZeroes(self, matrix):
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         r = []
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     r.append([i,j])
#        # print(r)
#         for i in r:
#             matrix[i[0]] = [0 for _ in range(n)]
#         for i in r:
#             for j in range(m):
#                 matrix[j][i[1]] = 0

#         return matrix
