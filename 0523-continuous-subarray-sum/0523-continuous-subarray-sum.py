class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Brute foce we can do a O(n^3) solution by constructing 
        # all subarrays of min length = 2 and checking for condt.
        # finding subarrays O(n^2) , computing sum O(n), we may be able to optimize it to O(n^2) by having a running sum
        # req = linear of log n
        # we seem to come to subproblem repitition of computation
        # can we save this
        # let's use PREFIX SUM!!!
        # useful to calculate the sum of subarrays. 
        
        # commutative sum or basically sum starting from 0 index
        # subarray sum for i+1 to j is prefix[j] - prefix[i]
        # (prefix[j] - prefix[i] ) % k == 0
        # prefix[j] % k = prefix[i] % kthen it satisfies the condition
        
        mod_seen = {0: -1}
        # prefix sum = 0 at index -1 which means we are considering the subarray from the start

        # we compute prefix sum and check in the same loop
        prefix_mod = 0

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            # now we check if this is in the dict
            if prefix_mod in mod_seen and i - mod_seen[prefix_mod] > 1:
                return True
            elif prefix_mod not in mod_seen :
                # we have to update ONLY if IT IS NOT IN mod_seen
                # because we want the longest subarry so that >=2
                mod_seen[prefix_mod] = i
        
        return False


        
        