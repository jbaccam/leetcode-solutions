class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in res:
                return [res[difference], i+1]
            res[numbers[i]] = i + 1
