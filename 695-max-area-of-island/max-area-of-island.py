class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
    
        rows = len(grid)
        cols = len(grid[0])

        # down up left right
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            # if its going out of bounds or is a 0
            if (r < 0 or c < 0 or r >= rows
                or c >= cols or grid[r][c] == 0):
                return 0
            
            # if it is a 1
            grid[r][c] = 0 # set to 0 so we dont try this position again
            area = 1 

            # now everytime a valid position is found, we return the area, 1, and increment to our area, so after every positions
            # recursive call stack is done, we add 1 for its spot, which pretty much counts all the index's we've been
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c) # run dfs and count the area of the new island we just found
                    max_island = max(current_area, max_island) # compare the maxes

        return max_island