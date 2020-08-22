# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ret = []

        while queue:

            size = len(queue)
            # 临时存放当层结果
            tmp = []

            for _ in range(size):

                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(tmp)
        return ret
