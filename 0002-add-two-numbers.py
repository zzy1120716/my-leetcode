"""
2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一：官方题解
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p, q, curr = l1, l2, dummy
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            digsum = carry + x + y
            carry = digsum // 10
            curr.next = ListNode(digsum % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next


# 方法二：链表转数字，相加再转回链表
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        i = 0
        while l1:
            num1 += l1.val * pow(10, i)
            i += 1
            l1 = l1.next
        i = 0
        while l2:
            num2 += l2.val * pow(10, i)
            i += 1
            l2 = l2.next
        num = num1 + num2
        dummy = ListNode(0)
        if num == 0:
            return dummy
        last = dummy
        while num > 0:
            curr = ListNode(num % 10)
            last.next = curr
            last = last.next
            num //= 10
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = Solution1().addTwoNumbers(l1, l2)
    while lsum:
        print(lsum.val)
        lsum = lsum.next
