from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = deque([root])
        ret = []
        flag = 0

        while queue:
            size = len(queue)
            tmp = []

            for _ in range(size):
                node = queue.popleft()
                if flag & 1 == 0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(tmp)
            # 层次
            flag += 1
        return ret


def createTree(nums, index):
    node = None
    if index < len(nums):
        if not nums[index]:
            return
        node = TreeNode(nums[index])
        node.left = createTree(nums, 2 * index + 1)
        node.right = createTree(nums, 2 * index + 2)
    return node


nums = [3, 9, 20, None, None, 15, 7]
# 创建树
root = createTree(nums, 0)
print(Solution().levelOrder(root))
