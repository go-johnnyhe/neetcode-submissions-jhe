class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        l = 0
        longest_seq = 0
        max_freq = 0
        for r in range(len(s)):
            if s[r] not in dictionary:
                dictionary[s[r]] = 0
            dictionary[s[r]] += 1
            max_freq = max(max_freq, dictionary[s[r]])
            
            while r - l + 1 - max_freq > k:
                dictionary[s[l]] -= 1
                l += 1
            longest_seq = max(longest_seq, r-l+1)
        return longest_seq
        # XYYX
        # lr

        # X:1,Y:3