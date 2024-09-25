class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # key and freq of occurrence
        # we use a MAX HEAP to always get the task having highest freq
        # POP is log n
        max_heap = [-freq for _,freq in count.items()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while q or max_heap:
            time += 1
            if max_heap:
                # not idle time
                ct = heapq.heappop(max_heap)
                # now once I pop it, I need to put it in queue if the freq is >0
                # in py < 0
                if ct + 1:
                    q.append([ct+1, time + n])
                    # next occurrence is after 'n' 
            if q and q[0][1] == time:
                # hihest priority element and time is matching
                # then pop
                # add it to heap so that next iterstion it is executed
                heapq.heappush(max_heap, q.popleft()[0])
        return time


        