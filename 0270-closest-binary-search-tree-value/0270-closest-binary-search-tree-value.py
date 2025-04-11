# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # BST 
        # closest can be less than or greater than
        # if diff is same then choose smallest
        # dfs of bst
        # when we reach a number - say 4 in ex
        # we look at both it's children instead of just one 
        # we select one branch from that and traverse, based on the closest distance
        # we simply traverse full BST O(n) and find min diff ele
        closest = root.val
        def dfs(node):
            nonlocal closest
            if not node:
                return
            
            # Update the closest value if the current node is closer to the target
            if abs(node.val - target) < abs(closest - target) or \
            (abs(node.val - target) == abs(closest - target) and node.val < closest):
                closest = node.val
            
            # Continue DFS in the left or right subtree based on the target value
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        
        # Start DFS from the root
        dfs(root)
        return closest


