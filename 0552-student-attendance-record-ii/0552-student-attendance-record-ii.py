class Solution:
    def checkRecord(self, n: int) -> int:
        # n = 1
        # A L P 3
        # N = 2
        # PA AP LA AL PL LP LL PP 8
        _mod = 1000000007

        # cache initialization
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        # 'n' th eligible award

        def eligible_combos(n, total_absences, consecutive_lates):
            # base case
            # if invalid
            if total_absences >= 2 or consecutive_lates >=3:
                return 0
            
            # if we have generated a combo of length 'n' we will count it
            if n == 0:
                return 1
            
            # if we have seen this problem earlier, we use cache
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]
            
            # if we choose 'P' for the current position
            count = eligible_combos(n-1, total_absences, 0)

            # if we choose A for the current pos
            count = (count + eligible_combos(n-1, total_absences + 1, 0)) % _mod

            # if we choose 'L' for current pos
            count = (count + eligible_combos(n-1, total_absences, consecutive_lates + 1)) % _mod
            memo[n][total_absences][consecutive_lates] = count
            return count
        return eligible_combos(n, 0, 0)
