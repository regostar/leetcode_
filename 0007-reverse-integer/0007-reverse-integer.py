class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # [-2147483648, 2147483647]

        sign = 1 if x >= 0 else -1
        x = abs(x)

        rev = 0
        # For negatives, we may allow the final last digit to be 8 (…3648 → -2147483648)
        last_digit_limit = 7 if sign == 1 else 8

        while x:
            digit = x % 10

            # Pre-check: will rev*10 + digit overflow?
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > last_digit_limit):
                return 0

            rev = rev * 10 + digit
            x //= 10

        rev *= sign
        # (Optional safety net) final range check:
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
