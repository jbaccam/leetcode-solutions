class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) 
        maxHeap = [[-count, char] for char, count in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        result = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            # want the most frequent, expect prev
            count, character = heapq.heappop(maxHeap)
            result += character
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = [count, character]

        return result