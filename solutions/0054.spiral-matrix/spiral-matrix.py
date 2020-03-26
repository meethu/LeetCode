# tql 做法!
# 将已经走过的地方置0，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向：
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                res.append(matrix[i][j])  # 将 maxtrix[i][j] 存入，将该位置的数置 none
                matrix[i][j]  = None
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == None:
                    di, dj = dj, -di
                i += di
                j += dj
            return res


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix : return []
#         res = []
#         while matrix:
#             res.extend(matrix.pop(0))
#             next_matrix = []
#             #print(matrix)
#             for x in zip(*matrix):
#                 next_matrix.append(x)
#             #print(next_matrix)
#             matrix = next_matrix[::-1]
#         return res

# class Solution:
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         if not matrix : return []
#         shang_row = 0
#         xia_row = len(matrix) - 1 
#         zuo_col = 0
#         you_col = len(matrix[0]) - 1
#         res = []
#         while shang_row <= xia_row  and  zuo_col <= you_col:
#             # 从左到右
#             for i in range(zuo_col, you_col+1):
#                 #print(shang_row, i)
#                 res.append(matrix[shang_row][i])
#             shang_row += 1
#             if shang_row > xia_row:break
#             # 从上到下
#             for i in range(shang_row, xia_row+1):
#                 res.append(matrix[i][you_col])
#             you_col -= 1
#             if zuo_col > you_col:break
#             # 从右到左
#             for i in range(you_col, zuo_col - 1,-1):
#                 #print(xia_row - 1, i)
#                 res.append(matrix[xia_row][i])
#             xia_row -= 1
#             # 从下到上
#             for i in range(xia_row , shang_row - 1, -1):
#                 #print(i, zuo_col)  
#                 res.append(matrix[i][zuo_col])
#             zuo_col += 1
#         return res


# 作者：powcai
# 链接：https://leetcode-cn.com/problems/spiral-matrix/solution/mo-ni-guo-cheng-by-powcai-2/
        
# 逆时针旋转矩阵：先转置，再上下翻转。
# 顺时针旋转矩阵：先上下翻转，再转置。

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         while matrix:
#             res += matrix.pop(0)
#             matrix = list(map(list, zip(*matrix)))[::-1]
#         return res

# 作者：suixin-3
# 链接：https://leetcode-cn.com/problems/spiral-matrix/solution/na-yi-xing-ni-shi-zhen-zhuan-yi-xia-by-suixin-3/
# 来源：力扣（LeetCode）
        
# class Solution:
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         res = []
#         while matrix:
#             res.extend(matrix.pop(0))
#             matrix = [*zip(*matrix)][::-1]
#         return res
        
# 将已经走过的地方置0，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向：

# r, i, j, di, dj = [], 0, 0, 0, 1
# if matrix != []:
#     for _ in range(len(matrix) * len(matrix[0])):
#         r.append(matrix[i][j])
#         matrix[i][j] = 0
#         if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
#             di, dj = dj, -di
#         i += di
#         j += dj
# return r



# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         # 取首行，去除首行后，对矩阵翻转来创建新的矩阵，
#         # 再递归直到新矩阵为[],退出并将取到的数据返回
#         ret = []
#         if matrix == []:
#             return ret
#         ret.extend(matrix[0]) # 上侧
#         new = [reversed(i) for i in matrix[1:]]
#         if new == []:
#             return ret
#         r = self.spiralOrder([i for i in zip(*new)])
#         ret.extend(r)
#         return ret