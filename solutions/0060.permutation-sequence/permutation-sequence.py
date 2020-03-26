import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [str(i) for i in range(1, n + 1)]
        res = ""
        n -= 1
        while n > -1:
            t = math.factorial(n)  # n的阶乘
            loc = math.ceil(k / t) - 1
            res += num[loc]
            num.pop(loc)
            k %= t
            n -= 1
        return res


# 需要先定义从1到n的数组。上文中说的 k/(n-1)! 和 mod/(n-2)! 其实并不严谨，第二位实际上应该是算完第一位后排除第一位的答案后，剩余数组的第 mod/(n-2)! 个元素。
# 由于引入了数组，第一位计算前mod 应该为 k-1。
# 当余数为0时，实际上没有必要继续计算了，只需将剩余数组元素，依次添加进答案即可。(join方法报错，没理解为什么，写了循环添加)

# 作者：zhangll
# 链接：https://leetcode-cn.com/problems/permutation-sequence/solution/zhao-gui-lu-zhi-jie-ji-suan-da-an-by-zhangll/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        mod = k - 1
        if n == 1: return '1'
        n_set = [str(i) for i in range(1, n + 1)]
        fac_n = math.factorial(n - 1)
        for i in range(n):
            val, mod = divmod(mod, fac_n)
            # print(i,fac_n,val,mod,result,n_set)
            fac_n = fac_n // (n - i - 1)
            result += n_set[val]
            del n_set[val]
            if mod == 0:
                for i in n_set: result += i
                return result

        return result


# 作者：zhangll
# 链接：https://leetcode-cn.com/problems/permutation-sequence/solution/zhao-gui-lu-zhi-jie-ji-suan-da-an-by-zhangll/


#         /**
#         直接用回溯法做的话需要在回溯到第k个排列时终止就不会超时了, 但是效率依旧感人
#         可以用数学的方法来解, 因为数字都是从1开始的连续自然数, 排列出现的次序可以推
#         算出来, 对于n=4, k=15 找到k=15排列的过程:

#         1 + 对2,3,4的全排列 (3!个)
#         2 + 对1,3,4的全排列 (3!个)         3, 1 + 对2,4的全排列(2!个)
#         3 + 对1,2,4的全排列 (3!个)-------> 3, 2 + 对1,4的全排列(2!个)-------> 3, 2, 1 + 对4的全排列(1!个)-------> 3214
#         4 + 对1,2,3的全排列 (3!个)         3, 4 + 对1,2的全排列(2!个)         3, 2, 4 + 对1的全排列(1!个)

#         确定第一位:
#             k = 14(从0开始计数)
#             index = k / (n-1)! = 2, 说明第15个数的第一位是3
#             更新k
#             k = k - index*(n-1)! = 2
#         确定第二位:
#             k = 2
#             index = k / (n-2)! = 1, 说明第15个数的第二位是2
#             更新k
#             k = k - index*(n-2)! = 0
#         确定第三位:
#             k = 0
#             index = k / (n-3)! = 0, 说明第15个数的第三位是1
#             更新k
#             k = k - index*(n-3)! = 0
#         确定第四位:
#             k = 0
#             index = k / (n-4)! = 0, 说明第15个数的第四位是4
#         最终确定n=4时第15个数为3214
#         **/
n, k = 4, 9
problems = Solution()
print(problems.getPermutation(n, k))
