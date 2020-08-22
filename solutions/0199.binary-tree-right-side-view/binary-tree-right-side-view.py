# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def __init__(self):
#         self.ret = []

#     def rightSideView(self, root: TreeNode) -> List[int]:

#         if not root:
#             return []

#         finalRet =  self.helper(root, 0)

#         return [num[-1] for num in finalRet]


#     def helper(self, node, level):
#         if len(self.ret) == level:
#             self.ret.append([])

#         self.ret[level].append(node.val)

#         if node.left:
#             self.helper(node.left, level+1)

#         if node.right:
#             self.helper(node.right, level+1)

#         return self.ret

# from collections import deque

# class Solution:

#     def rightSideView(self, root: TreeNode) -> List[int]:

#         if not root:
#             return []

#         # 存放结果
#         ret = []

#         queue = deque([root])


#         while queue:
#             size = len(queue)

#             # 遍历当前层的所有节点
#             for i in range(size):
#                 node = queue.popleft()

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#                 # （从左到右遍历）保留最后有一个节点的值
#                 if i == size - 1:
#                     ret.append(node.val)

#         return ret

# BFS
# from collections import deque

# class Solution:

#     def rightSideView(self, root: TreeNode) -> List[int]:

#         if not root:
#             return []

#         # 存放结果
#         ret = []

#         queue = deque([root])


#         while queue:
#             size = len(queue)

#             # 遍历当前层的所有节点
#             for i in range(size):
#                 node = queue.popleft()

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#                 # （从左到右遍历）保留最后有一个节点的值
#                 if i == size - 1:
#                     ret.append(node.val)

#         return ret


# DFS
# class Solution:

#     def rightSideView(self, root: TreeNode) -> List[int]:

#         if not root:
#             return []

#         # 存放结果
#         ret = []

#         queue = deque([root])


#         while queue:
#             size = len(queue)

#             # 遍历当前层的所有节点
#             for i in range(size):
#                 node = queue.popleft()

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#                 # （从左到右遍历）保留最后有一个节点的值
#                 if i == size - 1:
#                     ret.append(node.val)

#         return ret

# BFS

class Solution:
    def __init__(self):
        self.ret = []

    def dfs(self, node, level):
        if not node:
            return

        # 如果当前节点所在深度还没有出现在ret里，说明在该深度下当前节点是第一个被访问的节点，因此将当前节点加入ret中

        if len(self.ret) == level:
            self.ret.append(node.val)

        self.dfs(node.right, level + 1)

        self.dfs(node.left, level + 1)

        return self.ret

    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        return self.dfs(root, 0)