class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)]) # row, column, length
        visited = set((0,0))
        directions = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,1), (0,-1)]

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        while queue:
            row, col, length = queue.popleft()

            # could be at the end
            if row == N-1 and col == N-1:
                return length
            
            # bfs its neighbors
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                # only add its neighbors if its a valid position
                if (nr >= 0 and nc >= 0 and nr < N and nc < N and grid[nr][nc] == 0 and (nr,nc) not in visited):
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))

        return -1



