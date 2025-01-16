class Solution:
    def minFallingPathSum(self, matrix):
        # bottom up
        n = len(matrix)

        # Start from the second-to-last row and move upwards
        for row in range(n - 2, -1, -1):
            for col in range(n):
                # Current cell value plus the minimum of the cells directly below or diagonally below
                left = matrix[row + 1][col - 1] if col > 0 else float('inf')
                down = matrix[row + 1][col]
                right = matrix[row + 1][col + 1] if col < n - 1 else float('inf')

                matrix[row][col] += min(left, down, right)

        # The answer is the minimum value in the top row
        return min(matrix[0])