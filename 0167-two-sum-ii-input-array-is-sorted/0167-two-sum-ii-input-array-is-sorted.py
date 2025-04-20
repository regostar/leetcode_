class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 ptr
        left = 0
        right = len(numbers) - 1
        # only one sopln
        while left < right:
            tot = numbers[left] + numbers[right]
            if tot == target:
                return [left + 1, right + 1]
            elif tot < target:
                left += 1
            else:
                # tot > target
                right -= 1
        return [-1, -1]

        