class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        res = ['']
        for digit in digits:
            res = [pre + char for pre in res for char in mapping[digit]]
        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ret = []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(idx, tmp):

            if len(tmp) == len(digits):
                ret.append("".join(tmp))

            if idx >= len(digits):
                return

            for char in mapping[digits[idx]]:
                tmp.append(char)
                backtrack(idx + 1, tmp)
                tmp.pop()

        backtrack(0, [])
        return ret


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
