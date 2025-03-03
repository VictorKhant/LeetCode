class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            different = target - num
            if different in dic:
                return [dic[different], i]
            dic[num] = i
        return