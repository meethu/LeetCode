# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         segment = [0, 0, 0, 0]

#         ret = []

#         def dfs(segid, pos):
#             if segid == 4:
#                 if pos == len(s):
#                     ret.append(segment)
#                 return
#             if pos == len(s):
#                 return
#             if s[pos] == '0':
#                 segment[segid] = 0
#                 dfs(segid + 1, pos + 1)
#             ipAddr = 0

#             for i in range(pos, len(s)):
#                 ipAddr = ipAddr * 10 + ord(s[i]) - ord('0')
#                 if 0 <ipAddr <= 255:
#                     segment[segid] = ipAddr
#                     dfs(segid + 1, i + 1)
#                 else:
#                     break

#         dfs(0, 0)
#         return ret

class Solution:
    def restoreIpAddresses(self, s: str):

        ret = []

        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            seg1 = int(s[:a])
                            seg2 = int(s[a:a + b])
                            seg3 = int(s[a + b:a + b + c])
                            seg4 = int(s[a + b + c:a + b + c + d])

                            if seg1 <= 255 and seg2 <= 255 and seg3 <= 255 and seg4 <= 255:
                                ipAddr = str(seg1) + "." + str(seg2) + "." + str(seg3) + "." + str(seg4)
                                # 排除开头为 0 的情况， +3 为分隔符
                                if len(ipAddr) == len(s) + 3:
                                    ret.append(ipAddr)

        return ret
