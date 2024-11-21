class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # repition allowed
        # negative nos not allowed
        # no mod needed
        # find pairs shose sum = k
        # no of pairs = no of operations
        # can we sort it
        # yes
        # 2 ptr one from start one from end see if sum = k
        # if sum <k then increment ptr1
        # if sum > k then decrement ptr2
        # stop when no more pairs found ptr1==ptr2
        nums.sort()
        start_ptr = 0
        end_ptr = len(nums) - 1
        operations = 0
        while start_ptr < end_ptr:
            _sum = nums[start_ptr] + nums[end_ptr]
            if _sum == k:
                operations += 1
                start_ptr += 1
                end_ptr -= 1
            elif _sum < k:
                start_ptr += 1
            else:
                end_ptr -= 1
        return operations




        