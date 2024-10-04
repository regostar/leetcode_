class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we do dfs
        # lets say we find 1, we mark it as 2 (seen) and move to it's adjacent nodes
        # we do not consider a traversed 2 node
        # we iterate 4 directions recursively
        # stop when we encounter 0 
        # first 1 we encounter we increment counter
        if not grid or not grid[0]:
            return 0
        
        seen = set()
        no_of_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        
        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                # popright for dfs iterative
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col +dc
                    if (
                        r  in range(rows)
                        and c  in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in seen
                    ):
                        q.append((r, c))
                        seen.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    no_of_islands += 1
                    bfs(r, c)
        return no_of_islands
            

        