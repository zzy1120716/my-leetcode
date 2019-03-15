class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def stringifyLinkedList(head):
    s = ''
    while head:
        s += str(head.val) + ' -> '
        head = head.next
    s += 'None'
    return s


def convertList2LinkedList(values):
    dummy = ListNode(0)
    last = dummy
    for v in values:
        last.next = ListNode(v)
        last = last.next
    return dummy.next
