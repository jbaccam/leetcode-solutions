class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # iterate through every index of the substring
        # 0 potentially could not be the shortest sub string, but that doesnt matter cause we'll add some conditional to make
        # sure that the other strings dont go out of bound
        for i in range(len(strs[0])):
            # go through every string and make sure every string has the same character at index i
            for s in strs:
                # first, if i == len(s), that means i has just become out of bounds, so return res, if not, then  
                # if the index at the current string does not match strs 0, then it cant be a common prefix so we must return 
                # what we have
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # add common character to our result
            res += strs[0][i]
        
        return res
