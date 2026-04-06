class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "zxyzxyz"
        #      l r
        if not s:
            return 0
        seen = set()
        seen.add(s[0])
        count = 1
        max_count = 1
        l = 0

        for r in range(1, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                count -= 1
            count += 1
            max_count = max(max_count, count)
            seen.add(s[r])
        return max_count