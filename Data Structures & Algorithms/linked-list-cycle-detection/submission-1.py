# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        h = {}
        
        curr = head
        index = None

        while curr is not None:
            h[curr] = h.get(curr, 0) + 1

            if h[curr] > 1:
                return True
            
            curr = curr.next

        return False



            
        