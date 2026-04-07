class Solution:
    def isValid(self, s: str) -> bool:
        # when see closing, see if cancel out. stack pop
        # when see opening, keep adding. stack append
        # eventually needs to be empty,  check stack length

        # core operation:
        #   when close, pop last one to check
        #   case: when no matching, false
        #   edge case: ], when close but nothing in stack, false
        #   when stack is eventually empty, true else false
        stack = []

        closing = {"}": "{", 
                   "]": "[", 
                   ")": "("}
        for char in s:
            if char in closing:
                if not stack:
                    return False
                if closing[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False