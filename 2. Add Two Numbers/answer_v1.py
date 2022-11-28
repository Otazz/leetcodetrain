from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start_l3 = ListNode(0)
        l3 = start_l3
        carry = 0
        l1_ptr = l1
        l2_ptr = l2

        while l1_ptr != None or l2_ptr != None or carry != 0:
            a = b = 0
            if l1_ptr:
                a = l1_ptr.val
                l1_ptr = l1_ptr.next

            if l2_ptr:
                b = l2_ptr.val
                l2_ptr = l2_ptr.next
            
            result = a + b + carry

            carry = result // 10

            new_node = ListNode(val=result % 10, next=None)

            l3.next = new_node
            l3 = new_node
    
        return start_l3.next
