class Solution:
    def checkValidString(self, s: str) -> bool:
        # two stacks
        # stars and openings
        stars = []
        openings = []
        for i, char in enumerate(s):
            if char == "(":
                openings.append(i)
            elif char == "*":
                stars.append(i)
            else:
                if openings:
                    openings.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while openings:
            if stars and stars[-1] > openings[-1]:
                stars.pop()
                openings.pop()
            else:
                return False
        return True

        # add stars to star index, ( to opening index
        # whenever ), start popping from opening index, 
        #                   if it's ever empty during this, false
        # when opening is not empty, keep popping stars stack for indices
                                    #  greater than it
                            # when it runs out of stars but still openings, false
        # return True