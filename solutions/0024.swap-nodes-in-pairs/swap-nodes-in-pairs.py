# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# # 递归版本
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         next = head.next
#         head.next = self.swapPairs(next.next)
#         next.next = head
#         return next

# 非递归版本

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(-1)
        prev.next = head
        dummy = prev

        while head and head.next:
            a = head
            b = head.next
            a.next = b.next
            prev.next = b
            b.next = a

            # 交换节点，开启下一轮
            prev = a
            head = a.next
        return dummy.next
