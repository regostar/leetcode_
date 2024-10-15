# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def depth(self, node: Optional[TreeNode]) -> int:
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # save max diameter seen so far
        self.max_diameter = max(self.max_diameter, left + right)
        # return depth
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_diameter
        