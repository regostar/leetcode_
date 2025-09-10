class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize a variable to store the reversed number
        result = 0
        
        # Determine the sign of the input number
        sign = 1 if x > 0 else -1
        
        # Work with the absolute value of x
        x = abs(x)
        
        # Reverse the digits
        while x != 0:
                        
            # Check for overflow
            if result > INT_MAX - x:
                return 0
            # Extract the last digit
            digit = x % 10
            # Append the digit to the reversed number
            result = result * 10 + digit
            # Remove the last digit from x
            x //= 10

        
        # Apply the sign to the result and return
        return sign * result if INT_MIN <= sign * result <= INT_MAX else 0