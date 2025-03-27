# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                # base case empty treee
                return []
            
            # initialize hash map with root at index 0
            column_elements = defaultdict(list)

            queue = deque([(0, root)])

            # perform BFS
            while queue:
                n = len(queue)
                for i in range(n):
                    col, node = queue.popleft()
                    column_elements[col].append(node.val)

                    # first ele from queue
                    if node.left:
                        queue.append((col - 1, node.left))
                    if node.right:
                        queue.append((col + 1, node.right))
            
            # now convert the k - v to ordered list 
            indexes = sorted(column_elements.keys())
            result = []
            for each in indexes:
                result.append(column_elements[each])
            print(result)
            return result
            