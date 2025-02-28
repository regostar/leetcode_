# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Inorder traversal of BST will be a sorted list
        # L N R - inorder

        # DFS - Inorder traversal
        # check if diff with prev val for min distance
        min_dist = math.inf
        stack = []
        curr = root
        prev_val = None
        
        while curr is not None or len(stack) > 0:

            while curr is not None:
                # reach left most for inorder tx
                stack.append(curr)
                curr = curr.left
            
            # curr is none here
            curr = stack.pop()

            # now process the node
            if prev_val is None:
                prev_val = curr.val
            else:
                min_dist = min(min_dist, curr.val - prev_val)
                # we know for sure curr > prev
                prev_val = curr.val
            
            curr = curr.right
        
        return min_dist