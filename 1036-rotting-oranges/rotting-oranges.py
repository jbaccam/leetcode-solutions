class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this will be the rotten oranges
        queue = deque()
        minutes = 0 
        fresh_oranges = 0 
        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # find all the oranges and the rotten oranges 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        # run bfs on all of the rotten oranges, after we do 1 iteration
        # of bfs on all the current rotten oranges in the queue
        # increment minutes
        # then when all the oranges turn rotten and the condition
        # oranges > 0 returns false, return how many minutes it took to do that
        while fresh_oranges > 0 and queue:
            # run bfs on all the rotten oranges 
            for i in range(len(queue)):
                r, c = queue.popleft()
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # check if the new position is in bounds, and check if its also
                    # representing a fresh ornage
                    if (nr < len(grid) and nc < len(grid[0])
                        and nr >= 0 and nc >= 0 and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
            
            minutes += 1

        return minutes if fresh_oranges == 0 else -1
                    

[[2,2,2],
 [2,2,0],
 [0,2,2]]





