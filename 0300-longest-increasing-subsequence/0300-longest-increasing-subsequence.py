class Solution:  # 68 ms, faster than 93.92%
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # start with a[0]
#         # travrse, check if next one is greater than this
#         # if greater, increment counter ....
#         # O(2 ^ n) -> taking each number as start worst case
#         # compute longest each DFS tree 2 options for each so 2 pow n

#         # O(n^2) - optimization with DP
#         n = len(nums)
#         dp = [1 for _ in range(n)]
#         dp[n-1] = 1 # just showcasing red.
#         # base case since no other element is there in the array after this

#         for i in range(n-2, -1, -1):
#             # last to first
#             for j in range(i, n):
#                 if nums[i] < nums[j]:
#                     dp[i] = max(dp[i], 1+dp[j])
#         return max(dp)
#         # we don't know which one is starting point