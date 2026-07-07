# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node as head, then keep curr update
        dummy = ListNode()
        curr = dummy

        # Pointers for each list
        p1 = list1
        p2 = list2

        # Iterate until reach end of 1 linked list
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next

        # Correct for remaining sublist
        if not p1:
            curr.next = p2
        elif not p2:
            curr.next = p1
        
        return dummy.next


        