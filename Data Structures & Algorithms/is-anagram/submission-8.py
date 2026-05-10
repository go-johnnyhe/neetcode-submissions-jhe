class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictS = {}
        # for ch in s:
        #     if ch not in dictS:
        #         dictS[ch] = 1
        #     else:
        #         dictS[ch] += 1

        # dictT = {}
        # for ch in t:
        #     if ch not in dictT:
        #         dictT[ch] = 1
        #     else:
        #         dictT[ch] += 1
        # return dictT == dictS
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        for ch in t:
            counter[ord(ch) - ord('a')] -= 1
        for value in counter:
            if value != 0:
                return False
        return True
