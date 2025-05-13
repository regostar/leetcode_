from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        no_rows = len(image)
        no_cols = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image  # Nothing to do

        def get_neighbors(row, col):
            directions = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
            for r, c in directions:
                if 0 <= r < no_rows and 0 <= c < no_cols:
                    yield (r, c)

        def bfs():
            while q:
                row, col = q.popleft()
                image[row][col] = color  # Fill current

                for nr, nc in get_neighbors(row, col):
                    if image[nr][nc] == original_color:
                        image[nr][nc] = color
                        q.append((nr, nc))  # Add to queue

        q.append((sr, sc))
        bfs()
        return image
