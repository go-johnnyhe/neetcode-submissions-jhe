class Node:
    def __init__(self):
        self.letters = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                curr.letters[char] = Node()
            curr = curr.letters[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return True
        