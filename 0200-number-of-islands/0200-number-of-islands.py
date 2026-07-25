class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)
        return islands