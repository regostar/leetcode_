# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def find_leaves(self, root: Optional[TreeNode])->List:
        """
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.find_leaves(root.left) + self.find_leaves(root.right)

                



    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # find the leaves of tree 1 and tree 2
        # match corresponding values in the sequences
        # to find the leaves we need dfs 
        # let's do inorder traversal iterative approach
        return self.find_leaves(root1) == self.find_leaves(root2)
        # compare two lists



        

        