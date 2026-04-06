class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 1. arrives at same time (easy)
        # 2. catches up
        # catch up: when cars behind reach destination faster than
        #           the one in front --> delete this from stack
        # count stack length
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)