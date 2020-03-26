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
        self.index_map = {val: idx for idx, val in enumerate(inorder)}
        self.postidx = -1
        self.inorder = inorder
        self.postorder = postorder
        return self.helper(0, len(inorder))

    def helper(self, in_left, in_right):
        if in_left == in_right:
            return None

        root = TreeNode(self.postorder[self.postidx])

        location = self.index_map[self.postorder[self.postidx]]

        self.postidx -= 1

        root.right = self.helper(location + 1, in_right)
        root.left = self.helper(in_left, location)

        return root