class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time and space using hash map
        # non unique elements are present
        # 5,3,4,5,5,5
        # t = 10
        hashmap = {}
        for i, ele in enumerate(nums):
            compliment = target - ele
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[ele] = i
        return []

        


        