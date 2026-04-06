class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ()
        # (()) ()()
        # ((())) (()()) (())() ()(()) ()()()
        # backtrack for possibilities
        # (( )(
        # list all "valid" parens
        
        # base case: reached n pairs --> add to result array
        # recursive case: when valid, keep adding parens
        result = []
        def backtrack(s, left_count, right_count):
            # base
            if len(s) == 2 * n:
                result.append(s)
                return

            # recursive
            if left_count < n:
                backtrack(s + '(', left_count + 1, right_count)

            if right_count < left_count:
                backtrack(s + ')', left_count, right_count + 1)
        backtrack("",0,0)
        return result
