class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prevWord = None
        for s in words:
            currentWord = Counter(s)
            if currentWord != prevWord:
                ans.append(s)
                prevWord = currentWord
        
        return ans


        
                

            