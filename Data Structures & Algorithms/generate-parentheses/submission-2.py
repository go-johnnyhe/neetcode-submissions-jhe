class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking & recursion
        # build string permutations and add to array
        # n pairs of valid parens -> opening = closing = n
        # if not, add opening / closing as long as it's valid
        
        result = []
        
        def parensPermutation(string, openingCount, closingCount):
            if openingCount == closingCount == n:
                result.append(string)
            
            if openingCount < n:
                parensPermutation(string + "(", openingCount + 1, closingCount)
            if closingCount < n and closingCount < openingCount:
                parensPermutation(string + ")", openingCount, closingCount + 1)
        parensPermutation("", 0, 0)
        return result