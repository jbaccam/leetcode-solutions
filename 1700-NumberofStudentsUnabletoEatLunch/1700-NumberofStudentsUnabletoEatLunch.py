class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        output = len(students) # students who havent ate
        count = Counter(students) # hashmap of students and their 0 or 1

        for s in sandwiches:
            if count[s] > 0:
                output -= 1
                count[s] -= 1
            else:
                return output

        return output
