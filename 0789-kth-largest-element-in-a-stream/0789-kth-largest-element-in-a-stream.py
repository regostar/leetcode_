class KthLargest:
    """
    min heap
    we are only adding and never removing
    we only need min heap of k elements

    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        # O(n)
        # it it has more than k elements, we simply pop them
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
            # O(log n)  

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # O(log n)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        
