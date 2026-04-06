class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
# right off the bat, build a trie with "words" array
        self.root = TreeNode()
        result = []
        
        def buildTrie(words):
            for word in words:
                curr = self.root
                for char in word:
                    if char not in curr.children:
                        curr.children[char] = TreeNode()
                    curr = curr.children[char]
                curr.endOfWord = True
        buildTrie(words)
# iteratively explore each char in the array
        def dfs(r, c, curr, word):
            if curr.endOfWord:
                result.append(word)
                curr.endOfWord = False

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            
            char = board[r][c]
            if char not in curr.children:
                return
            
            board[r][c] = "#"
            for row, col in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r+row, c+col, curr.children[char], word+char)
            board[r][c] = char

        curr = self.root
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, curr, "")
        



        return result

# when it sees one character in the trie, it starts dfs recursive search
# to see if there is a word match to a trie path
# if so, add that into the result array
