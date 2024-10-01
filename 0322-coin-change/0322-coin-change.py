class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we need to check for using each coin everytime until the target is reached
        #for every penny we try every coin
        # dp soln.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for denomination in coins:
                if amt - denomination >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - denomination])
        return dp[amount] if dp[amount] != amount + 1 else -1

        