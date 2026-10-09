class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        indegree = {course: 0 for course in range(numCourses)}
        total_complete = 0

        for course, prereq in prerequisites:
            neighbors[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            total_complete += 1
            for neighbor in neighbors[course]:
                indegree[neighbor] -= 1            
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return total_complete == numCourses
