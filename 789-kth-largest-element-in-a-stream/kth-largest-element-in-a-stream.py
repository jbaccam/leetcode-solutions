class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # declare our minHeap
        self.k = k # declare our k
        heapq.heapify(self.minHeap) # heapify our array
        while len(self.minHeap) > k: # pop it to match size k
            heapq.heappop(self.minHeap) 


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # push the new value to the heap

        if len(self.minHeap) > self.k: # if we get greater than k, pop the min value so we have all the highest scores
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # return the k'th largest element which means 
        # k'th largest means go to the k’th number from the back of the sorted list.
        # so if we had [2, 4, 7, 9], 9 would be the 1st largest, 7 the 2nd, 4 the 3rd, etc
        # you want the kth largest element (the 4th largest)
