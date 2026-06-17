class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        path = path.split('/')
        for i in path:
            if not s:
                s.append('/')
            if s and i != "" and i != ".." and i != '.':
                s.append(i+'/')
            elif s and i == "..":
                s.pop()
            
        if s and s[-1].endswith('/') and len(s) >1:
            fw = s.pop()
            s.append(fw[:-1])
        s = "".join(s)
        return s