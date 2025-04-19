class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # int array sorted in asc
        # k pivot rotate
        # rotated array at a pivot
        # we need to find the target
        # binary 
        # no repition


        # start with high = n -1
        # low = 0
        # compare arr[high] >= arr[low]
        # yes - not rotated
        # do simple binary search
        # no - then go to mid
        # if mid == target found
        # if target < mid and mid -1 < mid
        # go left
        # if target < mid and mid-1 >mid - go right
        # if terget > mid and mid + 1 > mid go right
        # else left
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target < nums[low] or target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1

        