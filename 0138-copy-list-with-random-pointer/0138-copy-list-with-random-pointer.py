"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # keep a dict of node vs new node
        # in random if we find the node which already has a map
        # then we attach to new node address

        # LL clone
        # base case 1
        if not head:
            return None

        map_old_new = {}
        node = head
        new_node = new_head = Node(x = head.val)
        map_old_new[head] = new_node

        # # we return the mapped value for head
        while node:
            # iterate node and new_node
            temp_next = None
            if node.next:
                if node.next in map_old_new:
                    temp_next = map_old_new[node.next]
                else:
                    temp_next = Node(x = node.next.val)
                    map_old_new[node.next] = temp_next
            new_node.next = temp_next
            temp_random = None
            if node.random:
                if node.random in map_old_new:
                    temp_random = map_old_new[node.random]
                else:
                    temp_random = Node(x = node.random.val)
                    map_old_new[node.random] = temp_random
                new_node.random = temp_random
            node = node.next
            new_node = new_node.next
        
        return new_head
                


            

        
        