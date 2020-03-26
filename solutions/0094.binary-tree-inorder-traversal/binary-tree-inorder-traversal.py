# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []
#         else:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# 借用堆栈
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result