class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fewest no of coins to make up that amount
        # something like greedy
        # try to use more of higher denomincation coins
        # create a dp cache - 0 o target
        # dp[0] = 0 no of coins needed to make target = 0
        # initialize rest all to infy
        # for each denomination if i - denom >= 0 then 
        # dp[i] = min(dp[i], 1 + dp[i-denom])
        # what if multiple coins can do it (of the same denom)?
        # we can optimize in future
        dp = [amount + 1 for _ in range(amount + 1)]
        # freq  can never be amount +1 , for coun == 1, amount is freq
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],  1 + dp[i - coin])
        
        return dp[-1] if dp[-1] != amount + 1 else -1


