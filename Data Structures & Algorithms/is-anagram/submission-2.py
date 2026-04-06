class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictionary = {}
        # for char in s:
        #     dictionary[char] = dictionary.get(char, 0) + 1
        
        # dictionary2 = {}
        # for char in t:
        #     dictionary2[char] = dictionary2.get(char, 0) + 1

        # return dictionary == dictionary2
        return Counter(s) == Counter(t)