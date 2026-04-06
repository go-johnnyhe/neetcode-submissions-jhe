class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resL, resR = 0, 0
        def expandCenter(l, r):
            nonlocal resLen, resL, resR
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL = l
                    resR = r
                    resLen = r - l + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            expandCenter(i, i)
            expandCenter(i, i + 1)
        return s[resL:resR+1]