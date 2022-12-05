from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 1

        curr_element = head

        while curr_element.next:
            size += 1
            curr_element = curr_element.next
        
        middle = size // 2

        curr_element = head

        for _ in range(middle):
            curr_element = curr_element.next
        
        return curr_element
