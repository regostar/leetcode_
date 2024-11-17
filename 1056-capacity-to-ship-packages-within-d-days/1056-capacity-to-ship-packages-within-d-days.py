class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # every day one shipment of W total is shipped
        # no of days is within - days
        # we need to find the minimum W to minimize the ship size and cost
        # at the same time ship all containers in 'days' time

        # we need to divide the sum to sum / days if possible
        # every day we can ship max of sum / days
        # but not possible that the weights will sum to it exactly
        def feasible(capacity) -> bool:
            _no_of_days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    _no_of_days += 1
                    if _no_of_days > days:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

        