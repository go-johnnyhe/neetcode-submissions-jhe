class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()
        
        route = []

        def dfs(place):
            
            while graph[place]:
                dfs(graph[place].pop(0))
            route.append(place)
        dfs("JFK")
        return route[::-1]