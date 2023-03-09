# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer_slow = head
        pointer_fast = head
        while pointer_fast and pointer_fast.next:
            pointer_slow = pointer_slow.next
            pointer_fast = pointer_fast.next.next
            if pointer_slow == pointer_fast:
                pointer_slow = head
                while pointer_slow != pointer_fast:
                    pointer_slow = pointer_slow.next
                    pointer_fast = pointer_fast.next
                return pointer_slow
        