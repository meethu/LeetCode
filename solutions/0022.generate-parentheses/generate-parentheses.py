class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def gen(left, right, tmp):
            if left == n and right == n:
                ret.append(tmp)
            if left < n:
                gen(left + 1, right, tmp + "(")
            if left > right:
                gen(left, right + 1, tmp + ")")

        gen(0, 0, "")
        return ret


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans = []
#         def backtrack(S, left, right):
#             if len(S) == 2 * n:
#                 ans.append(''.join(S))
#                 return
#             if left < n:
#                 S.append('(')
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(')')
#                 backtrack(S, left, right+1)
#                 S.pop()

#         backtrack([], 0, 0)
#         return ans

n = 3
problems = Solution()
print(problems.generateParenthesis(n))