# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):  # 中序遍历，递增
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

#  class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def helper(node, lower = float('-inf'), upper = float('inf')):
#             if not node:
#                 return True

#             val = node.val
#             if val <= lower or val >= upper:
#                 return False

#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False
#             return True

#         return helper(root)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode/