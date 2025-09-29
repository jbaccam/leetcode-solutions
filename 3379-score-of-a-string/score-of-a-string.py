class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        i = 1
        while i < len(s):
            sum += abs(ord(s[i-1]) - ord(s[i]))
            i += 1
            
        return sum