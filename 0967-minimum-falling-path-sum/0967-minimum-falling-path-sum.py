class Solution:
    # TOP DOWN 
    def minFallingPathSum(self, matrix):
        import math

        # Initialize memoization table
        rows, cols = len(matrix), len(matrix[0])
        memo = [[None for _ in range(cols)] for _ in range(rows)]

        # Function to find the minimum falling path sum starting from (row, col)
        def findMinFallingPathSum(row, col):
            # Base cases
            if col < 0 or col >= cols:  # If column index is out of bounds
                return math.inf
            if row == rows - 1:  # If we reached the last row
                return matrix[row][col]

            # Check if the result is already calculated
            if memo[row][col] is not None:
                return memo[row][col]

            # Calculate the minimum falling path sum from the current position
            left = findMinFallingPathSum(row + 1, col - 1)
            middle = findMinFallingPathSum(row + 1, col)
            right = findMinFallingPathSum(row + 1, col + 1)

            memo[row][col] = min(left, middle, right) + matrix[row][col]
            return memo[row][col]

        # Start DFS from each cell in the first row and find the minimum
        minFallingSum = math.inf
        for startCol in range(cols):
            minFallingSum = min(minFallingSum, findMinFallingPathSum(0, startCol))

        return minFallingSum