# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge cases
        if not list1:
            return list2
        elif not list2:
            return list1

        # Two "pointers" for each linked list
        node1 = list1
        node2 = list2

        # Until we reach the end of 1 of the linked lists
        while node1 and node2:
            if node1.val <= node2.val:
                while node1.next and node1.next.val <= node2.val:
                    node1 = node1.next
                
                # Temp store next state, update next, then move pointer
                fragment = node1.next
                node1.next = node2
                node1 = fragment

            else:
                while node2.next and node2.next.val < node1.val:
                    node2 = node2.next

                # Temp store next state, update next, then move pointer
                fragment = node2.next
                node2.next = node1
                node2 = fragment

        # Final head is whichever head is smaller
        return list1 if list1.val <= list2.val else list2


        