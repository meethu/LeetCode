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
