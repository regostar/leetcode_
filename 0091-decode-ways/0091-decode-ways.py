class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        # Base case: An empty substring has exactly 1 way to be decoded.
        # dp[i] represents the number of ways to decode the substring starting from index i
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                # If a number starts with '0', it cannot be decoded
            else:
                dp[i] = dp[i+1]
                # Single-digit decoding (using just s[i])
            
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i+2]
                 # Two-digit decoding (using s[i] and s[i+1])
        return dp[0]