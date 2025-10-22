class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        
        sign = 1

        for num in str(n):
            result += sign * int(num)
            sign *= -1

        return result