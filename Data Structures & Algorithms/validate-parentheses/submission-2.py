class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in bracketMap:
                stack.append(char)
            else:
                if not stack:
                    return False
                opening = stack[-1]
                if opening != bracketMap[char]:
                    return False
                stack.pop()
        return len(stack) == 0