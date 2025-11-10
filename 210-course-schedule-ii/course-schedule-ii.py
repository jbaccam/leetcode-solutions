class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        courses = []
        visited = set() # loop
        processed = set() # whats been added to result

        def dfs(course):
            # base cases
            # cycle detection
            if course in visited:
                return False
            # already processed
            if course in processed:
                return True
            
            visited.add(course)

            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            processed.add(course)
            courses.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return courses
