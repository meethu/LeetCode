# 先用 hashmap 缓存两个数的和，平均O(n^2 )，最坏O(n^4 )，空间复杂度O(n^2)。

# class Solution():
#
#     def foursum(self, nums, target):
#
#         length = len(nums)
#         nums.sort()
#         d = {}
#         res = set()
#         for i in range(length - 1):
#             for j in range(i+1, length):
#                 if nums[i] + nums[j] in d:
#                     d[nums[i] + nums[j]].append((i, j))
#                 else:
#                     d[nums[i] + nums[j]] = [(i, j)]
#
#         for i in range(length - 1):
#             for j in range(i+1, length):
#                 result = target - nums[i] - nums[j]
#                 if result in d:
#                     for item in d[result]:
#                         if item[0] > j:   # 有重叠，因为存入map时pair中小下标在前，大下标在后
#                             res.add((nums[i], nums[j], nums[item[0]], nums[item[1]]))
#         return [list(k) for k in res]

# 双指针
class Solution():
    def foursum(self, nums, target):
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                left, right, sub = j + 1, length - 1, target - nums[i] - nums[j]
                while left < right:
                    if sub > nums[left] + nums[right]:
                        left += 1
                    elif sub < nums[left] + nums[right]:
                        right -= 1
                    elif sub == nums[left] + nums[right]:
                        res.append((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
        return list(set(res))


nums = [1, 0, -1, 0, -2, 2]
target = 0
problems = Solution()
print(problems.foursum(nums, 0))
