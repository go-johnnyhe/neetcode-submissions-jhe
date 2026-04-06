class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # build up a stack with two values
        # keep going with rules


        # stack = [] -> first val
        #               second, append or double
        # init secondLast, last = stack[-2], stack[-1]
        firstVal = int(operations[0])
        stack = [firstVal]

        
        for i in range(1, len(operations)):
            curr = operations[i]
            if curr == "+":
                stack.append(stack[-2] + stack[-1])
            elif curr == "D":
                stack.append(stack[-1]*2)
            elif curr == "C":
                stack.pop()
            else:
                stack.append(int(curr))
        return sum(stack) if len(stack) >= 1 else 0