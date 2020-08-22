class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] + s[i + 1] in dic:
                num += dic[s[i] + s[i + 1]]
                i += 1
            else:
                num += dic[s[i]]
            # 上面相当于计算了两个字母，所以再 + 1
            i += 1
        return num


# 优化版    
# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
#         res = 0
#         for i in range(len(s)-1):
#                 res = res-d[s[i]] if d[s[i]]<d[s[i+1]] else res+d[s[i]]
#         return res+d[s[-1]]


class Solution:
    def romanToInt(self, s: str) -> int:
        romadict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s) - 1):
            if romadict[s[i]] >= romadict[s[i + 1]]:
                ans += romadict[s[i]]
            else:
                ans -= romadict[s[i]]
        return ans + romadict[s[-1]]
