# 数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。只要 nums[i] = nums[j]，我们就增加 jj以跳过重复项。

# 当我们遇到 nums[j] 不等于 nums[i]  时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复制到nums[i+1]。然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。

class Solution:
    def removeduplicates(self, nums):
        flag = 0  # 定义一个指针变量，相当于慢指针
        for num in nums:  # 遍历数组，相当于一个快指针
            if nums[flag] != num:  # 若指针指向的元素与当前遍历数组的元素不同
                flag += 1  # 指针后移一位
                nums[flag] = num  # 修改数组，将不同的元素占用重复元素的位置
            # 若相同则指针不动，数组继续往后遍历
        # 注意考虑数组为空的情况（flag初始值为0，由于要求数组长度，故需要加1）
        return len(nums) and flag + 1


nums = [1, 1, 2]
problems = Solution()
print(problems.removeduplicates(nums))

# class Solution:
#     def removeDuplicates(self, nums: [int]) -> int:
#         nums[:]= sorted(list(set(nums)))#一定还有排序
#         #这个地方如果是nums= 就会错，因为只是单纯实现值传递，
#         # 可以自行实验 查看id 进行地址比较 就明白了
#         return len(nums)
#
# nums[:]= 是直接在原地址上对列表进行 赋值修改。你可以理解为，遍历列表对每一个值进行切片复制，这个过程中不会改变nums地址。
# 而nums=，就是重新创建一个名叫 nums 的列表且生成新的地址，赋值完之后 就会以新的地址掉覆盖掉原来的nums地址（因为重名就会覆盖）。
# 你可以自己实验，使用id 方法 查看地址
