# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# # 官方题解
# class Solution:
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         def helper(in_left = 0, in_right = len(inorder)):
#             nonlocal pre_idx
#             # if there is no elements to construct subtrees
#             if in_left == in_right:
#                 return None

#             # pick up pre_idx element as a root
#             root_val = preorder[pre_idx]
#             root = TreeNode(root_val)

#             # root splits inorder list
#             # into left and right subtrees
#             index = idx_map[root_val]

#             # recursion
#             pre_idx += 1
#             # build left subtree
#             root.left = helper(in_left, index)
#             # build right subtree
#             root.right = helper(index + 1, in_right)
#             return root

#         # start from first preorder element
#         pre_idx = 0
#         # build a hashmap value -> its index
#         idx_map = {val:idx for idx, val in enumerate(inorder)}
#         return helper()

# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         index_map = {val:idx for idx, val in enumerate(inorder)}
#         if len(inorder) == 0:
#             return None
#         # 前序遍历第一个值为根节点
#         root = TreeNode(preorder.pop(0))
#         # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
#         mid = index_map[root.val]
#         # 构建左子树
#         root.left = self.buildTree(preorder, inorder[:mid])
#         # 构建右子树
#         root.right = self.buildTree(preorder, inorder[mid+1:])

#         return root


# class Solution:
#     def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
#         if not inorder: return
#         root = TreeNode(preorder.pop(0))
#         i = inorder.index(root.val)
#         root.left = self.buildTree(preorder, inorder[:i])
#         root.right = self.buildTree(preorder, inorder[i+1:])
#         return root


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

# 我们在 inorder 中找到 mid 为根节点的下标
# 由于中序遍历特性，mid 左侧都为左子树节点，所以左子树的节点有 mid 个
# 那么同样的，由于前序遍历的特性，preorder 第一个元素（根节点）后跟着的就是它的左子树节点，一共有 mid 个，所以切了 [1:mid+1] 出来
# 作者：jalan
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/python-di-gui-xiang-jie-by-jalan/


# 按前序遍历的顺序每次pop并建立节点root，在中序遍历中找到root的对应index，划分出哪些节点构成此节点的左子树inorder[:i]，哪些构成右子树inorder[i+1:]。
# 返回值： 递归构建完当前节点root左右子树后，返回root，作为上轮递归父节点的left或right。
# 终止条件： 当inorder[:i]中序遍历无剩余元素时，说明当前root已经越过叶子节点，直接返回None。

# class Solution:
#     def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
#         if not inorder: return
#         root = TreeNode(preorder.pop(0))
#         i = inorder.index(root.val)
#         root.left = self.buildTree(preorder, inorder[:i])
#         root.right = self.buildTree(preorder, inorder[i+1:])
#         return root

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/qian-xu-zhong-xu-bian-li-gou-zao-er-cha-shu-mo-ni-/