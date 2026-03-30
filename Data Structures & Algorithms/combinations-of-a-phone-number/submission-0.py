class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t', 'u', 'v'], 9: ['w','x','y','z']}
        res = []
        def helper(string, i):
            if i == len(digits) and len(string) != 0:
                res.append(string)
                return
            
            for digit in mapping[int(digits[i])]:
                string += digit
                helper(string, i + 1)
                string = string[:-1]
        if digits:
            helper("", 0)
        return res

        