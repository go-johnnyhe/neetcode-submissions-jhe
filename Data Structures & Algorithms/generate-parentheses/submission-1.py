class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1
        # ()
        # 2
        # ()(),(())
        # 3
        # ((())),(())(),()(()),(()()),()()()
        # permutations built on previous ones -> backtracking&recursion
        # base case:
        # we have n pairs of "valid" parenthesis
        # when 2 * n = len(pairs)
        # recursive case:
        result = []
        def explore(string, openingCount, closingCount):
            if (openingCount + closingCount == 2 * n):
                result.append(string)
            if openingCount < n:
                explore(string + "(", openingCount + 1, closingCount)
            if closingCount < n and closingCount < openingCount:
                explore(string + ")", openingCount, closingCount + 1)
        explore("", 0, 0)
        return result
        
        