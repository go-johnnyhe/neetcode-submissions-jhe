class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. O(n^2)
        # 2. monotonic stack, make sure it's an increasing sequence
        # 3. two pointers, track min buy and max profit
        min_buy= float("infinity")
        max_profit = 0
        for p in prices:
            min_buy = min(min_buy, p)
            max_profit = max(max_profit, p - min_buy)
        return max_profit