class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            return sum(int(x)**2 for x in str(n))
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = next(n)
            
        return n == 1