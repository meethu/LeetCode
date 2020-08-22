# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        while head:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummyHead.next