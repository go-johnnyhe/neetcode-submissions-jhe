class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens = ["1","2","+","3","*","4","-"]
        # involves an ordered sequence, try stack
        # 1,2, (+)
        # 3,3, (*)
        # 9,4, (-)
        # 5
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(num2 / num1))
        return stack[-1]