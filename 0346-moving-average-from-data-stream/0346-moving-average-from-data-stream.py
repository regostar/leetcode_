class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum_till_size = 0
        self.cur_size = 0
        self.window = deque([])

        

    def next(self, val: int) -> float:
        # whenever we are adding a new element - tot ele > size
        # then we delete the first element in the window and add the new one
        if self.size == 0:
            return 0
        elif self.cur_size == self.size:
            # then delete the first element and add this, compute average
            self.sum_till_size -= self.window[0]
            self.sum_till_size += val
            # print("before", self.window)
            self.window.popleft()
        else:
            self.sum_till_size += val
            self.cur_size += 1
        self.window.append(val)
        
        # print("window ", self.window)
        return (self.sum_till_size) / self.cur_size

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)