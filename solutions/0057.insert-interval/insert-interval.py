class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
problems = Solution()
print(problems.insert(intervals, newInterval))
