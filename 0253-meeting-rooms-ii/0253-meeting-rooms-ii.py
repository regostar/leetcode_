class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the start and end times separately
        start = sorted([i[0] for i in intervals])  # Access the start time using i[0]
        end = sorted([i[1] for i in intervals])    # Access the end time using i[1]

        res, count = 0, 0
        s, e = 0, 0

        # Iterate over the intervals using two pointers
        while s < len(intervals):
            if start[s] < end[e]:
                # A meeting starts before one ends, so we need a new room
                count += 1
                s += 1
            else:
                # A meeting ends before another starts, so we free a room
                count -= 1
                e += 1

            # Maximum number of rooms needed
            res = max(res, count)

        return res
