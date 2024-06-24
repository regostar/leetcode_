class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put it in a set
        # iterate the set and count for max consecutive number

        unique = set(nums)
        # O(n) space
        if not nums:
            return 0
        max_count = 1
        for num in nums:
            # check if it's new sequence
            if num - 1 not in unique:
                count = 1
                while (num + count) in unique:
                    count += 1
                max_count = max(max_count, count)
        return max_count