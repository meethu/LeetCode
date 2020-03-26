# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#  def flatten(self, root: TreeNode):
#         if root is None:
#             return
#         self.flatten(root.left)
#         self.flatten(root.right)
#         if root.left:
#             pre = root.left
#             while pre.right:
#                 pre = pre.right
#             pre.right = root.right
#             root.right = root.left
#             root.left = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root

        self.flatten(root.left)
        self.flatten(root.right)
        ltree, rtree = root.left, root.right
        root.right = ltree
        root.left = None

        p = root
        while p.right:
            p = p.right
        p.right = rtree

#     可以看图理解下这个过程。

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# //将 1 的左子树插入到右子树的地方
#     1
#      \
#       2         5
#      / \         \
#     3   4         6
# //将原来的右子树接到左子树的最右边节点
#     1
#      \
#       2
#      / \
#     3   4
#          \
#           5
#            \
#             6

#  //将 2 的左子树插入到右子树的地方
#     1
#      \
#       2
#        \
#         3       4
#                  \
#                   5
#                    \
#                     6

#  //将原来的右子树接到左子树的最右边节点
#     1
#      \
#       2
#        \
#         3
#          \
#           4
#            \
#             5
#              \
#               6

#   ......

# 作者：windliang
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/

# class Solution(object):
#     def flatten(self, root):
#         """
#         :type root: TreeNode
#         :rtype: void Do not return anything, modify root in-place instead.
#         """
#         self.visit(root)
#     def visit(self,nd):
#         if not nd:return None,None
#         if not (nd.left or nd.right):return nd,nd
#         l1,l2 = self.visit(nd.left)
#         r1,r2 = self.visit(nd.right)
#         nd.left = None
#         if l1:
#             nd.right = l1
#             l2 .right = r1
#         else:
#             nd.right = r1
#         if r2:return nd,r2
#         else:return nd,l2