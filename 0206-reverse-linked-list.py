"""
206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from tools import convertList2LinkedList, stringifyLinkedList


class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev


class Solution1:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        next_node = head.next  # head -> next_node
        next_node.next = head  # head <- next_node
        head.next = None  # [x] <- head <- next_node
        return new_head


if __name__ == '__main__':
    head = convertList2LinkedList([1, 2, 3, 4, 5])
    print('result: ' + stringifyLinkedList(Solution1().reverseList(head)))
