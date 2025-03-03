# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        
        # Helper function for DFS traversal
        def dfs(node, row, col):
            if not node:
                return
            # Append tuple with (col, row, node value)
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        # Sort nodes by column, then row, then value
        nodes.sort()
        
        # Group the sorted nodes by column index
        vertical_order = []
        last_col = float('-inf')
        for col, row, value in nodes:
            if col != last_col:
                vertical_order.append([])
                last_col = col
            vertical_order[-1].append(value)
        
        return vertical_order
