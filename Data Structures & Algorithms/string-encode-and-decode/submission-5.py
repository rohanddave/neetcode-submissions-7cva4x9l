class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        '''
        while i < len(s):
            read length of string up until the #
            read the next length characters as string 
        
        5#hello5#world
        '''
        res = []
        i = 0
        while i < len(s):
            length_str = ''
            while s[i] != '#':
                length_str += s[i]
                i += 1
            i += 1
            length = int(length_str)
            res.append(s[i: i + length])
            i += length
        return res

             

