class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummyHead = ListNode(0)
#         curr, carry = dummyHead, 0
#         while l1 or l2:
#             sum = 0
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next
#             sum += carry
#             carry = sum // 10
#             curr.next = ListNode(sum % 10)
#             curr = curr.next
#
#         if carry > 0:
#             curr.next = ListNode(1)
#         return dummyHead.next

# 解法2
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0  # 进位

        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = Solution().addTwoNumbers(l1, l2)
    while result != None:
        print(result.val)
        result = result.next
