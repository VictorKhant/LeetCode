class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        res = nums[0]
        while r >= 0 and res > nums[r]:
            res = nums[r]
            r -= 1
        return res