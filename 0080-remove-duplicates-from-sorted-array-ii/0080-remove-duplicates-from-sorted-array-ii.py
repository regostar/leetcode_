class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # my first approach
        # have back ptr
        # temp = 3rd repeating ele
        # push all elements on right side to this poistion - shift by 1 left
        # copy this val - temp to back_ptr
        # increment it
        # this way lot of swaps

        # approach 2
        # have index - i
        # have index - curr_pos
        # iterate the array with curr_pos
        # if repeat found, increment curr_pos until unique is found
        # when un ique is found, declare ar[i] = ar[curr_pos]

        i = 1
        cur_pos = 1
        last_freq = 1
        last_ele = nums[0]
        while cur_pos < len(nums):
            if nums[cur_pos] == last_ele:
                if last_freq < 2:
                    # unique accepted
                    nums[i] = nums[cur_pos]
                    i += 1
                    last_freq += 1
                else:
                    # not unique so skip
                    pass
            else:
                # new element
                nums[i] = nums[cur_pos]
                i += 1
                last_freq = 1
                last_ele = nums[cur_pos]
            cur_pos += 1
        return i



        