# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         node = set()
#         while head:
#             node.add(head)
#             head = head.next
#             if head in node:
#                 return head
#         return None

# https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/xiang-xi-tu-jie-ken-ding-kan-de-ming-bai-by-xixili/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None