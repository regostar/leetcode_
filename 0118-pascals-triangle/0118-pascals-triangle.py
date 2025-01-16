class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        # edges are 1
        # start 1
        prev_row = []
        for i in range(1, numRows+1):
            curr = []
            for j in range(i):
                if j == 0 or j == i -1:
                    # edge
                    curr.append(1)
                else:
                    curr.append(prev_row[j-1] + prev_row[j])
            prev_row = curr
            result.append(curr)
        return result



        