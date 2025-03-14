class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # min no of jumps req to reach last index or step n-1
        # dp[0] = 0
        # dp[1] = min(1+dp[0], MAX)
        # dp[2] = min(1+dp[1], )
        # dp[n-1] = 1 + dp[j] if nums[j] >= n-1 -j

        # Need O(n) soln optimized
        # Greedy approach
        # we compute max reachable position from each index
        # then we simply jump greedily from the max index possible so that jumps are minimum
        min_jumps = 0
        for i in range(1, n):
            nums[i] = max(nums[i-1], nums[i] + i)
        print("new nums = ", nums)
        # guaranteed that you can reach nums[n-1]
        i = 0
        while i < n - 1:
            # n-1 because test case > [0]
            # i = n-1 then terminate
            min_jumps += 1
            i = nums[i]

        return min_jumps
