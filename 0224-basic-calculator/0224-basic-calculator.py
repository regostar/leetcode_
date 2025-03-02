class Solution:

    def evaluate_expr(self, stack):
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        res = stack.pop()

        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res
            



    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        # reversing
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():
                # operand in reverse order
                operand = (10**n * int(ch)) + operand
                n += 1
            
            elif ch != " ":
                if n:
                    # operator seen
                    # save operand on stack
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':
                    # actually close
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # append evalated result back to stack 
                    # there could be other bracklets
                    stack.append(res)
                else:
                    stack.append(ch)
        
        # push last operand to stack
        if n:
            stack.append(operand)
        
        return self.evaluate_expr(stack)
        
        