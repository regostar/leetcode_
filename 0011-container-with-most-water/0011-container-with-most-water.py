class Solution:
    def maxArea(self, height: List[int]) -> int:
        # basically we find the biggest bucket
        # taller and wider
        # we look for max area not just length  or width
        # 2 ptr approach
        # let's start from the ends
        # if l smaller than r then l+= 1
        # else r -= 1
        # compute area, check with max area
        # keep going towards the center
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left+= 1
            else:
                right -= 1
        return max_area

        