# class Solution:
#     def merge(self, intervals):
#         intervals.sort(key=lambda x: x[0])
#         #intervals.sort()
#         merged = []
#         for interval in intervals:
#             # 如果merged 为空或者 merged最后一个元素，右边界< 当前元素左边界interval，直接将interval 加入
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 merged[-1][1] = max(merged[-1][1], interval[1]) # 否则查看两者最大边界
#         return merged


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return intervals
        # 先把intervals按照第一个值进行排序
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # 此时必有重合，则重合区间的右值为最大的那个
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
