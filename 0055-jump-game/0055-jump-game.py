class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # aim : Reach last index
        # R : T/F
        # max jump length nums[i] from i
        # optimized min no of steps is not required
        # path to end or not
        # to reach step1 , 0
        # to reach step 2 - if nums[i-1] >=1
        # to reach step 3 - if nums[i-1] >=1 1 or nums[i-2] >=2
        # if nums[i] >= n - i can reach end terminate, return TRUE
        # function of f(n) relating prev elements
        # Last to first
        # dp[0] = True # True indicating reachable
        # dp[n-1] = dp[n-2] and nums[n-2] or dp[n-3] and nums[n-3] >= n-1 -n +3 = 2 jumps ....
        # start from step 1, recursively save in dp
        n = len(nums)
        # dp = [False for _ in range(n)]
        # dp[0] = True
        # # because we start from here - base case

        # # O (n^2)
        # for i in range(1, n):
        #     for j in range(0, i):
        #         condt = dp[j] and (nums[j] >= i - j)
        #         dp[i] = dp[i] or condt
        #         # we reuse already computed results so avoid 2^n tree
        #         if dp[i]:
        #             break # inner loop since path to this is possible
        # return dp[n-1]

        # Need to optimize
        # O(n)
        # have a max reachable index
        # if MRI >= last index then TRUE
        max_reachable_i = 0
        # index 0 is reachable

        for i, num in enumerate(nums):
            if max_reachable_i < i:
                # cannot reach this index
                return False
                # if we cannot reach this index, for sure we cannot reach the last index
            max_reachable_i = max(max_reachable_i, num + i)

            # terminating condt - success:
            if max_reachable_i >= n - 1:
                return True




        