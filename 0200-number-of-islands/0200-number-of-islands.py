class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS with seen or just change the matrix element to 2 - seen
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        
        def dfs(r, c):
            nonlocal rows
            nonlocal cols

            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] != "1"
            ):
                return
            grid[r][c] = "2"
            #seen

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    # this is an island
                    # mark all of it's adjacent 1s
                    islands += 1
                    dfs(i, j)
                    # print("grid after dfs ")
                    # print(grid)
        return islands
                    
        
        
#         [["1","1","0","0","0"],
#          ["1","1","0","0","0"],
#          ["0","0","1","0","0"],
#          ["0","0","0","1","1"]]
        