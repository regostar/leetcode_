# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -math.inf

        # post order traversal of subtree rooted at node
        # LRN
        def gainFromSubtree(node: Optional[TreeNode])-> int:
            nonlocal max_path

            if not node:
                return 0
            
            # add gain from left subtree, note that if the gain is negative
            # we can ignore it or count as 0 hence max
            gain_from_left = max(gainFromSubtree(node.left), 0)

            # add the gain/path
            gainFromRight = max(gainFromSubtree(node.right), 0)

            max_path = max(max_path, gain_from_left + gainFromRight + node.val)

            return max(gain_from_left + node.val, gainFromRight + node.val)
                
        gainFromSubtree(root)
        return max_path       