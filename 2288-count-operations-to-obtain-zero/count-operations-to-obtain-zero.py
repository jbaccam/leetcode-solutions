class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while num1 and num2: # while both are still not zero, if one goes to zero this condition fails
            if num1 >= num2:
                num1 -= num2
                counter += 1
            else:
                num2 -= num1
                counter += 1
        
        return counter