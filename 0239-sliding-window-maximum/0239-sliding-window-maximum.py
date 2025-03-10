class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = deque()
        l = 0
        r = 0
        res = []
        while r < len(nums):
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[r])
            r += 1
            if r + 1 > k:
                res += [max_q[0]]
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
        return res