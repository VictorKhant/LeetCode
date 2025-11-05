class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def is_valid(r, c):
            if r < 0 or c < 0 or r >= N or c >= N:
                return False
            return True

        def dfs(r, c, label):
            if not is_valid(r,c) or grid[r][c] != 1:
                return 0
            nei = [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]
            grid[r][c] = label
            currSize = 1
            for nr, nc in nei:
                currSize += dfs(nr, nc, label)
            return currSize

        #Precompute Islands
        size = defaultdict(int)
        label = 2
        res = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    res = max(res, size[label])
                    label += 1

        def connect(r, c):
            nei = [[r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1]]
            seen = set()
            currMax = 1
            for nr, nc in nei:
                if is_valid(nr, nc) and grid[nr][nc] not in seen:
                    seen.add(grid[nr][nc])
                    currMax += size[grid[nr][nc]]
            return currMax

        #flipping zero
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))
        return res