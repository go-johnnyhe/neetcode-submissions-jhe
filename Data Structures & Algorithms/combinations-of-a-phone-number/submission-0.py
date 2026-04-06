class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combo = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i):
            if i == len(digits):
                if not combo:
                    return
                res.append("".join(combo))
                return
            for letter in digitToChar[digits[i]]:
                combo.append(letter)
                dfs(i+1)
                combo.pop()
        dfs(0)
        return res