# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next: # both need to exist so fast.next.next can be happy
            # advance ptrs
            slow = slow.next
            fast = fast.next.next
            if slow is fast: # actual node equivalence rather than val
                return True
        return False

