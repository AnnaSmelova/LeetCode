# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        previous, current, root = None, head, head.next
        while current and current.next:
            adj = current.next
            if previous: 
                previous.next = adj
            current.next, adj.next = adj.next, current
            previous, current = current, current.next
        return root or head
