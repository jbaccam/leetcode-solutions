class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid) # len of grid
        # edge case
        # if start or end is blocked
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        
        # init queue where we'll put the neighbors of nodes
        queue = deque([(0, 0, 1)]) # also saving length in our queue here, we start at 1
        visit = set((0, 0)) 
        # all 4 directions + diagnals
        # right, down, left, up, bottom right, top left, bottom left, top right
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # while there node still in our queue
        while queue:
            r, c, length = queue.popleft() # get row, col, and our length of the current node
            # if its in the end zone then return our length it took to get there
            if r == N - 1 and c == N - 1:
                return length

            # if its not in our endzone, run bfs on it
            for dr, dc in direct:
                # nr, nc = new row, new col 
                nr, nc = r + dr, c + dc
                # if nr and nc are in bounds and the position of the node isnt blocked and we havent been there yet
                # then add it to the queue and visit it 
                if (0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and
                    (nr, nc) not in visit):
                    queue.append((nr, nc, length + 1))
                    visit.add((nr, nc))

        return -1 # if our length isnt returned early then we return -1 cause we couldnt get to the end