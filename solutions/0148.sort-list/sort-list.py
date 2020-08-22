class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1  # 获取列表长度
        res = ListNode(0)  # 声明一个节点res，作为头部后面接整个链表
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv  # 链表头部给 h1
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next


def createList(nums):
    head = ListNode(0)
    cur = head
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')


if __name__ == "__main__":
    nums = [4, 1, 2, 3]
    head = createList(nums)
    printList(head)
    res = Solution().sortList(head)
    printList(res)
