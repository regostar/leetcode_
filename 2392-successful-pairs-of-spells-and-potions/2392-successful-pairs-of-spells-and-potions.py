class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Brute force soln -> n * m time and n space
        # portions can be sorted, since we only need the no of spells[i] * portions
        # find the portion[i] in portions which results in min. stregth required to be successful
        # we know m -i is the res for that spell

        # m log m sort
        # binary search - log m, binary search n times - n log m
        # (m+n) log m

        # need to find min (pivot)
        # FIX: The original helper function and binary search logic were flawed.
        # A standard binary search for the lower bound is simpler and correct.

        potions.sort()
        m = len(potions)
        n = len(spells)
        pairs = [0] * n

        # FIX: Use correct variable names from enumerate: `i` for index, `spell` for value.
        for i, spell in enumerate(spells):
            # FIX: Reset binary search bounds for each spell.
            low = 0
            high = m - 1
            first_success_idx = m  # Default to an index out of bounds

            while low <= high:
                mid = low + (high - low) // 2
                product = potions[mid] * spell
                if product >= success:
                    # This is a successful pair. Store the index and
                    # try to find an even smaller potion to the left.
                    first_success_idx = mid
                    high = mid - 1
                else:
                    # Potion is too weak, search in the right half.
                    low = mid + 1
            
            # The number of successful potions is the total count minus the
            # index of the first successful one.
            pairs[i] = m - first_success_idx

        return pairs