# 思路一:单词按字典顺序排序

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         from collections import defaultdict
#         lookup = defaultdict(list)
#         for s in strs:
#             lookup["".join(sorted(s))].append(s)
#         return list(lookup.values())
        

        
# 思路二:用素数.        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        lookup = defaultdict(list)
        for _str in strs:
            key_val = 1
            for s in _str:
                key_val *= prime[ord(s) - 97]
            lookup[key_val].append(_str)
        return list(lookup.values())
    
    
    
        
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = defaultdict(list)
#         for string in strs:
#             #用排序后的字符串作为字典的键值
#             ans[''.join(sorted(string))].append(string)
#         return list(ans.values())
    
    
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         chardict = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61, 's':67, 't':71, 'u':73, 'v':79, 'w':83, 'x':89, 'y':97, 'z':101}
#         ans = defaultdict(list)
        
#         for string in strs:
#             temp = 1
#             for char in string:
#                 temp *= chardict[char]
#             #用字符串内字符对应的质数值的乘积作为键值
#             ans[temp].append(string)
 
#         return list(ans.values())