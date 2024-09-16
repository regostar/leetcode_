class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap which will always have heaviest stone on top
        # pop twice get x, y
        # then push difference of |x - y| if it is >0
        # continue until len <= 1 
        # to use a max heap we use -ve nos of the array values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        # heapify happens in place O(n)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if abs(x - y) > 0:
                heapq.heappush(max_heap, -1*abs(x - y))
        if max_heap:
            return -max_heap[0]
        else:
            return 0
