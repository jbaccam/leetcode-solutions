class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

        # returns the k largest nums, it also returns k largest nums in descending order
        # so indexing [-1] gets us the last element in the list, which is the kth largest value
