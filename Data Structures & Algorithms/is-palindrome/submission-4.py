class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = ""
        for c in s:
            if c.isalnum():
                res1 += c.lower()
            else:
                continue
        res2 = ""
        for c in s[::-1]:
            if c.isalnum():
                res2 += (c.lower())
            else:
                continue
        return res1 == res2