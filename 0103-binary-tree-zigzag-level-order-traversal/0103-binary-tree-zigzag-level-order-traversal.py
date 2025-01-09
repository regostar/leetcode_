# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order traversal
        # when we have the queue, copy it and reverse it based on the zig zag pattern
        if not root:
            return []
        queue = deque([root])
        RIGHT = "left_to_right"
        LEFT = "right_to_left"
        zig_zag = RIGHT
        result = []
        while queue:
            level_len = len(queue)
            level_elements = list(queue)
            if zig_zag == LEFT:
                #  reverse
                level_elements.reverse()
            # add level_ele to result
            level_vals = [ele.val for ele in level_elements]
            
            # continue level order traversal
            for i in range(level_len):
                element = queue.popleft()
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            zig_zag = RIGHT if zig_zag == LEFT else LEFT
            result.append(level_vals)
        return result
                





        

        