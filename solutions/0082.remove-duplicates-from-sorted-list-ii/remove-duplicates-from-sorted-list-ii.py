# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        pre.next, slow, fast = head, pre, head
        while fast:
            while fast.next and fast.next.val == slow.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = fast
            else:
                slow.next = fast.next
            fast = fast.next
        return pre.next



