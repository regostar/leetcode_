class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
         A key observation is that the sum of a subarray [i, j]
         is equal to the sum of [0, j] minus the sum of [0, i - 1].

         we compute prefix sums and store in dict with index
         we find curr sum - target in the dict, if yes we have found
        """
        prefix_sum = 0
        count = 0
        prefix_sum_dict = {0: 1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_sum_dict:
                count += prefix_sum_dict[prefix_sum - k]
                # return prefix_sum_dict[prefix_sum - target] +1
            prefix_sum_dict[prefix_sum] = prefix_sum_dict.get(prefix_sum, 0) + 1
            # print(prefix_sum_dict)
        return count




        