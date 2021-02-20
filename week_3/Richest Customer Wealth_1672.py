'''

1672번 Richest Customer Wealth
mxn 정수 그리드 계정이 제공됩니다. 
여기서 accounts [i] [j]는 i 번째 고객이 j 은행. 가장 부유 한 고객이 가진 부를 반환합니다.

고객의 부는 모든 은행 계좌에있는 금액입니다.
가장 부유 한 고객은 최대의 부를 가진 고객입니다.


- 주어진 중첩 리스트에서 가장 합이 큰 리스트의 합을 출력
- 리스트 내부에 있는 각 리스트의 합을 map으로 sum함수에 
  매핑한 후 리스트로 반환하고 가장 큰 값을 리턴해준다.

'''

# leetcode 1672 : Richest Customer Wealth
# 44 ms 
class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        return max(map(sum, accounts))