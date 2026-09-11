# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        stack_travel = set()
        curr = head
        
        while curr:
            if curr in stack_travel:
                return True
            
            stack_travel.add(curr)
            curr = curr.next

        return False