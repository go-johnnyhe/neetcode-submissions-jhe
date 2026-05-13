class Solution:
    def validPalindrome(self, s: str) -> bool:
        # canDelete = True
        # still go front and back, when front != back, see if moving either
        # solves problem and canDelete is still true, 
        # if so, put canDelete to False and move on
        # canDelete = True
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(l+1, r) or isPal(l, r-1)


        return True