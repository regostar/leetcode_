class Solution:
    def minFallingPathSum(self, matrix):
        """
        Find the minimum falling path sum for a given matrix using a bottom-up approach with O(n) space.

        :param matrix: List[List[int]] - a square matrix of integers
        :return: int - the minimum falling path sum
        """
        n = len(matrix)

        # Initialize a dp array to store the minimum path sums for the current row
        dp = matrix[-1][:]  # Start with the last row of the matrix

        # Iterate from the second-to-last row to the top row
        for row in range(n - 2, -1, -1):
            new_dp = [0] * n  # Temporary array for the current row
            for col in range(n):
                # Current cell value plus the minimum of the cells directly below or diagonally below
                left = dp[col - 1] if col > 0 else float('inf')
                down = dp[col]
                right = dp[col + 1] if col < n - 1 else float('inf')

                new_dp[col] = matrix[row][col] + min(left, down, right)
            dp = new_dp  # Update dp array for the next iteration

        # The answer is the minimum value in the dp array
        return min(dp)