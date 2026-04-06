class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = {}
        for char in s1:
            if char not in dict1:
                dict1[char] = 0
            dict1[char] += 1
        l = 0
        r = len(s1) - 1
        dict2 = {}
        for i in range(len(s1)):
            if s2[i] not in dict2:
                dict2[s2[i]] = 0
            dict2[s2[i]] += 1
        if dict1 == dict2:
            return True
        for i in range(len(s1), len(s2)):
            dict2[s2[i]] = dict2.get(s2[i], 0) + 1
            dict2[s2[i - len(s1)]] -= 1
            if dict2[s2[i - len(s1)]] == 0:
                del dict2[s2[i - len(s1)]]
            if dict1 == dict2:
                return True
        return False
            