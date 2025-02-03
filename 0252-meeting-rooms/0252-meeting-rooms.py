
class Solution:
    def canAttendMeetings(self, intervals):
        
        if not intervals:
            return True
        intervals.sort()  # Sort intervals by start time

        # check for overlapping intervals
        prev_last = intervals[0][1]
        for start, last in intervals[1:]:
            # print(start)
            if start < prev_last:
                return False
            else:
                prev_last = last
                # always last > start
                # wkt start > prev_last so no need to find min no overlap
        return True