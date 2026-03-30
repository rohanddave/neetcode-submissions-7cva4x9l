class Solution:

    ### we#2say#3:#1yes#3
    ### #2we#3say#1:#3yes
    ### 2#we3#say1#:3#yes
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))+"#"+string
        print(res)
        return res            

    def decode(self, s: str) -> List[str]:
        res = []
        curr_word_length = 0
        i = 0
        while i < len(s):
            curr_word_length_string = ""
            while s[i] != "#":
                curr_word_length_string += s[i]
                i+= 1
            curr_word_length = int(curr_word_length_string)
            word = s[i + 1: i + curr_word_length + 1]
            i += curr_word_length + 1
            res.append(word)

        return res
