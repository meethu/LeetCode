class Solution:
    def generateParenthesis(self, n):
        self.result, temp = [], ""
        return self.gen(0, 0, n, temp)

    def gen(self, left, right, n, temp):
        if left == n and right == n:
            self.result.append(temp)
        if left < n:
            self.gen(left + 1, right, n, temp + "(")
        if right < n and left > right:
            self.gen(left, right + 1, n, temp + ")")
        return self.result


n = 3
problems = Solution()
print(problems.generateParenthesis(n))