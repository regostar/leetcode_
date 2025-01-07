class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on first element in each interval
        # then start merging if next < prev right
        intervals.sort(reverse=False, key= lambda x : x[0])
        final_intervals = []
        final_intervals.append([intervals[0][0], ''])
        last_max = intervals[0][1]
        for each in intervals[1:]:
            if each[0] <= last_max:
                last_max = max(last_max, each[1])
            else:
                final_intervals[-1][1] = last_max
                final_intervals.append([each[0], ''])
                last_max = each[1]
        final_intervals[-1][1] = last_max
        return final_intervals


