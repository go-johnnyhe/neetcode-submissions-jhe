class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictionary = {}
        for char in s1:
            if char not in dictionary:
                dictionary[char] = 0
            dictionary[char] += 1
        left = 0
        dictionary2 = {}
        for right in range(len(s2)):
            dictionary2[s2[right]] = 1 + dictionary2.get(s2[right],0)
            if right - left + 1 > len(s1):
                dictionary2[s2[left]] -= 1
                if dictionary2[s2[left]] == 0:
                    del dictionary2[s2[left]]
                left += 1
            if dictionary == dictionary2:
                return True
        print(dictionary)
        print(dictionary2)
        return False