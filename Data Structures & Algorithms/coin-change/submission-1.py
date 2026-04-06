class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #    12 
        #  1  5  10
        # 1
        # 1
        # 
        # dfs, decrease the amount by coin, take amount it takes to reach 0
        # one path that reaches 0 is counted, tally up the shortest

        # base case 1: reach zero => return 1
        # base case 2: reach negative => return inf
        # get minimum out of all this

        # build up the dp array to amount + 1
        #  0 1  ... 12 
        # [0 1       ?]

        memo = {}
        def dfs(left):
            if left in memo:
                return memo[left]
            if left == 0:
                return 0
            elif left < 0:
                return float('inf')
            min_steps = float('inf')
            for coin in coins:
                # if left - coin >= 0:
                min_steps = min(min_steps, 1 + dfs(left - coin))
            memo[left] = min_steps
            return min_steps
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res