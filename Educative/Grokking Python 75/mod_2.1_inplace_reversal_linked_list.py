# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/5342484351811584

from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
            
def reverse(head):
    prev, curr, next = None, head, head.next

    while curr:
        curr.next = prev
        head = curr
        prev, curr, next = curr, next, next.next if next else None
    
    return head