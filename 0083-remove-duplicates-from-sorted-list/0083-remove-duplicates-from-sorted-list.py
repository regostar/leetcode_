# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr:
            return None
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.val == prev.val:
                prev.next = curr.next
                curr = prev
            
        return head
            

        