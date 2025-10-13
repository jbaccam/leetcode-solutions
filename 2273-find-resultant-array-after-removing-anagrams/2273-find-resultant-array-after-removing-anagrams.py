class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [] # store the answers in here
        prevWord = None # prevWord for comparision 

        # iterate over every string
        for s in words:
            # map currentWord to a counter which will allow us to do direct comparison
            currentWord = Counter(s)

            # compare the current word, words[i] to words[i-1]
            # if they arent anagrams, add words[i] to result
            # if they are anagrams we dont add them at all
            if currentWord != prevWord:
                ans.append(s)
                prevWord = currentWord
        
        return ans

# o(N * M)
# num of words * lenth of words
        
                

            