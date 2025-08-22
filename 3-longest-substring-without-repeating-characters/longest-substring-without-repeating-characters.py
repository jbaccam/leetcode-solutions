class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterTracker = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in characterTracker:
                characterTracker.remove(s[left])
                left += 1
            characterTracker.add(s[right])
            longest = max(longest, right - left + 1)
        return longest