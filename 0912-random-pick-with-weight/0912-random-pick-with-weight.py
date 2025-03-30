class Solution:

    def __init__(self, w: List[int]):
        # we compute prefix sums so that 
        # they represent the indices for probability
        self.prefix_sums = []
        pref_sum = 0
        for weight in w:
            pref_sum += weight
            self.prefix_sums.append(pref_sum)
        self.total_sum = pref_sum
        

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        # binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()