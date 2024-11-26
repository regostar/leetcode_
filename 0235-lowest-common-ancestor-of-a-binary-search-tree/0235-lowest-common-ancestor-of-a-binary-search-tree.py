# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        print(root.val)
        if root == p or root == q:
            print("returning ", root.val)
            return root
        print("CAME HERE")
        if p.val > root.val and q.val > root.val:
            # proceed to right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # p in one subtree and q in one sub tree
            return root
        
        