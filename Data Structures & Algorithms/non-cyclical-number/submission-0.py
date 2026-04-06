class Solution:
    def isHappy(self, n: int) -> bool:
        # loop all the digits and add to see if it's one
        # if so, return true
        # else, keep looping till if it sees a result it's seen before
        # in which case we return false
        seen = set()
        startVal = n
        while True:
            sumVal = 0
            for i in range(len(str(startVal))):
                digit = str(startVal)[i]
                print(digit)

                sumVal += int(digit)**2
            if sumVal == 1:
                return True
            elif sumVal in seen:
                return False
            seen.add(sumVal)
            startVal = sumVal