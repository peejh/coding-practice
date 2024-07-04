from utils.linked_list import LinkedList

def detect_cycle(head):
    slow = head
    fast = head.next # can be a problem if head is None
    while fast:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next # can be a problem if fast.next is None
    return False