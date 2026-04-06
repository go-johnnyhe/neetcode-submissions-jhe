class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0 -> 1 -> 4
        #   -> 2
        #   -> 3

        # 0 -> 1 -> 2 -> 3
        #   
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return True

