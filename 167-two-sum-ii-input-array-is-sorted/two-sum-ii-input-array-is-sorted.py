class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(numbers):
            difference = target - num
            if difference in res:
                return [res[difference] + 1, i+1]
            res[num] = i
