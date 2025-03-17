class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        l, r = 0, len(nums) - 1
        nums = sorted(nums)
        while l < r:
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count