class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O (n^2) brute force
        # nums2 - cimply compute next greater element and save

        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap.get(i, -1) for i in nums1]