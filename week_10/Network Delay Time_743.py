'''
### 743. Network Delay Time
---
K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 
입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는  n으로 입력받는다.

times [i] = (ui, vi, wi), 여기서 ui는 소스 노드, vi는 target 노드, wi는 신호에 걸리는 시간입니다. 
소스에서 target으로 이동합니다.


기존 그래프를 보고 새로운 그래프를 만든다. 
이때, 새로 만든 그래프의 개수가 n개일 때는 모든 노드가 신호를 받을 수 있다는 의미이다.

그리고 만일 n개가 아닐때는 모든 노드가 신호를 받을 수 없다는 의미이므로 -1을 리턴한다.


1. times()를 dict() 형식으로 변환한다. [graph]
2. 새롭게 만들면서 모든 노드가 신호를 받을 수 있는지 체크하는 dijk, bfs로 다음 경로를 받아오는 heap_Q를 생성한다.

3. heap_Q의 다음 갈 경로가 있는 경우 pop을 해서 어디 node로 가는지 알려준다.

3-1. 이때, dijk에 이미 해당 경로를 방문했으면, continue해서 다시 heap_Q에 다음 경로를 받아온다.
3-2. heap_Q에서 받아온 경로를 새롭게 그래프에 만들어준 후 해당 경로를 시작으로 다른 노드를 갈 수 있으면
     반복문을 통해 해당 노드를 받아옵니다.

4. 마지막 경로까지 돌았을때 생성된 노드의 개수와 n이 일치하면 그 떄의 시간을 return하고 아닐 경우 
   -1을 return 한다.

'''
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times :
            graph[u].append((v,w))

        heap_Q = [(0, k)]
        dijk = dict()

        while heap_Q:
            time, node = heapq.heappop(heap_Q)            
            if dijk.get(node) :  # dijk 안에 node가 있으면 반복문 실행
                continue

            dijk[node]= time    # 위의 if문을 거치지 않았으니 dijk에 없는 노드니 time을 넣어준다.

            if len(dijk) == n : 
                                # return 할때 dijk[node]와 time의 값은 같다.
                return time     # time 값은 반복문이 반복될 수록 계속 증가되니 마지막 값이 가장 긴 경로이다.

            for node, sub_time  in graph[node] : 
                heapq.heappush(heap_Q, (time + sub_time, node) )

        return -1


times = [[3,1,5], [3,2,2], [2,1,2], [3,4,1], 
         [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]]
n = 8   # 전체 노드 개수
k = 3  # k번 노드 부터 시작
res = Solution.networkDelayTime(0, times, n, k)
print(res)