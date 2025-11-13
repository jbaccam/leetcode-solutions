class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]
        queue = deque()
        queue.append((0,0,1))
        visited = set()
        visited.add((0,0))
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][-1] == 1:
            return -1
        
        while queue:
            row, col, length = queue.popleft()
            
            if row == n-1 and col == n-1:
                return length
            
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                if (nr < n and nc < n and nc >= 0 and nr >= 0 and grid[nr][nc] == 0 and (nr,nc) not in visited):
                    queue.append((nr,nc,length+1))
                    visited.add((nr,nc))
        
        return -1