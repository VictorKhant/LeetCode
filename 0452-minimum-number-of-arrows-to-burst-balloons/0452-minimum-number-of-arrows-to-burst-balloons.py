class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        prev = float("-inf")
        arrow = 0

        for point in points:
            if prev < point[0]:
                prev = point[1]
                arrow += 1
        return arrow