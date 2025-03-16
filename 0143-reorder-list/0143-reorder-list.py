# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = fast = head
        # in 1->2->3->4->5->6 find 4
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now reverse the second part of the prob
        prev = None
        cur = slow

        # reverse in place
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        # merge 2 sorted lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
