class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # we generate prefix sum matrix

        # base case - 
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # one time compute at the time of initialization O(mn)
        # at query time, we do O(1)
        # cumulative sum wrt origin
        self.prefix_sum = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        # initialize one set of row col to 0 for ease of computation

        for r in range(ROWS):
            for c in range(COLS):
                # above + left - topleft 
                # because it was added twice while computing left and right in itself
                self.prefix_sum[r+1][c+1] = self.prefix_sum[r+1][c] + self.prefix_sum[r][c+1] - self.prefix_sum[r][c] + matrix[r][c]

        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # our result is 1+
        # same formula curr - left - top + topleft since it was computed already
        result = self.prefix_sum[row2+1][col2+1] + self.prefix_sum[row1][col1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1]

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)