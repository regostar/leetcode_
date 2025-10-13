class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down
        # recursive
        # end to start
        # memoize the results computed
        def recursive_find_min_cost(step: int)->int:
            # base cases - 
            if step <= 1:
                return 0
            if step in results:
                return results[step]
            # recursive case -
            min_cost_to_reach_n_1 = cost[step - 1] + recursive_find_min_cost(step - 1)
            min_cost_to_reach_n_2 = cost[step - 2] + recursive_find_min_cost(step - 2)
            results[step] = min(min_cost_to_reach_n_1, min_cost_to_reach_n_2)
            return results[step] 
        
        results = {}
        # can use arrays or dict
        # arrays more efficient
        n = len(cost)
        return recursive_find_min_cost(n )
