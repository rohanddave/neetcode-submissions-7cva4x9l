class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for string in strs:
            key = ""
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1

            for i in range(0, 26):
                key += alphabets[i] + str(char_count[i])
            
            if key in dic:
                dic[key].append(string)
            else:
                dic[key] = [string]

        for key in dic.keys():
            res.append(dic[key])
            
        return res