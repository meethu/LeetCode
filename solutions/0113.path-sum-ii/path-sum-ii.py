# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result, temp = [], []
        if not root:
            return []
        return self.helper(root, sum, temp)

    def helper(self, root, sum, temp):

        if not root.left and not root.right and sum - root.val == 0:
            temp += [root.val]
            self.result.append(temp)
        if root.left:
            self.helper(root.left, sum - root.val, temp + [root.val])
        if root.right:
            self.helper(root.right, sum - root.val, temp + [root.val])
        return self.result