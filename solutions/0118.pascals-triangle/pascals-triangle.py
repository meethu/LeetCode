# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         result = [[1]]
#         if not numRows:
#             return []
#         if numRows == 1:
#             return [[1]]

#         for i in range(1, numRows):
#             result.append([])
#             for j in range(i + 1): # i 第一次循环为1时，其实已经是第二层！有两个元素！
#                 if j == 0 or j == i:
#                     result[i].append(1)
#                 else:
#                     result[i].append(result[i-1][j-1] + result[i-1][j])

#         return result

class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode/
