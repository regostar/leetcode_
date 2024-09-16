class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap with k points
        # return all k elements
        # but how will we store the min heap -> [dist, x, y]
        # can the result points be inm any order? - Yes
        min_heap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            min_heap.append([dist, x, y])
        
        heapq.heapify(min_heap)
        result = []

        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            result.append([x, y])
            k -= 1
        
        return result



        