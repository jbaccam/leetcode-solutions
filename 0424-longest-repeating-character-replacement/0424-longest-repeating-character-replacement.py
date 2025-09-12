class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first were going initilize our hashmap that tracks the frequencys of characters and our result
        count = {}
        res = 0

        # next, since this is a sliding window problem we need to initilzze our pointers
        l = 0
        # instead of initlizing r as some arbitary number, we are going to use it to iterate in our for loop because r is always going to iterate across the whole array
        for r in range(len(s)):
            # so here we are incrementing the count of the character as the right pointer into our hashmap
            count[s[r]] = 1 + count.get(s[r], 0)
            # 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res