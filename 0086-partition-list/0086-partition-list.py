# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode()
        after = after_head = ListNode()
        # we have to initialize to a new LL because we do before.next = head 

        # avoid swapping, just create 2 new LL O(1) space

        while head:
            if head.val < x:
                # add to before LL
                before.next = head
                before = before.next
            else:
                # add to after LL to maintain relative order
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        # end
        before.next = after_head.next
        # combine

        return before_head.next






        # # get pos of x = x_pos
        # # traverse now if ele < x then check if pos is < x_pos
        # # if yes do nothing else, swap x_pos x and pos 
        # node = head
        # x_pos = 0
        # while node is not None:
        #     x_pos += 1
        #     if node.val == x:
        #         break
        #     node = node.next
        # node = head
        # ctr = 0
        # while node is not None:
        #     # greater ptr > than pos
        #     # lesser ptr < pos
        #     ctr += 1
        #     if node.val < x and ctr >= x_pos:
        #         # swap
        #     if node.val >= x and ctr < x_pos:
        #         # swap
        #     node = node.next

            
            

        