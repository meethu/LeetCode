# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         self.result, self.flag, level = [], 1, 0
#         return self.helper(root, level)

#     def helper(self, node, level):

#         if len(self.result) == level:
#             self.result.append([])
#         if level & 1 == 1:
#             self.result[level].insert(0, node.val)
#         else:
#              self.result[level].append(node.val)

#         if node.left:
#             self.helper(node.left, level + 1)
#         if node.right:
#             self.helper(node.right, level + 1)
#         return self.result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        d1 = []  # 从左向右存储的栈
        d2 = []  # 从右向左存储的栈 d2和d1完成锯齿状存储的任务
        res = []  # 保存输出结果
        tmp = []  # 临时存储结果
        d1.append(root)
        while (True):
            while d1:
                curr = d1[-1]
                d1.pop()
                tmp.append(curr.val)
                if curr.left:  # 左边的节点先入栈
                    d2.append(curr.left)
                if curr.right:
                    d2.append(curr.right)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break

            while d2:
                curr = d2[-1]
                d2.pop()
                tmp.append(curr.val)
                if curr.right:  # 这里是右边的节点先入栈
                    d1.append(curr.right)
                if curr.left:
                    d1.append(curr.left)
            if tmp:
                res.append(tmp)
                tmp = []
            else:
                break

        return res

        # if ((level & 1) == 1){
        #     res.get(level).add(0, root.val);
        # } else {
        #     res.get(level).add(root.val);
        # }

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         self.result, level = [], 0
#         return self.helper(root, level)

#     def helper(self, node, level):
#         flag = 1
#         if len(self.result) == level:
#             self.result.append([])
#         self.result[level].append(node.val)
#         if node.left:
#             self.helper(node.left, level + 1)
#         if node.right:
#             self.helper(node.right, level + 1)
#         return self.result

