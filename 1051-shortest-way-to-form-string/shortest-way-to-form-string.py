class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # if there still something inside of target after we subtract their unique values, 
        # then obviously there is a character we dont have 
        if set(target) - set(source):
            return -1
        
        j = 0
        res = 0

        # j is our pointer to target
        # i is our pointer for source
        # if they are the same that means that they are matching characters in relative order and to move to the next 
        # character in j
        # if we exit a whole for loop for i, then we iterated over an entire subsequence of source that was in the target
        # that means we can increment our result which counts subsequences
        # and the while loop will run the for loop again, because target still has remaining characters to run checks on
        while j < len(target):
            for i in range(len(source)):
                if j < len(target) and target[j] == source[i]:
                    j += 1
            res += 1
        
        return res
