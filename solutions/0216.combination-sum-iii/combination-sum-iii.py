class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        visited = [False] * 10

        def backtrack(idx, k, tmp):

            if sum(tmp) == n and k == 0:
                ret.append(tmp[:])
                return
            if k == 0:
                return
            for i in range(idx, 10):
                if visited[i]:
                    continue
                tmp.append(i)
                visited[i] = True
                backtrack(i + 1, k - 1, tmp)
                visited[i] = False
                tmp.pop()

        backtrack(1, k, [])
        return ret
