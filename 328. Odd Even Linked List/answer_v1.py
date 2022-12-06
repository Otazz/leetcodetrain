from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        curr_node = head.next
        last_odd = head
        while curr_node and curr_node.next:
            bkp = last_odd.next
            last_odd.next = curr_node.next
            last_odd = last_odd.next
            curr_node.next = last_odd.next
            last_odd.next = bkp
            curr_node = curr_node.next
        
        return head