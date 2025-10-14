class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        def sub(items):
            if len(items) == 1:
                return items
            left = sub(items[:len(items)//2])
            right = sub(items[len(items)//2:])
            l_index = 0
            for num in right:
                while l_index < len(left) and left[l_index] <= 2 * num:
                    l_index += 1
                self.ans += len(left) - l_index
            return sorted(items)
        sub(nums)
        return self.ans
