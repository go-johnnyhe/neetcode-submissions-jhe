class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # '''
    # 10
    #                 7
    #             6
    #         5
    #     1               1
    # '''
        min_profit = float("infinity")
        max_profit = 0
        for p in prices:
            min_profit = min(min_profit, p)
            max_profit = max(max_profit, p - min_profit)
        return max_profit