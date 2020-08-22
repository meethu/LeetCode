# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def reversePrint(self, head):
    #     if head is None:
    #         return []
    #     return self.reversePrint(head.next) + [head.val]

    def reversePrint(self, head):
        ret = []
        while head:
            ret.append(head.val)
            head = head.next

        return ret[::-1]