# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [(root, 1)]
        max_dep = 0
        while queue:
            node, depth = queue.pop()
            max_dep = max(max_dep, depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return max_dep

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))