class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dvdf
        #  1 2
        # zxyzxyz
        #     1 2
        # xxxx
        #    2
        #    1
        # left&right pointer at first two indices
        # keep moving right if there isn't duplicates
        # when encounters, move left till all unique <= right
        seen = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            count = max(count, len(seen))
        return count
            
        