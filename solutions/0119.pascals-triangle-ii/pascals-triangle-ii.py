class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tmp = []
        for _ in range(rowIndex + 1):
            tmp.insert(0, 1)
            for i in range(1, len(tmp) - 1):
                tmp[i] = tmp[i] + tmp[i + 1]
        return tmp

# # 118题
# class Solution:
#     def generate(self, num_rows):
#         triangle = []

#         for row_num in range(num_rows):
#             # The first and last row elements are always 1.
#             row = [None for _ in range(row_num+1)]
#             row[0], row[-1] = 1, 1

#             # Each triangle element is equal to the sum of the elements
#             # above-and-to-the-left and above-and-to-the-right.
#             for j in range(1, len(row)-1):
#                 row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

#             triangle.append(row)

#         return triangle


#     def getRow(self, rowIndex: int) -> List[int]:
#         tmp = []
#         for _ in range(rowIndex + 1):
#             tmp.insert(0, 1)
#             for i in range(1, len(tmp) - 1):
#                 tmp[i] = tmp[i] + tmp[i+1]
#         return tmp

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii/solution/mo-ni-guo-cheng-by-powcai-5/


# def getRow(rowIndex):
#     # j行的数据, 应该由j - 1行的数据计算出来.
#     # 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
#     # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
#     r = [1]
#     for i in range(1, rowIndex + 1):
#         r.insert(0, 0)
#         # 因为i行的数据长度为i+1, 所以j+1不会越界, 并且最后一个1不会被修改.
#         for j in range(i):
#             r[j] = r[j] + r[j + 1]
#     return r

# print(getRow(5))

# 作者：leicj
# 链接：https://leetcode-cn.com/problems/pascals-triangle-ii/solution/python3-yang-hui-san-jiao-ii-by-leicj/
