# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 范例 中序打印为 321 为例，应该调整 3 和 1 的位置，但是会错误选择到 3 和 2 上去。 他给的判断语句是

#             if not firstNode and pre.val > p.val:
#                     firstNode = pre
#             if firstNode and pre.val > p.val:
#                 secondNode = p
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                # print(firstNode.val,pre.val, p.val)
                secondNode = p
            pre = p
            p = p.right

        firstNode.val, secondNode.val = secondNode.val, firstNode.val

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/zhong-xu-bian-li-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。