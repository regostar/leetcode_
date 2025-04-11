# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # memory is the path till now
        # return the final path
        total = 0

        def dfs(node, so_far: int):
            nonlocal total
            if not node:
                return
            cur = (so_far * 10) + node.val
            if not node.left and (not node.right):
                total += cur
            dfs(node.left, cur)
            dfs(node.right, cur)
        dfs(root, 0)
        return total
        