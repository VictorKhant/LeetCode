class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        lst = sorted(list(s))
        for i in range(len(lst)):
            nums[i] = lst[i]
        return len(s)