class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(0, len(strs)):
            s = strs[i]
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = 0
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i = j + 1 + length
        return result
