# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         self.result, self.flag, level = [], 1, 0
#         return self.helper(root, level)

#     def helper(self, node, level):

#         if len(self.result) == level:
#             self.result.append([])
#         if level & 1 == 1:
#             self.result[level].insert(0, node.val)
#         else:
#              self.result[level].append(node.val)

#         if node.left:
#             self.helper(node.left, level + 1)
#         if node.right:
#             self.helper(node.right, level + 1)
#         return self.result


class Solution:


    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = deque([root])
        ret = []
        flag = 0

        while queue:
            size = len(queue)
            tmp = []

            for _ in range(size):
                node = queue.popleft()
                if flag & 1 == 0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(tmp)
            # 层次
            flag += 1
        return ret