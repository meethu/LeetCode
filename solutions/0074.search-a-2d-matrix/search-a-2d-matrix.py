# 菜鸡的写法
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

#         if not matrix or len(matrix[0]) == 0:
#             return False

#         row = len(matrix)
#         if target < matrix[0][0] or target > matrix[-1][-1]:
#             return False
#         for i in range(row):
#             if target in matrix[i]:
#                 return True
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1

        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
        return matrix[left // col][left % col] == target