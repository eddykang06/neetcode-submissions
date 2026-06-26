# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Two pointers
        p1 = head
        if not p1:
            return None
        p2 = head.next

        # Traverse linked list
        while p2: # condition for stop?

            # Skip 1 position 
            p1.next = p2.next

            # Reorder pointer 1 and 2
            p2.next = head

            # Track head 
            head = p2

            # Reset pointers
            p2 = p1.next
        
        return head                                                                                                                                                                                          

            
        