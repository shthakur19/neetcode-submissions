class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(ver):
            p = ver
            while p!= parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def unioun(u,v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return 0
            if rank[pv] > rank[pu]:
                parent[pu] = pv
                rank[pv] += rank[pu]
            else:
                parent[pv] = pu
                rank[pu] += rank[pv]
            return 1

        res = n
        for n1, n2 in edges:
            res -= unioun(n1, n2)
        return res

        

        