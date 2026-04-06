class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["we","say",":","yes"]
        # "2*we3*say1*:3*yes"
        # add number and delimeter for encoding
        result = ""
        for st in strs:
            result += str(len(st)) + "*" + st
        return result
        # starting reading after the delimeter for decoding

    def decode(self, s: str) -> List[str]:
        # "2*we3*say1*:3*yes"
        # ["we","say",":","yes"]
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


