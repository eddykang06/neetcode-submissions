# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Keep track of which nodes we've already seen - O(n) space
        tracker = set()
        curr = head

        # Iterate through the list - O(n) time
        while curr:
            if curr in tracker:
                return True
            tracker.add(curr)
            curr = curr.next
        
        return False
