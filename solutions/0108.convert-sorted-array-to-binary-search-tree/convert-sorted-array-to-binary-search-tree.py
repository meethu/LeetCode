# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 平衡二叉搜索树的特点是：每个节点的左右子树都高度差在1以内，每个节点左子树小于右子树。
# 根据平衡二叉搜索树的特点，可以联想到，每个节点当做根节点的时候，左子树形成的数组一定比它小，右子树形成的数组一定比他大。
# 因此，符合有序数组任意子数组中点的性质。
# 结合树结构常用的递归思想，可以采用DFS，递归构建这颗树，为了实现每个节点都是平衡二叉搜索树，可以递归二分数组来分配资源，
# 左面的构建左子树，右面的构建右子树，以此递归。

# 作者：chencyudel
# 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/dfsdi-gui-er-fen-fa-by-chencyudel/

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if not nums:
            return None
        else:
            mid = length // 2
            tn = TreeNode(nums[mid])
            tn.left = self.sortedArrayToBST(nums[0:mid])
            tn.right = self.sortedArrayToBST(nums[mid + 1:length])
        return tn
