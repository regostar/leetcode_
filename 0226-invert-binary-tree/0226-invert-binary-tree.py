# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # left sub tree and right sub tree at every node must be interchanged
        # BFS using a queue
        # iterative - queue
        # O(N)
        # when we pop from queue, swap left and right subtrees
        if not root:
            return None
        queue = deque([root])

        while queue:
            node = queue.popleft()
            # fifo
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        return root
