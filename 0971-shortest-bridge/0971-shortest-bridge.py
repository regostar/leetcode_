class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N
        
        visited = set()

        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visited):
                return
            visited.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        def bfs():
            res, q = 0, deque(visited)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        cur_r, cur_c = r + dr, c + dc
                        if invalid(cur_r, cur_c) or (cur_r, cur_c) in visited:
                            continue
                        if grid[cur_r][cur_c]:
                            return res
                        q.append([cur_r, cur_c])
                        visited.add((cur_r, cur_c))
                res+= 1
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()



        # 1 1 1 1 1
        # 1 0 0 0 1
        # 1 0 1 0 1
        # 1 0 0 0 1
        # 1 1 1 1 1

        