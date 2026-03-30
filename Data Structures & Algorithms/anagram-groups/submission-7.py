class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = set()

        # empty_strings = []
        # for i in range(0, len(strs)):
        #     s = strs[i]
        #     if s == "":
        #         empty_strings.append(s)

        # if len(empty_strings) != 0:
        #     result.append(empty_strings)
        #     seen.add("")
        
        
        for i in range(0, len(strs)):
            s = strs[i]
            anagrams = [s]
            if i in seen:
                continue
            else:
                seen.add(i)
            for j in range(0, len(strs)):
                t = strs[j]
                if j in seen:
                    continue
                if self.isAnagram(s,t):
                    seen.add(j)
                    anagrams.append(t)
            # seen.add(i)
            result.append(anagrams)
        return result
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        dic = {}
        for i in range(0, len(s)):
            char_in_s = s[i]
            char_in_t = t[i]
            if char_in_s in dic.keys():
                dic[char_in_s] += 1
            else:
                dic[char_in_s] = 1

            if char_in_t in dic.keys():
                dic[char_in_t] -= 1
            else:
                dic[char_in_t] = -1
        
        for key in dic.keys():
            if dic[key] != 0:
                return False
        return True
        