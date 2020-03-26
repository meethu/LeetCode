# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        return self.dfs(root, 0)
        
    def dfs(self, root, tmp):
        if not root:
            return 0
        tmp = tmp * 10 + root.val
        
        if not root.left and not root.right:
            self.res += tmp
            
        self.dfs(root.left, tmp)
        self.dfs(root.right, tmp)
        
        return self.res


# class Solution:
#     def __init__(self):
#         self.result = 0
        
#     def sumNumbers(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return
#         if root.left:
#             root.left.val += 10 * root.val
#         if root.right:
#             root.right.val += 10 * root.val

#         if not root.left and not root.right:
#             self.result += root.val

#         self.sumNumbers(root.left)
#         self.sumNumbers(root.right)
#         return self.result