class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of the longest string in the window,
        # when the window length <= most freq + k, it's fine
        # otherwise, move the left pointer forward
        l, r = 0, 0
        highest_freq = 0
        freq_map = defaultdict(int)
        while r < len(s):
            new_char = s[r]
            freq_map[new_char] += 1
            highest_freq = max(highest_freq, freq_map[new_char])
            if r - l + 1 > highest_freq + k:
                freq_map[s[l]] -= 1
                l += 1
            r += 1
        return r - l