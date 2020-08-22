"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return
#         ret = [root.val]

#         for node in root.children:
#             ret.extend(self.preorder(node))

#         return ret

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        # s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            # for child in node.children[::-1]:
            #     s.append(child)
            s.extend(node.children[::-1])
        return res
