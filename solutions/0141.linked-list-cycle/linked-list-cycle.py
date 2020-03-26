# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hascycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next  # 每次走一步
            fast = fast.next.next  # 每次走两步
        if slow == fast:
            return True
        return False

# 本质还是哈希法，只不过不需要额外空间

#     def hasCycle(self, head):
#         if not head:
#             return False
#         while head.next and head.val != None:
#             head.val = None  # 遍历的过程中将值置空
#             head = head.next
#         if not head.next:  # 如果碰到空发现已经结束，则无环
#             return False
#         return True  # 否则有环


head = [3, 2, 0, -4]
problems = Solution()
print(problems.hascycle(head))

