class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for ele in nums:
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        # we have ele and their frequency
        # sort and return the top k 
        sorted_list = [key for key, val in sorted(counter.items(), key=lambda item: item[1], reverse=True)]
        
        return sorted_list[:k] 

        