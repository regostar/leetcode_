class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time and space using hash map
        nums_dict = {nums[i]: i for i in range(len(nums))}
        print(nums_dict)
        for i in range(len(nums)):

            look_for_other = target - nums[i]
            if look_for_other in nums_dict and nums_dict[look_for_other] != i:
                return[i, nums_dict[look_for_other]]
        


        