class Solution:
    def reorganizeString(self, s: str) -> str:
        # keep rotating the top 2 most frequent
        freq_map = Counter(s)

        heap = []
        for letter, freq in freq_map.items():
            heapq.heappush(heap, [-freq, letter])
        res = []
        while heap:
            freq_one, letter_one = heapq.heappop(heap)
            if not res or (res and letter_one != res[-1]):
                res.append(letter_one)
                if freq_one + 1 != 0:
                    heapq.heappush(heap, [freq_one + 1, letter_one])
            else:
                if not heap:
                    return ""
                freq_two, letter_two = heapq.heappop(heap)
                if not res or (res and letter_two != res[-1]):
                    res.append(letter_two)
                    if freq_two + 1 != 0:
                        heapq.heappush(heap, [freq_two + 1, letter_two])
                heapq.heappush(heap, [freq_one, letter_one])
        return "".join(res)