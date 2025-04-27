# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # consider as binary tree
        # simply do DFS
        ans = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal ans

            if not node:
                return
            if low <= node.val <= high:
                ans += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        dfs(root)
        return ans
        