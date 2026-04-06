class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # while needed and got aren't the same, keep increasing right
        # otherwise, keep updating
        t_count = Counter(t)
        s_count = defaultdict(int)
        matches_needed = len(t_count)
        matches_got = 0
        l, r = 0, 0
        ans = ""
        minLength = float('inf')
        while r < len(s):
            new_char = s[r]
            s_count[new_char] += 1
            if new_char in t_count and s_count[new_char] == t_count[new_char]:
                matches_got += 1
            
            while matches_got == matches_needed:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    ans = s[l:r+1]

                to_remove = s[l]
                s_count[to_remove] -= 1
                if to_remove in t_count and s_count[to_remove] < t_count[to_remove]:
                    matches_got -= 1
                l += 1
            r += 1
        return ans