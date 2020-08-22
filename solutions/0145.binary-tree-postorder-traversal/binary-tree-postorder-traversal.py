# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ret = [], []

        while root or stack:
            while root:
                ret.insert(0, root.val)
                stack.append(root)
                root = root.right
            node = stack.pop()
            root = node.left
        return ret