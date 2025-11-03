class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = [nums[0], nums[0]]
        notfirst = [0, nums[1]]

        for i in range(2, len(nums) - 1):
            first.append(max(first[-1], first[-2] + nums[i]))
            notfirst.append(max(notfirst[-1], notfirst[-2] + nums[i]))
        return max(notfirst[-2] + nums[-1], notfirst[-1], first[-1])