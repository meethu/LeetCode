# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if not inorder: return None
#         root = TreeNode(postorder[-1])
#         loc = inorder.index(postorder[-1])
#         root.left = self.buildTree(inorder[ : loc], postorder[ :loc])
#         root.right = self.buildTree(inorder[loc+1:], postorder[loc:-1])
#         return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        idx_map = {val:idx for idx, val in enumerate(inorder)}
        root = TreeNode(postorder.pop())
        idx = idx_map[root.val]

        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root