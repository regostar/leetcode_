class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ctr = 0
        i = 0
        if numRows == 1:
            return s

        res = [[] for _ in range(numRows)]

        for each in s:
            res[i].append(each)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        # print(res)
        for i, row in enumerate(res):
            res[i] = ''.join(row)
        # print(res)

        return ''.join(res)


        