class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up

        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        min_cost = [0] * (len(cost) + 1)

        # start from step 2
        # cost for step 1 or 2 is 0
        # 1 2 3 4 5
        for i in range(2, len(cost) + 1):
            take_one_step = min_cost[i-1] + cost[i-1]
            take_two_steps = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(take_one_step, take_two_steps)
        
        return min_cost[-1]