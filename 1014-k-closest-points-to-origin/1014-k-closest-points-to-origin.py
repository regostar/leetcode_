class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # creating a list for the min heap and adding all the distance values to it
        min_heap = []
        res = []
        # pop k times
        heapq.heapify(min_heap)

        for x, y in points:
            dist = sqrt((x**2) + (y**2))
            heapq.heappush(min_heap, (dist, x, y))

        while k> 0:
            d, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
        
        return res
            



