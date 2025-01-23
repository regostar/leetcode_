class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # we cannot go greedy because even though it is not the 
        # immediate minimum in row, the path through it can have lower path sum
        # hence we need to check for all paths
        # but to avoid re-computation, we save the results we find
        # dp[i][j] will say min path through this
        # dp[0][0] = given base case
        # recursive case :- dp[i][j] = num[i][j] + MIN(dp[i-1][j], dp[i-1][j-1])
        # final result in the last row, find min

        dp = [[ triangle[0][0] ]]
        # base case
        for i in range(1, len(triangle)):
            row = []
            for j in range(i+1): # i+1 since it's triangle cols = row no
                prev_min = float('inf')
                if j <= i-1 and j >= 0:
                    prev_min = min(prev_min, dp[i-1][j])
                if j-1 >= 0 and j - 1 <= i - 1:
                    prev_min = min(prev_min, dp[i-1][j-1])

                path_i_j = triangle[i][j] + prev_min
                row.append(path_i_j)
            dp.append(row)
        print(dp)
        return min(dp[-1])

        