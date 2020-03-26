# python3 用回溯递归的方法去试探每一种可能性 对于一个字符串s，有len(s)种方法把它分成左右两个部分（分割方法看代码），假如左侧的不是回文，则舍弃这次尝试；假如左侧的是回文串，则把右侧的进行递归的分割，并返回右侧的分割的所有情况


# 解法一 分治
# 将大问题分解为小问题，利用小问题的结果，解决当前大问题。

# 这道题的话，举个例子。

# aabb
# 先考虑在第 1 个位置切割，a | abb
# 这样我们只需要知道 abb 的所有结果，然后在所有结果的头部把 a 加入
# abb 的所有结果就是 [a b b] [a bb]
# 每个结果头部加入 a，就是 [a a b b] [a a bb]

# aabb
# 再考虑在第 2 个位置切割，aa | bb
# 这样我们只需要知道 bb 的所有结果，然后在所有结果的头部把 aa 加入
# bb 的所有结果就是 [b b] [bb]
# 每个结果头部加入 aa,就是 [aa b b] [aa bb]

# aabb
# 再考虑在第 3 个位置切割，aab|b
# 因为 aab 不是回文串，所有直接跳过

# aabb
# 再考虑在第 4 个位置切割，aabb |
# 因为 aabb 不是回文串，所有直接跳过

# 最后所有的结果就是所有的加起来
# [a a b b] [a a bb] [aa b b] [aa bb]

# 作者：windliang
# 链接：https://leetcode-cn.com/problems/palindrome-partitioning/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-3-7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         if len(s) == 0:
#             return [[]]
#         if len(s) == 1:
#             return [[s]]
#         tmp = []
#         for i in range(1,len(s)+1):
#             left = s[:i]
#             right = s[i:]
#             if left ==left[::-1]: #如果左侧不是回文的，则舍弃这种尝试
#                 right = self.partition(right)
#                 for i in range(len(right)):
#                     tmp.append([left]+right[i])
#         return tmp
        
        
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(List,tmp):
            if not List:
                res.append(tmp)
                return
            for i in range(len(List)):
                if List[:i+1]==List[i::-1]:
                    backtrack(List[i+1:],tmp+[List[:i+1]])
        backtrack(s,[])
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


# python3 用回溯递归的方法去试探每一种可能性 对于一个字符串s，有len(s)种方法把它分成左右两个部分（分割方法看代码），假如左侧的不是回文，则舍弃这次尝试；假如左侧的是回文串，则把右侧的进行递归的分割，并返回右侧的分割的所有情况

# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         if len(s) == 0:
#             return [[]]
#         if len(s) == 1:
#             return [[s]]
#         tmp = []
#         for i in range(1,len(s)+1):
#             left = s[:i]
#             right = s[i:]
#             if left ==left[::-1]: #如果左侧不是回文的，则舍弃这种尝试
#                 right = self.partition(right)
#                 for i in range(len(right)):
#                     tmp.append([left]+right[i])
#         return tmp