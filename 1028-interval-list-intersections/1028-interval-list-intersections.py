class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if not firstList or not secondList:
            return []
            # no intersection with null
        p1 = p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start1 > end2:
                # no overlap
                p2 += 1
            elif start2 > end1:
                # no overlap, 2 right of 1
                p1 += 1
            # elif end1 <= start2 or end2 <= start1:
            else:
                max_start = max(start1, start2)
                min_end = min(end1, end2)
                res.append([max_start, min_end])
                
                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
        return res

        