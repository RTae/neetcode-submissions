# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a stack to keep track travel node

        # if there is no data, it mean there is no cycle
        if head is None:
            return False

        # create a stack
        stack_travel = []
        curr = head
        
        while curr:
            # check do we already travel this node
            # if yes, it's mean there is a cycle
            if curr in stack_travel:
                return True
            
            # move to next node and track we already pass this node
            stack_travel.append(curr)
            curr = curr.next

        return False