# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root: TreeNode, max_so_far: int):
            if not root:
                return 0
            count = 0
            if root.val >= max_so_far:
                # print(root.val)
                count += 1
            count += dfs(root.left, max(root.val, max_so_far))
            count += dfs(root.right, max(root.val, max_so_far))
            return count
        return dfs(root, -10000)
        
        