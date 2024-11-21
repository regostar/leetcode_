# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # inorder iterative dfs
        if not root:
            return 0

        stack = []
        max_depth = 0
        current_depth = 0
        current = root

        while stack or current:
            # Traverse to the leftmost node, increasing the depth
            while current:
                stack.append((current, current_depth + 1))
                current_depth += 1
                current = current.left
            
            # Process the node at the top of the stack
            current, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)

            # Move to the right child
            current = current.right

        return max_depth



        