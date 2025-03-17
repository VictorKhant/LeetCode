class Solution:
    def check(self, nums: List[int]) -> bool:
        inc = False
        if len(nums) <= 2:
            return True
        prev = nums[0]
        for num in nums:
            if num < prev:
                if inc:
                    return False
                else:
                    inc = True
            prev = num
        if inc:
            return nums[0] >= nums[-1]
        return True



