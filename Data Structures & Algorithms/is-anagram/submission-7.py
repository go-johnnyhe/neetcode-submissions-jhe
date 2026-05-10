class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for ch in s:
            if ch not in dictS:
                dictS[ch] = 1
            else:
                dictS[ch] += 1

        dictT = {}
        for ch in t:
            if ch not in dictT:
                dictT[ch] = 1
            else:
                dictT[ch] += 1
        return dictT == dictS