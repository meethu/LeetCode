# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 首先判断 p 和 q 是不是 None，然后判断它们的值是否相等。
# 若以上判断通过，则递归对子结点做同样操作。
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True  # p q 均为 None，直接返回 True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)