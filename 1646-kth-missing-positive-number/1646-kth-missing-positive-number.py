class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # ascending order which means there may be a log n soln
        # only +ve nos
        # missing ?
        # not in list but in numeric sequence

        # find k th missing
        # edge cases -
        # cas be in the left side
        # can be in right side after array
        # can be in the middle

        # left side case
        if arr[0] != 1:
            if arr[0] > k:
                return k
                # atleast k missing elements in left
            else:
                # <= k
                k -= arr[0] - 1
        print("k = ", k)
        
        for i in range(1, len(arr)):
            print("initial k = ", k)
            missing_nos = arr[i] - arr[i-1] - 1
            print("arr[i-1] ", arr[i-1], "missing_nos = ", missing_nos)
            if missing_nos < k:
                k -= missing_nos
            else:
                return arr[i - 1] + k
        if k:
            return arr[-1] + k
            














        # increasing order
        # binary search
        # what is missing?
        # which is not in the list
        # simple approach -
        # find all the missing nos
        # then iterate it, start counter for positive nos till k times 
        # edge cases if the counter is not over then find that

        # count no of missing elements 
        # for every missing element increment ctr
        # 

        # less than O(n)
        # can we do bnary search ?
        # n/2 location we need 

        