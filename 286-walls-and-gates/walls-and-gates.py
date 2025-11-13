class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        rows = len(rooms)
        cols = len(rooms[0])

        # find all the gates and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < rows and nc < cols and nc >= 0 and nr >= 0 and rooms[nr][nc] == 2147483647):
                        rooms[nr][nc] = rooms[r][c] + 1 # neighbors distance = current distance + 1
                        queue.append((nr, nc))

                    