class Solution:

    def encode(self, strs: List[str]) -> str:
        # split by adding string length and delimiter
        # 4*neet4*code4*love4*you
        res = ""
        for s in strs:
            res += str(len(s)) + "*" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            i = j+length+1
            word = s[j+1:i]
            res.append(word)
        return res
            