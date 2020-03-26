class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums) / 2
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
            if dic[i] >= length:
                return i

# class Solution:
#     def majorityElement(self, nums):
#         leng = len(nums)
#         if leng == 1:
#             return nums[0]
#         dic = {}
#         for i in nums:
#             if i in dic:
#                 dic[i] += 1
#                 if dic[i] >= leng / 2:
#                     return i
#             else:
#                 dic[i] = 1
# python3 因为一定有众数，且众数个数大于n/2，所以直接排序输出n/2位置的数即可。[力扣]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[int(len(nums)/2)]