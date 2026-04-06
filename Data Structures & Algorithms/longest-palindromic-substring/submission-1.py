class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resL, resR = 0, 0
        def expandCenter(l, r):
            nonlocal resL, resR, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    resLen = length
                    resL = l
                    resR = r
                l -= 1
                r += 1
        for i in range(len(s)):
            expandCenter(i, i)
            expandCenter(i, i + 1)
        
        return s[resL:resR+1]