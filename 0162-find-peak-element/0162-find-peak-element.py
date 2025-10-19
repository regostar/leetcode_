class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peak may not be the max
        # return first peak found
        # doesn't matter if there are many peaks
        # peak > orev and peak > next
        # log n
        # binary search

        # edge cases
        # 1 - no peak ? NO all nos be same ? NO
        # 2 -peak can be first or last also since boundaries are given
        # 1010101 => 1 => index = 2 or 1
        # sorted and rotatedf ? no random
        # can 2 consecutive elements be same? NO

        # 0 1 2 3 2 1 0
        # low and mid compare => if mid > low --> go right
        # 0 7 2 3 2 1 0 
        low = 0
        high = len(nums) - 1
        # let's compare mid and mid+1, mid-1
        while low < high:
            mid = low + (high - low) // 2
            # if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid+1]:
            #     return mid + 1
            if nums[mid] > nums[mid+1]:
                # go towards left
                high = mid
            else:
                low = mid + 1
        
        return low






        