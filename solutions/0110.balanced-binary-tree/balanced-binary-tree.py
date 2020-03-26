# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        depth_left, depth_right = self.depth(root.left), self.depth(root.right)
        return abs(depth_left - depth_right) <= 1

# 是平衡二叉树的条件：

# 左子树是平衡二叉树。
# 右子树是平衡二叉树。
# 左右子树之间的深度不超过1
