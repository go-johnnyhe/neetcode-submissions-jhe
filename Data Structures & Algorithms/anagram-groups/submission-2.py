class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {[letter]}
        group_dict = {}
        for word in strs:

            word_arr = [0] * 26
            for letter in word:
                word_arr[ord(letter) - ord('a')] += 1
            key = tuple(word_arr)
            if key not in group_dict:
                group_dict[key] = []
            group_dict[key].append(word)
        return group_dict.values()
            