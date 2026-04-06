class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # part 1: build adjacency graph
        # compare pares of two each time
        # find the first difference in letter, adjacency list -> 
        # if we get prefix matching but there's more in the first word
        # then immediately return empty string
        # while building the adjacency list, also track indegree
        
        # part 2:
        # start topo sort, if indegree is 0, put in queue
        # keep pulling out level by level to return a valid res
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)


        adjacency_list = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i+1]
            used = False
            for j in range(min(len(first_word), len(second_word))):
                first_letter, second_letter = first_word[j], second_word[j]
                if first_letter != second_letter:
                    adjacency_list[first_letter].append(second_letter)
                    indegree[second_letter] += 1
                    used = True
                    break
            if used == False and len(first_word) > len(second_word):
                return ""
        
        queue = deque()
        for char in chars:
            if indegree[char] == 0:
                queue.append(char)
        res = []
        while queue:
            char = queue.popleft()
            res.append(char)

            for neighbor in adjacency_list[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return "".join(res) if len(res) == len(chars) else ""
