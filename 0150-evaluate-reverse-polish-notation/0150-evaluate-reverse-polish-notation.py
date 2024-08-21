class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                # Push number onto stack
                stack.append(int(token))
            else:
                # Pop last two numbers for operation
                b = stack.pop()
                a = stack.pop()

                # Perform operation and push the result back to stack
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Integer division, truncate towards zero
                    stack.append(int(a / b))

        # Final result is the only element in stack
        return stack[0]
