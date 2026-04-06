class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # partition at each index
        # choose to backtrack or not
        
        res = []
        path = []
        def pali(s, i, j):
            while i < j and i < len(s) and j > 0:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
        
        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if pali(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res