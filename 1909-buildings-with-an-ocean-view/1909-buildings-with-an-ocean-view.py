class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # n buildings
        # n heights
        # rightside ocean
        # ocean view - building to right are smaller
        # indices (0) having ocean view
        # Clarifications
        # 0 height ? yes
        # no -ve heights
        # no buildins []

        # for every building we need the max building on the right
        # compare it with max
        # we have the ans
        # max till here from right let's precompute
        # [3,3,1,0]
        # 0 2 3
        max_from_right = [0 for _ in range(len(heights))]

        # edge case empty arr
        if not heights:
            return []

        for i in range(len(heights)-2, -1, -1):
            # traverse from right
            max_from_right[i] = max(max_from_right[i+1], heights[i+1])

        print(max_from_right)
        result = []
        for i in range(len(heights)):
            if heights[i] > max_from_right[i]:
                result.append(i)
        
        return result


