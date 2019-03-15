"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from tools import convertList2LinkedList, stringifyLinkedList


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge2Lists(left, right)

    def merge2Lists(self, headA, headB):
        dummy = ListNode(0)
        last = dummy
        while headA and headB:
            if headA.val < headB.val:
                last.next = headA
                headA = headA.next
            else:
                last.next = headB
                headB = headB.next
            last = last.next
        if headA:
            last.next = headA
        if headB:
            last.next = headB

        # print(stringifyLinkedList(dummy.next))

        return dummy.next


if __name__ == '__main__':
    a = [1, 4, 5]
    b = [1, 3, 4]
    c = [2, 6]
    d = [3, 7]
    headA = convertList2LinkedList(a)
    headB = convertList2LinkedList(b)
    headC = convertList2LinkedList(c)
    headD = convertList2LinkedList(d)
    lists = [headA, headB, headC, headD]
    s = stringifyLinkedList(Solution().mergeKLists(lists))
    print(s)
