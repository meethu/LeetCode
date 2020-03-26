# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 最简单的解法就是递归，首先确认树非空，然后调用递归函数 helper(node, level)，参数是当前节点和节点的层次。程序过程如下：

# 输出列表称为 levels，当前最高层数就是列表的长度 len(levels)。比较访问节点所在的层次 level 和当前最高层次 len(levels) 的大小，如果前者更大就向 levels 添加一个空列表。
# 将当前节点插入到对应层的列表 levels[level] 中。
# 递归非空的孩子节点：helper(node.left / node.right, level + 1)。

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/


# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         self.levels, level = [], 0
#         if root is None: return []

#         return self.helper(root, level)

#     def helper(self, node, level):
#         if len(self.levels) == level:   # 开始新的一层
#             self.levels.append([])
#         # 添加当前层节点
#         self.levels[level].append(node.val)

#         # 处理下一层的孩子节点

#         if node.left:
#             self.helper(node.left, level + 1)
#         if node.right:
#             self.helper(node.right, level + 1)

#         return self.levels

# # https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/


# 第 0 层只包含根节点 root ，算法实现如下：

# 初始化队列只包含一个节点 root 和层次编号 0 ： level = 0。
# 当队列非空的时候：
# 在输出结果 levels 中插入一个空列表，开始当前层的算法。
# 计算当前层有多少个元素：等于队列的长度。
# 将这些元素从队列中弹出，并加入 levels 当前层的空列表中。
# 将他们的孩子节点作为下一层压入队列中。
# 进入下一层 level++。

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/


# 迭代
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            current_level = []  # 该轮循环的结果集
            for _ in range(level_size):  # 把该次queue里的数据循环一下,作为当前层的结果添加到 current_level
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)  # 判断当前的数据有没有子节点,有就加到node里
                if node.right:
                    queue.append(node.right)
            result.append(current_level)  # 重提示超时 我说怎么会超时呢!
        return result

# # # 迭代
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return []
#         queue = [root]                       #把root初始化一下进去
#         out = []
#         while queue:
#             child = []                       #该轮循环的结果集
#             node = []                        #存放while下一次的 数据集
#             for item in queue:               #把该次queue里的数据循环一下 添加到 child
#                 child.append(item.val)
#                 if item.left:
#                     node.append(item.left)   #判断当前的数据有没有子节点,有就加到node里
#                 if item.right:
#                     node.append(item.right)
#             out.append(child)                #把while这次的结果集放到输出数组里
#             queue = node                     #重要! 这是把 node里 搜集的该次循环节点的子节点 放到 queue里 之前漏写这一步就提示超时 我说怎么会超时呢!
#         return out
# 作者：ma-wen-bo
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/python3-bfsjian-ming-shi-xian-ceng-ci-bian-li-by-m/


