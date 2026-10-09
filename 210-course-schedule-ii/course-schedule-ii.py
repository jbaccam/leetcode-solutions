class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        indegree = {course: 0 for course in range(numCourses)}
        neighbors = defaultdict(list)

        for course, prereq in prerequisites:
            neighbors[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            result.append(course)
            for neighbor in neighbors[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        print(result)
        if len(result) == numCourses:
            return result
        else:
            return []


        