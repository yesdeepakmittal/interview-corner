class Solution:
    def mostCommonWord(self, st: str, banned: List[str]) -> str:
        l = []
        s = ''
        st += '.'  # for case ['bob'],[] | else condition won't hit in this case without 'non-alpha'
        ans = []
        for i in st:
            if i.isalpha():
                s += i.lower() 
            else:
                if s == '': continue
                l.append(s)
                s = ''
        d = {}
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i ] = 1
        keys = d.keys()

        for key in banned:
            if key.lower() in keys:
                del d[key.lower()]
        mx = 0
        for k,v in d.items():
            if v > mx:
                mx = v 
                ans = k 
        return ans