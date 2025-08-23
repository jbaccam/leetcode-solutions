class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # keeps count of the occurences
        bucket = [[] for i in range(len(nums)+1)] # our buckets, where each subarray is a bucket

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            bucket[c].append(n)
         
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res


