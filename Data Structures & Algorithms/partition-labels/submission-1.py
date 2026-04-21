from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        example: 
             0  1. 2. 3. 4  5  6  7  8. 9. 10 11 12
        s = [x, y, x, x, y, z, b, z, b, b, i, s, l]"
        e = {x: 3, y: 4, z: 7, b: 9, i: 10, s: 11, l: 12}

        i = 0; start = 0; curr_end = 3
        i = 1; start = 0; curr_end = 4
        i = 2; start = 0; curr_end = 4
        i = 3; start = 0; curr_end = 4
        i = 4; start = 0; curr_end = 4
        i = 5; start = 5; curr_end = 7
        i = 6; start = 5; curr_end = 9
        i = 7; start = 5; curr_end = 9
        i = 8; start = 5; curr_end = 9
        i = 9; start = 5; curr_end = 9
        '''
        res = [] 
        end = defaultdict(int)

        for i in range(len(s) - 1, -1, -1): 
            char = s[i] 
            if char in end:
                continue 
            end[char] = i

        print(end)
        curr_end, start = -1, 0
        for i, char in enumerate(s): 
            curr_end = max(curr_end, end[char])
            if curr_end == i: 
                res.append(curr_end - start + 1)
                start = curr_end + 1

        return res