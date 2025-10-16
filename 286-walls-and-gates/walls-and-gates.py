class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # run bfs on the GRIDS
        visited = set()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque()
        rows = len(rooms)
        cols = len(rooms[0])

        def addRoom(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols
                or (r,c) in visited or rooms[r][c] == -1):
                return
            queue.append((r,c))
            visited.add((r,c))

        # find all the grids and add them to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        distance = 0
        
        # like rotten oranges, bfs all the items in the queue first before moving to the next
        # this runs bfs on each gate once before incrementing distance and moving onto other positions
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # will initally be zero but doesnt matter because by default they start at zero
                # but next iteration, when we actually move to a distance of 1, the distance variable will change
                # and it will position the position thats 1 away from the grid to 2, and then it will change to 2
                # etc etc
                rooms[r][c] = distance

                # add all 4 adjacent rooms to the queue
                for dr, dc in directions:
                    addRoom(r + dr, c + dc)
            
            distance += 1
