# class Solution:
#    def climbStairs(self, n: int) -> int:
#        if n < 2:
#            return n
#        else:
#            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n + 1):
            a, b = b, a + b
        return a


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b