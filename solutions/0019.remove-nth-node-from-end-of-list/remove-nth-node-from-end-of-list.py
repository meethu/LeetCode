# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针，快指针先走n步，然后快慢一起走，直到快指针走到最后，要注意的是可能是要删除第一个节点，这个时候可以直接返回head -> next

# 删除从列表开头数起的第 (L - n + 1)个结点，其中 L 是列表的长度。只要我们找到列表的长度 L
#
# 算法
#
# 首先我们将添加一个哑结点作为辅助，该结点位于列表头部。哑结点用来简化某些极端情况，
# 例如列表中只含有一个结点，或需要删除列表的头部。在第一次遍历中，我们找出列表的长度 L。
# 然后设置一个指向哑结点的指针，并移动它遍历列表，直至它到达第 (L - n) 个结点那里。
# 我们把第 (L - n)个结点的 next 指针重新链接至第 (L - n + 2) 个结点，完成这个算法

# # 两次遍历
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         pre = ListNode(0)
#         pre.next, first, length = head, head, 0
#         while first:  # 获取链表长度
#             first = first.next
#             length += 1
#         length -= n
#         first = pre  # 将 first 置 pre ，进行第二次循环
#         while length:
#             first = first.next
#             length -= 1
#         first.next = first.next.next  # 有于first 一开始为pre，那么length 为0时候，恰好指向 第 n-1个元素
#         return pre.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next, slow, fast = head, pre, pre
        while n:  # 先让 fast 指针走n步
            fast = fast.next
            n -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return pre.next
