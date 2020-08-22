# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        ret = []


        def dfs(root, target, tmp):
            if not root:
                return

            if target == root.val and not root.left and not root.right:
                ret.append(tmp + [root.val])
                return

            tmp.append(root.val)
            dfs(root.left, target - root.val, tmp)
            dfs(root.right, target - root.val, tmp)
            tmp.pop()

        dfs(root, sum, [])

        return ret
