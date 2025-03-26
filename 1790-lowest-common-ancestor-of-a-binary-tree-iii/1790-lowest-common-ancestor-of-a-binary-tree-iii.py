"""
Intuition
Basically, if the two nodes are on the same row/height of the tree, you just have to swim up until they match.

But what if they're not on the same height?

Easy! Just find the one that is lower, and swim up until it's on the same height.

Boom - Same time complexity, but no funny hacks. Let's jump into the code -
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Calculates how far a node is from the top
        def distFromTop(n: 'Node') -> int:
            if not n:
                return -1
            return 1 + distFromTop(n.parent)

        pDistFromTop = distFromTop(p)
        qDistFromTop = distFromTop(q)

        # Make the lower node swim to the same height as the higher node 
        while pDistFromTop > qDistFromTop:
            p = p.parent
            pDistFromTop -= 1
        while qDistFromTop > pDistFromTop:
            q = q.parent
            qDistFromTop -= 1

        # p and q are on the same level, simply swim up one by one until they match
        while p != q:
            p = p.parent
            q = q.parent

        return p # p now equals q, they found the same parent