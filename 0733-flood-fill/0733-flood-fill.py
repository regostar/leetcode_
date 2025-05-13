class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # graph BFS
        q = deque()
        original_color = image[sr][sc]
        no_rows = len(image)
        no_cols = len(image[0])

        if original_color == color:
            return image
        
        def get_neighbors(row, col):
            nonlocal no_rows
            nonlocal no_cols
            directions = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
            for r, c in directions:
                if r >= 0 and r <no_rows and c >=0 and c < no_cols:
                    yield(r, c)
        
        q.append((sr, sc))
        
        while q:
            row, col = q.popleft()

            image[row][col] = color

            for nr, nc in get_neighbors(row, col):
                if image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image
        