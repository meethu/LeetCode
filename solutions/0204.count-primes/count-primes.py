class Solution:

    # def isPrime(self, n):
    #     for i in range(2, int(n ** 0.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # def countPrimes(self, n: int) -> int:
    #     if n <= 2: return 0
    #     cnt = 0
    #     for i in range(2, n):
    #         if self.isPrime(i):
    #             cnt += 1

    #     return  cnt



    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        isPrime = [1] * n
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:

                # 2x2 2x3 2x4 2x5 ...
                # 3x2 3x3 3x4 3x5 ...
                # 计算重复，直接 i * i 开始跳过重复部分

                j = i * i

                while j < n:
                    isPrime[j] = 0
                    j += i

        return  sum(isPrime[2:])



# https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/