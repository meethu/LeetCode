class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def backtrack(idx, tmp):
            if len(tmp) == k:
                ret.append(tmp[:])
                return
            for i in range(idx, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp)
                tmp.pop()

        backtrack(1, [])
        return ret

# class Solution:
#     def combine(self, n, k):
#         def backtrack(first=1, curr=[]):
#             # if the combination is done
#             if len(curr) == k:
#                 output.append(curr[:])
#             for i in range(first, n + 1):
#                 # add i into the current combination
#                 curr.append(i)
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
#
#         output = []
#         backtrack()
#         return output


n, k = 4, 2
problems = Solution()
print(problems.combine(n, k))

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def backtrack(first = 1, curr = []):
#             # if the combination is done
#             if len(curr) == k:
#                 output.append(curr[:])
#             for i in range(first, n + 1):
#                 # add i into the current combination
#                 curr.append(i)
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()

#         output = []
#         backtrack()
#         return output

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/combinations/solution/zu-he-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
