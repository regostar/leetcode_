class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find min k
        # eat all bananas
        # <=k bananas in a pile every hour
        # total hours given = h
        # all suitable ranges no int overflow
        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2
            hours_spent = 0

            for pile in piles:
                hours_spent += math.ceil(pile/middle)
            
            if hours_spent <= h:
                right = middle
            else:
                left = middle + 1
        return right