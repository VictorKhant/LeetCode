class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDic = {0:1}
        count = 0
        sum = 0
        for num in nums:
            sum += num
            count += sumDic.get(sum - k, 0)
            sumDic[sum] = sumDic.get(sum, 0) + 1
        return count