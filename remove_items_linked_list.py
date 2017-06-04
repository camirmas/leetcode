class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements(head, val):
    dummy = ListNode(-1)
    dummy.next = head

    current_node = dummy

    while current_node.next:
        if current_node.next.val == val:
            next_node = current_node.next
            current_node.next = next_node.next
        else:
            current_node = current_node.next

    return dummy.next
