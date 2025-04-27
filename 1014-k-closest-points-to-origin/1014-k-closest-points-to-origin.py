class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # creating a list for the min heap and adding all the distance values to it
        minHeap = []

        def compute_dist(x, y):
            return x**2 + y**2


        dist_array = [(compute_dist(x, y), x, y) for x, y in points]
        heapq.heapify(dist_array)

        k_closest_points = []
        while k:
            dist, x, y = heapq.heappop(dist_array)
            k_closest_points.append([x, y])
            k -= 1

        return k_closest_points