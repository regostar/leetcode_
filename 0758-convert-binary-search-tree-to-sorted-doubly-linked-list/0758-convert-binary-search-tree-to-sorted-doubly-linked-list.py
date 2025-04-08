"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BST to sorted C DLL
        # bst has sorting order
        # how do we show sorting in DLL (circ)?
        # if we traverse a BST using DFS in inorder traversal / DFS
        # it will be easy to record the sorting sequence
        # 1 - 2 - 3 - 4 - 5
        # inorder traversal of BST gives us the sorted list
        # now when we get this list, we need to create the DLL
        # we can make it circular in the end by tracking 1st and last

        # how are we implementing dfs ?
        # recursive is easy
        # later if we want we can use stack and make it iterative
        
        def dfs_inorder(node: 'Optional[Node]'):
            """
            left - node - right
            recursive
            """
            nonlocal first, last

            if not node:
                return
            # left
            if node.left:
                dfs_inorder(node.left)
            
            # node
            ####
            # here we use prev and curr to make LL
            if not first:
                first = node
            else:
                # 1 - was last visited
                # 1 was first
                last.right = node
                node.left = last
            
            last = node

            # right
            dfs_inorder(node.right)
        
        if not root:
            return None
        
        # call
        first, last = None, None
        dfs_inorder(root)

        # make closed DLL
        # first, last
        last.right = first
        first.left = last

        return first







        