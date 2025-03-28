class Solution:



    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        directions = [(-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1)]

        def get_neighbors(row, col):
            for r_dif, c_dif in directions:
                new_row = row + r_dif
                new_col = col + c_dif
                if not ((0 <= new_row <= max_row) and \
                (0 <= new_col <= max_col)):
                    continue
                if grid[new_row][new_col] != 0:
                    # seen already so we do not traverse
                    continue

                yield (new_row, new_col)

        # base case -
        # check if first and last cells are open
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        # seen now - saving distance

        while queue:
            # BFS
            row, col = queue.popleft()
            dist = grid[row][col]
            if (row, col) == (max_row, max_col):
                #terminating condition
                return dist
            
            for n_row, n_col in get_neighbors(row, col):
                grid[n_row][n_col] = dist + 1
                queue.append((n_row, n_col))
        
        return -1
        # no path
