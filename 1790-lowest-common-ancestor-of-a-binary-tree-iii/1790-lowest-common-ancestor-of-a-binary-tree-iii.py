"""
Intuition
Basically, if the two nodes are on the same row/height of the tree, you just have to swim up until they match.

But what if they're not on the same height?

Easy! Just find the one that is lower, and swim up until it's on the same height.

Boom - Same time complexity, but no funny hacks. Let's jump into the code -
"""


def get_depth(node: TreeNode)-> int:
    if not node:
        return -1
    return 1 + get_depth(node.parent)




class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Calculates how far a node is from the top

        depth_p = get_depth(p)
        depth_q = get_depth(q)

        if depth_p > depth_q:
            # traverse up - from p until it reaches same level as q
            while depth_p > depth_q:
                p = p.parent
                depth_p -= 1
        else:
            while depth_q > depth_p:
                q = q.parent
                depth_q -= 1
        # now both are at same depth 

        # traverse top at the same time
        while p != q:
            p = p.parent 
            q = q.parent
        
        return p
