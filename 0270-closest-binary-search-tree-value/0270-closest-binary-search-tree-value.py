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
        min_diff = float('inf')
        closest = root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal min_diff
            nonlocal closest
            if not node:
                # terminating condition
                return
            if node.val == target:
                # case  1
                closest = node.val
            # Update the closest value if the current node is closer to the target
            if abs(node.val - target) < abs(closest - target) or \
            (abs(node.val - target) == abs(closest - target) and node.val < closest):
                closest = node.val
            
            # Continue DFS in the left or right subtree based on the target value
                        # Traverse only one branch based on the target value
            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)

        # now if 2 has same min diff, we need to consider smallest
        dfs(root)
        return closest

