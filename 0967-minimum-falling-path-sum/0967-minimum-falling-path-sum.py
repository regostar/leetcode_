from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        max_row_i = len(matrix)
        max_col_i = len(matrix[0])

        # Memoization table to store results of subproblems
        memo = [[None for _ in range(max_col_i)] for _ in range(max_row_i)]

        def compute_path_sum(row, col) -> int:
            # Base case: if out of bounds, return a very large value
            if col < 0 or col >= max_col_i:
                return float('inf')
            
            # Base case: when we reach the last row, return the value at that position
            if row == max_row_i - 1:
                return matrix[row][col]
            
            # If already computed, return the memoized value
            if memo[row][col] is not None:
                return memo[row][col]

            # Recursive case: calculate the minimum path sum by moving to one of the three possible directions
            down_left = compute_path_sum(row + 1, col - 1)
            down = compute_path_sum(row + 1, col)
            down_right = compute_path_sum(row + 1, col + 1)

            # Current cell value + min of the three possible next steps
            memo[row][col] = matrix[row][col] + min(down_left, down, down_right)
            return memo[row][col]

        # Start from any cell in the first row and find the minimum falling path sum
        min_path_sum = float('inf')
        for col in range(max_col_i):
            min_path_sum = min(min_path_sum, compute_path_sum(0, col))
        
        return min_path_sum
