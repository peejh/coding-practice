# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/5284737744764928

from utils.linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

def get_middle_node(head):

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next    
    return slow