<h2><a href="https://leetcode.com/problems/minimum-falling-path-sum">967. Minimum Falling Path Sum</a></h2><h3>Medium</h3><hr><p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the <strong>minimum sum</strong> of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="width: 499px; height: 500px;" />
<pre>
<strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="width: 164px; height: 365px;" />
<pre>
<strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is shown.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>


MY SOLUTION
----------

Brute Force Approach Explanation:
The brute force approach explores all possible paths starting from any element in the first row and recursively computes the sum of all possible falling paths through the matrix. The goal is to find the minimum falling path sum by traversing the matrix using recursive depth-first search.

Here's the explanation of your brute force solution:

Initial Setup:
The matrix is an n x n grid, and the goal is to find the minimum sum of any path that starts from the first row and moves down, with each step moving to an element directly below or diagonally left/right.
You start by iterating over every element in the first row and recursively compute the sum of all valid paths starting from that element.
Recursive Helper Function (compute_path_sum):

The recursive function compute_path_sum is defined to explore all the valid paths from any given position (row, col).
For each cell (row, col), the function recursively explores the next row and computes the sum of all paths moving to:
The element directly below (row + 1, col)
The element diagonally to the left (row + 1, col - 1)
The element diagonally to the right (row + 1, col + 1)
At each recursive call, the function adds the value of the current cell to the running sum (curr_sum).
Base Case:

The base case occurs when you reach the last row of the matrix. At this point, you check whether the current path sum (curr_sum) is smaller than the global minimum sum (min_sum). If it is, you update min_sum.

Global Minimum Tracking:
A global variable min_sum is used to keep track of the smallest sum encountered. It is initialized to a very large value (math.inf) to ensure that any valid path sum will be smaller.
After exploring all the possible paths, the final result is the value of min_sum, which represents the minimum falling path sum.
Starting the Recursion:

You start the recursive process by calling the compute_path_sum function for each element in the first row. For each starting element, you compute the sum of all valid paths and update the global minimum if a smaller sum is found.

Approach
Do brute force, start for top row, go for every element.
Look for the next valid element which will make the SUM
For every SUM check for MIN SUM

Complexity
Time complexity:
Exponential Time Complexity: The brute force solution has a time complexity of O(3^n), where n is the number of rows in the matrix. This is because for each element in the first row, you recursively explore up to three possible paths (down-left, down, down-right) at each step. With each step, the number of possible paths grows exponentially.
Brute Force - Solve this first in your interview
import math

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Recursive approach
        # take all choices initially
        # compute min when u reach the end of the matrix
        # for each of the item, keep row, col in recursive fn
        # traverse only to valid paths recursively
        # have a global MIN, check sum at the end and compare with MIN
        min_sum = math.inf
        # initialize with min sum as highest number initially

        max_row_i = len(matrix)
        max_col_i = len(matrix[0])

        def compute_path_sum(curr_sum, row, col)-> None:
            """
            This function is used to compute he entire path sum
            then update the global MIN if the sum is less than MIN

            When is it called - 
            start with every element in first row
            call this function for each of the elements in 1 st row

            """
            nonlocal  min_sum
            # Base case
            if row == max_row_i - 1:
                # reached the end
                # check if sum is less the min
                if curr_sum < min_sum:
                    min_sum = curr_sum

            # Recursive case explore all the possibilities
            if row + 1 < max_row_i:
                if col + 1 < max_col_i:
                    compute_path_sum(curr_sum + matrix[row + 1][col + 1], row + 1, col + 1)
                if col - 1 >= 0:
                    compute_path_sum(curr_sum + matrix[row + 1][col - 1], row + 1, col - 1)
                compute_path_sum(curr_sum + matrix[row + 1][col], row + 1, col)

        
        for col_i in range(len(matrix[0])):
            compute_path_sum(matrix[0][col_i], 0, col_i)
            # row is always 0
            # col changes
        
        return min_sum
Approach Bottom UP Memoization
In a bottom-up approach, we start solving the problem from the last row and work our way upwards. For each cell in the matrix, we compute the minimum falling path sum by considering the three possible paths from the row directly below it (down-left, down, and down-right). The final solution will be the minimum value in the first row after processing all rows.

Steps:
Start from the last row: The falling path sum for the last row is simply the values in the last row themselves.
Move upwards: For each cell in the rows above, compute the minimum path sum by considering the three cells below (down-left, down, down-right).
The result: Once we reach the first row, the minimum value in the first row will be the minimum falling path sum

Memoization Bottom-up DP
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
Explanation:
Bottom-up DP:
We start from the second-last row and work our way up to the first row. For each cell (row, col), we update it with the minimum path sum considering the three possible paths from the row directly below:
down: The cell directly below (row + 1, col).
down_left: The cell diagonally left (row + 1, col - 1) (if it exists).
down_right: The cell diagonally right (row + 1, col + 1) (if it exists).

Final Step:
Once we have updated all rows, the minimum falling path sum will be the minimum value in the first row because it now contains the minimum sums starting from the top of the matrix.

Time Complexity:
The time complexity is O(n^2), where n is the number of rows (or columns, since the matrix is square). We iterate over each cell in the matrix once and compute the minimum of three values for each.
