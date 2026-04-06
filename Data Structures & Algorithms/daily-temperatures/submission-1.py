class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]
        # 1,4,1,2,1,0,0
        # Naive takes O(n^2) scanning each item
        # index stack: 
        # 0, 1-0 -> 1
        # 1, 2, 3 -> 3-2=1
        # 1,3,4,5 -> 5-4=1 ...
        # 5,6

        # result [1,4,1,2,1,0,0]
        result = [0] * len(temperatures)
        indexStack = [0]
        for i in range(1, len(temperatures)):
            print(indexStack)
            if indexStack and temperatures[indexStack[-1]] >= temperatures[i]:
                indexStack.append(i)
            else:
                while indexStack and temperatures[i] > temperatures[indexStack[-1]]:
                    prevIndex = indexStack.pop()
                    result[prevIndex] = i - prevIndex
                indexStack.append(i)
        return result