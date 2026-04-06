class Solution:
    def numDecodings(self, s: str) -> int:

# take 1 or 2 digits at a time
# 1. if leading is zero, skip that path
# 2. if 2 digits and outside of 1 - 26 range, skip that path
# 3. if reached the end, return 1
# count total paths
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            count = dfs(i+1)            
            if i + 1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
                count += dfs(i+2)
            memo[i] = count
            return count
        return dfs(0)