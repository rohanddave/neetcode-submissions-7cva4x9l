from collections import Counter, defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        we iterate through each index and choose if we want to split there 
        maintain a Counter of freq of characters of given string 
        maintain a sliding window where the window state is the count of freq of characters in window 
        if the count of all chars in the window is equal to the counts of characters in string then we can partition at that index 
        else we increment the count of character at index in current window 

        example: 
        s = "xyxxyzbzbbisl"
        freq = {x: 3, y: 2, z: 2, b: 3, i: 1, s: 1, l: 1}

        i = 0; window = {x: 1}
        i = 1; window = {x: 1, y: 1}
        i = 2; window = {x: 2, y: 1}
        i = 3; window = {x: 3, y: 1}
        i = 4; window = {x: 3, y: 2}
        '''
        res = []
        freq = Counter(s)
        window = defaultdict(int)
        l = 0

        def can_partition(): 
            for char, count in window.items(): 
                if count != freq[char]:
                    return False 
            return True

        for r, char in enumerate(s): 
            window[char] += 1
            if can_partition():
                res.append(r - l + 1)
                # reset window
                l = r + 1
                window = defaultdict(int)
        
        return res

