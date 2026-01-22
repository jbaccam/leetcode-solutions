class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2 = Counter(s)
        t2 = Counter(t)
        
        return s2 == t2