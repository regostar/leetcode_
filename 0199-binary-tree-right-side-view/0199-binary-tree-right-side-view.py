# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS - save last element 
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            for i in range(n):
                ele = queue.popleft()
                if i == n - 1:
                    result.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
        
        return result
            
        