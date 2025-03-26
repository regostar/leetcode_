# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case 1 empty tree
        if not root:
            return None
        # p or q is root, then the lca is the root
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            # case 3 branch off from here, LCA is root
            return root
        else:
            # both p and q are in same sub tree 
            return left or right
        