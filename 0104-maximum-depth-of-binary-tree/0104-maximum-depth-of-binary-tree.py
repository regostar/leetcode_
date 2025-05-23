# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root :
            stack.append((1, root))

        depth = 0
        while stack:
            cur_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, cur_depth)
                stack.append((cur_depth + 1, root.left))
                stack.append((cur_depth + 1, root.right))
        return depth 





    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # perform dfs
    #     # count every node check max
    #     # perform bfs - count no of max levels

    #     # recur4sive dfs
    #     max_depth = 0

    #     def dfs(node: Optional[TreeNode], depth_so_far: int =0):
    #         if not node:
    #             return
    #         nonlocal max_depth
    #         max_depth = max(max_depth, depth_so_far + 1)
    #         dfs(node.left, depth_so_far + 1)
    #         dfs(node.right, depth_so_far + 1)
        
    #     dfs(root, 0)
    #     return max_depth
    #     # Time complexity is O(N)
    #     # Space complexity is O(N) - recursion call stack
    #     # best case - tree is balanced O(log(N)).
        