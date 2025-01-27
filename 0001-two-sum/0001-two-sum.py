class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[index]: index for index in range(len(nums))}
        result = []
        print(nums_dict)
        for j, each_num in enumerate(nums):
            if target - each_num in nums_dict and  nums_dict[target - each_num] != j:
                i = nums_dict[target - each_num]
                result.append(min(i, j))
                result.append(max(i, j))
                break
        return result
