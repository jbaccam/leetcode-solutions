class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
       
        for start, end in intervals[1:]:
            prev_endtime = res[-1][1]

            if prev_endtime >= start:
                res[-1][1] = max(prev_endtime, end)
            else:
                res.append([start,end])
        
        return res

        
        