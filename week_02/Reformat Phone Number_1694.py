# 24ms
# leetcode 1694 :  Reformat Phone Number 
class Solution:
    def reformatNumber(self, number: str) -> str:
        num_s = [n for n in number if n.isdecimal()] # 문자열에서 숫자인 부분만 따로 저장
        result=[]
        while len(num_s)>0 : 
            if len(num_s) >4:
                result += num_s[:3]+['-']
                num_s= num_s[3:]
            else : # 끝이 4,3,2 으로 끝나는 것들
                if len(num_s) %2==0 :
                    result += num_s[:2]+['-']
                    num_s= num_s[2:]
                else : 
                    result += num_s[:3]+['-']
                    num_s= num_s[3:]
                    
        return "".join(result[:-1])


number1 = "1-23-45 6" # "123-456"
number2 = "123 4-567" # "123-45-67"
number3 = "12"  #  "12"
number4 = "123 4-5678" # "123-456-78"
number5 = "--17-5 229 35-39475 "  # "175-229-353-94-75"
res = Solution.reformatNumber(0,number5)
print(res)