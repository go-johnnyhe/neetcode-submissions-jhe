class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        s = s.lower()
        for i in range(len(s)):
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if not s[i].isalnum():
                continue
            if s[i] != s[j]:
                return False
            j -= 1
        return True
