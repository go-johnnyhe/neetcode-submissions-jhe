class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            substring = s[j+1:j+1+length]
            res.append(substring)
            i = j + 1 + length
        return res