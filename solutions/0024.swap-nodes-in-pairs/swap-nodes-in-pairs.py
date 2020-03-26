# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# # 递归版本
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         next = head.next
#         head.next = self.swapPairs(next.next)
#         next.next = head
#         return next

# http://lylblog.cn/blog/4

# 非递归版本

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:  # 当 头结点存在，并且头结点的下一个元素存在，才会发生交换
            a = pre.next
            b = pre.next.next
            a.next = b.next
            b.next = a
            pre.next = b

            pre = a
        return self.next
