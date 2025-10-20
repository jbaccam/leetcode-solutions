class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        number = str(x)
        return number[::-1] == number