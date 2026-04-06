class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        path = set()
        seen = set()
        def dfs(node):
            if node in path:
                return False
            if node in seen:
                return True
            path.add(node)
            for neighbor in graph.get(node, []):
                if not dfs(neighbor):
                    return False
            seen.add(node)
            path.remove(node)
            return True
            
        for node in graph:
            if not dfs(node):
                return False
        return True