# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val

        # post order traversal of subtree rooted at node
        # LRN
        def gainFromSubtree(node: Optional[TreeNode])-> int:
            nonlocal max_path

            if not node:
                return 0
            
            # add gain from left subtree, note that if the gain is negative
            # we can ignore it or count as 0 hence max
            max_left = max(gainFromSubtree(node.left), 0)

            # add the gain/path
            max_right = max(gainFromSubtree(node.right), 0)

            max_path = max(max_path, max_right + max_left + node.val)

            return node.val + max(max_left, max_right)
            # we can't choose both, 
                
        gainFromSubtree(root)
        return max_path       