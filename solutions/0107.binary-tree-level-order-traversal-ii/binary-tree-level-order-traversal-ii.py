# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        ret = []

        while queue:
            size = len(queue)
            tmp = []

            for _ in range(size):
                node = queue.popleft()

                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ret.insert(0, tmp)

        return ret

# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         self.result, level = [], 0
#         return self.helper(root, level)
#
#     def helper(self, node, level):
#         len_size = len(self.result)
#         if len_size == level:
#             self.result.insert(0, [])
#         self.result[len_size - 1 - level].append(node.val)
#         if node.left:
#             self.helper(node.left, level + 1)
#         if node.right:
#             self.helper(node.right, level + 1)
#         return self.result


# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#
#         stack, result = [root], []
#
#         while stack:
#             current_level = []
#             temp = []
#             for item in stack:
#                 current_level.append(item.val)
#                 if item.left:
#                     temp.append(item.left)
#                 if item.right:
#                     temp.append(item.right)
#                 stack = temp
#             result.insert(0, current_level)
#         return result

nums = [1, 2, 2]
problems = Solution()
print(problems.subsetsWithDup(nums))
