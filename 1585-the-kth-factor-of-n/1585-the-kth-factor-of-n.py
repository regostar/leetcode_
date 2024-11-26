class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # # first approach start from 1, compute all factors by checking each no after 1
        # # increment coutner, when you find kth retrun
        # factor_ctr = 0
        # last_factor = -1
        # curr_num = 1
        # while curr_num <= n and factor_ctr < k:
        #     if n % curr_num == 0:
        #         # factor
        #         factor_ctr += 1
        #         last_factor = curr_num
        #         print(curr_num)
        #         print("f ", factor_ctr)
        #     curr_num += 1
        # # condt = factor_ctr <= k and curr_num <= n
        # # return curr_num - 1 if condt else -1

        # # -1 condition
        # condt = curr_num == n + 1 and factor_ctr < k
        # return -1 if condt else last_factor
        factors_under_n, factors_above_n = [], []
        for num in range(1, int(sqrt(n) + 1) ):
            if n % num == 0:
                # factor
                factors_under_n += [num]
                factors_above_n += [n//num]

        if factors_under_n[-1] == factors_above_n[-1]:
            # edge case 9 sqrt = 3 is a factor
            factors_under_n.pop()
        factors = factors_under_n + factors_above_n[::-1]
        print(factors)
        return -1 if len(factors) < k else factors[k-1]
        

        