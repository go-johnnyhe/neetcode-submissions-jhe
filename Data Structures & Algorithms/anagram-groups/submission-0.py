class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. find anagrams through validating that they
        # have the same character counts in a dictionary
        # 1+. we can sort the characters, but sorting every element makes
        # n log n
        # since all lowercase, count through ascii index occurences
        # 2. use that as keys, append same ones under the same keys
        # values are stores in an array
        # 3. return that array

        result = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in result:
                result[tuple(count)] = []
            result[tuple(count)].append(s)
        return result.values()