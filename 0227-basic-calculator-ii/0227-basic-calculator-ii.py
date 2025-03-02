class Solution:
    def calculate(self, s: str) -> int:
        i = 0

        cur = prev = res = 0
        cur_operation = '+'

        while i < len(s):
            # traverse each chatr
            # find the number - complete number
            cur_char = s[i]

            if cur_char.isdigit():
                cur = 0
                # multi digit no
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                # reason is when loop is exited i is incremented to next polace

                # if + - simple operation
                # but for / *

                # we need prev number so that (res-prev) + (prev/cur)
                if cur_operation == '+':
                    prev = cur
                    res += cur
                elif cur_operation == '-':
                    prev = -cur
                    res -= cur
                elif cur_operation == '*':
                    res -= prev
                    res += prev * cur

                    prev = prev * cur
                else:
                    # /
                    res -= prev
                    res += int(prev / cur)

                    prev = int(prev / cur)
            elif cur_char != ' ':
                # operators
                cur_operation = cur_char
            i += 1
            print(" res = ", res, " prev = ", prev)
        return res
            



        