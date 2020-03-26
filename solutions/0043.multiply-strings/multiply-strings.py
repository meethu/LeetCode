class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        res = [0 for _ in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                x, y = d[num1[i]], d[num2[j]]
                res[i + j + 1] += x * y % 10
                res[i + j] += x * y // 10  # 进位

        for i in range(m + n - 1, 0, -1):  # 逆序处理进位
            carry = res[i] // 10
            # if carry:
            res[i] = res[i] % 10
            res[i - 1] += carry
        ans = ''.join([str(x) for x in res]).lstrip('0')
        return ans


nums1, nums2 = "96", "313"
problems = Solution()
print(problems.multiply(nums1, nums2))
