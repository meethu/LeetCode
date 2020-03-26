class Solution:
    def __init__(self):
        self.result, self.tmp = [], []

    def combine(self, n, k):
        return self.backtrack(1, n, k, [])

    def backtrack(self, start, n, k, tmp):
        if len(tmp) == k:
            self.result.append(tmp)
            return
        for i in range(start, n + 1):
            self.backtrack(i + 1, n, k, tmp + [i])
        return self.result


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


# class Solution:

#     def combine(self, n: int, k: int) -> List[List[int]]:
#         self.res=[]
#         self.temp=[]
#         def answer(nums: List[int] , k: int):
#             if k==0:
#                 self.res.append(self.temp[:])
#             for i in range(len(nums)):
#                 self.temp.append(nums[i])
#                 answer(nums[i+1:],k-1)
#                 self.temp.pop()

#         nums=[i for i in range(1,n+1)]
#         answer(nums,k)
#         return self.res

# from itertools import combinations
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return combinations(range(1,n+1),k)

# 典型回溯题
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def pick(nums, k):
#             if k == 1:
#                 return [[i] for i in nums]
#             res = []
#             for i, num in enumerate(nums):
#                 for j in pick(nums[i+1:], k-1):
#                     res.append([num]+j)
#             return res

#         return pick(list(range(1, n + 1)), k)


# # 执行用时 : 96 ms, 在Combinations的Python提交中击败了100.00% 的用户# 终于骄傲一次。这题让我想到了排列组合的性质C(m,n)=C(m-1,n)+C(m-1,n-1)

# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         if k>n or k==0:
#             return []
#         if k==1:
#             return [[i] for i in range(1,n+1)]
#         if k==n:
#             return [[i for i in range(1,n+1)]]

#         answer=self.combine(n-1,k)
#         for item in self.combine(n-1,k-1):
#             item.append(n)
#             answer.append(item)

#         return answer