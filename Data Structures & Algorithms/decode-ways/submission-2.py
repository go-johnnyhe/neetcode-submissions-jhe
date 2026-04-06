class Solution:
    def numDecodings(self, s: str) -> int:
        # what's valid?
        # 1-26, no leading 0

        # edge case: if not s or leading is 0: return 0

        #    12         
        #  1.   12
        # 2      /

        #          1623
        #    1        16
        #   6        2  23
        #  2 23     3
        # 3
        # 
        #       1 6 2 3
        #    dp 6 3 2 1   
        # for i in range(n - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]
        #         if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
        #             dp[i] += dp[i + 2]
        #
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]
        # memo = {}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     count = dfs(i+1)
        #     if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         count += dfs(i+2)
        #     memo[i] = count
        #     return count
        # return dfs(0)
            # first_pos = int(s[i])
            # second_pos = int(s[i:i+2])
            # if 1 < first_pos < 26:
            #     res += 1
            #     dfs(s, i+1)
            # elif 1 < second_pos < 26:
            #     res += 1
            #     dfs(s, i+2)
