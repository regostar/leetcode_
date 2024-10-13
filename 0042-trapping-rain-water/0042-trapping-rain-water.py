class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        lmax = height[l]
        rmax = height[r]
        while l <= r:
            if lmax < rmax:
                temp = lmax - height[l]
                res += temp if temp > 0 else 0
                print("pos = ", l, " res = ", temp, "lmax = ", lmax, " curr = ", height[l])
                lmax = max(lmax, height[l])
                l += 1
            else:
                temp = rmax - height[r]
                res += temp if temp > 0 else 0
                print("pos r = ", r, " res = ", temp, "rmax = ", rmax, " curr = ", height[r])
                rmax = max(rmax, height[r])
                r -= 1
        return res
                
        