class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # neetcode
        #               ""
        #          neet        code (X)
        #     neet(X)  code
        #     base case: 
        #     1. if doesn't match, bye
        #     2. if matches and is last index => true
        #     recursive case, iterate for loop for each word, pass the index
        memo = {}
        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for word in wordDict:
                if s.startswith(word, start):
                    if dfs(start + len(word)):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        return dfs(0)
           