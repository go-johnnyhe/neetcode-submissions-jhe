class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expandCenter(l, r):
            nonlocal res
            # count = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                # count += 1
                l -= 1
                r += 1
                res += 1
        for i in range(len(s)):
            expandCenter(i, i)
            expandCenter(i, i + 1)
        return res