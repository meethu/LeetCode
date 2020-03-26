# Sorted 方法
class Solution:
    def isanagram(self, s, t):
        return sorted(s) == sorted(t)


# Map 方法
"""
dict.get(key, default=None)

 - key 字典中要查找的键。
 - default 如果指定键的值不存在时，返回该默认值。
"""
# class Solution:
#     def isanagram(self, s, t):
#         dict1, dict2 = {}, {}
#         for item in s:
#             dict1[item] = dict1.get(item, 0) + 1  # dict.get(key, default=None)
#         for item in t:
#             dict2[item] = dict2.get(item, 0) + 1
#         return dict1 == dict2

s, t = "anagram", "nagaram"
problems = Solution()
print(problems.isanagram(s, t))