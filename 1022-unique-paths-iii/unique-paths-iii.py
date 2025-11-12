class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0  # count cells we need to visit
        start_r, start_c = 0, 0
        
        # find start position and count empty squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                if grid[r][c] != -1:  # count all non-obstacles
                    empty += 1
        
        res = 0
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            nonlocal res 
            
            # base cases
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                grid[r][c] == -1 or (r, c) in visited):
                return
            
            # found the end - check if we visited all squares
            if grid[r][c] == 2:
                if len(visited) == empty - 1:  # -1 because we haven't added end yet
                    res += 1
                return
            
            # mark as visited
            visited.add((r, c))
            
            # try all 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
            # backtrack
            visited.remove((r, c))
        
        dfs(start_r, start_c)
        return res