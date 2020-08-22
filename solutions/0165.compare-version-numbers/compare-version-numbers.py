# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:

#         if not version1 or not version2:
#             return -1

#         v1 = [int(i) for i in version1.split(".")]
#         v2 = [int(i) for i in version2.split(".")]

#         if len(v1) > len(v2):
#             v2.extend([0] * (len(v1) - len(v2)))
#         elif len(v1) < len(v2):
#             v1.extend([0] * (len(v2) - len(v1)))

#         if v1 == v2:
#             return 0
#         elif v1 > v2:
#             return 1
#         else:
#             return -1


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        if not version1 or not version2:
            return -1

        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        k = max(len(v1), len(v2))

        for i in range(k):
            v1_cmp = 0 if v1 == [] else v1.pop(0)
            v2_cmp = 0 if v2 == [] else v2.pop(0)

            if v1_cmp > v2_cmp:
                return 1
            elif v1_cmp < v2_cmp:
                return -1
        return 0