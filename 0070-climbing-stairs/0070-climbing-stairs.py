class Solution:
    def climbStairs(self, n: int) -> int:
        # any step we take should help us reach the top
        # let'sstart from the end
        # we can take both one step and two steps as long as the steps are in bounds
        steps = [1, 2]
        # initialize base cases
        # 1 step only one way, 2 step 2 ways
        # we need to write an equation which is a functio of the past value
        # 3rd step -> 3 > sum of prev 2
        # 4th step -> 3+2 ? = 5 
        # 1111 112 211 22 121
        for i in range(2, n):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n-1]

