# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # consider as binary tree
        # simply do DFS
        # ans = 0
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         if low <= node.val <= high:
        #             ans += node.val
        #         # can we go to left subtree
        #         # yes if node val is not lesser than low
        #         if node.val > low:
        #             stack.append(node.left)
        #         if node.val < high:
        #             stack.append(node.right)
        #     return ans
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans