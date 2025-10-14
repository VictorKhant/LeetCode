class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visited, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)
            for src, nei in edges:
                adj[src].append(nei)
            visited, path = set(), set()

            order = []
            for src in range(1, k + 1):
                if src not in visited:
                    if not dfs(src, adj, visited, path, order):
                        return []
            return order[::-1]

        
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []
        
        val_to_row = {i:j for j, i in enumerate(row_order)}
        val_to_col = {i:j for j, i in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num
        return res