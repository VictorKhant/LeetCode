class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.dp = {() : 0}
        self.newdp = {}
        m, n = len(seats), len(seats[0])

        def traverse(row, col, prev, path):
            if col == n:
                storedPath = tuple(path)
                self.newdp[storedPath] = max(self.newdp.get(storedPath, 0), self.dp[prev] + len(path))
                return
            
            if col - 1 not in prev and col + 1 not in prev and col - 1 not in path and seats[row][col] == ".":
                traverse(row, col + 1, prev, path + [col])
            traverse(row, col + 1, prev, path)
        
        for row in range(m):
            for key in self.dp.keys():
                traverse(row, 0, key, [])
            self.dp, self.newdp = self.newdp, {}

        return max(self.dp.values())