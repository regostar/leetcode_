class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 2^ 100
        # (2 x 2)^50
        # (4 x 4)^25
        # 16 * (16 x 16)^12
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        # binary exponentiation
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, (n-1)/2)
        
        # time ans space log n

        