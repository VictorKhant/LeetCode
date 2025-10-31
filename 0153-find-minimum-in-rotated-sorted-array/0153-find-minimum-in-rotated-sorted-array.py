class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        res = float("inf")
        while r >= 0 and nums[0] > nums[r]:
            res = min(res, nums[r])
            r -= 1
        return min(nums[0], res)