class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and newInterval[0] > intervals[i][1]:
            # well defined base case no changes to these and 
            # NO Overlapping since higher bound is < lower bound of new
            res.append(intervals[i])
            i += 1
        start = newInterval[0]
        end = newInterval[1]
        while i < n and intervals[i][0] <= newInterval[1]:
            # find one overlapping interval 
            # find the last interval which overlaps
            # print("i = ", i, " intervals ", intervals[i])
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            # print("start = ", start)
            # print("end = ", end)
            i += 1
        res.append([start, end])

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

