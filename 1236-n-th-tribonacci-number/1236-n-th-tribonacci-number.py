class Solution:
    def tribonacci(self, n: int) -> int:
        # overflow possible ?
        # 32 bit integer fit? == yes
        # max n ? == 37

        # sum of last 3 numbers in the sequence
        # save - last 3 nos
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        ctr = 3
        while ctr <= n:
            temp = sum(t)
            t[0] = t[1]
            t[1] = t[2]
            t[2] = temp
            ctr += 1

        return t[2]


        