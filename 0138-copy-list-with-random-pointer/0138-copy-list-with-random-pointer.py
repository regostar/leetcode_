"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None  # Base case: empty list

        map_old_new = {}

        # First pass: Create a copy of each node and store them in the map
        current = head
        while current:
            map_old_new[current] = Node(current.val)
            current = current.next

        # Second pass: Assign next and random pointers
        current = head
        while current:
            copy_node = map_old_new[current]
            copy_node.next = map_old_new.get(current.next)
            copy_node.random = map_old_new.get(current.random)
            current = current.next

        return map_old_new[head]  # Return the copied head node


        
        