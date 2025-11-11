class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        visited.add((0,0,k)) # rows, col, k
        queue = deque()
        queue.append((0,0,0,k)) # rows, col, length, k

        directions = [(1,0), (-1,0), (0,-1), (0,1)]

        while queue:
            row, col, length, k = queue.popleft()
            
            if row == rows - 1 and col == cols - 1:
                return length
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 0 and (nr, nc, k) not in visited:
                    visited.add((nr,nc,k))
                    queue.append((nr,nc,length+1,k))
                
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1 and (nr, nc, k) not in visited and k > 0:
                    visited.add((nr,nc,k))
                    queue.append((nr,nc,length+1,k-1))
        
        return -1
                
                
