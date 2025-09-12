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
            # if the size of the window, minus the most frequent character, is greater than k, than we know that our window is TOO large, we dont have enough replacements, to be able to make this a valid substring, so we need to increment our left pointer to the next spot so we try out other substrings. And since were incrementing our pointer to the next position, first we have to decrement the character count that the previous pointer tracked, because that character, will no longer be in our window
            if (r - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1 # decrement the prev character at this pointer
                l += 1 # move the pointer to the right

            # then we can take the size of the valid window (substring) and compare it to the previous ones and take the meax
            res = max(res, r - l + 1)
            
        return res