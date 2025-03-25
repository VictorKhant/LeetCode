class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        temp = abs(n)
        while temp != 0:
            if temp % 2 == 1:
                result *= x
            x *= x
            temp //= 2

        if n < 0:
            return 1 / result
        return result
    