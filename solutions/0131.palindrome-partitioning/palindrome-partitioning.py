class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []

        def backtrack(s, idx, tmp):
            if idx == len(s):
                ret.append(tmp[:])
                return

            for i in range(idx, len(s)):
                if s[idx:i + 1] == s[idx:i + 1][::-1]:
                    tmp.append(s[idx:i + 1])
                    backtrack(s, i + 1, tmp)
                    tmp.pop()

        backtrack(s, 0, [])

        return ret


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(List, tmp):
            if not List:
                res.append(tmp)
                return
            for i in range(len(List)):
                if List[:i + 1] == List[i::-1]:
                    backtrack(List[i + 1:], tmp + [List[:i + 1]])

        backtrack(s, [])
        return res

# python3回溯算法，时间76%，空间98%

# def partition(self, s: str) -> List[List[str]]:
#         if not s: return [[]]
#         res = []
#         for i in range(len(s)):
#             temp = s[:i+1]
#             if temp == temp[::-1]:
#                 for j in self.partition(s[i+1:]):
#                     res.append([temp]+j)
#         return res

# 思路：遍历字符串s中从开始位置到i，如果s[:i+1]是回文串，把S[:i+1]添加到临时数组中，继续dfs其余s[i+1:]。返回的条件是需要dfs的字符串长度为空，此时把这种情况的临时数组添加到最终的结果数组中。注意str是不可变字符串，所以我们要用下标来操作，而不能像list一样修改数组。

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         def dfs(s, path, res):
#             if not s:
#                 res.append(path)
#                 return
#             for i in range(len(s)):
#                 if s[:i+1] == s[i::-1]:
#                     dfs(s[i+1:], path+[s[:i+1]], res)    
#         tmp,res = [],[]
#         dfs(s, tmp, res)
#         return res