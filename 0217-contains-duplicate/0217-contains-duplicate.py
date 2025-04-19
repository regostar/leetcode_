class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash
        # len of hash and this list compare
        # O(N) space
        # O(1) time
        unique = set(nums)
        if len(unique) != len(nums):
            return True
        return False
        