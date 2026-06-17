class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        path = path.split('/')
        print(path)
        for i in path:
            if not s:
                s.append('/')
                print("Appending in sempty s", s)
            print(i)
            if s and i != "" and i != ".." and i != '.':
                s.append(i+'/')
                print("appending i in s", s, 'i+/' , i +'/')
            elif s and i == "..":
                s.pop()
                print("after poping s ",s)
            
        if s and s[-1].endswith('/') and len(s) >1:
            fw = s.pop()
            s.append(fw[:-1])
            print("final world was having / so removed", s)
        s = "".join(s)
        return s