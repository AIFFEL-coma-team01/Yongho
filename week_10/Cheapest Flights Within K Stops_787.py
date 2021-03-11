'''
### 787. Cheapest Flights Within K Stops
---

m 개의 항공편으로 연결된 n 개의 도시가 있습니다. 각 비행은 도시 u에서 시작하여 가격이 w 인 v에 도착합니다.

이제 시작 도시 src 및 목적지 dst와 함께 모든 도시 및 항공편이 주어지면 
최대 k 개의 경유지로 src에서 dst까지 가장 저렴한 가격을 찾는 것입니다. 
그러한 경로가 없으면 -1을 출력하십시오.


743번 문제에서 목적지와 몇번의 경로를 거쳐야만 하는 제한이 추가된 문제이다. 

743번과는 다르게 heap_Q에 경유지에 해당하는 값을 입력 받는다.

K번 경유 했을때의 목적지로 가야하니 K번 미만의 경우는 계속 다음 노드를 찾게 만든다.

K번 미만의 경우에만 node가 다음 노드를 가리키게 만들었으니 
node가 목적지에 도달한 경우 해당 노드가 K번을 돈것이고 그때의 최종 경비를 출력하게 하면 된다.


'''



from collections import defaultdict# # 그래프를 딕셔너리로 구성
import heapq # 최소 힙

# 84 ms
class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in flights :  # 출발지, 도착지, 경비
            graph[u].append((v,w))

        heap_Q = [(0,src,0)] # 경비, 현재 노드, 경유 횟수
        dijk = dict()

        while heap_Q :
            price, node, k = heapq.heappop(heap_Q)

            if dijk.get(node) : continue  

            if node == dst : return price

            for node, add_price in graph[node] :  # 현재 노드를 출발지로 하는 노드들을 찾는다.
                if K >= k   :   # 이때 총 경유해야하는 경유 횟수보다 작은 경우 에만 다음 노드로 갈 수 있게한다.
                    heapq.heappush(heap_Q, (price+add_price,node, k+1))  # 경유를 했으니 1을 더해준다.

        return -1