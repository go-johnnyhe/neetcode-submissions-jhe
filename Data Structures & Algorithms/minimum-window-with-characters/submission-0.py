class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count t
        # Keep track of "want" and "got"
        
        # Keep extending till "got" matches "want"
        # Move in the left side and checking if they still match
        # if so, keep checking if it's the smallest length
        # else keep adding right again

        t_count = Counter(t)

        l, r = 0, 0
        matches_needed = len(t_count)
        matches_got = 0
        s_count = defaultdict(int)
        ans = (float('inf'), l, r)
        while r < len(s):
            new_char = s[r]
            s_count[new_char] += 1
            if new_char in t_count and s_count[new_char] == t_count[new_char]:
                matches_got += 1
            while l <= r and matches_got >= matches_needed:
                to_remove = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                s_count[to_remove] -= 1
                if to_remove in t_count and s_count[to_remove] < t_count[to_remove]:
                    matches_got -= 1
                l += 1
            r += 1
            
        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]:ans[2]+1]
                