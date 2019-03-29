"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        start = dummy

        for i in range(m - 1):
            start = start.next

        pre = None
        cur = start.next

        for i in range(m, n + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        start.next.next = cur
        start.next = pre

        return dummy.next


class Solution1:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur, front, last = None, dummy, None, None
        for i in range(1, m):
            cur = cur.next
        pre = cur
        last = cur.next
        for i in range(m, n + 1):
            cur = pre.next
            pre.next = cur.next
            cur.next = front
            front = cur
        cur = pre.next
        pre.next = front
        last.next = cur
        return dummy.next


if __name__ == '__main__':
    import tools

    head1 = tools.convertList2LinkedList([1, 2, 3, 4, 5])
    print(tools.stringifyLinkedList(head1))
    print(tools.stringifyLinkedList(Solution().reverseBetween(head1, 2, 4)))

    head2 = tools.convertList2LinkedList([3, 5])
    print(tools.stringifyLinkedList(head2))
    print(tools.stringifyLinkedList(Solution().reverseBetween(head2, 1, 2)))
