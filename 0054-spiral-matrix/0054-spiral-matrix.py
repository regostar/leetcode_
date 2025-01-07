class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we need 4 loops
        # right down left up in this order
        # everytime we switch to next loop, the boundaries must be updated
        spiral = []
        rows, cols = len(matrix), len(matrix[0])
        # bounds -
        up = left = 0
        right = cols - 1
        down = rows - 1

        while len(spiral) < rows * cols:
            # left to right
            for col in range(left, right + 1):
                spiral.append(matrix[up][col])
            
            # down
            for row in range(up + 1, down + 1):
                spiral.append(matrix[row][right])
            
            # right to left - different row
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    spiral.append(matrix[down][col])
            
            # different column
            if left != right:
                for row in range(down - 1, up, -1):
                    spiral.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        return spiral
