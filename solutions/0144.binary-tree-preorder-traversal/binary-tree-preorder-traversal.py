# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        stack, ret = [], []

        while root or stack:
            while root:
                ret.append(root.val)
                stack.append(root)
                root = root.left

            node = stack.pop()
            root = node.right
        return ret

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return res