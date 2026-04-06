class WordTree:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = WordTree()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordTree()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    # explore all paths of children @ current node
                    # if any path is valid return True
                    # another nested for loop / recursion
                    # recursion->word index, current node
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.endOfWord
        return dfs(0, self.root)
