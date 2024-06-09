# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # once we reach the middle of the list
        # we reverse second part of list
        # then we join the 2 lists
        slow = head
        if not head.next:
            return
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow is the middle of the linked list
        second_ll = slow.next
        slow.next = None
        second = self.reverseList(second_ll)

        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2