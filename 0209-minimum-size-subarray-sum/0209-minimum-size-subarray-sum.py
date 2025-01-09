class Solution:
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # # there can be multiple sub arrays whose sum is >= target
        # # we only want the min length
        # # brute force soln - we check for each sub array
        # # O(n^2) soln.
        # # lets try O (n) soln. 
        # # traverse from left to right using sliding window
        # # start ptr, end ptr
        # # increment end ptr if sum of subarray < target
        # # if sum >= target then record it find min len
        # # increment start ptr then repeat until 
        # # start ptr < end ptr and both in range of array len
        # start_ptr = 0 # inclusive
        # end_ptr = 1 # exclusive
        # n = len(nums)
        # min_len = 10**5 # given max length of array
        # found = False
        # curr_sum = 0

        # while start_ptr <= end_ptr and start_ptr < n and end_ptr <= n:
        #     curr_sum += nums[end_ptr - 1]
        #     # sub_array_sum = sum(nums[start_ptr:end_ptr])
        #     # print("sub_array_sum = ", curr_sum, " array = ", nums[start_ptr:end_ptr])
        #     if curr_sum < target:
        #         # increment the end_ptr
        #         end_ptr += 1
        #     else:
        #         # >= a potential match
        #         # we don't need the sum to be the least only the length
        #         min_len = min(end_ptr - start_ptr, min_len)
        #         # move start_ptr by 1
        #         curr_sum -= nums[start_ptr]
        #         start_ptr += 1
        #         curr_sum -= nums[end_ptr - 1]
                
        #         found = True

        # return min_len if found else 0
        # # O(n²) due to recalculating the subarray sum with slicing in every iteration
        # # instead we can compute running sum



    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_ptr = 0  # Inclusive
        current_sum = 0  # Running sum of the current window
        min_len = float('inf')  # Initialize to a large value
        n = len(nums)

        for end_ptr in range(n):
            # Expand the window by adding the current number to the running sum
            current_sum += nums[end_ptr]

            # Check if the current sum is greater than or equal to the target
            while current_sum >= target:
                # Update the minimum length if the current window is smaller
                min_len = min(min_len, end_ptr - start_ptr + 1)
                # Shrink the window from the left
                current_sum -= nums[start_ptr]
                start_ptr += 1

        # If no valid subarray was found, return 0
        return min_len if min_len != float('inf') else 0


        