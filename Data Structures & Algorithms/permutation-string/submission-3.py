from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        fixed length sliding window of length len(s1)
        target/window = {a: 1, b: 1, c: 1}
        need = 3, have = 0 
        
        window 1 = {lec}; have = 1, need = 2
        window 2 = {eca}; have = 2, need = 1
        window 3 = {caa}; 



        if the count of char in window is 0 means we have the correct number of that character 
        if the count of char in window > 0 means we NEED more of that character 
        if the count of char in window < 0 means we HAVE more of that character 

        if window[char] == 0: have += 1
        if window[char] < 0; have -= 1
        if window[char] > 0; have -= 1
        if need == 0 means we have the substirng 
        '''
        l = 0 
        k = len(s1)
        window = Counter(s1) 
        have, need = 0, len(window)
        
        for r, char in enumerate(s2): 
            # grow window 
            if char in window: 
                window[char] -= 1
                if window[char] == 0: 
                    have += 1

            # shrink window
            if r >= k: 
                if s2[l] in window: 
                    if window[s2[l]] == 0:
                        have -= 1
                    window[s2[l]] += 1
                l += 1
            
            if have == need:
                return True 
        return False
            
            







