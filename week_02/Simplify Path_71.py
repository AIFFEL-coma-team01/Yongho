class Solution:
    def simplifyPath(self, path: str) -> str:
        result=[]
        split_path = path.split('/')
        for p in split_path: 
            if len(result)>0 and p == ".." :
                result.pop()  
            elif p and p!='.' and p!='..': #  ''과 '.'가 아닌 경우
                result.append("/"+p)  #  /../  pop 부분이 if 여서 해당 코드를 넘길 수 있다.
        if len(result) ==0 :  #  exception '/..' 
            return '/'
        return ''.join(result)



path1 = "/home/"  #   "/home"
path2 = "/../"  # "/"
path3 = "/home//foo/"  # "/home/foo"
path4 = "/a/./b/../../c/"
res = Solution.simplifyPath(0,path3)
print(res)