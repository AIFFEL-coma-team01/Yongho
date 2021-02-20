'''
 Daily Temperatures) 

일일 온도 T 목록이 주어지면 입력의 각 날짜에 대해 더 따뜻한 온도까지 기다려야하는 날 수를 알려주는 목록을 반환합니다. 
이것이 가능한 미래 날이 없으면 대신 0을 입력하십시오.

예를 들어 온도 목록 T = [73, 74, 75, 71, 69, 72, 76, 73]이 주어지면 
출력은 [1, 1, 4, 2, 1, 1, 0, 0]이어야합니다.

참고 : 온도 길이는 [1, 30000] 범위에 있습니다.
각 온도는 [30, 100] 범위의 정수입니다.


풀이 :
가장 큰 값을 제외하고 모든 값들은 공통적으로 
'자기보다 큰 값이 위치한 인덱스 ( - ) 자기 자신의 인덱스'의 차이의 거리를 가진다.


#### Example)
73일때는 인덱스가 **0**  
- 스택에 있는 값과 다음 인덱스를 비교 인덱스가 1인 경우 값 **74**
- 73보다 74가 더크니 74일때의 인덱스인 **1**과 스택에 가장 위에 있는 인덱스 stack[-1]의 거리 차이를 구한다.
   - 거리 차이는 **1** 따라서, 0번 인덱스의 자기보다 큰 인덱스 거리는 1이다.
   
리스트 끝까지 위의 과정을 반복한다.

- 위의 과정 수행 중 가장 큰 값 max(T)가 나올 시 다음 값으로 continue 해준다.

'''

# 최소 508 ms ~ 544ms [변수 길이에따라 시간이 변동된다.]
class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        max_T, ln_T = max(T), len(T)
        result = [0] * ln_T
        stack = []
        for idx,t in enumerate(T) :
            stack.append(idx)
            if t == max_T: # 가장 큰 값이기에 0이다.
                result[idx] = 0 
                continue
            while stack and idx+1 < ln_T and T[stack[-1]] < T[idx+1] :
                 #  해당 리스트의 값이 아닌 index 값을 넣어서 순서를 찾는다.
                result[stack[-1]] = (idx+1) - stack[-1]  
                #  스택에 가장 최근에 있는 인덱스 값 위치를  pop
                stack.pop()
        return result
            

T = [73, 74, 75, 71, 69, 72, 76, 73] #  [1, 1, 4, 2, 1, 1, 0, 0]
res = Solution.dailyTemperatures(0, T)
print(res)