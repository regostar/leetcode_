# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # basically find 2 nodes with max depth
        # can the path be without root?
        # lets say sub tree on left has very deep 2 branches
        # we ignore the root
        # from one node we find the depths through left sub tree
        # depth of right sub tree
        # compare it with max diameter we found
        max_diameter = 0

        def dfs(node: TreeNode)->int:
            """
            recursive 
            Updates  the max internally
            returns the max depth
            # so that recursively we can check
            """
            if not node:
                return -1
            nonlocal max_diameter

            left_depth = 1 + dfs(node.left)
            right_depth = 1 + dfs(node.right)

            max_depth = max(left_depth, right_depth)
            # because we count this node
            max_diameter = max(max_diameter,  left_depth + right_depth)
            return max_depth

        dfs(root)
        return max_diameter
        # T -> O(n) -> visit each node once
        # S -> O(h) -> height of tree - stack recursive size
