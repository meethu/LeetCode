# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        prev = ListNode(0)
        prev.next = head
        dummyHead = prev
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next

        return dummyHead.next