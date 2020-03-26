class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        self.result = []
        return self.helper('', 0, n)

    def helper(self, now, x, n):
        if len(now) == n:
            self.result.append(int(now, 2))
        elif x == 0:
            self.helper(now + '0', 0, n)
            self.helper(now + '1', 1, n)
        else:
            self.helper(now + '1', 0, n)
            self.helper(now + '0', 1, n)
        return self.result

if __name__ == '__main__':
    n = 2
    print(Solution().grayCode(n))