class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        # declare directions
        # down, up, right, left
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # dfs here
        def dfs(r, c):
            # if r is less than 0, or c is less than 0 this means its trying to leave the grid 
            # if r >= rows or c >= cols, this means that its trying to leave the grid
            # or the position is a 0
            # then return because its INVALID
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or grid[r][c] == "0"):
                return
            
            # if it is valid (a "1")
            # set the current position to a 0 so we know that we've already been here
            grid[r][c] = "0"
            # continue to dfs the other directions of the 1 we just found
            for dr, dc in directions:
                dfs(r + dr, c + dc) 
                # this works because dr and dc is getting unpacked
                # so first the first one would be (1,0), dr would be 1, dc is 0, 
                # this means that we are going to go DOWN a row
                # so add 1 to our current r, and leave our current c alone
                # then we run dfs on this position

        # check each position in the grid, running dfs on it if its a new island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands