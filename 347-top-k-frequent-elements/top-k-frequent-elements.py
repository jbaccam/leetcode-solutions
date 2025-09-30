class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # keeps count of the occurences
        bucket = [[] for i in range(len(nums)+1)] # our buckets, where each subarray is a bucket
        # each bucket represents the count, so bucket at 3, would mean that the number in here has a count of 3
        # so we know that the buckets on the right side, if they contain anything, are the most frequently
        # counted numbers
        # so we can find the frequency of all numbers in a hashmap, put them in the corresponding buckets
        # and then we can append k amount of buckets at the end to our result and return that result

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


