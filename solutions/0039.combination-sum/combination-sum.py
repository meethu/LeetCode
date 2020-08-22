class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ret = []
        def backtrack(target, idx, tmp):
            if target == 0:
                ret.append(tmp[:])
                return

            for i in range(idx, len(candidates)):
                if target < candidates[i]:
                    break
                tmp.append(candidates[i])
                # 可重复使用，所以下次开始位置可以包含在内
                backtrack(target - candidates[i], i, tmp)
                tmp.pop()

        backtrack(target, 0, [])

        return ret
# 下面代码有 4个 0，对应的路径是 [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]，而示例中的解集只有 [[7], [2, 2, 3]]，
# 结果集出现了重复。重复的原因是后面分支的更深层的边出现了前面分支低层的边的值。
# 把候选数组排个序，后面选取的数不能比前面选的数还要小，
# 即 “更深层的边上的数值不能比它上层的边上的数值小”，按照这种策略，剪枝就可以去掉重复的组合。


# class Solution:
#     def combinationSum(self, candidates, target):
#         self.result, temp = [], []
#         self.findres(candidates, target, temp)
#         return self.result
#
#     def findres(self, candidates, target, temp):
#         if target < 0:
#             return
#         if target == 0:
#             self.result.append(temp)
#             return
#         for i in range(len(candidates)):
#             self.findres(candidates, target - candidates[i], temp + [candidates[i]])


# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         results = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, [], results)
#         return results
#     def dfs(self, candidates, target, index, result, results):
#         if target < 0:
#             return
#         if target == 0:
#             results.append(result)
#             return
#         for i in range(index, len(candidates)):
#             self.dfs(candidates, target-candidates[i], i,result+[candidates[i]], results)
candidates = [2, 3, 6, 7]
target = 7
problems = Solution()
print(problems.combinationSum(candidates, target))
