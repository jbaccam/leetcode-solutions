class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((0,0,0,k)) # row, column, length, k
        visited = set()
        visited.add((0,0,k))
        directions = [(1,0), (-1,0), (0,-1), (0,1)]

        while queue:
            r, c, l, k = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return l
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 0 and (nr,nc,k) not in visited):
                    queue.append((nr, nc, l+1, k))
                    visited.add((nr,nc,k))
                
                if (nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1 and k > 0 and (nr,nc,k-1) not in visited):
                    queue.append((nr, nc, l+1, k-1))
                    visited.add((nr,nc,k-1))
        
        return -1
