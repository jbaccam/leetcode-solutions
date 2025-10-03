class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        nums_bucket = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, i in count.items():
            nums_bucket[i].append(n)
        
        for i in range(len(nums_bucket)-1, 0, -1):
            for j in nums_bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res


        
