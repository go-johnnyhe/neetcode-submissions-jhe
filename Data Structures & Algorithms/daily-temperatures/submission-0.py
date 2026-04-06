class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # worse case: o(n^2) count everything forward
        # stack
        # 28 40  35.  36.  30. 38. 30
        # 0.  0.  1.   2.  1.  4.   1
        
        # result: [1 4 1 2 1 0 0]
        # temp arr [30,38,30,36,35,40,28]
        # stack: 40 28 

        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([t,i])
        return res