class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_string = ""
            
            for i in range(len(s)-1):
                next_string += str((int(s[i]) + int(s[i+1])) % 10)

            s = next_string

        return s[0] == s[1]

        
