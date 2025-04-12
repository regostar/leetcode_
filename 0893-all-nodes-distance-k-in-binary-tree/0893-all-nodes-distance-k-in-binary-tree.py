# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Binary tree
        # distance of k element can be in the other sub tree also like in ex 1
        # this problem comes down to distance between 2 nodes
        # one node is fixed
        # other node can be many

        if not root or not target:
            return []

        # Create a graph from the binary tree
        graph = defaultdict(list)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)

        # BFS to find all nodes at distance k
        res = []
        visited = set([target])
        queue = deque([(target, 0)])

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, distance + 1))

        return res

        