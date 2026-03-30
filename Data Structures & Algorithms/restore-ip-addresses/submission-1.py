class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # consists of 4 integers separated by single dots 
        # each integer is between 0 and 255 (inclusive) and cannot have leading zeros 
        # valid = 0.1.2.201, 192.168.1.1
        # invalid = 0.011.255.245, 192.168.1.312, 192.168@1.1
        self.res = [] 
        
        def dfs(start, current): 
            def is_valid_segment(seg):
                return int(seg) <= 255 and (len(seg) == 1 or seg[0] != '0') and len(seg) <= 3 

            if len(current) == 4 and start == len(s):
                self.res.append('.'.join(current))
                return 
            
            remaining_parts = 4 - len(current)
            remaining_chars = len(s) - start

            if remaining_chars < remaining_parts or remaining_chars > 3 * remaining_parts:
                return 

            for i in range(1, 4):
                end = start + i
                if end > len(s):
                    break
                segment = s[start:end]
                if is_valid_segment(segment): 
                    current.append(segment[:])
                    dfs(end, current)
                    current.pop()
        dfs(0, [])
        return self.res
        



        