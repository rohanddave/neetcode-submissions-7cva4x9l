from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        ["hrn","hrf","er","enn","rfnn"]
        unique letters = {h: [], r: [], n: [], f: [], e: []}
        the answer is some unique arrangement of these unique letters 
        the list is lexicographically sorted based on the language rules 
        string a is smaller than string b if : 
        1. the first lettter where they differe is smaller in a than b
        example: a = "hrn" and b = "hrf" -> n < f
        2. a is a prefix of b and a.len < b.len 
        example: a = hr and b = hrf -> this does not really give any idea for the additional characters like f

        if n < f then f is the child of n 
        we create a graph using this logic.
        if it was guaranteed that only one ordering exists then it would be a flat 
        linked list and not a graph i.e. every node will have only one child 
        but since multiple orderings are possible every node can have multiple children 
        the resultant answer is any one of these orderings 

        adj = {h: [e], r: [n], n: [f], f: [], e: [r]}
        in_degree = {h: 0, r: 1, n: 1, f: 1, e: 1}
        h->e->r->n->f

        start with node that has an in_degree of 0 and use DFS 
        it is possible that a cycle is detected then that path is invalid 
        and we should try another? 
        
        a is a prefix of b: a = ab; b = abc
        valid case: a = hrn; b = hrf or a = er and b = enn or a = err and b = er or a = er and b = enn (this case will never happen because then a > b and it's guaranteed a < b)
        '''

        n = len(words) 

        adj = defaultdict(set)
        in_degree = {}

        for word in words: 
            for c in word:
                in_degree[c] = 0

        for i in range(0, n - 1): 
            a, b = words[i], words[i + 1]
            boundry = min(len(a), len(b))
            j = 0 
            while j < boundry and a[j] == b[j]:
                j += 1
            # prefix case 
            if j == boundry:
                if len(a) > len(b):
                    return ""
                continue 

            parent, child = a[j], b[j]
            if child not in adj[parent]:
                adj[parent].add(child)
                in_degree[child] += 1

        q = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while q: 
            node = q.popleft() 
            res.append(node)

            for nei in adj[node]: 
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return ''.join(res) if len(res) == len(in_degree) else ''
