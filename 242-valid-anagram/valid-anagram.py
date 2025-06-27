class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)): # Right here we can just iterate over the length of either of strings since we know they're the same length
            countS[s[i]] = 1 + countS.get(s[i], 0) # Use get instead of += 1 because if the value does not already exist in the dict then we would get an error
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT