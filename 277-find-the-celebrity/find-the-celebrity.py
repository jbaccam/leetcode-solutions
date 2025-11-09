# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        for person in range(1, n):
            if knows(candidate, person): 
                candidate = person
        
        for person in range(n):
            if person == candidate:
                continue
            
            if not knows(person, candidate):
                return -1
            
            if knows(candidate, person):
                return -1
        
        return candidate