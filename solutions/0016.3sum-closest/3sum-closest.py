# 标签：排序和双指针
# 本题目因为要计算三个数，如果靠暴力枚举的话时间复杂度会到 O(n^3），需要降低时间复杂度
# 首先进行数组排序，时间复杂度 O(nlogn)
# 在数组 nums 中，进行遍历，每遍历一个值利用其下标i，形成一个固定值 nums[i]
# 再使用前指针指向 start = i + 1 处，后指针指向 end = nums.length - 1 处，也就是结尾处
# 根据 sum = nums[i] + nums[start] + nums[end] 的结果，判断 sum 与目标 target 的距离，如果更近则更新结果 ans
# 同时判断 sum 与 target 的大小关系，因为数组有序，如果 sum > target 则 end--，如果 sum < target 则 start++，如果 sum == target 则说明距离为 0 直接返回结果
# 整个遍历过程，固定值为 n 次，双指针为 n 次，时间复杂度为 O(n^2)




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 3:
            return
        nums.sort()
        curr_min = float('inf')
        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                x = abs(target - three_sum)
                if x <= curr_min:
                    curr_min = x
                    sum_min = three_sum
                if three_sum == target:
                    return target
                elif three_sum < target:
                    left += 1
                else:
                    right -= 1
        return sum_min