# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Perform a level order traversal and get the first element of each level
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            # now while level order traversal we only need the first element
            # i = 
            en = len(q) - 1
            for i in range(len(q)):
                node = q.popleft()
                if i == en:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
 