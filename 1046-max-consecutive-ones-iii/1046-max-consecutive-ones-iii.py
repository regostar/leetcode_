class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # flip the 0s that lead to joining 2 chains of 1s
        # thus creating a longer cons 1s chain
        # 1 -> k = len(ar)
        # return len(ar)
        # 2 -> k = 0
        # max cons 1s
        # 3 -> k,  
        # idea - count cons 1s  and 0s until no_0s == k,
        # once 0s exceed k, new cons 1 should start, reset no_0s = 0
        
        no_0s = 0
        cons_1s = 0
        max_cons_1s = 0
        cons_flag = False

        for i, num in enumerate(nums):
            if not cons_flag:
                if num == 0:
                    no_0s += 1
                    if no_0s > k:
                        continue
                cons_1s += 1
                cons_flag = True
            else:
                if num == 0:
                    no_0s += 1
                    if no_0s > k:
                        # reset
                        no_0s = 0
                        cons_1s = 0
                        cons_flag = False
                        continue
                cons_1s += 1
            max_cons_1s = max(max_cons_1s, cons_1s)

        return  max_cons_1s
                
                
                    



