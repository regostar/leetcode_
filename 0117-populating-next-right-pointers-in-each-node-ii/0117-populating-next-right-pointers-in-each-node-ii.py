"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # node's right is  node.left.next = node.right or super parent.right....
        # node.right.next = None if no 
        # level order traversal - we add connections that's all
        # how do we do level order traversal ?
        # using a queue
        # but we need to know when we reach the end of the level so that we add none
        # add None in queue or any other flag
        if not root:
            return root
        queue = deque([])
        # append and popleft
        queue.append(root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                ele = queue.popleft()
                if i < level_size - 1:
                    # ignore last one
                    ele.next = queue[0]
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
        return root
