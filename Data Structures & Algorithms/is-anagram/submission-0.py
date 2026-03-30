class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_map = {}
        for i in range(0, len(s)):
            char_in_s = s[i]
            char_in_t = t[i]
            if char_in_s not in count_map.keys():
                count_map[char_in_s] = 1
            else:
                count_map[char_in_s] += 1
            
            if char_in_t not in count_map.keys():
                count_map[char_in_t] = -1
            else:
                count_map[char_in_t] -= 1
        
        for key in count_map.keys():
            if count_map[key] != 0:
                return False
        return True
        