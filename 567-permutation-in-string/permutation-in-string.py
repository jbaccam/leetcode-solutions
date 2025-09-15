class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case where s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        # here we are going to track the characters in s1, 
        # but since were iterating through s1, we might aswell start to add s2 chars here too
        # so if s1 is len 3 and we add 3 characters to the s1Count
        # we can be efficient and add the first 3 characters of s2 to s2Count too
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # this is where we will track our matches, if it == 26 than we know we found a permutation
        matches = 0
        # initial setup for tracking matches, before we start our sliding window
        # we need to how many of the 26 possible letters already have the same count in both the arrays
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # now we can do our sliding window portion
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # since this method we are using arrays, each letter is mapped to an index, and not a key
            # so we have to get the index using this method
            # this is the character that was just added
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # if they WERE equal before the increment at line 34, but now arent
            # then we made then unequal
                matches -= 1
            
            # now here is the same exact thing, but above we were adding characters to the right of our window
            # but our window is sliding, obviously, so now we have to also remove the characters at the left of the window
            # which we can handle the same way

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 # decrement instead, cause we just removed it from the left side of our window
            
            # these stay the same cause
            # if somehow by decrementing it we made them equal, than we increase our matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # and if we changed it from being equal to being slightly too small
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                
            #icnrement left pointer for sliding window
            l += 1
        
        return matches == 26

