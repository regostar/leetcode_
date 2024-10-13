class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 ptr one from start one from end
        slow = 0
        last = len(numbers) - 1
        while slow < last:
            computation = numbers[slow] + numbers[last]
            if computation == target:
                return [slow+1, last+1]
            elif computation < target:
                slow += 1
            else:
                last -= 1
        
        